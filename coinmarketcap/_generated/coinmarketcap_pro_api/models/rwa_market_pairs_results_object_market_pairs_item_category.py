from typing import Literal, cast

RWAMarketPairsResultsObjectMarketPairsItemCategory = Literal["derivatives", "otc", "perpetual", "spot"]

RWA_MARKET_PAIRS_RESULTS_OBJECT_MARKET_PAIRS_ITEM_CATEGORY_VALUES: set[
    RWAMarketPairsResultsObjectMarketPairsItemCategory
] = {
    "derivatives",
    "otc",
    "perpetual",
    "spot",
}


def check_rwa_market_pairs_results_object_market_pairs_item_category(
    value: str,
) -> RWAMarketPairsResultsObjectMarketPairsItemCategory:
    if value in RWA_MARKET_PAIRS_RESULTS_OBJECT_MARKET_PAIRS_ITEM_CATEGORY_VALUES:
        return cast(RWAMarketPairsResultsObjectMarketPairsItemCategory, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RWA_MARKET_PAIRS_RESULTS_OBJECT_MARKET_PAIRS_ITEM_CATEGORY_VALUES!r}"
    )
