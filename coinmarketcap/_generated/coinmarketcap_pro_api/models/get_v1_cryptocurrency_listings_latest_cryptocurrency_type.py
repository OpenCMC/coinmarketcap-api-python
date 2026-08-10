from typing import Literal, cast

GetV1CryptocurrencyListingsLatestCryptocurrencyType = Literal["all", "coins", "tokens"]

GET_V1_CRYPTOCURRENCY_LISTINGS_LATEST_CRYPTOCURRENCY_TYPE_VALUES: set[
    GetV1CryptocurrencyListingsLatestCryptocurrencyType
] = {
    "all",
    "coins",
    "tokens",
}


def check_get_v1_cryptocurrency_listings_latest_cryptocurrency_type(
    value: str,
) -> GetV1CryptocurrencyListingsLatestCryptocurrencyType:
    if value in GET_V1_CRYPTOCURRENCY_LISTINGS_LATEST_CRYPTOCURRENCY_TYPE_VALUES:
        return cast(GetV1CryptocurrencyListingsLatestCryptocurrencyType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_LISTINGS_LATEST_CRYPTOCURRENCY_TYPE_VALUES!r}"
    )
