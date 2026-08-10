from typing import Literal, cast

RWAAssetListResultsObjectRwaAssetsItemAssetType = Literal[
    "commodity", "currency", "etf", "government_security", "real_estate", "stock"
]

RWA_ASSET_LIST_RESULTS_OBJECT_RWA_ASSETS_ITEM_ASSET_TYPE_VALUES: set[
    RWAAssetListResultsObjectRwaAssetsItemAssetType
] = {
    "commodity",
    "currency",
    "etf",
    "government_security",
    "real_estate",
    "stock",
}


def check_rwa_asset_list_results_object_rwa_assets_item_asset_type(
    value: str,
) -> RWAAssetListResultsObjectRwaAssetsItemAssetType:
    if value in RWA_ASSET_LIST_RESULTS_OBJECT_RWA_ASSETS_ITEM_ASSET_TYPE_VALUES:
        return cast(RWAAssetListResultsObjectRwaAssetsItemAssetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RWA_ASSET_LIST_RESULTS_OBJECT_RWA_ASSETS_ITEM_ASSET_TYPE_VALUES!r}"
    )
