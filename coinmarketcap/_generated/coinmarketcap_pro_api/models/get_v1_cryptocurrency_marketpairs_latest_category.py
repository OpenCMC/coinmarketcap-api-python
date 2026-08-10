from typing import Literal, cast

GetV1CryptocurrencyMarketpairsLatestCategory = Literal["all", "derivatives", "otc", "perpetual", "spot"]

GET_V1_CRYPTOCURRENCY_MARKETPAIRS_LATEST_CATEGORY_VALUES: set[GetV1CryptocurrencyMarketpairsLatestCategory] = {
    "all",
    "derivatives",
    "otc",
    "perpetual",
    "spot",
}


def check_get_v1_cryptocurrency_marketpairs_latest_category(value: str) -> GetV1CryptocurrencyMarketpairsLatestCategory:
    if value in GET_V1_CRYPTOCURRENCY_MARKETPAIRS_LATEST_CATEGORY_VALUES:
        return cast(GetV1CryptocurrencyMarketpairsLatestCategory, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_MARKETPAIRS_LATEST_CATEGORY_VALUES!r}"
    )
