from typing import Literal, cast

DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuoteCurrencyType = Literal[
    "cryptocurrency", "fiat"
]

DERIVATIVES_CRYPTO_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_MARKET_PAIR_QUOTE_CURRENCY_TYPE_VALUES: set[
    DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuoteCurrencyType
] = {
    "cryptocurrency",
    "fiat",
}


def check_derivatives_crypto_market_pairs_list_latest_results_object_market_pairs_item_market_pair_quote_currency_type(
    value: str,
) -> DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuoteCurrencyType:
    if (
        value
        in DERIVATIVES_CRYPTO_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_MARKET_PAIR_QUOTE_CURRENCY_TYPE_VALUES
    ):
        return cast(
            DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuoteCurrencyType, value
        )
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DERIVATIVES_CRYPTO_MARKET_PAIRS_LIST_LATEST_RESULTS_OBJECT_MARKET_PAIRS_ITEM_MARKET_PAIR_QUOTE_CURRENCY_TYPE_VALUES!r}"
    )
