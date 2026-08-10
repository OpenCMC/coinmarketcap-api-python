from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CryptocurrencyListingsLatestQuoteObject")


@_attrs_define
class CryptocurrencyListingsLatestQuoteObject:
    """A market quote in the currency conversion option.

    Attributes:
        price (float): Price in the specified currency at the end of the requested UTC day. Example: 7139.82.
        volume_24h (float): 24 hour adjusted volume in the specified currency at the end of the requested UTC day.
            Example: 4885880000.
        market_cap (float): Market cap in the specified currency at the end of the requested UTC day. Example:
            121020662982.
        percent_change_1h (float): 1 hour change in the specified currency at the end of the requested UTC day. Example:
            0.03.
        percent_change_24h (float): 24 hour change in the specified currency at the end of the requested UTC day.
            Example: 5.75.
        percent_change_7d (float): 7 day change in the specified currency at the end of the requested UTC day. Example:
            -19.64.
        last_updated (str): Timestamp (ISO 8601) of when the conversion currency's current value was referenced.
            Example: 2018-06-02T23:59:59.999Z.
    """

    price: float
    volume_24h: float
    market_cap: float
    percent_change_1h: float
    percent_change_24h: float
    percent_change_7d: float
    last_updated: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price = self.price

        volume_24h = self.volume_24h

        market_cap = self.market_cap

        percent_change_1h = self.percent_change_1h

        percent_change_24h = self.percent_change_24h

        percent_change_7d = self.percent_change_7d

        last_updated = self.last_updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "price": price,
                "volume_24h": volume_24h,
                "market_cap": market_cap,
                "percent_change_1h": percent_change_1h,
                "percent_change_24h": percent_change_24h,
                "percent_change_7d": percent_change_7d,
                "last_updated": last_updated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price = d.pop("price")

        volume_24h = d.pop("volume_24h")

        market_cap = d.pop("market_cap")

        percent_change_1h = d.pop("percent_change_1h")

        percent_change_24h = d.pop("percent_change_24h")

        percent_change_7d = d.pop("percent_change_7d")

        last_updated = d.pop("last_updated")

        cryptocurrency_listings_latest_quote_object = cls(
            price=price,
            volume_24h=volume_24h,
            market_cap=market_cap,
            percent_change_1h=percent_change_1h,
            percent_change_24h=percent_change_24h,
            percent_change_7d=percent_change_7d,
            last_updated=last_updated,
        )

        cryptocurrency_listings_latest_quote_object.additional_properties = d
        return cryptocurrency_listings_latest_quote_object

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
