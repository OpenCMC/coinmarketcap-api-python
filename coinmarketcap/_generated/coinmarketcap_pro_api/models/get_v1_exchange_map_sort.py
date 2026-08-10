from typing import Literal, cast

GetV1ExchangeMapSort = Literal["id", "volume_24h"]

GET_V1_EXCHANGE_MAP_SORT_VALUES: set[GetV1ExchangeMapSort] = {
    "id",
    "volume_24h",
}


def check_get_v1_exchange_map_sort(value: str) -> GetV1ExchangeMapSort:
    if value in GET_V1_EXCHANGE_MAP_SORT_VALUES:
        return cast(GetV1ExchangeMapSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_V1_EXCHANGE_MAP_SORT_VALUES!r}")
