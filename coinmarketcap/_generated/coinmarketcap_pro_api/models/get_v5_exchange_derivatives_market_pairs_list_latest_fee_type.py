from typing import Literal, cast

GetV5ExchangeDerivativesMarketPairsListLatestFeeType = Literal[
    "all", "no-fees", "percentage", "transactional-mining", "unknown"
]

GET_V5_EXCHANGE_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_FEE_TYPE_VALUES: set[
    GetV5ExchangeDerivativesMarketPairsListLatestFeeType
] = {
    "all",
    "no-fees",
    "percentage",
    "transactional-mining",
    "unknown",
}


def check_get_v5_exchange_derivatives_market_pairs_list_latest_fee_type(
    value: str,
) -> GetV5ExchangeDerivativesMarketPairsListLatestFeeType:
    if value in GET_V5_EXCHANGE_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_FEE_TYPE_VALUES:
        return cast(GetV5ExchangeDerivativesMarketPairsListLatestFeeType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V5_EXCHANGE_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_FEE_TYPE_VALUES!r}"
    )
