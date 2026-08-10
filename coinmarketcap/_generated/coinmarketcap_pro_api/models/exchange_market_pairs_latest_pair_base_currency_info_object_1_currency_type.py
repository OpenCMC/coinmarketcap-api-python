from typing import Literal, cast

ExchangeMarketPairsLatestPairBaseCurrencyInfoObject1CurrencyType = Literal["cryptocurrency", "fiat"]

EXCHANGE_MARKET_PAIRS_LATEST_PAIR_BASE_CURRENCY_INFO_OBJECT_1_CURRENCY_TYPE_VALUES: set[
    ExchangeMarketPairsLatestPairBaseCurrencyInfoObject1CurrencyType
] = {
    "cryptocurrency",
    "fiat",
}


def check_exchange_market_pairs_latest_pair_base_currency_info_object_1_currency_type(
    value: str,
) -> ExchangeMarketPairsLatestPairBaseCurrencyInfoObject1CurrencyType:
    if value in EXCHANGE_MARKET_PAIRS_LATEST_PAIR_BASE_CURRENCY_INFO_OBJECT_1_CURRENCY_TYPE_VALUES:
        return cast(ExchangeMarketPairsLatestPairBaseCurrencyInfoObject1CurrencyType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXCHANGE_MARKET_PAIRS_LATEST_PAIR_BASE_CURRENCY_INFO_OBJECT_1_CURRENCY_TYPE_VALUES!r}"
    )
