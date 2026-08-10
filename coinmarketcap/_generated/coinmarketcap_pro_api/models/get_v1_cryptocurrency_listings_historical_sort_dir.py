from typing import Literal, cast

GetV1CryptocurrencyListingsHistoricalSortDir = Literal["asc", "desc"]

GET_V1_CRYPTOCURRENCY_LISTINGS_HISTORICAL_SORT_DIR_VALUES: set[GetV1CryptocurrencyListingsHistoricalSortDir] = {
    "asc",
    "desc",
}


def check_get_v1_cryptocurrency_listings_historical_sort_dir(
    value: str,
) -> GetV1CryptocurrencyListingsHistoricalSortDir:
    if value in GET_V1_CRYPTOCURRENCY_LISTINGS_HISTORICAL_SORT_DIR_VALUES:
        return cast(GetV1CryptocurrencyListingsHistoricalSortDir, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_LISTINGS_HISTORICAL_SORT_DIR_VALUES!r}"
    )
