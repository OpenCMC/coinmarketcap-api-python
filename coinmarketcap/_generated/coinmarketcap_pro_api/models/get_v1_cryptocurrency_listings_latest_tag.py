from typing import Literal, cast

GetV1CryptocurrencyListingsLatestTag = Literal["all", "defi", "filesharing"]

GET_V1_CRYPTOCURRENCY_LISTINGS_LATEST_TAG_VALUES: set[GetV1CryptocurrencyListingsLatestTag] = {
    "all",
    "defi",
    "filesharing",
}


def check_get_v1_cryptocurrency_listings_latest_tag(value: str) -> GetV1CryptocurrencyListingsLatestTag:
    if value in GET_V1_CRYPTOCURRENCY_LISTINGS_LATEST_TAG_VALUES:
        return cast(GetV1CryptocurrencyListingsLatestTag, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_V1_CRYPTOCURRENCY_LISTINGS_LATEST_TAG_VALUES!r}")
