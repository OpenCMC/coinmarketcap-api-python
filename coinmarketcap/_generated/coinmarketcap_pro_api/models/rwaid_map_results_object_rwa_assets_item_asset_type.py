from typing import Literal, cast

RWAIDMapResultsObjectRwaAssetsItemAssetType = Literal[
    "commodity", "currency", "etf", "government_security", "real_estate", "stock"
]

RWAID_MAP_RESULTS_OBJECT_RWA_ASSETS_ITEM_ASSET_TYPE_VALUES: set[RWAIDMapResultsObjectRwaAssetsItemAssetType] = {
    "commodity",
    "currency",
    "etf",
    "government_security",
    "real_estate",
    "stock",
}


def check_rwaid_map_results_object_rwa_assets_item_asset_type(
    value: str,
) -> RWAIDMapResultsObjectRwaAssetsItemAssetType:
    if value in RWAID_MAP_RESULTS_OBJECT_RWA_ASSETS_ITEM_ASSET_TYPE_VALUES:
        return cast(RWAIDMapResultsObjectRwaAssetsItemAssetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RWAID_MAP_RESULTS_OBJECT_RWA_ASSETS_ITEM_ASSET_TYPE_VALUES!r}"
    )
