from typing import Literal, cast

GetV1CryptocurrencyOhlcvHistoricalInterval = Literal[
    "12h",
    "14d",
    "15d",
    "1d",
    "1h",
    "2d",
    "2h",
    "30d",
    "365d",
    "3d",
    "3h",
    "4h",
    "60d",
    "6h",
    "7d",
    "90d",
    "daily",
    "hourly",
    "monthly",
    "weekly",
    "yearly",
]

GET_V1_CRYPTOCURRENCY_OHLCV_HISTORICAL_INTERVAL_VALUES: set[GetV1CryptocurrencyOhlcvHistoricalInterval] = {
    "12h",
    "14d",
    "15d",
    "1d",
    "1h",
    "2d",
    "2h",
    "30d",
    "365d",
    "3d",
    "3h",
    "4h",
    "60d",
    "6h",
    "7d",
    "90d",
    "daily",
    "hourly",
    "monthly",
    "weekly",
    "yearly",
}


def check_get_v1_cryptocurrency_ohlcv_historical_interval(value: str) -> GetV1CryptocurrencyOhlcvHistoricalInterval:
    if value in GET_V1_CRYPTOCURRENCY_OHLCV_HISTORICAL_INTERVAL_VALUES:
        return cast(GetV1CryptocurrencyOhlcvHistoricalInterval, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_OHLCV_HISTORICAL_INTERVAL_VALUES!r}"
    )
