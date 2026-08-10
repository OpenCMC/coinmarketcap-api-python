from typing import Literal, cast

GetV1CryptocurrencyOhlcvHistoricalTimePeriod = Literal["daily", "hourly"]

GET_V1_CRYPTOCURRENCY_OHLCV_HISTORICAL_TIME_PERIOD_VALUES: set[GetV1CryptocurrencyOhlcvHistoricalTimePeriod] = {
    "daily",
    "hourly",
}


def check_get_v1_cryptocurrency_ohlcv_historical_time_period(
    value: str,
) -> GetV1CryptocurrencyOhlcvHistoricalTimePeriod:
    if value in GET_V1_CRYPTOCURRENCY_OHLCV_HISTORICAL_TIME_PERIOD_VALUES:
        return cast(GetV1CryptocurrencyOhlcvHistoricalTimePeriod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_OHLCV_HISTORICAL_TIME_PERIOD_VALUES!r}"
    )
