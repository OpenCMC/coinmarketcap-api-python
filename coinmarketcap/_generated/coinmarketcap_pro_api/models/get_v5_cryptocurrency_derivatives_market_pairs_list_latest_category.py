from typing import Literal, cast

GetV5CryptocurrencyDerivativesMarketPairsListLatestCategory = Literal["all", "futures", "perpetual"]

GET_V5_CRYPTOCURRENCY_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_CATEGORY_VALUES: set[
    GetV5CryptocurrencyDerivativesMarketPairsListLatestCategory
] = {
    "all",
    "futures",
    "perpetual",
}


def check_get_v5_cryptocurrency_derivatives_market_pairs_list_latest_category(
    value: str,
) -> GetV5CryptocurrencyDerivativesMarketPairsListLatestCategory:
    if value in GET_V5_CRYPTOCURRENCY_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_CATEGORY_VALUES:
        return cast(GetV5CryptocurrencyDerivativesMarketPairsListLatestCategory, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V5_CRYPTOCURRENCY_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_CATEGORY_VALUES!r}"
    )
