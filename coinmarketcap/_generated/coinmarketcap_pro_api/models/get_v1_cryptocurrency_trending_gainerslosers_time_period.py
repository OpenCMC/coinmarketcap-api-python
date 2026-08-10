from typing import Literal, cast

GetV1CryptocurrencyTrendingGainerslosersTimePeriod = Literal["1h", "24h", "30d", "7d"]

GET_V1_CRYPTOCURRENCY_TRENDING_GAINERSLOSERS_TIME_PERIOD_VALUES: set[
    GetV1CryptocurrencyTrendingGainerslosersTimePeriod
] = {
    "1h",
    "24h",
    "30d",
    "7d",
}


def check_get_v1_cryptocurrency_trending_gainerslosers_time_period(
    value: str,
) -> GetV1CryptocurrencyTrendingGainerslosersTimePeriod:
    if value in GET_V1_CRYPTOCURRENCY_TRENDING_GAINERSLOSERS_TIME_PERIOD_VALUES:
        return cast(GetV1CryptocurrencyTrendingGainerslosersTimePeriod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_TRENDING_GAINERSLOSERS_TIME_PERIOD_VALUES!r}"
    )
