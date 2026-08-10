from typing import Literal, cast

GetV1AltcoinSeasonIndexHistoricalTimeframe = Literal["30d", "7d", "90d"]

GET_V1_ALTCOIN_SEASON_INDEX_HISTORICAL_TIMEFRAME_VALUES: set[GetV1AltcoinSeasonIndexHistoricalTimeframe] = {
    "30d",
    "7d",
    "90d",
}


def check_get_v1_altcoin_season_index_historical_timeframe(value: str) -> GetV1AltcoinSeasonIndexHistoricalTimeframe:
    if value in GET_V1_ALTCOIN_SEASON_INDEX_HISTORICAL_TIMEFRAME_VALUES:
        return cast(GetV1AltcoinSeasonIndexHistoricalTimeframe, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_V1_ALTCOIN_SEASON_INDEX_HISTORICAL_TIMEFRAME_VALUES!r}"
    )
