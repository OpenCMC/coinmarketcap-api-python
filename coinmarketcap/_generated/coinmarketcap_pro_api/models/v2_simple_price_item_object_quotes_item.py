from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="V2SimplePriceItemObjectQuotesItem")


@_attrs_define
class V2SimplePriceItemObjectQuotesItem:
    """
    Attributes:
        symbol (str): Convert currency symbol (e.g. `USD`). Example: USD.
        price (float): Latest price in the convert currency. Example: 63319.879266088545.
        market_cap (float | Unset): Market cap in the convert currency. Present only when `include_market_cap` (or
            `include_all`) is true.
        volume_24h (float | Unset): 24-hour trading volume in the convert currency. Present only when
            `include_24h_volume` (or `include_all`) is true.
        percent_change_24h (float | Unset): 24-hour price change percentage. Present only when `include_24h_change` (or
            `include_all`) is true.
        last_updated (datetime.datetime | Unset): ISO 8601 timestamp of the price. Present only when
            `include_last_updated` (or `include_all`) is true.
    """

    symbol: str
    price: float
    market_cap: float | Unset = UNSET
    volume_24h: float | Unset = UNSET
    percent_change_24h: float | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        price = self.price

        market_cap = self.market_cap

        volume_24h = self.volume_24h

        percent_change_24h = self.percent_change_24h

        last_updated: str | Unset = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
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
        symbol = d.pop("symbol")

        price = d.pop("price")

        market_cap = d.pop("market_cap", UNSET)

        volume_24h = d.pop("volume_24h", UNSET)

        percent_change_24h = d.pop("percent_change_24h", UNSET)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        v2_simple_price_item_object_quotes_item = cls(
            symbol=symbol,
            price=price,
            market_cap=market_cap,
            volume_24h=volume_24h,
            percent_change_24h=percent_change_24h,
            last_updated=last_updated,
        )

        v2_simple_price_item_object_quotes_item.additional_properties = d
        return v2_simple_price_item_object_quotes_item

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
