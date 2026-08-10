"""Tests for client HTTP assembly (sync/async base_url, auth, retry)."""

import httpx

from coinmarketcap import CoinMarketCap, ENVIRONMENTS
from coinmarketcap._transport import AsyncRetryTransport, RetryTransport


def test_sync_client_has_base_url_and_auth():
    cmc = CoinMarketCap(api_key="test-key")
    client = cmc._gen_client.get_httpx_client()

    assert str(client.base_url).rstrip("/") == ENVIRONMENTS["pro"]
    assert client.headers.get("X-CMC_PRO_API_KEY") == "test-key"


def test_async_client_has_base_url_and_auth():
    cmc = CoinMarketCap(api_key="test-key")
    client = cmc._gen_client.get_async_httpx_client()

    assert str(client.base_url).rstrip("/") == ENVIRONMENTS["pro"]
    assert client.headers.get("X-CMC_PRO_API_KEY") == "test-key"


def test_sync_uses_retry_transport():
    cmc = CoinMarketCap(api_key="test-key")
    client = cmc._gen_client.get_httpx_client()
    assert isinstance(client._transport, RetryTransport)


def test_async_uses_async_retry_transport():
    cmc = CoinMarketCap(api_key="test-key")
    client = cmc._gen_client.get_async_httpx_client()
    assert isinstance(client._transport, AsyncRetryTransport)


def test_public_mode_no_auth_header():
    cmc = CoinMarketCap(environment="public")
    client = cmc._gen_client.get_httpx_client()

    assert str(client.base_url).rstrip("/") == ENVIRONMENTS["public"]
    assert "X-CMC_PRO_API_KEY" not in client.headers


def test_sync_request_uses_absolute_url():
    """Verify sync client can build a valid request URL (not relative-only)."""
    cmc = CoinMarketCap(api_key="test-key")
    client = cmc._gen_client.get_httpx_client()
    req = client.build_request("GET", "/v1/cryptocurrency/map", params={"limit": 1})
    assert req.url.host == "pro-api.coinmarketcap.com"
