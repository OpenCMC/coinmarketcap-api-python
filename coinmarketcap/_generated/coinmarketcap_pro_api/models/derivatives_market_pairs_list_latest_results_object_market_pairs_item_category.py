from typing import Literal, cast

DerivativesMarketPairsListLatestResultsObjectMarketPairsItemCategory = Literal["futures", "perpetual"]

DERIVATIVES_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_CATEGORY_VALUES: set[
    DerivativesMarketPairsListLatestResultsObjectMarketPairsItemCategory
] = {
    "futures",
    "perpetual",
}


def check_derivatives_market_pairs_list_latest_results_object_market_pairs_item_category(
    value: str,
) -> DerivativesMarketPairsListLatestResultsObjectMarketPairsItemCategory:
    if value in DERIVATIVES_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_CATEGORY_VALUES:
        return cast(DerivativesMarketPairsListLatestResultsObjectMarketPairsItemCategory, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DERIVATIVES_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_CATEGORY_VALUES!r}"
    )
