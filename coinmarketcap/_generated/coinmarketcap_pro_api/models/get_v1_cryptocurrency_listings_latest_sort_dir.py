from typing import Literal, cast

GetV1CryptocurrencyListingsLatestSortDir = Literal["asc", "desc"]

GET_V1_CRYPTOCURRENCY_LISTINGS_LATEST_SORT_DIR_VALUES: set[GetV1CryptocurrencyListingsLatestSortDir] = {
    "asc",
    "desc",
}


def check_get_v1_cryptocurrency_listings_latest_sort_dir(value: str) -> GetV1CryptocurrencyListingsLatestSortDir:
    if value in GET_V1_CRYPTOCURRENCY_LISTINGS_LATEST_SORT_DIR_VALUES:
        return cast(GetV1CryptocurrencyListingsLatestSortDir, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_LISTINGS_LATEST_SORT_DIR_VALUES!r}"
    )
