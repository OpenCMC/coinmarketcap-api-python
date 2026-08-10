from typing import Literal, cast

GetV5ExchangeDerivativesListSort = Literal["exchange_score", "name", "volume_24h", "volume_24h_adjusted"]

GET_V5_EXCHANGE_DERIVATIVES_LIST_SORT_VALUES: set[GetV5ExchangeDerivativesListSort] = {
    "exchange_score",
    "name",
    "volume_24h",
    "volume_24h_adjusted",
}


def check_get_v5_exchange_derivatives_list_sort(value: str) -> GetV5ExchangeDerivativesListSort:
    if value in GET_V5_EXCHANGE_DERIVATIVES_LIST_SORT_VALUES:
        return cast(GetV5ExchangeDerivativesListSort, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_V5_EXCHANGE_DERIVATIVES_LIST_SORT_VALUES!r}")
