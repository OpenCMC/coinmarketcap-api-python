"""A client library for accessing CoinMarketCap Cryptocurrency API Documentation"""

from ._auth import create_client
from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
    "create_client",
)
