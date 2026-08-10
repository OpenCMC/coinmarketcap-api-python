from typing import Literal, cast

GetV5DerivativesLiquidationsCryptocurrencyListLatestSortDir = Literal["asc", "desc"]

GET_V5_DERIVATIVES_LIQUIDATIONS_CRYPTOCURRENCY_LIST_LATEST_SORT_DIR_VALUES: set[
    GetV5DerivativesLiquidationsCryptocurrencyListLatestSortDir
] = {
    "asc",
    "desc",
}


def check_get_v5_derivatives_liquidations_cryptocurrency_list_latest_sort_dir(
    value: str,
) -> GetV5DerivativesLiquidationsCryptocurrencyListLatestSortDir:
    if value in GET_V5_DERIVATIVES_LIQUIDATIONS_CRYPTOCURRENCY_LIST_LATEST_SORT_DIR_VALUES:
        return cast(GetV5DerivativesLiquidationsCryptocurrencyListLatestSortDir, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V5_DERIVATIVES_LIQUIDATIONS_CRYPTOCURRENCY_LIST_LATEST_SORT_DIR_VALUES!r}"
    )
