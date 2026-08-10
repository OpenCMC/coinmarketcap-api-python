"""Tests for error hierarchy."""

from coinmarketcap._errors import (
    AuthenticationError,
    BadRequestError,
    CMCError,
    InternalServerError,
    RateLimitError,
    APITimeoutError,
    APIConnectionError,
)


def test_from_response_400():
    err = CMCError.from_response(400, {"message": "bad"}, {})
    assert isinstance(err, BadRequestError)
    assert err.status_code == 400


def test_from_response_401():
    err = CMCError.from_response(401, {}, {})
    assert isinstance(err, AuthenticationError)


def test_from_response_429():
    err = CMCError.from_response(429, {}, {})
    assert isinstance(err, RateLimitError)


def test_from_response_500():
    err = CMCError.from_response(502, {}, {})
    assert isinstance(err, InternalServerError)


def test_extracts_cmc_error_message():
    body = {"status": {"error_message": "API key invalid"}}
    err = CMCError.from_response(401, body, {})
    assert "API key invalid" in str(err)


def test_timeout_error():
    err = APITimeoutError(5.0)
    assert isinstance(err, APIConnectionError)
    assert "5.0s" in str(err)
    assert err.timeout == 5.0
