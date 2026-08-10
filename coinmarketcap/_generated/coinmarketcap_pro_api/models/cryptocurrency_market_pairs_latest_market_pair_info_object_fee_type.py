from typing import Literal, cast

CryptocurrencyMarketPairsLatestMarketPairInfoObjectFeeType = Literal[
    "no-fees", "percentage", "transactional-mining", "unknown"
]

CRYPTOCURRENCY_MARKET_PAIRS_LATEST_MARKET_PAIR_INFO_OBJECT_FEE_TYPE_VALUES: set[
    CryptocurrencyMarketPairsLatestMarketPairInfoObjectFeeType
] = {
    "no-fees",
    "percentage",
    "transactional-mining",
    "unknown",
}


def check_cryptocurrency_market_pairs_latest_market_pair_info_object_fee_type(
    value: str,
) -> CryptocurrencyMarketPairsLatestMarketPairInfoObjectFeeType:
    if value in CRYPTOCURRENCY_MARKET_PAIRS_LATEST_MARKET_PAIR_INFO_OBJECT_FEE_TYPE_VALUES:
        return cast(CryptocurrencyMarketPairsLatestMarketPairInfoObjectFeeType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CRYPTOCURRENCY_MARKET_PAIRS_LATEST_MARKET_PAIR_INFO_OBJECT_FEE_TYPE_VALUES!r}"
    )
