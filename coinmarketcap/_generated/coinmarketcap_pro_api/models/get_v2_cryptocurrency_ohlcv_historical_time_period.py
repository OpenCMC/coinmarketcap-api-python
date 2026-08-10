from typing import Literal, cast

GetV2CryptocurrencyOhlcvHistoricalTimePeriod = Literal["daily", "hourly"]

GET_V2_CRYPTOCURRENCY_OHLCV_HISTORICAL_TIME_PERIOD_VALUES: set[GetV2CryptocurrencyOhlcvHistoricalTimePeriod] = {
    "daily",
    "hourly",
}


def check_get_v2_cryptocurrency_ohlcv_historical_time_period(
    value: str,
) -> GetV2CryptocurrencyOhlcvHistoricalTimePeriod:
    if value in GET_V2_CRYPTOCURRENCY_OHLCV_HISTORICAL_TIME_PERIOD_VALUES:
        return cast(GetV2CryptocurrencyOhlcvHistoricalTimePeriod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V2_CRYPTOCURRENCY_OHLCV_HISTORICAL_TIME_PERIOD_VALUES!r}"
    )
