from typing import Literal, cast

GetV5RealWorldAssetsAssetsListSort = Literal[
    "average_tokenized_price", "rwa_rank", "symbol", "tokenized_market_cap", "tokenized_volume_24h"
]

GET_V5_REAL_WORLD_ASSETS_ASSETS_LIST_SORT_VALUES: set[GetV5RealWorldAssetsAssetsListSort] = {
    "average_tokenized_price",
    "rwa_rank",
    "symbol",
    "tokenized_market_cap",
    "tokenized_volume_24h",
}


def check_get_v5_real_world_assets_assets_list_sort(value: str) -> GetV5RealWorldAssetsAssetsListSort:
    if value in GET_V5_REAL_WORLD_ASSETS_ASSETS_LIST_SORT_VALUES:
        return cast(GetV5RealWorldAssetsAssetsListSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_V5_REAL_WORLD_ASSETS_ASSETS_LIST_SORT_VALUES!r}")
