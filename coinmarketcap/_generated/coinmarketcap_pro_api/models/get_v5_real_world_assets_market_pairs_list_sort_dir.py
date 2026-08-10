from typing import Literal, cast

GetV5RealWorldAssetsMarketPairsListSortDir = Literal["asc", "desc"]

GET_V5_REAL_WORLD_ASSETS_MARKET_PAIRS_LIST_SORT_DIR_VALUES: set[GetV5RealWorldAssetsMarketPairsListSortDir] = {
    "asc",
    "desc",
}


def check_get_v5_real_world_assets_market_pairs_list_sort_dir(value: str) -> GetV5RealWorldAssetsMarketPairsListSortDir:
    if value in GET_V5_REAL_WORLD_ASSETS_MARKET_PAIRS_LIST_SORT_DIR_VALUES:
        return cast(GetV5RealWorldAssetsMarketPairsListSortDir, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V5_REAL_WORLD_ASSETS_MARKET_PAIRS_LIST_SORT_DIR_VALUES!r}"
    )
