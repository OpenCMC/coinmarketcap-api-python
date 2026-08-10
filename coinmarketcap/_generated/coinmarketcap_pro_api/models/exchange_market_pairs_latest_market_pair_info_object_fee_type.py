from typing import Literal, cast

ExchangeMarketPairsLatestMarketPairInfoObjectFeeType = Literal[
    "no-fees", "percentage", "transactional-mining", "unknown"
]

EXCHANGE_MARKET_PAIRS_LATEST_MARKET_PAIR_INFO_OBJECT_FEE_TYPE_VALUES: set[
    ExchangeMarketPairsLatestMarketPairInfoObjectFeeType
] = {
    "no-fees",
    "percentage",
    "transactional-mining",
    "unknown",
}


def check_exchange_market_pairs_latest_market_pair_info_object_fee_type(
    value: str,
) -> ExchangeMarketPairsLatestMarketPairInfoObjectFeeType:
    if value in EXCHANGE_MARKET_PAIRS_LATEST_MARKET_PAIR_INFO_OBJECT_FEE_TYPE_VALUES:
        return cast(ExchangeMarketPairsLatestMarketPairInfoObjectFeeType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXCHANGE_MARKET_PAIRS_LATEST_MARKET_PAIR_INFO_OBJECT_FEE_TYPE_VALUES!r}"
    )
