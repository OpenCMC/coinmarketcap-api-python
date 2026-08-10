from typing import Literal, cast

GetV1ExchangeListingsLatestSort = Literal["exchange_score", "name", "volume_24h", "volume_24h_adjusted"]

GET_V1_EXCHANGE_LISTINGS_LATEST_SORT_VALUES: set[GetV1ExchangeListingsLatestSort] = {
    "exchange_score",
    "name",
    "volume_24h",
    "volume_24h_adjusted",
}


def check_get_v1_exchange_listings_latest_sort(value: str) -> GetV1ExchangeListingsLatestSort:
    if value in GET_V1_EXCHANGE_LISTINGS_LATEST_SORT_VALUES:
        return cast(GetV1ExchangeListingsLatestSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_V1_EXCHANGE_LISTINGS_LATEST_SORT_VALUES!r}")
