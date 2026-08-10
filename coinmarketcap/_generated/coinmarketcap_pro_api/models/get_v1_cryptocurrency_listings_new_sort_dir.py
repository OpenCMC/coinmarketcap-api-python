from typing import Literal, cast

GetV1CryptocurrencyListingsNewSortDir = Literal["asc", "desc"]

GET_V1_CRYPTOCURRENCY_LISTINGS_NEW_SORT_DIR_VALUES: set[GetV1CryptocurrencyListingsNewSortDir] = {
    "asc",
    "desc",
}


def check_get_v1_cryptocurrency_listings_new_sort_dir(value: str) -> GetV1CryptocurrencyListingsNewSortDir:
    if value in GET_V1_CRYPTOCURRENCY_LISTINGS_NEW_SORT_DIR_VALUES:
        return cast(GetV1CryptocurrencyListingsNewSortDir, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_LISTINGS_NEW_SORT_DIR_VALUES!r}"
    )
