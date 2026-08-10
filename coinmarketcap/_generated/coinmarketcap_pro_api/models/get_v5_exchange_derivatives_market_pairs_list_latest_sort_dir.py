from typing import Literal, cast

GetV5ExchangeDerivativesMarketPairsListLatestSortDir = Literal["asc", "desc"]

GET_V5_EXCHANGE_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_SORT_DIR_VALUES: set[
    GetV5ExchangeDerivativesMarketPairsListLatestSortDir
] = {
    "asc",
    "desc",
}


def check_get_v5_exchange_derivatives_market_pairs_list_latest_sort_dir(
    value: str,
) -> GetV5ExchangeDerivativesMarketPairsListLatestSortDir:
    if value in GET_V5_EXCHANGE_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_SORT_DIR_VALUES:
        return cast(GetV5ExchangeDerivativesMarketPairsListLatestSortDir, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V5_EXCHANGE_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_SORT_DIR_VALUES!r}"
    )
