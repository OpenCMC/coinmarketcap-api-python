from typing import Literal, cast

GetV1GlobalmetricsQuotesHistoricalInterval = Literal[
    "10m",
    "12h",
    "14d",
    "15d",
    "15m",
    "1d",
    "1h",
    "24h",
    "2d",
    "2h",
    "30d",
    "30m",
    "365d",
    "3d",
    "3h",
    "45m",
    "4h",
    "5m",
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

GET_V1_GLOBALMETRICS_QUOTES_HISTORICAL_INTERVAL_VALUES: set[GetV1GlobalmetricsQuotesHistoricalInterval] = {
    "10m",
    "12h",
    "14d",
    "15d",
    "15m",
    "1d",
    "1h",
    "24h",
    "2d",
    "2h",
    "30d",
    "30m",
    "365d",
    "3d",
    "3h",
    "45m",
    "4h",
    "5m",
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


def check_get_v1_globalmetrics_quotes_historical_interval(value: str) -> GetV1GlobalmetricsQuotesHistoricalInterval:
    if value in GET_V1_GLOBALMETRICS_QUOTES_HISTORICAL_INTERVAL_VALUES:
        return cast(GetV1GlobalmetricsQuotesHistoricalInterval, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_GLOBALMETRICS_QUOTES_HISTORICAL_INTERVAL_VALUES!r}"
    )
