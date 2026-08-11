"""CoinMarketCap Python SDK."""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _pkg_version

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

try:
    __version__ = _pkg_version("coinmarketcap-sdk")
except PackageNotFoundError:  # running from source without an installed dist
    __version__ = "0.0.0.dev0"

__all__ = [
    "__version__",
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
# PyPI package: pip install coinmarketcap-sdk
# Import as: from coinmarketcap import CoinMarketCap
