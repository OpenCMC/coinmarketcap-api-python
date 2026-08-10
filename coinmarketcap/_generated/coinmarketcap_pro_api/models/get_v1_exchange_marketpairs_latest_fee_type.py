from typing import Literal, cast

GetV1ExchangeMarketpairsLatestFeeType = Literal["all", "no-fees", "percentage", "transactional-mining", "unknown"]

GET_V1_EXCHANGE_MARKETPAIRS_LATEST_FEE_TYPE_VALUES: set[GetV1ExchangeMarketpairsLatestFeeType] = {
    "all",
    "no-fees",
    "percentage",
    "transactional-mining",
    "unknown",
}


def check_get_v1_exchange_marketpairs_latest_fee_type(value: str) -> GetV1ExchangeMarketpairsLatestFeeType:
    if value in GET_V1_EXCHANGE_MARKETPAIRS_LATEST_FEE_TYPE_VALUES:
        return cast(GetV1ExchangeMarketpairsLatestFeeType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_EXCHANGE_MARKETPAIRS_LATEST_FEE_TYPE_VALUES!r}"
    )
