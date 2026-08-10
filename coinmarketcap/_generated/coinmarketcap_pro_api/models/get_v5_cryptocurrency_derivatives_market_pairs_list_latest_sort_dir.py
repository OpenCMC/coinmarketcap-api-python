from typing import Literal, cast

GetV5CryptocurrencyDerivativesMarketPairsListLatestSortDir = Literal["asc", "desc"]

GET_V5_CRYPTOCURRENCY_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_SORT_DIR_VALUES: set[
    GetV5CryptocurrencyDerivativesMarketPairsListLatestSortDir
] = {
    "asc",
    "desc",
}


def check_get_v5_cryptocurrency_derivatives_market_pairs_list_latest_sort_dir(
    value: str,
) -> GetV5CryptocurrencyDerivativesMarketPairsListLatestSortDir:
    if value in GET_V5_CRYPTOCURRENCY_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_SORT_DIR_VALUES:
        return cast(GetV5CryptocurrencyDerivativesMarketPairsListLatestSortDir, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V5_CRYPTOCURRENCY_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_SORT_DIR_VALUES!r}"
    )
