from typing import Literal, cast

GetV5ExchangeDerivativesListSortDir = Literal["asc", "desc"]

GET_V5_EXCHANGE_DERIVATIVES_LIST_SORT_DIR_VALUES: set[GetV5ExchangeDerivativesListSortDir] = {
    "asc",
    "desc",
}


def check_get_v5_exchange_derivatives_list_sort_dir(value: str) -> GetV5ExchangeDerivativesListSortDir:
    if value in GET_V5_EXCHANGE_DERIVATIVES_LIST_SORT_DIR_VALUES:
        return cast(GetV5ExchangeDerivativesListSortDir, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_V5_EXCHANGE_DERIVATIVES_LIST_SORT_DIR_VALUES!r}")
