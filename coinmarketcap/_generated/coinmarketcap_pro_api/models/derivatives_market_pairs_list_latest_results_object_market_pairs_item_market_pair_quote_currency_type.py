from typing import Literal, cast

DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuoteCurrencyType = Literal[
    "cryptocurrency", "fiat"
]

DERIVATIVES_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_MARKET_PAIR_QUOTE_CURRENCY_TYPE_VALUES: set[
    DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuoteCurrencyType
] = {
    "cryptocurrency",
    "fiat",
}


def check_derivatives_market_pairs_list_latest_results_object_market_pairs_item_market_pair_quote_currency_type(
    value: str,
) -> DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuoteCurrencyType:
    if (
        value
        in DERIVATIVES_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_MARKET_PAIR_QUOTE_CURRENCY_TYPE_VALUES
    ):
        return cast(DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuoteCurrencyType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DERIVATIVES_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_MARKET_PAIR_QUOTE_CURRENCY_TYPE_VALUES!r}"
    )
