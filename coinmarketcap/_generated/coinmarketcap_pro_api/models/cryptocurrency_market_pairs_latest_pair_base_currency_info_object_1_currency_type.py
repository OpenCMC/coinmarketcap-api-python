from typing import Literal, cast

CryptocurrencyMarketPairsLatestPairBaseCurrencyInfoObject1CurrencyType = Literal["cryptocurrency", "fiat"]

CRYPTOCURRENCY_MARKET_PAIRS_LATEST_PAIR_BASE_CURRENCY_INFO_OBJECT_1_CURRENCY_TYPE_VALUES: set[
    CryptocurrencyMarketPairsLatestPairBaseCurrencyInfoObject1CurrencyType
] = {
    "cryptocurrency",
    "fiat",
}


def check_cryptocurrency_market_pairs_latest_pair_base_currency_info_object_1_currency_type(
    value: str,
) -> CryptocurrencyMarketPairsLatestPairBaseCurrencyInfoObject1CurrencyType:
    if value in CRYPTOCURRENCY_MARKET_PAIRS_LATEST_PAIR_BASE_CURRENCY_INFO_OBJECT_1_CURRENCY_TYPE_VALUES:
        return cast(CryptocurrencyMarketPairsLatestPairBaseCurrencyInfoObject1CurrencyType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CRYPTOCURRENCY_MARKET_PAIRS_LATEST_PAIR_BASE_CURRENCY_INFO_OBJECT_1_CURRENCY_TYPE_VALUES!r}"
    )
