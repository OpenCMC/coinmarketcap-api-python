from typing import Literal, cast

GetV2CryptocurrencyMarketpairsLatestCategory = Literal["all", "derivatives", "otc", "perpetual", "spot"]

GET_V2_CRYPTOCURRENCY_MARKETPAIRS_LATEST_CATEGORY_VALUES: set[GetV2CryptocurrencyMarketpairsLatestCategory] = {
    "all",
    "derivatives",
    "otc",
    "perpetual",
    "spot",
}


def check_get_v2_cryptocurrency_marketpairs_latest_category(value: str) -> GetV2CryptocurrencyMarketpairsLatestCategory:
    if value in GET_V2_CRYPTOCURRENCY_MARKETPAIRS_LATEST_CATEGORY_VALUES:
        return cast(GetV2CryptocurrencyMarketpairsLatestCategory, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V2_CRYPTOCURRENCY_MARKETPAIRS_LATEST_CATEGORY_VALUES!r}"
    )
