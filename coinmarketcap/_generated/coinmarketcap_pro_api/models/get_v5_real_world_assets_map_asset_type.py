from typing import Literal, cast

GetV5RealWorldAssetsMapAssetType = Literal[
    "commodity", "currency", "etf", "government_security", "real_estate", "stock"
]

GET_V5_REAL_WORLD_ASSETS_MAP_ASSET_TYPE_VALUES: set[GetV5RealWorldAssetsMapAssetType] = {
    "commodity",
    "currency",
    "etf",
    "government_security",
    "real_estate",
    "stock",
}


def check_get_v5_real_world_assets_map_asset_type(value: str) -> GetV5RealWorldAssetsMapAssetType:
    if value in GET_V5_REAL_WORLD_ASSETS_MAP_ASSET_TYPE_VALUES:
        return cast(GetV5RealWorldAssetsMapAssetType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_V5_REAL_WORLD_ASSETS_MAP_ASSET_TYPE_VALUES!r}")
