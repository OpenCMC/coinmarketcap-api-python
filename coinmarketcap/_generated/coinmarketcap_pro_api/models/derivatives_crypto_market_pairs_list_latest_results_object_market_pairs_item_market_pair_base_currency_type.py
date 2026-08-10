from typing import Literal, cast

DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBaseCurrencyType = Literal[
    "cryptocurrency", "fiat"
]

DERIVATIVES_CRYPTO_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_MARKET_PAIR_BASE_CURRENCY_TYPE_VALUES: set[
    DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBaseCurrencyType
] = {
    "cryptocurrency",
    "fiat",
}


def check_derivatives_crypto_market_pairs_list_latest_results_object_market_pairs_item_market_pair_base_currency_type(
    value: str,
) -> DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBaseCurrencyType:
    if (
        value
        in DERIVATIVES_CRYPTO_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_MARKET_PAIR_BASE_CURRENCY_TYPE_VALUES
    ):
        return cast(DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBaseCurrencyType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DERIVATIVES_CRYPTO_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_MARKET_PAIR_BASE_CURRENCY_TYPE_VALUES!r}"
    )
