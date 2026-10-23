from typing import Literal, cast

RWAMarketPairsResultsObjectMarketPairsItemMarketPairQuotesCurrencyType = Literal["cryptocurrency", "fiat"]

RWA_MARKET_PAIRS_RESULTS_OBJECT_MARKET_PAIRS_ITEM_MARKET_PAIR_QUOTES_CURRENCY_TYPE_VALUES: set[
    RWAMarketPairsResultsObjectMarketPairsItemMarketPairQuotesCurrencyType
] = {
    "cryptocurrency",
    "fiat",
}


def check_rwa_market_pairs_results_object_market_pairs_item_market_pair_quotes_currency_type(
    value: str,
) -> RWAMarketPairsResultsObjectMarketPairsItemMarketPairQuotesCurrencyType:
    if value in RWA_MARKET_PAIRS_RESULTS_OBJECT_MARKET_PAIRS_ITEM_MARKET_PAIR_QUOTES_CURRENCY_TYPE_VALUES:
        return cast(RWAMarketPairsResultsObjectMarketPairsItemMarketPairQuotesCurrencyType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RWA_MARKET_PAIRS_RESULTS_OBJECT_MARKET_PAIRS_ITEM_MARKET_PAIR_QUOTES_CURRENCY_TYPE_VALUES!r}"
    )
