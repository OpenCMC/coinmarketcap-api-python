from typing import Literal, cast

GetV5RealWorldAssetsQuotesHistoricalInterval = Literal[
    "10m",
    "12h",
    "14d",
    "15d",
    "15m",
    "1d",
    "1h",
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

GET_V5_REAL_WORLD_ASSETS_QUOTES_HISTORICAL_INTERVAL_VALUES: set[GetV5RealWorldAssetsQuotesHistoricalInterval] = {
    "10m",
    "12h",
    "14d",
    "15d",
    "15m",
    "1d",
    "1h",
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


def check_get_v5_real_world_assets_quotes_historical_interval(
    value: str,
) -> GetV5RealWorldAssetsQuotesHistoricalInterval:
    if value in GET_V5_REAL_WORLD_ASSETS_QUOTES_HISTORICAL_INTERVAL_VALUES:
        return cast(GetV5RealWorldAssetsQuotesHistoricalInterval, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V5_REAL_WORLD_ASSETS_QUOTES_HISTORICAL_INTERVAL_VALUES!r}"
    )
