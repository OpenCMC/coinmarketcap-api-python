"""End-to-end tests: client -> generated function -> wrap -> transport.

We inject an ``httpx.MockTransport`` into the underlying generated client so the
full call path is exercised without real network access. This is the regression
guard for two bugs that reflection-only tests could not catch:

1. async namespace methods returning an un-awaited coroutine instead of the
   parsed body / raising the mapped error;
2. response headers never reaching ``CMCError.headers``.
"""

from __future__ import annotations

import asyncio

import httpx
import pytest

from coinmarketcap import CoinMarketCap
from coinmarketcap._errors import RateLimitError


def _err_body(message: str) -> dict:
    """A CMC error envelope the generated models can fully parse."""
    return {
        "status": {
            "timestamp": "2024-01-01T00:00:00.000Z",
            "error_code": 1008,
            "error_message": message,
            "elapsed": 1,
            "credit_count": 0,
        }
    }


def _make_client(handler) -> CoinMarketCap:
    # max_retries=0 keeps the mocked 429 from being retried (and sleeping).
    cmc = CoinMarketCap(api_key="test-key", max_retries=0)
    gen = cmc._gen_client
    gen._client = httpx.Client(base_url=cmc.base_url, transport=httpx.MockTransport(handler))
    gen._async_client = httpx.AsyncClient(
        base_url=cmc.base_url, transport=httpx.MockTransport(handler)
    )
    return cmc


def test_sync_error_maps_with_headers():
    """Endpoint that models its error schema (global metrics)."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(429, headers={"Retry-After": "5"}, json=_err_body("rate limited"))

    cmc = _make_client(handler)
    with pytest.raises(RateLimitError) as ei:
        cmc.global_metrics.globalmetrics_quotes_latest()

    assert ei.value.status_code == 429
    assert ei.value.headers.get("Retry-After") == "5"


def test_error_headers_on_undocumented_error_endpoint():
    """Endpoint that does NOT model its error schema (GET /v3/cryptocurrency/quotes/latest).

    Regression guard: previously these hit ``raise_on_unexpected_status`` →
    ``UnexpectedStatus`` (no headers), so ``CMCError.headers`` was always ``{}``
    and ``Retry-After`` was lost. ~30% of endpoints are in this class.
    """
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(429, headers={"Retry-After": "13"}, json=_err_body("rate limited"))

    cmc = _make_client(handler)
    with pytest.raises(RateLimitError) as ei:
        cmc.cryptocurrency.quotes_latest(symbol="BTC")

    assert ei.value.status_code == 429
    assert ei.value.headers.get("Retry-After") == "13"


def test_async_error_headers_on_undocumented_error_endpoint():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(429, headers={"Retry-After": "17"}, json=_err_body("rate limited"))

    cmc = _make_client(handler)

    async def run():
        return await cmc.cryptocurrency.async_quotes_latest(symbol="BTC")

    with pytest.raises(RateLimitError) as ei:
        asyncio.run(run())
    assert ei.value.headers.get("Retry-After") == "17"


def test_async_method_awaits_and_maps():
    """async_* must resolve to the mapped error, not a bare coroutine."""

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(429, headers={"Retry-After": "9"}, json=_err_body("rate limited"))

    cmc = _make_client(handler)

    async def run():
        return await cmc.global_metrics.async_globalmetrics_quotes_latest()

    with pytest.raises(RateLimitError) as ei:
        asyncio.run(run())
    assert ei.value.headers.get("Retry-After") == "9"


def test_async_result_is_not_a_coroutine():
    """Guard the specific regression: awaiting must not yield another coroutine."""

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(429, json=_err_body("x"))

    cmc = _make_client(handler)

    async def run():
        try:
            return await cmc.global_metrics.async_globalmetrics_quotes_latest()
        except RateLimitError:
            return "raised"

    assert asyncio.run(run()) == "raised"
