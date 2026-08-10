from typing import Literal, cast

DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBaseCurrencyType = Literal[
    "cryptocurrency", "fiat"
]

DERIVATIVES_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_MARKET_PAIR_BASE_CURRENCY_TYPE_VALUES: set[
    DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBaseCurrencyType
] = {
    "cryptocurrency",
    "fiat",
}


def check_derivatives_market_pairs_list_latest_results_object_market_pairs_item_market_pair_base_currency_type(
    value: str,
) -> DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBaseCurrencyType:
    if (
        value
        in DERIVATIVES_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_MARKET_PAIR_BASE_CURRENCY_TYPE_VALUES
    ):
        return cast(DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBaseCurrencyType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DERIVATIVES_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_MARKET_PAIR_BASE_CURRENCY_TYPE_VALUES!r}"
    )
