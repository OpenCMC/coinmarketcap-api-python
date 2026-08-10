from typing import Literal, cast

GetV1CryptocurrencyTrendingGainerslosersSort = Literal["percent_change_24h"]

GET_V1_CRYPTOCURRENCY_TRENDING_GAINERSLOSERS_SORT_VALUES: set[GetV1CryptocurrencyTrendingGainerslosersSort] = {
    "percent_change_24h",
}


def check_get_v1_cryptocurrency_trending_gainerslosers_sort(value: str) -> GetV1CryptocurrencyTrendingGainerslosersSort:
    if value in GET_V1_CRYPTOCURRENCY_TRENDING_GAINERSLOSERS_SORT_VALUES:
        return cast(GetV1CryptocurrencyTrendingGainerslosersSort, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_TRENDING_GAINERSLOSERS_SORT_VALUES!r}"
    )
