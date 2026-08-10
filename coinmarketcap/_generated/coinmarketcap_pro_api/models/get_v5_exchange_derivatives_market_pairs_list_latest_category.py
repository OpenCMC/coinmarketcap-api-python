from typing import Literal, cast

GetV5ExchangeDerivativesMarketPairsListLatestCategory = Literal["all", "futures", "perpetual"]

GET_V5_EXCHANGE_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_CATEGORY_VALUES: set[
    GetV5ExchangeDerivativesMarketPairsListLatestCategory
] = {
    "all",
    "futures",
    "perpetual",
}


def check_get_v5_exchange_derivatives_market_pairs_list_latest_category(
    value: str,
) -> GetV5ExchangeDerivativesMarketPairsListLatestCategory:
    if value in GET_V5_EXCHANGE_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_CATEGORY_VALUES:
        return cast(GetV5ExchangeDerivativesMarketPairsListLatestCategory, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V5_EXCHANGE_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_CATEGORY_VALUES!r}"
    )
