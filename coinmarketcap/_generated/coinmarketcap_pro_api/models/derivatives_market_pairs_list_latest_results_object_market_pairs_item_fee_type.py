from typing import Literal, cast

DerivativesMarketPairsListLatestResultsObjectMarketPairsItemFeeType = Literal[
    "no-fees", "percentage", "transactional-mining", "unknown"
]

DERIVATIVES_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_FEE_TYPE_VALUES: set[
    DerivativesMarketPairsListLatestResultsObjectMarketPairsItemFeeType
] = {
    "no-fees",
    "percentage",
    "transactional-mining",
    "unknown",
}


def check_derivatives_market_pairs_list_latest_results_object_market_pairs_item_fee_type(
    value: str,
) -> DerivativesMarketPairsListLatestResultsObjectMarketPairsItemFeeType:
    if value in DERIVATIVES_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_FEE_TYPE_VALUES:
        return cast(DerivativesMarketPairsListLatestResultsObjectMarketPairsItemFeeType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DERIVATIVES_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_FEE_TYPE_VALUES!r}"
    )
