from typing import Literal, cast

ExchangeMarketPairsLatestMarketPairInfoObjectCategory = Literal["derivatives", "otc", "spot"]

EXCHANGE_MARKET_PAIRS_LATEST_MARKET_PAIR_INFO_OBJECT_CATEGORY_VALUES: set[
    ExchangeMarketPairsLatestMarketPairInfoObjectCategory
] = {
    "derivatives",
    "otc",
    "spot",
}


def check_exchange_market_pairs_latest_market_pair_info_object_category(
    value: str,
) -> ExchangeMarketPairsLatestMarketPairInfoObjectCategory:
    if value in EXCHANGE_MARKET_PAIRS_LATEST_MARKET_PAIR_INFO_OBJECT_CATEGORY_VALUES:
        return cast(ExchangeMarketPairsLatestMarketPairInfoObjectCategory, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXCHANGE_MARKET_PAIRS_LATEST_MARKET_PAIR_INFO_OBJECT_CATEGORY_VALUES!r}"
    )
