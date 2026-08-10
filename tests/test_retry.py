"""Tests for retry logic."""

from coinmarketcap._retry import DEFAULT_RETRY, get_retry_delay, should_retry


def test_should_retry_429():
    assert should_retry(429, DEFAULT_RETRY) is True


def test_should_retry_500():
    assert should_retry(500, DEFAULT_RETRY) is True


def test_should_not_retry_400():
    assert should_retry(400, DEFAULT_RETRY) is False


def test_should_not_retry_401():
    assert should_retry(401, DEFAULT_RETRY) is False


def test_retry_after_header():
    delay = get_retry_delay(0, 429, DEFAULT_RETRY, {"Retry-After": "3"})
    assert delay == 3.0


def test_exponential_backoff():
    d0 = get_retry_delay(0, 500, DEFAULT_RETRY)
    d1 = get_retry_delay(1, 500, DEFAULT_RETRY)
    assert d1 > d0


def test_caps_at_max():
    delay = get_retry_delay(10, 500, DEFAULT_RETRY)
    assert delay <= DEFAULT_RETRY.max_delay
