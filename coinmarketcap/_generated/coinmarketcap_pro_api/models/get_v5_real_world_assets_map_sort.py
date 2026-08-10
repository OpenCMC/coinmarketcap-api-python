from typing import Literal, cast

GetV5RealWorldAssetsMapSort = Literal["name", "rwa_id", "rwa_rank"]

GET_V5_REAL_WORLD_ASSETS_MAP_SORT_VALUES: set[GetV5RealWorldAssetsMapSort] = {
    "name",
    "rwa_id",
    "rwa_rank",
}


def check_get_v5_real_world_assets_map_sort(value: str) -> GetV5RealWorldAssetsMapSort:
    if value in GET_V5_REAL_WORLD_ASSETS_MAP_SORT_VALUES:
        return cast(GetV5RealWorldAssetsMapSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_V5_REAL_WORLD_ASSETS_MAP_SORT_VALUES!r}")
