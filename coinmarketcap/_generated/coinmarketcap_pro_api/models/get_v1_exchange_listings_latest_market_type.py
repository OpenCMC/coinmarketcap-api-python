from typing import Literal, cast

GetV1ExchangeListingsLatestMarketType = Literal["all", "fees", "no_fees"]

GET_V1_EXCHANGE_LISTINGS_LATEST_MARKET_TYPE_VALUES: set[GetV1ExchangeListingsLatestMarketType] = {
    "all",
    "fees",
    "no_fees",
}


def check_get_v1_exchange_listings_latest_market_type(value: str) -> GetV1ExchangeListingsLatestMarketType:
    if value in GET_V1_EXCHANGE_LISTINGS_LATEST_MARKET_TYPE_VALUES:
        return cast(GetV1ExchangeListingsLatestMarketType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_EXCHANGE_LISTINGS_LATEST_MARKET_TYPE_VALUES!r}"
    )
