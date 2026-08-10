from typing import Literal, cast

GetV1ExchangeListingsLatestCategory = Literal["all", "derivatives", "dex", "lending", "spot"]

GET_V1_EXCHANGE_LISTINGS_LATEST_CATEGORY_VALUES: set[GetV1ExchangeListingsLatestCategory] = {
    "all",
    "derivatives",
    "dex",
    "lending",
    "spot",
}


def check_get_v1_exchange_listings_latest_category(value: str) -> GetV1ExchangeListingsLatestCategory:
    if value in GET_V1_EXCHANGE_LISTINGS_LATEST_CATEGORY_VALUES:
        return cast(GetV1ExchangeListingsLatestCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_V1_EXCHANGE_LISTINGS_LATEST_CATEGORY_VALUES!r}")
