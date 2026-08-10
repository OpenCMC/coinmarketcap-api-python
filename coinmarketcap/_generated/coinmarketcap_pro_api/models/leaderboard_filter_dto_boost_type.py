from typing import Literal, cast

LeaderboardFilterDTOBoostType = Literal["all, onlyBoost, hideBoost"]

LEADERBOARD_FILTER_DTO_BOOST_TYPE_VALUES: set[LeaderboardFilterDTOBoostType] = {
    "all, onlyBoost, hideBoost",
}


def check_leaderboard_filter_dto_boost_type(value: str) -> LeaderboardFilterDTOBoostType:
    if value in LEADERBOARD_FILTER_DTO_BOOST_TYPE_VALUES:
        return cast(LeaderboardFilterDTOBoostType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LEADERBOARD_FILTER_DTO_BOOST_TYPE_VALUES!r}")
