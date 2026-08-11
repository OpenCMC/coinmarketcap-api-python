"""Tests for error hierarchy."""

from coinmarketcap._errors import (
    APIConnectionError,
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    CMCError,
    InternalServerError,
    RateLimitError,
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
    cause = TimeoutError("slow")
    err = APITimeoutError(cause=cause)
    assert isinstance(err, APIConnectionError)
    assert "timed out" in str(err).lower()
    assert err.cause is cause


def test_connection_error_carries_cause():
    cause = OSError("refused")
    err = APIConnectionError("Connection failed", cause=cause)
    assert err.cause is cause
    assert "Connection failed" in str(err)
