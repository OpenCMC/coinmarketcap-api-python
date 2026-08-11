"""Tests for wrap_call error conversion."""

from types import SimpleNamespace

import pytest

from coinmarketcap._errors import AuthenticationError, RateLimitError
from coinmarketcap._wrap import wrap_call


def _response(parsed=None, status_code=200, headers=None, content=None):
    """A stand-in for the generated ``Response`` (status_code drives errors)."""
    return SimpleNamespace(
        parsed=parsed, status_code=status_code, headers=headers or {}, content=content
    )


def test_wrap_call_raises_on_unexpected_status():
    from coinmarketcap._generated.coinmarketcap_pro_api.errors import UnexpectedStatus

    def fn():
        raise UnexpectedStatus(401, b'{"status":{"error_message":"Invalid API key"}}')

    with pytest.raises(AuthenticationError):
        wrap_call(fn)


def test_wrap_call_raises_on_error_object():
    from coinmarketcap._generated.coinmarketcap_pro_api.models import HTTPStatus429ErrorObject

    def fn():
        return _response(parsed=HTTPStatus429ErrorObject(), status_code=429)

    with pytest.raises(RateLimitError):
        wrap_call(fn)


def test_wrap_call_returns_success():
    payload = {"status": {"error_code": 0}, "data": [1, 2, 3]}

    def fn():
        return _response(parsed=payload, status_code=200)

    assert wrap_call(fn) == payload


def test_clean_return_type_strips_error_unions():
    from coinmarketcap._wrap import clean_return_type

    raw = (
        "ApiResponseOfIndexLatestResponseDTO | HTTPStatus400ErrorObject"
        " | HTTPStatus401ErrorObject | HTTPStatus429ErrorObject | None"
    )
    cleaned = clean_return_type(raw)
    assert "HTTPStatus" not in cleaned
    assert "None" not in cleaned
    assert cleaned == "ApiResponseOfIndexLatestResponseDTO"


def test_models_public_import():
    from coinmarketcap.models import CryptoQuoteV3DTO, DqueryBatchPriceRequestDTO

    assert DqueryBatchPriceRequestDTO is not None
    assert CryptoQuoteV3DTO is not None
