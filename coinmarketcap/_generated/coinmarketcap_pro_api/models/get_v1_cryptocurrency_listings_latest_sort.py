from typing import Literal, cast

GetV1CryptocurrencyListingsLatestSort = Literal[
    "circulating_supply",
    "date_added",
    "market_cap",
    "market_cap_by_total_supply_strict",
    "market_cap_strict",
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
    "volume_30d",
    "volume_7d",
]

GET_V1_CRYPTOCURRENCY_LISTINGS_LATEST_SORT_VALUES: set[GetV1CryptocurrencyListingsLatestSort] = {
    "circulating_supply",
    "date_added",
    "market_cap",
    "market_cap_by_total_supply_strict",
    "market_cap_strict",
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
    "volume_30d",
    "volume_7d",
}


def check_get_v1_cryptocurrency_listings_latest_sort(value: str) -> GetV1CryptocurrencyListingsLatestSort:
    if value in GET_V1_CRYPTOCURRENCY_LISTINGS_LATEST_SORT_VALUES:
        return cast(GetV1CryptocurrencyListingsLatestSort, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_LISTINGS_LATEST_SORT_VALUES!r}"
    )
