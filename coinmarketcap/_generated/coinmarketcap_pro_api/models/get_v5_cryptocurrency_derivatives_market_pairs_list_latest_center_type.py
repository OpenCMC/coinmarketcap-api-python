from typing import Literal, cast

GetV5CryptocurrencyDerivativesMarketPairsListLatestCenterType = Literal["all", "cex", "dex"]

GET_V5_CRYPTOCURRENCY_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_CENTER_TYPE_VALUES: set[
    GetV5CryptocurrencyDerivativesMarketPairsListLatestCenterType
] = {
    "all",
    "cex",
    "dex",
}


def check_get_v5_cryptocurrency_derivatives_market_pairs_list_latest_center_type(
    value: str,
) -> GetV5CryptocurrencyDerivativesMarketPairsListLatestCenterType:
    if value in GET_V5_CRYPTOCURRENCY_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_CENTER_TYPE_VALUES:
        return cast(GetV5CryptocurrencyDerivativesMarketPairsListLatestCenterType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V5_CRYPTOCURRENCY_DERIVATIVES_MARKET_PAIRS_LIST_LATEST_CENTER_TYPE_VALUES!r}"
    )
