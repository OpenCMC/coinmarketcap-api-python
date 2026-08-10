from typing import Literal, cast

GetV1ExchangeListingsLatestSortDir = Literal["asc", "desc"]

GET_V1_EXCHANGE_LISTINGS_LATEST_SORT_DIR_VALUES: set[GetV1ExchangeListingsLatestSortDir] = {
    "asc",
    "desc",
}


def check_get_v1_exchange_listings_latest_sort_dir(value: str) -> GetV1ExchangeListingsLatestSortDir:
    if value in GET_V1_EXCHANGE_LISTINGS_LATEST_SORT_DIR_VALUES:
        return cast(GetV1ExchangeListingsLatestSortDir, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_V1_EXCHANGE_LISTINGS_LATEST_SORT_DIR_VALUES!r}")
