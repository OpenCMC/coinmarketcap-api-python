from typing import Literal, cast

GetV1CryptocurrencyTrendingMostvisitedTimePeriod = Literal["24h", "30d", "7d"]

GET_V1_CRYPTOCURRENCY_TRENDING_MOSTVISITED_TIME_PERIOD_VALUES: set[GetV1CryptocurrencyTrendingMostvisitedTimePeriod] = {
    "24h",
    "30d",
    "7d",
}


def check_get_v1_cryptocurrency_trending_mostvisited_time_period(
    value: str,
) -> GetV1CryptocurrencyTrendingMostvisitedTimePeriod:
    if value in GET_V1_CRYPTOCURRENCY_TRENDING_MOSTVISITED_TIME_PERIOD_VALUES:
        return cast(GetV1CryptocurrencyTrendingMostvisitedTimePeriod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_TRENDING_MOSTVISITED_TIME_PERIOD_VALUES!r}"
    )
