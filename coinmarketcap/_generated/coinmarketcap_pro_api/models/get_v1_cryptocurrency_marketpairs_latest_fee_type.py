from typing import Literal, cast

GetV1CryptocurrencyMarketpairsLatestFeeType = Literal["all", "no-fees", "percentage", "transactional-mining", "unknown"]

GET_V1_CRYPTOCURRENCY_MARKETPAIRS_LATEST_FEE_TYPE_VALUES: set[GetV1CryptocurrencyMarketpairsLatestFeeType] = {
    "all",
    "no-fees",
    "percentage",
    "transactional-mining",
    "unknown",
}


def check_get_v1_cryptocurrency_marketpairs_latest_fee_type(value: str) -> GetV1CryptocurrencyMarketpairsLatestFeeType:
    if value in GET_V1_CRYPTOCURRENCY_MARKETPAIRS_LATEST_FEE_TYPE_VALUES:
        return cast(GetV1CryptocurrencyMarketpairsLatestFeeType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_MARKETPAIRS_LATEST_FEE_TYPE_VALUES!r}"
    )
