"""Real-request retry tests for RetryTransport / AsyncRetryTransport.

These drive the transports through actual ``httpx.Client`` / ``httpx.AsyncClient``
instances backed by ``httpx.MockTransport`` so we exercise the exact retry
counting, status handling and exception propagation paths that ship to users.
"""

from __future__ import annotations

import asyncio

import httpx
import pytest

from coinmarketcap._retry import RetryConfig
from coinmarketcap._transport import AsyncRetryTransport, RetryTransport

# Zero-delay config keeps the test suite fast while still exercising retries.
NO_DELAY = RetryConfig(max_retries=2, initial_delay=0.0, max_delay=0.0)


def _sync_client(handler) -> httpx.Client:
    inner = httpx.MockTransport(handler)
    return httpx.Client(
        base_url="https://test.local",
        transport=RetryTransport(transport=inner, retry_config=NO_DELAY),
    )


def _async_client(handler) -> httpx.AsyncClient:
    inner = httpx.MockTransport(handler)
    return httpx.AsyncClient(
        base_url="https://test.local",
        transport=AsyncRetryTransport(transport=inner, retry_config=NO_DELAY),
    )


# --------------------------------------------------------------------------- #
# Status-based retries
# --------------------------------------------------------------------------- #

def test_retries_500_until_exhausted():
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        return httpx.Response(500, json={"err": "boom"})

    with _sync_client(handler) as client:
        resp = client.get("/v1/x")

    assert resp.status_code == 500
    assert calls["n"] == 3  # initial + 2 retries


def test_success_not_retried():
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        return httpx.Response(200, json={"ok": True})

    with _sync_client(handler) as client:
        resp = client.get("/v1/x")

    assert resp.status_code == 200
    assert calls["n"] == 1


def test_400_not_retried():
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        return httpx.Response(400, json={"err": "bad"})

    with _sync_client(handler) as client:
        resp = client.get("/v1/x")

    assert resp.status_code == 400
    assert calls["n"] == 1


def test_recovers_after_transient_500():
    seq = [500, 500, 200]
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        status = seq[calls["n"]]
        calls["n"] += 1
        return httpx.Response(status, json={})

    with _sync_client(handler) as client:
        resp = client.get("/v1/x")

    assert resp.status_code == 200
    assert calls["n"] == 3


def test_429_retry_after_header_preserved():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(429, headers={"Retry-After": "0"}, json={})

    with _sync_client(handler) as client:
        resp = client.get("/v1/x")

    assert resp.status_code == 429
    assert resp.headers["Retry-After"] == "0"


# --------------------------------------------------------------------------- #
# Network-error retries (the P0 gaps: previously only ConnectError/Timeout)
# --------------------------------------------------------------------------- #

@pytest.mark.parametrize(
    "exc",
    [
        httpx.ConnectError("refused"),
        httpx.ConnectTimeout("slow"),
        httpx.ReadTimeout("slow"),
        httpx.PoolTimeout("pool"),
        httpx.ReadError("reset"),
        httpx.WriteError("reset"),
        httpx.RemoteProtocolError("server hung up"),
    ],
)
def test_network_errors_retried_then_reraised(exc):
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        raise exc

    with _sync_client(handler) as client:
        with pytest.raises(type(exc)):
            client.get("/v1/x")

    assert calls["n"] == 3  # retried, not passed through on first failure


# --------------------------------------------------------------------------- #
# Async parity
# --------------------------------------------------------------------------- #

def test_async_retries_500():
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        return httpx.Response(500, json={})

    async def run():
        async with _async_client(handler) as client:
            return await client.get("/v1/x")

    resp = asyncio.run(run())
    assert resp.status_code == 500
    assert calls["n"] == 3


def test_async_network_error_retried():
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        raise httpx.RemoteProtocolError("hung up")

    async def run():
        async with _async_client(handler) as client:
            await client.get("/v1/x")

    with pytest.raises(httpx.RemoteProtocolError):
        asyncio.run(run())
    assert calls["n"] == 3


# --------------------------------------------------------------------------- #
# Mixed HTTP / transport outcomes must surface the final attempt
# --------------------------------------------------------------------------- #

@pytest.mark.parametrize("error_type", [httpx.ConnectError, httpx.ReadTimeout])
def test_last_network_error_replaces_earlier_http_response(error_type):
    calls = {"n": 0}
    final_error = error_type("final attempt failed")

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        if calls["n"] == 1:
            return httpx.Response(503, json={})
        if calls["n"] == 2:
            raise error_type("second attempt failed")
        raise final_error

    with _sync_client(handler) as client:
        with pytest.raises(error_type) as ei:
            client.get("/v1/x")

    assert ei.value is final_error
    assert calls["n"] == 3


@pytest.mark.parametrize("error_type", [httpx.ConnectError, httpx.ReadTimeout])
def test_async_last_network_error_replaces_earlier_http_response(error_type):
    calls = {"n": 0}
    final_error = error_type("final attempt failed")

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        if calls["n"] == 1:
            return httpx.Response(503, json={})
        if calls["n"] == 2:
            raise error_type("second attempt failed")
        raise final_error

    async def run():
        async with _async_client(handler) as client:
            await client.get("/v1/x")

    with pytest.raises(error_type) as ei:
        asyncio.run(run())
    assert ei.value is final_error
    assert calls["n"] == 3


def test_last_http_response_replaces_earlier_network_error():
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        if calls["n"] == 1:
            raise httpx.ConnectError("first attempt failed")
        return httpx.Response(503 if calls["n"] == 2 else 502, json={})

    with _sync_client(handler) as client:
        response = client.get("/v1/x")

    assert response.status_code == 502
    assert calls["n"] == 3


def test_async_last_http_response_replaces_earlier_network_error():
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        if calls["n"] == 1:
            raise httpx.ConnectError("first attempt failed")
        return httpx.Response(503 if calls["n"] == 2 else 502, json={})

    async def run():
        async with _async_client(handler) as client:
            return await client.get("/v1/x")

    response = asyncio.run(run())
    assert response.status_code == 502
    assert calls["n"] == 3
