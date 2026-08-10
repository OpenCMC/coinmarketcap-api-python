from typing import Literal, cast

DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemFeeType = Literal[
    "no-fees", "percentage", "transactional-mining", "unknown"
]

DERIVATIVES_CRYPTO_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_FEE_TYPE_VALUES: set[
    DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemFeeType
] = {
    "no-fees",
    "percentage",
    "transactional-mining",
    "unknown",
}


def check_derivatives_crypto_market_pairs_list_latest_results_object_market_pairs_item_fee_type(
    value: str,
) -> DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemFeeType:
    if value in DERIVATIVES_CRYPTO_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_FEE_TYPE_VALUES:
        return cast(DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemFeeType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DERIVATIVES_CRYPTO_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_FEE_TYPE_VALUES!r}"
    )
