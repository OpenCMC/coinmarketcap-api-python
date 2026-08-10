"""CoinMarketCap Python SDK."""

from ._client import ENVIRONMENTS, CoinMarketCap
from ._errors import (
    APIConnectionError,
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    CMCError,
    ForbiddenError,
    InternalServerError,
    NotFoundError,
    PaymentRequiredError,
    RateLimitError,
)

__all__ = [
    "CoinMarketCap",
    "ENVIRONMENTS",
    "CMCError",
    "BadRequestError",
    "AuthenticationError",
    "PaymentRequiredError",
    "ForbiddenError",
    "NotFoundError",
    "RateLimitError",
    "InternalServerError",
    "APIConnectionError",
    "APITimeoutError",
]

# Models live in coinmarketcap.models (generated re-exports).
# Import explicitly: from coinmarketcap.models import DqueryBatchPriceRequestDTO
