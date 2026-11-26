from typing import Literal, cast

GetV5CryptocurrencyOhlcvHistoricalInterval = Literal["15m", "1d", "1h", "1M", "1w", "4h"]

GET_V5_CRYPTOCURRENCY_OHLCV_HISTORICAL_INTERVAL_VALUES: set[GetV5CryptocurrencyOhlcvHistoricalInterval] = {
    "15m",
    "1d",
    "1h",
    "1M",
    "1w",
    "4h",
}


def check_get_v5_cryptocurrency_ohlcv_historical_interval(value: str) -> GetV5CryptocurrencyOhlcvHistoricalInterval:
    if value in GET_V5_CRYPTOCURRENCY_OHLCV_HISTORICAL_INTERVAL_VALUES:
        return cast(GetV5CryptocurrencyOhlcvHistoricalInterval, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V5_CRYPTOCURRENCY_OHLCV_HISTORICAL_INTERVAL_VALUES!r}"
    )
