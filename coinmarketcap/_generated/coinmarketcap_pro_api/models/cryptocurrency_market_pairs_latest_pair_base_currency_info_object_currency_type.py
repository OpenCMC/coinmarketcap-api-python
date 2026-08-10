from typing import Literal, cast

CryptocurrencyMarketPairsLatestPairBaseCurrencyInfoObjectCurrencyType = Literal["cryptocurrency", "fiat"]

CRYPTOCURRENCY_MARKET_PAIRS_LATEST_PAIR_BASE_CURRENCY_INFO_OBJECT_CURRENCY_TYPE_VALUES: set[
    CryptocurrencyMarketPairsLatestPairBaseCurrencyInfoObjectCurrencyType
] = {
    "cryptocurrency",
    "fiat",
}


def check_cryptocurrency_market_pairs_latest_pair_base_currency_info_object_currency_type(
    value: str,
) -> CryptocurrencyMarketPairsLatestPairBaseCurrencyInfoObjectCurrencyType:
    if value in CRYPTOCURRENCY_MARKET_PAIRS_LATEST_PAIR_BASE_CURRENCY_INFO_OBJECT_CURRENCY_TYPE_VALUES:
        return cast(CryptocurrencyMarketPairsLatestPairBaseCurrencyInfoObjectCurrencyType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CRYPTOCURRENCY_MARKET_PAIRS_LATEST_PAIR_BASE_CURRENCY_INFO_OBJECT_CURRENCY_TYPE_VALUES!r}"
    )
