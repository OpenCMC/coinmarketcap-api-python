from typing import Literal, cast

ExchangeMapExchangeObjectStatus = Literal["active", "inactive", "untracked"]

EXCHANGE_MAP_EXCHANGE_OBJECT_STATUS_VALUES: set[ExchangeMapExchangeObjectStatus] = {
    "active",
    "inactive",
    "untracked",
}


def check_exchange_map_exchange_object_status(value: str) -> ExchangeMapExchangeObjectStatus:
    if value in EXCHANGE_MAP_EXCHANGE_OBJECT_STATUS_VALUES:
        return cast(ExchangeMapExchangeObjectStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EXCHANGE_MAP_EXCHANGE_OBJECT_STATUS_VALUES!r}")
