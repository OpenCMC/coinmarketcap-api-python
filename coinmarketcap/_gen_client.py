"""Generated client subclasses with retry transport injection."""

from __future__ import annotations

from typing import Any

import httpx
from attrs import define, field

from coinmarketcap._generated.coinmarketcap_pro_api.client import (
    AuthenticatedClient,
    Client,
)
from coinmarketcap._retry import RetryConfig
from coinmarketcap._transport import AsyncRetryTransport, RetryTransport


@define
class RetryClient(Client):
    """Client subclass that injects retry transports."""

    _retry_config: RetryConfig = field(factory=RetryConfig, init=False)

    def get_httpx_client(self) -> httpx.Client:
        if self._client is None:
            self._client = httpx.Client(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                transport=RetryTransport(retry_config=self._retry_config),
                **self._httpx_args,
            )
        return self._client

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        if self._async_client is None:
            self._async_client = httpx.AsyncClient(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                transport=AsyncRetryTransport(retry_config=self._retry_config),
                **self._httpx_args,
            )
        return self._async_client


@define
class RetryAuthenticatedClient(AuthenticatedClient):
    """Authenticated client subclass that injects retry transports."""

    _retry_config: RetryConfig = field(factory=RetryConfig, init=False)

    def get_httpx_client(self) -> httpx.Client:
        if self._client is None:
            self._headers[self.auth_header_name] = (
                f"{self.prefix} {self.token}" if self.prefix else self.token
            )
            self._client = httpx.Client(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                transport=RetryTransport(retry_config=self._retry_config),
                **self._httpx_args,
            )
        return self._client

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        if self._async_client is None:
            self._headers[self.auth_header_name] = (
                f"{self.prefix} {self.token}" if self.prefix else self.token
            )
            self._async_client = httpx.AsyncClient(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                transport=AsyncRetryTransport(retry_config=self._retry_config),
                **self._httpx_args,
            )
        return self._async_client


def create_retry_client(
    api_key: str | None,
    base_url: str,
    timeout: float,
    max_retries: int,
    httpx_kwargs: dict[str, Any],
) -> RetryAuthenticatedClient | RetryClient:
    """Create a generated client with retry, base_url, and auth configured."""
    retry_config = RetryConfig(max_retries=max_retries)
    client_kwargs: dict[str, Any] = {
        "base_url": base_url,
        "timeout": httpx.Timeout(timeout),
        "raise_on_unexpected_status": True,
        "httpx_args": httpx_kwargs,
    }

    if api_key:
        client = RetryAuthenticatedClient(
            token=api_key,
            prefix="",
            auth_header_name="X-CMC_PRO_API_KEY",
            **client_kwargs,
        )
    else:
        client = RetryClient(**client_kwargs)

    client._retry_config = retry_config
    return client
