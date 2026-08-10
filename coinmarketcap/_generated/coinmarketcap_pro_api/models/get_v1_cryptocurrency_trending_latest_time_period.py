from typing import Literal, cast

GetV1CryptocurrencyTrendingLatestTimePeriod = Literal["24h", "30d", "7d"]

GET_V1_CRYPTOCURRENCY_TRENDING_LATEST_TIME_PERIOD_VALUES: set[GetV1CryptocurrencyTrendingLatestTimePeriod] = {
    "24h",
    "30d",
    "7d",
}


def check_get_v1_cryptocurrency_trending_latest_time_period(value: str) -> GetV1CryptocurrencyTrendingLatestTimePeriod:
    if value in GET_V1_CRYPTOCURRENCY_TRENDING_LATEST_TIME_PERIOD_VALUES:
        return cast(GetV1CryptocurrencyTrendingLatestTimePeriod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_TRENDING_LATEST_TIME_PERIOD_VALUES!r}"
    )
