from typing import Literal, cast

GetV1CryptocurrencyMapSort = Literal["cmc_rank", "id"]

GET_V1_CRYPTOCURRENCY_MAP_SORT_VALUES: set[GetV1CryptocurrencyMapSort] = {
    "cmc_rank",
    "id",
}


def check_get_v1_cryptocurrency_map_sort(value: str) -> GetV1CryptocurrencyMapSort:
    if value in GET_V1_CRYPTOCURRENCY_MAP_SORT_VALUES:
        return cast(GetV1CryptocurrencyMapSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_MAP_SORT_VALUES!r}")
