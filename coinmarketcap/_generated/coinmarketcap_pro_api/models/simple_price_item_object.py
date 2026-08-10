from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SimplePriceItemObject")


@_attrs_define
class SimplePriceItemObject:
    """Simple spot price entry for a single cryptocurrency.

    Attributes:
        id (int): CoinMarketCap cryptocurrency ID. Example: 1.
        price (float): Spot price in USD. Example: 65432.12.
        market_cap (float | Unset): Market cap in USD. Returned only when include_market_cap=true. Example:
            1284000000000.
        volume_24h (float | Unset): 24-hour trading volume in USD. Returned only when include_volume_24h=true. Example:
            32500000000.
        percent_change_24h (float | Unset): 24-hour price change percentage. Returned only when
            include_percent_change_24h=true. Example: 1.23.
        last_updated (str | Unset): Last update time (ISO 8601 UTC). Returned only when include_last_updated=true.
            Example: 2024-09-30T12:00:00.000Z.
    """

    id: int
    price: float
    market_cap: float | Unset = UNSET
    volume_24h: float | Unset = UNSET
    percent_change_24h: float | Unset = UNSET
    last_updated: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        price = self.price

        market_cap = self.market_cap

        volume_24h = self.volume_24h

        percent_change_24h = self.percent_change_24h

        last_updated = self.last_updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "price": price,
            }
        )
        if market_cap is not UNSET:
            field_dict["market_cap"] = market_cap
        if volume_24h is not UNSET:
            field_dict["volume_24h"] = volume_24h
        if percent_change_24h is not UNSET:
            field_dict["percent_change_24h"] = percent_change_24h
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        price = d.pop("price")

        market_cap = d.pop("market_cap", UNSET)

        volume_24h = d.pop("volume_24h", UNSET)

        percent_change_24h = d.pop("percent_change_24h", UNSET)

        last_updated = d.pop("last_updated", UNSET)

        simple_price_item_object = cls(
            id=id,
            price=price,
            market_cap=market_cap,
            volume_24h=volume_24h,
            percent_change_24h=percent_change_24h,
            last_updated=last_updated,
        )

        simple_price_item_object.additional_properties = d
        return simple_price_item_object

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
