from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.exchange_map_exchange_object_status import (
    ExchangeMapExchangeObjectStatus,
    check_exchange_map_exchange_object_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExchangeMapExchangeObject")


@_attrs_define
class ExchangeMapExchangeObject:
    """Exchange object description

    Attributes:
        id (int): The unique CoinMarketCap ID for this exchange. Example: 270.
        name (str): The name of this exchange. Example: Binance.
        slug (str): The web URL friendly shorthand version of this exchange name. Example: binance.
        is_active (int | Unset): 1 if this exchange is still being actively tracked and updated, otherwise 0. Example:
            1.
        status (ExchangeMapExchangeObjectStatus | Unset): The listing status of the exchange. *This field is only
            returned if requested through the `aux` request parameter.* Example: active.
        first_historical_data (str | Unset): Timestamp (ISO 8601) of the earliest market data record available to query
            using our historical endpoints. `null` if there is no historical data currently available for this exchange.
            Example: 2018-04-26T00:45:00.000Z.
        last_historical_data (str | Unset): Timestamp (ISO 8601) of the latest market data record available to query
            using our historical endpoints. `null` if there is no historical data currently available for this exchange.
            Example: 2019-06-02T21:25:00.000Z.
    """

    id: int
    name: str
    slug: str
    is_active: int | Unset = UNSET
    status: ExchangeMapExchangeObjectStatus | Unset = UNSET
    first_historical_data: str | Unset = UNSET
    last_historical_data: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        is_active = self.is_active

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        first_historical_data = self.first_historical_data

        last_historical_data = self.last_historical_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if status is not UNSET:
            field_dict["status"] = status
        if first_historical_data is not UNSET:
            field_dict["first_historical_data"] = first_historical_data
        if last_historical_data is not UNSET:
            field_dict["last_historical_data"] = last_historical_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        is_active = d.pop("is_active", UNSET)

        _status = d.pop("status", UNSET)
        status: ExchangeMapExchangeObjectStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_exchange_map_exchange_object_status(_status)

        first_historical_data = d.pop("first_historical_data", UNSET)

        last_historical_data = d.pop("last_historical_data", UNSET)

        exchange_map_exchange_object = cls(
            id=id,
            name=name,
            slug=slug,
            is_active=is_active,
            status=status,
            first_historical_data=first_historical_data,
            last_historical_data=last_historical_data,
        )

        exchange_map_exchange_object.additional_properties = d
        return exchange_map_exchange_object

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
