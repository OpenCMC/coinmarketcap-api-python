"""Tests that transport failures and error responses map to typed exceptions.

Covers the documented contract in the README:
  Network  -> APIConnectionError
  Timeout  -> APITimeoutError
  4xx/5xx  -> CMCError subclasses (with response headers)
"""

from __future__ import annotations

import asyncio
from types import SimpleNamespace

import httpx
import pytest

from coinmarketcap._errors import (
    APIConnectionError,
    APITimeoutError,
    CMCError,
    RateLimitError,
)
from coinmarketcap._wrap import wrap_call, wrap_call_async


def _detailed(parsed=None, headers=None, status_code=200, content=None):
    """Fake a generated ``Response`` object.

    Mirrors the real generated shape: ``status_code`` (an ``http.HTTPStatus`` on
    real responses) drives success/error, ``headers`` always present, and
    ``parsed`` is the typed body — a data model, a typed error model, or ``None``
    for endpoints that do not model their error responses.
    """
    return SimpleNamespace(
        parsed=parsed,
        headers=headers or {},
        status_code=status_code,
        content=content,
    )


# --------------------------------------------------------------------------- #
# Transport exceptions -> typed errors
# --------------------------------------------------------------------------- #

@pytest.mark.parametrize(
    "exc",
    [
        httpx.ConnectTimeout("slow"),
        httpx.ReadTimeout("slow"),
        httpx.PoolTimeout("pool"),
    ],
)
def test_timeout_maps_to_api_timeout(exc):
    def fn():
        raise exc

    with pytest.raises(APITimeoutError) as ei:
        wrap_call(fn)
    assert ei.value.cause is exc


@pytest.mark.parametrize(
    "exc",
    [
        httpx.ConnectError("refused"),
        httpx.ReadError("reset"),
        httpx.RemoteProtocolError("hung up"),
        httpx.ProxyError("proxy"),
    ],
)
def test_network_maps_to_api_connection(exc):
    def fn():
        raise exc

    with pytest.raises(APIConnectionError) as ei:
        wrap_call(fn)
    assert ei.value.cause is exc
    # Timeouts are a subclass; make sure a pure network error is NOT one.
    assert not isinstance(ei.value, APITimeoutError)


def test_timeout_is_subclass_of_connection():
    def fn():
        raise httpx.ReadTimeout("slow")

    # Users catching the broad APIConnectionError still catch timeouts.
    with pytest.raises(APIConnectionError):
        wrap_call(fn)


# --------------------------------------------------------------------------- #
# Error responses -> CMCError with headers
# --------------------------------------------------------------------------- #

def test_error_object_raises_with_headers():
    """Endpoint that DOES model its error body (parsed is a typed error model)."""
    from coinmarketcap._generated.coinmarketcap_pro_api.models import (
        HTTPStatus429ErrorObject,
    )

    def fn():
        return _detailed(
            HTTPStatus429ErrorObject(),
            headers={"Retry-After": "7", "X-Trace": "abc"},
            status_code=429,
        )

    with pytest.raises(RateLimitError) as ei:
        wrap_call(fn)

    err = ei.value
    assert err.status_code == 429
    assert err.headers.get("Retry-After") == "7"
    assert err.headers.get("X-Trace") == "abc"


def test_undocumented_error_raises_with_headers():
    """Endpoint that does NOT model its error body (parsed is None).

    ~30% of endpoints (e.g. GET /v3/cryptocurrency/quotes/latest) fall here.
    Errors must still be typed AND carry response headers — keyed off the
    Response status code, with the body decoded from raw content.
    """

    def fn():
        return _detailed(
            parsed=None,
            headers={"Retry-After": "11"},
            status_code=429,
            content=b'{"status":{"error_message":"slow down"}}',
        )

    with pytest.raises(RateLimitError) as ei:
        wrap_call(fn)

    err = ei.value
    assert err.status_code == 429
    assert err.headers.get("Retry-After") == "11"
    assert "slow down" in str(err)


def test_unexpected_status_raises_cmc_error():
    from coinmarketcap._generated.coinmarketcap_pro_api.errors import UnexpectedStatus

    def fn():
        raise UnexpectedStatus(418, b'{"status":{"error_message":"teapot"}}')

    with pytest.raises(CMCError) as ei:
        wrap_call(fn)
    assert ei.value.status_code == 418
    assert "teapot" in str(ei.value)


def test_success_returns_parsed():
    payload = {"data": [1, 2, 3]}

    def fn():
        return _detailed(payload)

    assert wrap_call(fn) == payload


# --------------------------------------------------------------------------- #
# Async wrap path (previously returned an un-awaited coroutine)
# --------------------------------------------------------------------------- #

def test_async_wrap_returns_parsed():
    payload = {"ok": True}

    async def fn():
        return _detailed(payload)

    assert asyncio.run(wrap_call_async(fn)) == payload


def test_async_wrap_maps_timeout():
    async def fn():
        raise httpx.ReadTimeout("slow")

    with pytest.raises(APITimeoutError):
        asyncio.run(wrap_call_async(fn))


def test_async_wrap_maps_error_object():
    from coinmarketcap._generated.coinmarketcap_pro_api.models import (
        HTTPStatus429ErrorObject,
    )

    async def fn():
        return _detailed(
            HTTPStatus429ErrorObject(), headers={"Retry-After": "1"}, status_code=429
        )

    with pytest.raises(RateLimitError) as ei:
        asyncio.run(wrap_call_async(fn))
    assert ei.value.headers.get("Retry-After") == "1"
