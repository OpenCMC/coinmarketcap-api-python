"""Wrap generated API calls with typed error conversion.

The generated ``*_detailed`` functions return a ``Response`` carrying
``status_code``, ``headers``, ``content`` and ``parsed`` (the typed body, a
typed error model, or ``None`` for endpoints that do not model their errors).
The retry client is configured with ``raise_on_unexpected_status=False`` so a
``Response`` is always returned — even on 4xx/5xx — and we map errors here:

* any 4xx/5xx becomes a typed ``CMCError`` subclass **with response headers**
  (e.g. ``Retry-After`` on 429), keyed off the HTTP status code so it holds
  uniformly whether or not the endpoint modelled its error body;
* transport failures become ``APITimeoutError`` / ``APIConnectionError`` so the
  documented exception contract actually holds.

``UnexpectedStatus`` is still handled defensively in case a client is built with
``raise_on_unexpected_status=True``, but is not part of the normal path.
"""

from __future__ import annotations

import json as _json
import re
from collections.abc import Awaitable, Callable
from typing import Any, TypeVar

import httpx

from ._errors import APIConnectionError, APITimeoutError, CMCError

T = TypeVar("T")


def _decode_body(content: bytes | str | None) -> Any:
    if content is None:
        return None
    try:
        return _json.loads(content)
    except Exception:
        return content


def _handle_detailed(response: Any) -> Any:
    """Turn a generated ``Response`` into a parsed body or raise ``CMCError``.

    Error detection is driven by the HTTP status code on the ``Response`` — not
    by whether the generated endpoint happened to model its error bodies. Only
    ~70% of endpoints declare error schemas; the rest return ``parsed=None`` on
    failure. Keying off ``status_code`` means the raised ``CMCError`` always
    carries the real response ``headers`` (e.g. ``Retry-After`` on 429),
    uniformly across every endpoint.
    """
    raw_headers = getattr(response, "headers", None)
    # httpx.Headers is case-insensitive, so ``err.headers.get("Retry-After")``
    # works regardless of the wire casing.
    headers = httpx.Headers(raw_headers) if raw_headers is not None else httpx.Headers()

    status_code = getattr(response, "status_code", None)
    status = int(status_code) if status_code is not None else 0

    parsed = getattr(response, "parsed", None)

    if status >= 400:
        # Prefer a typed error model's dict form when the endpoint modelled it;
        # otherwise fall back to decoding the raw response body.
        if parsed is not None and hasattr(parsed, "to_dict"):
            body = parsed.to_dict()
        else:
            body = _decode_body(getattr(response, "content", None))
        raise CMCError.from_response(status, body, headers)

    return parsed


def _raise_unexpected(exc: Any) -> None:
    body = _decode_body(getattr(exc, "content", None))
    raise CMCError.from_response(exc.status_code, body, {}) from exc


def wrap_call(fn: Callable[..., T], *args: Any, **kwargs: Any) -> Any:
    """Call a generated ``*_detailed`` sync function and normalize errors."""
    from coinmarketcap._generated.coinmarketcap_pro_api.errors import UnexpectedStatus

    try:
        response = fn(*args, **kwargs)
    except httpx.TimeoutException as e:
        raise APITimeoutError(cause=e) from e
    except httpx.TransportError as e:
        raise APIConnectionError(str(e) or "Connection failed", cause=e) from e
    except UnexpectedStatus as e:
        _raise_unexpected(e)

    return _handle_detailed(response)


async def wrap_call_async(fn: Callable[..., Awaitable[T]], *args: Any, **kwargs: Any) -> Any:
    """Call a generated ``*_detailed`` async function and normalize errors."""
    from coinmarketcap._generated.coinmarketcap_pro_api.errors import UnexpectedStatus

    try:
        response = await fn(*args, **kwargs)
    except httpx.TimeoutException as e:
        raise APITimeoutError(cause=e) from e
    except httpx.TransportError as e:
        raise APIConnectionError(str(e) or "Connection failed", cause=e) from e
    except UnexpectedStatus as e:
        _raise_unexpected(e)

    return _handle_detailed(response)


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
