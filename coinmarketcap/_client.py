"""CoinMarketCap SDK client with authentication, retry, and environment support."""

from __future__ import annotations

from typing import Any, Literal

from ._client_attrs_gen import NamespacesMixin, init_namespaces
from ._gen_client import RetryAuthenticatedClient, RetryClient, create_retry_client

Environment = Literal["pro", "public"]

ENVIRONMENTS: dict[Environment, str] = {
    "pro": "https://pro-api.coinmarketcap.com",
    "public": "https://pro-api.coinmarketcap.com/public-api",
}


class CoinMarketCap(NamespacesMixin):
    """CoinMarketCap API client.

    Wraps openapi-python-client generated code with authentication,
    retry, timeout, and typed namespace access.
    """

    _gen_client: RetryAuthenticatedClient | RetryClient

    def __init__(
        self,
        api_key: str | None = None,
        *,
        environment: Environment = "pro",
        base_url: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 2,
        **httpx_kwargs: Any,
    ) -> None:
        if environment == "pro" and not api_key:
            raise ValueError("api_key is required for pro environment")

        self._environment = environment
        self._base_url = base_url or ENVIRONMENTS[environment]
        self._timeout = timeout

        self._gen_client = create_retry_client(
            api_key, self._base_url, timeout, max_retries, httpx_kwargs
        )

        init_namespaces(self)

    @property
    def base_url(self) -> str:
        return self._base_url

    def close(self) -> None:
        """Close underlying HTTP connections."""
        self._gen_client.get_httpx_client().close()

    async def aclose(self) -> None:
        """Close underlying async HTTP connections."""
        client = self._gen_client.get_async_httpx_client()
        if client:
            await client.aclose()

    def __enter__(self) -> CoinMarketCap:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    async def __aenter__(self) -> CoinMarketCap:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.aclose()
