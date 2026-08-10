from typing import Literal, cast

RWAMarketPairsResultsObjectMarketPairsItemMarketPairBaseCurrencyType = Literal["cryptocurrency", "fiat"]

RWA_MARKET_PAIRS_RESULTS_OBJECT_MARKET_PAIRS_ITEM_MARKET_PAIR_BASE_CURRENCY_TYPE_VALUES: set[
    RWAMarketPairsResultsObjectMarketPairsItemMarketPairBaseCurrencyType
] = {
    "cryptocurrency",
    "fiat",
}


def check_rwa_market_pairs_results_object_market_pairs_item_market_pair_base_currency_type(
    value: str,
) -> RWAMarketPairsResultsObjectMarketPairsItemMarketPairBaseCurrencyType:
    if value in RWA_MARKET_PAIRS_RESULTS_OBJECT_MARKET_PAIRS_ITEM_MARKET_PAIR_BASE_CURRENCY_TYPE_VALUES:
        return cast(RWAMarketPairsResultsObjectMarketPairsItemMarketPairBaseCurrencyType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RWA_MARKET_PAIRS_RESULTS_OBJECT_MARKET_PAIRS_ITEM_MARKET_PAIR_BASE_CURRENCY_TYPE_VALUES!r}"
    )
