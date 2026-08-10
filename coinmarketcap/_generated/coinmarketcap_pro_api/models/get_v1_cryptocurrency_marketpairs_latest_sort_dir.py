from typing import Literal, cast

GetV1CryptocurrencyMarketpairsLatestSortDir = Literal["asc", "desc"]

GET_V1_CRYPTOCURRENCY_MARKETPAIRS_LATEST_SORT_DIR_VALUES: set[GetV1CryptocurrencyMarketpairsLatestSortDir] = {
    "asc",
    "desc",
}


def check_get_v1_cryptocurrency_marketpairs_latest_sort_dir(value: str) -> GetV1CryptocurrencyMarketpairsLatestSortDir:
    if value in GET_V1_CRYPTOCURRENCY_MARKETPAIRS_LATEST_SORT_DIR_VALUES:
        return cast(GetV1CryptocurrencyMarketpairsLatestSortDir, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_MARKETPAIRS_LATEST_SORT_DIR_VALUES!r}"
    )
