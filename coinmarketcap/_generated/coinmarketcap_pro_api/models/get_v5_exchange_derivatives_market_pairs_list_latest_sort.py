from typing import Literal, cast

GetV5ExchangeDerivativesMarketPairsListLatestSort = Literal[
    "cmc_rank", "cmc_rank_advanced", "effective_liquidity", "volume_24h_strict"
]

GET_V5_EXCHANGE_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_SORT_VALUES: set[
    GetV5ExchangeDerivativesMarketPairsListLatestSort
] = {
    "cmc_rank",
    "cmc_rank_advanced",
    "effective_liquidity",
    "volume_24h_strict",
}


def check_get_v5_exchange_derivatives_market_pairs_list_latest_sort(
    value: str,
) -> GetV5ExchangeDerivativesMarketPairsListLatestSort:
    if value in GET_V5_EXCHANGE_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_SORT_VALUES:
        return cast(GetV5ExchangeDerivativesMarketPairsListLatestSort, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V5_EXCHANGE_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_SORT_VALUES!r}"
    )
