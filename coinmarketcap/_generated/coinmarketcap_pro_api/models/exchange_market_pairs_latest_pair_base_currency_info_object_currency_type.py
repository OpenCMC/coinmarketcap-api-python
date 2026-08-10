from typing import Literal, cast

ExchangeMarketPairsLatestPairBaseCurrencyInfoObjectCurrencyType = Literal["cryptocurrency", "fiat"]

EXCHANGE_MARKET_PAIRS_LATEST_PAIR_BASE_CURRENCY_INFO_OBJECT_CURRENCY_TYPE_VALUES: set[
    ExchangeMarketPairsLatestPairBaseCurrencyInfoObjectCurrencyType
] = {
    "cryptocurrency",
    "fiat",
}


def check_exchange_market_pairs_latest_pair_base_currency_info_object_currency_type(
    value: str,
) -> ExchangeMarketPairsLatestPairBaseCurrencyInfoObjectCurrencyType:
    if value in EXCHANGE_MARKET_PAIRS_LATEST_PAIR_BASE_CURRENCY_INFO_OBJECT_CURRENCY_TYPE_VALUES:
        return cast(ExchangeMarketPairsLatestPairBaseCurrencyInfoObjectCurrencyType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXCHANGE_MARKET_PAIRS_LATEST_PAIR_BASE_CURRENCY_INFO_OBJECT_CURRENCY_TYPE_VALUES!r}"
    )
