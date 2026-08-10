from typing import Literal, cast

GetV5RealWorldAssetsMarketPairsListSort = Literal["price", "volume_24h"]

GET_V5_REAL_WORLD_ASSETS_MARKET_PAIRS_LIST_SORT_VALUES: set[GetV5RealWorldAssetsMarketPairsListSort] = {
    "price",
    "volume_24h",
}


def check_get_v5_real_world_assets_market_pairs_list_sort(value: str) -> GetV5RealWorldAssetsMarketPairsListSort:
    if value in GET_V5_REAL_WORLD_ASSETS_MARKET_PAIRS_LIST_SORT_VALUES:
        return cast(GetV5RealWorldAssetsMarketPairsListSort, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V5_REAL_WORLD_ASSETS_MARKET_PAIRS_LIST_SORT_VALUES!r}"
    )
