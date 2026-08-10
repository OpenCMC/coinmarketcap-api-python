from typing import Literal, cast

GetV5CryptocurrencyDerivativesMarketPairsListLatestFeeType = Literal[
    "all", "no-fees", "percentage", "transactional-mining", "unknown"
]

GET_V5_CRYPTOCURRENCY_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_FEE_TYPE_VALUES: set[
    GetV5CryptocurrencyDerivativesMarketPairsListLatestFeeType
] = {
    "all",
    "no-fees",
    "percentage",
    "transactional-mining",
    "unknown",
}


def check_get_v5_cryptocurrency_derivatives_market_pairs_list_latest_fee_type(
    value: str,
) -> GetV5CryptocurrencyDerivativesMarketPairsListLatestFeeType:
    if value in GET_V5_CRYPTOCURRENCY_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_FEE_TYPE_VALUES:
        return cast(GetV5CryptocurrencyDerivativesMarketPairsListLatestFeeType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V5_CRYPTOCURRENCY_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_FEE_TYPE_VALUES!r}"
    )
