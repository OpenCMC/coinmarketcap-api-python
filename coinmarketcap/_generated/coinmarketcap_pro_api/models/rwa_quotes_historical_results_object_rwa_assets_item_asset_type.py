from typing import Literal, cast

RWAQuotesHistoricalResultsObjectRwaAssetsItemAssetType = Literal[
    "commodity", "currency", "etf", "government_security", "real_estate", "stock"
]

RWA_QUOTES_HISTORICAL_RESULTS_OBJECT_RWA_ASSETS_ITEM_ASSET_TYPE_VALUES: set[
    RWAQuotesHistoricalResultsObjectRwaAssetsItemAssetType
] = {
    "commodity",
    "currency",
    "etf",
    "government_security",
    "real_estate",
    "stock",
}


def check_rwa_quotes_historical_results_object_rwa_assets_item_asset_type(
    value: str,
) -> RWAQuotesHistoricalResultsObjectRwaAssetsItemAssetType:
    if value in RWA_QUOTES_HISTORICAL_RESULTS_OBJECT_RWA_ASSETS_ITEM_ASSET_TYPE_VALUES:
        return cast(RWAQuotesHistoricalResultsObjectRwaAssetsItemAssetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RWA_QUOTES_HISTORICAL_RESULTS_OBJECT_RWA_ASSETS_ITEM_ASSET_TYPE_VALUES!r}"
    )
