from typing import Literal, cast

GetV1CryptocurrencyListingsHistoricalCryptocurrencyType = Literal["all", "coins", "tokens"]

GET_V1_CRYPTOCURRENCY_LISTINGS_HISTORICAL_CRYPTOCURRENCY_TYPE_VALUES: set[
    GetV1CryptocurrencyListingsHistoricalCryptocurrencyType
] = {
    "all",
    "coins",
    "tokens",
}


def check_get_v1_cryptocurrency_listings_historical_cryptocurrency_type(
    value: str,
) -> GetV1CryptocurrencyListingsHistoricalCryptocurrencyType:
    if value in GET_V1_CRYPTOCURRENCY_LISTINGS_HISTORICAL_CRYPTOCURRENCY_TYPE_VALUES:
        return cast(GetV1CryptocurrencyListingsHistoricalCryptocurrencyType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_LISTINGS_HISTORICAL_CRYPTOCURRENCY_TYPE_VALUES!r}"
    )
