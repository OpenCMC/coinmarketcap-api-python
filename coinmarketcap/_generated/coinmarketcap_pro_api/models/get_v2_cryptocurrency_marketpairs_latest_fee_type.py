from typing import Literal, cast

GetV2CryptocurrencyMarketpairsLatestFeeType = Literal["all", "no-fees", "percentage", "transactional-mining", "unknown"]

GET_V2_CRYPTOCURRENCY_MARKETPAIRS_LATEST_FEE_TYPE_VALUES: set[GetV2CryptocurrencyMarketpairsLatestFeeType] = {
    "all",
    "no-fees",
    "percentage",
    "transactional-mining",
    "unknown",
}


def check_get_v2_cryptocurrency_marketpairs_latest_fee_type(value: str) -> GetV2CryptocurrencyMarketpairsLatestFeeType:
    if value in GET_V2_CRYPTOCURRENCY_MARKETPAIRS_LATEST_FEE_TYPE_VALUES:
        return cast(GetV2CryptocurrencyMarketpairsLatestFeeType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V2_CRYPTOCURRENCY_MARKETPAIRS_LATEST_FEE_TYPE_VALUES!r}"
    )
