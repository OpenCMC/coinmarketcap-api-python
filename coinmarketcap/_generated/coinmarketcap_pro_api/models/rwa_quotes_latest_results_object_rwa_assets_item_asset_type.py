from typing import Literal, cast

RWAQuotesLatestResultsObjectRwaAssetsItemAssetType = Literal[
    "commodity", "currency", "etf", "government_security", "real_estate", "stock"
]

RWA_QUOTES_LATEST_RESULTS_OBJECT_RWA_ASSETS_ITEM_ASSET_TYPE_VALUES: set[
    RWAQuotesLatestResultsObjectRwaAssetsItemAssetType
] = {
    "commodity",
    "currency",
    "etf",
    "government_security",
    "real_estate",
    "stock",
}


def check_rwa_quotes_latest_results_object_rwa_assets_item_asset_type(
    value: str,
) -> RWAQuotesLatestResultsObjectRwaAssetsItemAssetType:
    if value in RWA_QUOTES_LATEST_RESULTS_OBJECT_RWA_ASSETS_ITEM_ASSET_TYPE_VALUES:
        return cast(RWAQuotesLatestResultsObjectRwaAssetsItemAssetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RWA_QUOTES_LATEST_RESULTS_OBJECT_RWA_ASSETS_ITEM_ASSET_TYPE_VALUES!r}"
    )
