from typing import Literal, cast

GetV1CryptocurrencyListingsHistoricalSort = Literal[
    "circulating_supply",
    "cmc_rank",
    "market_cap",
    "max_supply",
    "name",
    "num_market_pairs",
    "percent_change_1h",
    "percent_change_24h",
    "percent_change_7d",
    "price",
    "symbol",
    "total_supply",
    "volume_24h",
]

GET_V1_CRYPTOCURRENCY_LISTINGS_HISTORICAL_SORT_VALUES: set[GetV1CryptocurrencyListingsHistoricalSort] = {
    "circulating_supply",
    "cmc_rank",
    "market_cap",
    "max_supply",
    "name",
    "num_market_pairs",
    "percent_change_1h",
    "percent_change_24h",
    "percent_change_7d",
    "price",
    "symbol",
    "total_supply",
    "volume_24h",
}


def check_get_v1_cryptocurrency_listings_historical_sort(value: str) -> GetV1CryptocurrencyListingsHistoricalSort:
    if value in GET_V1_CRYPTOCURRENCY_LISTINGS_HISTORICAL_SORT_VALUES:
        return cast(GetV1CryptocurrencyListingsHistoricalSort, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_LISTINGS_HISTORICAL_SORT_VALUES!r}"
    )
