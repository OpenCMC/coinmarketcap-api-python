from typing import Literal, cast

GetV1CryptocurrencyTrendingGainerslosersSortDir = Literal["asc", "desc"]

GET_V1_CRYPTOCURRENCY_TRENDING_GAINERSLOSERS_SORT_DIR_VALUES: set[GetV1CryptocurrencyTrendingGainerslosersSortDir] = {
    "asc",
    "desc",
}


def check_get_v1_cryptocurrency_trending_gainerslosers_sort_dir(
    value: str,
) -> GetV1CryptocurrencyTrendingGainerslosersSortDir:
    if value in GET_V1_CRYPTOCURRENCY_TRENDING_GAINERSLOSERS_SORT_DIR_VALUES:
        return cast(GetV1CryptocurrencyTrendingGainerslosersSortDir, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_TRENDING_GAINERSLOSERS_SORT_DIR_VALUES!r}"
    )
