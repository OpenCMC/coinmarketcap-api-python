from typing import Literal, cast

GetV1ExchangeMarketpairsLatestCategory = Literal["all", "derivatives", "futures", "otc", "perpetual", "spot"]

GET_V1_EXCHANGE_MARKETPAIRS_LATEST_CATEGORY_VALUES: set[GetV1ExchangeMarketpairsLatestCategory] = {
    "all",
    "derivatives",
    "futures",
    "otc",
    "perpetual",
    "spot",
}


def check_get_v1_exchange_marketpairs_latest_category(value: str) -> GetV1ExchangeMarketpairsLatestCategory:
    if value in GET_V1_EXCHANGE_MARKETPAIRS_LATEST_CATEGORY_VALUES:
        return cast(GetV1ExchangeMarketpairsLatestCategory, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_EXCHANGE_MARKETPAIRS_LATEST_CATEGORY_VALUES!r}"
    )
