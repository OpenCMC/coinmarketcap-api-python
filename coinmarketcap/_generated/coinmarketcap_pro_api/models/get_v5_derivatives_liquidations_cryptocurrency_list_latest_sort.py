from typing import Literal, cast

GetV5DerivativesLiquidationsCryptocurrencyListLatestSort = Literal[
    "total_liquidations_1h", "total_liquidations_24h", "total_liquidations_4h"
]

GET_V5_DERIVATIVES_LIQUIDATIONS_CRYPTOCURRENCY_LIST_LATEST_SORT_VALUES: set[
    GetV5DerivativesLiquidationsCryptocurrencyListLatestSort
] = {
    "total_liquidations_1h",
    "total_liquidations_24h",
    "total_liquidations_4h",
}


def check_get_v5_derivatives_liquidations_cryptocurrency_list_latest_sort(
    value: str,
) -> GetV5DerivativesLiquidationsCryptocurrencyListLatestSort:
    if value in GET_V5_DERIVATIVES_LIQUIDATIONS_CRYPTOCURRENCY_LIST_LATEST_SORT_VALUES:
        return cast(GetV5DerivativesLiquidationsCryptocurrencyListLatestSort, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V5_DERIVATIVES_LIQUIDATIONS_CRYPTOCURRENCY_LIST_LATEST_SORT_VALUES!r}"
    )
