"""Retry logic with exponential backoff and jitter."""

from __future__ import annotations

import asyncio
import random
import time
from dataclasses import dataclass, field


@dataclass(frozen=True)
class RetryConfig:
    max_retries: int = 2
    retryable_statuses: frozenset[int] = field(
        default_factory=lambda: frozenset({408, 409, 429, 500, 502, 503, 504})
    )
    initial_delay: float = 0.5
    max_delay: float = 8.0


DEFAULT_RETRY = RetryConfig()


def should_retry(status_code: int, config: RetryConfig) -> bool:
    return status_code in config.retryable_statuses


def get_retry_delay(
    attempt: int,
    status_code: int,
    config: RetryConfig,
    headers: dict[str, str] | None = None,
) -> float:
    """Calculate delay before next retry attempt."""
    if status_code == 429 and headers:
        retry_after = headers.get("retry-after") or headers.get("Retry-After")
        if retry_after:
            try:
                return float(retry_after)
            except ValueError:
                pass

    base = config.initial_delay * (2**attempt)
    jitter = random.random() * 0.5 * base
    return min(base + jitter, config.max_delay)


def sleep_sync(seconds: float) -> None:
    time.sleep(seconds)


async def sleep_async(seconds: float) -> None:
    await asyncio.sleep(seconds)
