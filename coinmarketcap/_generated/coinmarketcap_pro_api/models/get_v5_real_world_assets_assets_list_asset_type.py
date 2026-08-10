from typing import Literal, cast

GetV5RealWorldAssetsAssetsListAssetType = Literal[
    "commodity", "currency", "etf", "government_security", "real_estate", "stock"
]

GET_V5_REAL_WORLD_ASSETS_ASSETS_LIST_ASSET_TYPE_VALUES: set[GetV5RealWorldAssetsAssetsListAssetType] = {
    "commodity",
    "currency",
    "etf",
    "government_security",
    "real_estate",
    "stock",
}


def check_get_v5_real_world_assets_assets_list_asset_type(value: str) -> GetV5RealWorldAssetsAssetsListAssetType:
    if value in GET_V5_REAL_WORLD_ASSETS_ASSETS_LIST_ASSET_TYPE_VALUES:
        return cast(GetV5RealWorldAssetsAssetsListAssetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V5_REAL_WORLD_ASSETS_ASSETS_LIST_ASSET_TYPE_VALUES!r}"
    )
