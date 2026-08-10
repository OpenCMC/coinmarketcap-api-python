from typing import Literal, cast

DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemCategory = Literal["futures", "perpetual"]

DERIVATIVES_CRYPTO_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_CATEGORY_VALUES: set[
    DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemCategory
] = {
    "futures",
    "perpetual",
}


def check_derivatives_crypto_market_pairs_list_latest_results_object_market_pairs_item_category(
    value: str,
) -> DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemCategory:
    if value in DERIVATIVES_CRYPTO_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_CATEGORY_VALUES:
        return cast(DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemCategory, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DERIVATIVES_CRYPTO_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_CATEGORY_VALUES!r}"
    )
