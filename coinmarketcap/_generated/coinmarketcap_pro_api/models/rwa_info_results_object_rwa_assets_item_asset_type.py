from typing import Literal, cast

RWAInfoResultsObjectRwaAssetsItemAssetType = Literal[
    "commodity", "currency", "etf", "government_security", "real_estate", "stock"
]

RWA_INFO_RESULTS_OBJECT_RWA_ASSETS_ITEM_ASSET_TYPE_VALUES: set[RWAInfoResultsObjectRwaAssetsItemAssetType] = {
    "commodity",
    "currency",
    "etf",
    "government_security",
    "real_estate",
    "stock",
}


def check_rwa_info_results_object_rwa_assets_item_asset_type(value: str) -> RWAInfoResultsObjectRwaAssetsItemAssetType:
    if value in RWA_INFO_RESULTS_OBJECT_RWA_ASSETS_ITEM_ASSET_TYPE_VALUES:
        return cast(RWAInfoResultsObjectRwaAssetsItemAssetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RWA_INFO_RESULTS_OBJECT_RWA_ASSETS_ITEM_ASSET_TYPE_VALUES!r}"
    )
