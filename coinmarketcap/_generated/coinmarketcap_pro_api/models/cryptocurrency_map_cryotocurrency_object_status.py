from typing import Literal, cast

CryptocurrencyMapCryotocurrencyObjectStatus = Literal["active", "inactive", "untracked"]

CRYPTOCURRENCY_MAP_CRYOTOCURRENCY_OBJECT_STATUS_VALUES: set[CryptocurrencyMapCryotocurrencyObjectStatus] = {
    "active",
    "inactive",
    "untracked",
}


def check_cryptocurrency_map_cryotocurrency_object_status(value: str) -> CryptocurrencyMapCryotocurrencyObjectStatus:
    if value in CRYPTOCURRENCY_MAP_CRYOTOCURRENCY_OBJECT_STATUS_VALUES:
        return cast(CryptocurrencyMapCryotocurrencyObjectStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CRYPTOCURRENCY_MAP_CRYOTOCURRENCY_OBJECT_STATUS_VALUES!r}"
    )
