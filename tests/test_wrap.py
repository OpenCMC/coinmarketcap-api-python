"""Tests for wrap_call error conversion."""

import pytest

from coinmarketcap._errors import AuthenticationError, CMCError, RateLimitError
from coinmarketcap._wrap import wrap_call


def test_wrap_call_raises_on_unexpected_status():
    from coinmarketcap._generated.coinmarketcap_pro_api.errors import UnexpectedStatus

    def fn():
        raise UnexpectedStatus(401, b'{"status":{"error_message":"Invalid API key"}}')

    with pytest.raises(AuthenticationError):
        wrap_call(fn)


def test_wrap_call_raises_on_error_object():
    from coinmarketcap._generated.coinmarketcap_pro_api.models import HTTPStatus429ErrorObject

    def fn():
        return HTTPStatus429ErrorObject()

    with pytest.raises(RateLimitError):
        wrap_call(fn)


def test_wrap_call_returns_success():
    def fn():
        return {"status": {"error_code": 0}, "data": [1, 2, 3]}

    assert wrap_call(fn) == {"status": {"error_code": 0}, "data": [1, 2, 3]}


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
    from coinmarketcap.models import DqueryBatchPriceRequestDTO, CryptoQuoteV3DTO

    assert DqueryBatchPriceRequestDTO is not None
    assert CryptoQuoteV3DTO is not None
