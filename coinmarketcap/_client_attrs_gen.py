"""Auto-generated typed namespace attributes — DO NOT EDIT."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._namespaces_gen import CmcIndexApi, CommunityApi, ContentApi, CryptoOthersApi, CryptocurrencyApi, DeprecatedApi, DerivativesApi, ExchangeApi, GlobalMetricsApi, HolderApi, OhlcvApi, PlatformApi, RealWorldAssetsApi, TokenApi, ToolsApi


class NamespacesMixin:
    """Typed namespace attributes for CoinMarketCap client."""

    cmc_index: CmcIndexApi
    community: CommunityApi
    content: ContentApi
    crypto_others: CryptoOthersApi
    cryptocurrency: CryptocurrencyApi
    deprecated: DeprecatedApi
    derivatives: DerivativesApi
    exchange: ExchangeApi
    global_metrics: GlobalMetricsApi
    holder: HolderApi
    ohlcv: OhlcvApi
    platform: PlatformApi
    real_world_assets: RealWorldAssetsApi
    token: TokenApi
    tools: ToolsApi



def init_namespaces(client: "CoinMarketCap") -> None:
    """Initialize namespace instances on the client."""
    from ._namespaces_gen import (
        CmcIndexApi,
        CommunityApi,
        ContentApi,
        CryptoOthersApi,
        CryptocurrencyApi,
        DeprecatedApi,
        DerivativesApi,
        ExchangeApi,
        GlobalMetricsApi,
        HolderApi,
        OhlcvApi,
        PlatformApi,
        RealWorldAssetsApi,
        TokenApi,
        ToolsApi,
    )
    client.cmc_index = CmcIndexApi(client)
    client.community = CommunityApi(client)
    client.content = ContentApi(client)
    client.crypto_others = CryptoOthersApi(client)
    client.cryptocurrency = CryptocurrencyApi(client)
    client.deprecated = DeprecatedApi(client)
    client.derivatives = DerivativesApi(client)
    client.exchange = ExchangeApi(client)
    client.global_metrics = GlobalMetricsApi(client)
    client.holder = HolderApi(client)
    client.ohlcv = OhlcvApi(client)
    client.platform = PlatformApi(client)
    client.real_world_assets = RealWorldAssetsApi(client)
    client.token = TokenApi(client)
    client.tools = ToolsApi(client)
