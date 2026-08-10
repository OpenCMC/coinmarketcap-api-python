from typing import Literal, cast

CryptocurrencyMarketPairsLatestMarketPairInfoObjectCategory = Literal["derivatives", "otc", "spot"]

CRYPTOCURRENCY_MARKET_PAIRS_LATEST_MARKET_PAIR_INFO_OBJECT_CATEGORY_VALUES: set[
    CryptocurrencyMarketPairsLatestMarketPairInfoObjectCategory
] = {
    "derivatives",
    "otc",
    "spot",
}


def check_cryptocurrency_market_pairs_latest_market_pair_info_object_category(
    value: str,
) -> CryptocurrencyMarketPairsLatestMarketPairInfoObjectCategory:
    if value in CRYPTOCURRENCY_MARKET_PAIRS_LATEST_MARKET_PAIR_INFO_OBJECT_CATEGORY_VALUES:
        return cast(CryptocurrencyMarketPairsLatestMarketPairInfoObjectCategory, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CRYPTOCURRENCY_MARKET_PAIRS_LATEST_MARKET_PAIR_INFO_OBJECT_CATEGORY_VALUES!r}"
    )
