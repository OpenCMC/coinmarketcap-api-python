from typing import Literal, cast

GetV1FiatMapSort = Literal["id", "name"]

GET_V1_FIAT_MAP_SORT_VALUES: set[GetV1FiatMapSort] = {
    "id",
    "name",
}


def check_get_v1_fiat_map_sort(value: str) -> GetV1FiatMapSort:
    if value in GET_V1_FIAT_MAP_SORT_VALUES:
        return cast(GetV1FiatMapSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_V1_FIAT_MAP_SORT_VALUES!r}")
