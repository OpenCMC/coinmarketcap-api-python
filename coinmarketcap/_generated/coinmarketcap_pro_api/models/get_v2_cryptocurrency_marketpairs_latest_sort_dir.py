from typing import Literal, cast

GetV2CryptocurrencyMarketpairsLatestSortDir = Literal["asc", "desc"]

GET_V2_CRYPTOCURRENCY_MARKETPAIRS_LATEST_SORT_DIR_VALUES: set[GetV2CryptocurrencyMarketpairsLatestSortDir] = {
    "asc",
    "desc",
}


def check_get_v2_cryptocurrency_marketpairs_latest_sort_dir(value: str) -> GetV2CryptocurrencyMarketpairsLatestSortDir:
    if value in GET_V2_CRYPTOCURRENCY_MARKETPAIRS_LATEST_SORT_DIR_VALUES:
        return cast(GetV2CryptocurrencyMarketpairsLatestSortDir, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V2_CRYPTOCURRENCY_MARKETPAIRS_LATEST_SORT_DIR_VALUES!r}"
    )
