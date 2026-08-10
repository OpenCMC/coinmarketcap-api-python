from typing import Literal, cast

GetV1CryptocurrencyAirdropsStatus = Literal["ENDED", "ONGOING", "UPCOMING"]

GET_V1_CRYPTOCURRENCY_AIRDROPS_STATUS_VALUES: set[GetV1CryptocurrencyAirdropsStatus] = {
    "ENDED",
    "ONGOING",
    "UPCOMING",
}


def check_get_v1_cryptocurrency_airdrops_status(value: str) -> GetV1CryptocurrencyAirdropsStatus:
    if value in GET_V1_CRYPTOCURRENCY_AIRDROPS_STATUS_VALUES:
        return cast(GetV1CryptocurrencyAirdropsStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_AIRDROPS_STATUS_VALUES!r}")
