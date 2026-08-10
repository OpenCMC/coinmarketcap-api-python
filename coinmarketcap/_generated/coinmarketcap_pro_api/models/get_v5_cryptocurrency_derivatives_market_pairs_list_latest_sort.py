from typing import Literal, cast

GetV5CryptocurrencyDerivativesMarketPairsListLatestSort = Literal[
    "cmc_rank", "cmc_rank_advanced", "effective_liquidity", "volume_24h_strict"
]

GET_V5_CRYPTOCURRENCY_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_SORT_VALUES: set[
    GetV5CryptocurrencyDerivativesMarketPairsListLatestSort
] = {
    "cmc_rank",
    "cmc_rank_advanced",
    "effective_liquidity",
    "volume_24h_strict",
}


def check_get_v5_cryptocurrency_derivatives_market_pairs_list_latest_sort(
    value: str,
) -> GetV5CryptocurrencyDerivativesMarketPairsListLatestSort:
    if value in GET_V5_CRYPTOCURRENCY_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_SORT_VALUES:
        return cast(GetV5CryptocurrencyDerivativesMarketPairsListLatestSort, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V5_CRYPTOCURRENCY_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_SORT_VALUES!r}"
    )
