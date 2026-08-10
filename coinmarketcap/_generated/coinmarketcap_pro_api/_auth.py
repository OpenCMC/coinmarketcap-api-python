"""Convenience factory for CoinMarketCap Pro API authentication."""

from .client import AuthenticatedClient


def create_client(
    api_key: str,
    base_url: str = "https://pro-api.coinmarketcap.com",
    **kwargs,
) -> AuthenticatedClient:
    """Create an authenticated CoinMarketCap Pro API client.

    Args:
        api_key: Your CoinMarketCap Pro API key.
        base_url: API base URL (override for sandbox/staging).
        **kwargs: Extra arguments forwarded to ``AuthenticatedClient``
                  (e.g. ``timeout``, ``follow_redirects``).

    Returns:
        A ready-to-use ``AuthenticatedClient``.

    Example::

        from coinmarketcap_pro_api import create_client

        client = create_client("your-api-key")
    """
    return AuthenticatedClient(
        base_url=base_url,
        token=api_key,
        prefix="",
        auth_header_name="X-CMC_PRO_API_KEY",
        **kwargs,
    )
