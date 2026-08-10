"""Wrap generated API calls with typed error conversion."""

from __future__ import annotations

import re
from typing import Any, Callable, TypeVar

from ._errors import CMCError

T = TypeVar("T")

# Map generated error model class names to HTTP status codes.
_ERROR_TYPE_STATUS: dict[str, int] = {
    "HTTPStatus400ErrorObject": 400,
    "HTTPStatus401ErrorObject": 401,
    "HTTPStatus402ErrorObject": 402,
    "HTTPStatus403ErrorObject": 403,
    "HTTPStatus404ErrorObject": 404,
    "HTTPStatus429ErrorObject": 429,
    "HTTPStatus500ErrorObject": 500,
}


def _status_from_error_object(result: Any) -> int | None:
    """Extract HTTP status code from a generated error response object."""
    return _ERROR_TYPE_STATUS.get(type(result).__name__)


def wrap_call(fn: Callable[..., T], *args: Any, **kwargs: Any) -> T:
    """Call a generated sync/async function and raise typed CMCError on failure."""
    from coinmarketcap._generated.coinmarketcap_pro_api.errors import UnexpectedStatus

    try:
        result = fn(*args, **kwargs)
    except UnexpectedStatus as e:
        try:
            import json as _json
            body = _json.loads(e.content)
        except Exception:
            body = e.content
        raise CMCError.from_response(e.status_code, body, {}) from e

    if result is not None:
        status = _status_from_error_object(result)
        if status is not None:
            body = result.to_dict() if hasattr(result, "to_dict") else result
            raise CMCError.from_response(status, body, {})

    return result


def clean_return_type(return_type: str) -> str:
    """Strip HTTPStatus error types and redundant None from return annotations."""
    parts = [p.strip() for p in return_type.split("|")]
    cleaned = [
        p for p in parts
        if not re.fullmatch(r"HTTPStatus\d+ErrorObject", p)
        and p != "None"
    ]
    if not cleaned:
        return return_type
    return " | ".join(cleaned)
