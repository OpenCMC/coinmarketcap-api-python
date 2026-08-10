"""Retry transports for sync and async httpx clients."""

from __future__ import annotations

import httpx

from ._retry import RetryConfig, get_retry_delay, should_retry, sleep_async, sleep_sync


class RetryTransport(httpx.BaseTransport):
    """Sync httpx transport that retries on transient status codes."""

    def __init__(
        self,
        transport: httpx.BaseTransport | None = None,
        retry_config: RetryConfig | None = None,
    ) -> None:
        self._transport = transport or httpx.HTTPTransport()
        self._retry_config = retry_config or RetryConfig()

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        last_response: httpx.Response | None = None
        last_error: BaseException | None = None

        for attempt in range(self._retry_config.max_retries + 1):
            try:
                response = self._transport.handle_request(request)

                if response.status_code < 400 or not should_retry(
                    response.status_code, self._retry_config
                ):
                    return response

                last_response = response
                if attempt < self._retry_config.max_retries:
                    delay = get_retry_delay(
                        attempt,
                        response.status_code,
                        self._retry_config,
                        dict(response.headers),
                    )
                    sleep_sync(delay)

            except (httpx.ConnectError, httpx.TimeoutException) as e:
                last_error = e
                if attempt < self._retry_config.max_retries:
                    delay = get_retry_delay(attempt, 0, self._retry_config)
                    sleep_sync(delay)

        if last_response is not None:
            return last_response
        if last_error is not None:
            raise last_error
        raise httpx.ConnectError("Request failed")  # pragma: no cover

    def close(self) -> None:
        self._transport.close()


class AsyncRetryTransport(httpx.AsyncBaseTransport):
    """Async httpx transport that retries on transient status codes."""

    def __init__(
        self,
        transport: httpx.AsyncBaseTransport | None = None,
        retry_config: RetryConfig | None = None,
    ) -> None:
        self._transport = transport or httpx.AsyncHTTPTransport()
        self._retry_config = retry_config or RetryConfig()

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        last_response: httpx.Response | None = None
        last_error: BaseException | None = None

        for attempt in range(self._retry_config.max_retries + 1):
            try:
                response = await self._transport.handle_async_request(request)

                if response.status_code < 400 or not should_retry(
                    response.status_code, self._retry_config
                ):
                    return response

                last_response = response
                if attempt < self._retry_config.max_retries:
                    delay = get_retry_delay(
                        attempt,
                        response.status_code,
                        self._retry_config,
                        dict(response.headers),
                    )
                    await sleep_async(delay)

            except (httpx.ConnectError, httpx.TimeoutException) as e:
                last_error = e
                if attempt < self._retry_config.max_retries:
                    delay = get_retry_delay(attempt, 0, self._retry_config)
                    await sleep_async(delay)

        if last_response is not None:
            return last_response
        if last_error is not None:
            raise last_error
        raise httpx.ConnectError("Request failed")  # pragma: no cover

    async def aclose(self) -> None:
        await self._transport.aclose()
