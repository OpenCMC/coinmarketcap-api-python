from typing import Literal, cast

GetV5DerivativesLiquidationsExchangeListLatestSortDir = Literal["asc", "desc"]

GET_V5_DERIVATIVES_LIQUIDATIONS_EXCHANGE_LIST_LATEST_SORT_DIR_VALUES: set[
    GetV5DerivativesLiquidationsExchangeListLatestSortDir
] = {
    "asc",
    "desc",
}


def check_get_v5_derivatives_liquidations_exchange_list_latest_sort_dir(
    value: str,
) -> GetV5DerivativesLiquidationsExchangeListLatestSortDir:
    if value in GET_V5_DERIVATIVES_LIQUIDATIONS_EXCHANGE_LIST_LATEST_SORT_DIR_VALUES:
        return cast(GetV5DerivativesLiquidationsExchangeListLatestSortDir, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V5_DERIVATIVES_LIQUIDATIONS_EXCHANGE_LIST_LATEST_SORT_DIR_VALUES!r}"
    )
