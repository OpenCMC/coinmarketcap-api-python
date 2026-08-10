"""Typed error hierarchy for the CoinMarketCap SDK."""

from __future__ import annotations

from typing import Any


class CMCError(Exception):
    """Base error for all CoinMarketCap API errors."""

    status_code: int
    body: Any
    headers: dict[str, str]

    def __init__(
        self,
        status_code: int,
        body: Any = None,
        headers: dict[str, str] | None = None,
        message: str | None = None,
    ) -> None:
        self.status_code = status_code
        self.body = body
        self.headers = headers or {}
        super().__init__(message or f"Request failed with status {status_code}")

    @classmethod
    def from_response(cls, status_code: int, body: Any, headers: dict[str, str]) -> "CMCError":
        """Create the appropriate error subclass based on status code."""
        message = _extract_message(body)

        error_map: dict[int, type[CMCError]] = {
            400: BadRequestError,
            401: AuthenticationError,
            402: PaymentRequiredError,
            403: ForbiddenError,
            404: NotFoundError,
            429: RateLimitError,
        }

        error_cls = error_map.get(status_code)
        if error_cls:
            return error_cls(status_code, body, headers, message)
        if status_code >= 500:
            return InternalServerError(status_code, body, headers, message)
        return cls(status_code, body, headers, message)


class BadRequestError(CMCError):
    """400 — Invalid request parameters."""


class AuthenticationError(CMCError):
    """401 — API key is missing or invalid."""


class PaymentRequiredError(CMCError):
    """402 — API key's plan doesn't cover this endpoint."""


class ForbiddenError(CMCError):
    """403 — Access denied."""


class NotFoundError(CMCError):
    """404 — Resource not found."""


class RateLimitError(CMCError):
    """429 — Too many requests."""


class InternalServerError(CMCError):
    """5xx — Server-side error."""


class APIConnectionError(Exception):
    """Network-level connection failure."""

    def __init__(self, message: str = "Connection failed", cause: BaseException | None = None) -> None:
        self.cause = cause
        super().__init__(message)


class APITimeoutError(APIConnectionError):
    """Request timed out."""

    def __init__(self, timeout: float) -> None:
        self.timeout = timeout
        super().__init__(f"Request timed out after {timeout}s")


def _extract_message(body: Any) -> str | None:
    """Extract error message from CMC response body."""
    if isinstance(body, dict):
        status = body.get("status", {})
        if isinstance(status, dict):
            msg = status.get("error_message")
            if msg:
                return str(msg)
        msg = body.get("message") or body.get("error")
        if msg:
            return str(msg)
    return None
