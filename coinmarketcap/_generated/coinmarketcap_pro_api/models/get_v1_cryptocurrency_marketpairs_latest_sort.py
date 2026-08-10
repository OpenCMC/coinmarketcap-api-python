from typing import Literal, cast

GetV1CryptocurrencyMarketpairsLatestSort = Literal[
    "cmc_rank", "cmc_rank_advanced", "effective_liquidity", "market_reputation", "market_score", "volume_24h_strict"
]

GET_V1_CRYPTOCURRENCY_MARKETPAIRS_LATEST_SORT_VALUES: set[GetV1CryptocurrencyMarketpairsLatestSort] = {
    "cmc_rank",
    "cmc_rank_advanced",
    "effective_liquidity",
    "market_reputation",
    "market_score",
    "volume_24h_strict",
}


def check_get_v1_cryptocurrency_marketpairs_latest_sort(value: str) -> GetV1CryptocurrencyMarketpairsLatestSort:
    if value in GET_V1_CRYPTOCURRENCY_MARKETPAIRS_LATEST_SORT_VALUES:
        return cast(GetV1CryptocurrencyMarketpairsLatestSort, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_MARKETPAIRS_LATEST_SORT_VALUES!r}"
    )
