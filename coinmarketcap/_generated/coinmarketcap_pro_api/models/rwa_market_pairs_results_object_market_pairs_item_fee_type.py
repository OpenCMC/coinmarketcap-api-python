from typing import Literal, cast

RWAMarketPairsResultsObjectMarketPairsItemFeeType = Literal["no-fees", "percentage", "transactional-mining", "unknown"]

RWA_MARKET_PAIRS_RESULTS_OBJECT_MARKET_PAIRS_ITEM_FEE_TYPE_VALUES: set[
    RWAMarketPairsResultsObjectMarketPairsItemFeeType
] = {
    "no-fees",
    "percentage",
    "transactional-mining",
    "unknown",
}


def check_rwa_market_pairs_results_object_market_pairs_item_fee_type(
    value: str,
) -> RWAMarketPairsResultsObjectMarketPairsItemFeeType:
    if value in RWA_MARKET_PAIRS_RESULTS_OBJECT_MARKET_PAIRS_ITEM_FEE_TYPE_VALUES:
        return cast(RWAMarketPairsResultsObjectMarketPairsItemFeeType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RWA_MARKET_PAIRS_RESULTS_OBJECT_MARKET_PAIRS_ITEM_FEE_TYPE_VALUES!r}"
    )
