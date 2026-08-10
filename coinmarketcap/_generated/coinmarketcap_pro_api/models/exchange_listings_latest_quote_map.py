from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exchange_listings_latest_quote_object import ExchangeListingsLatestQuoteObject


T = TypeVar("T", bound="ExchangeListingsLatestQuoteMap")


@_attrs_define
class ExchangeListingsLatestQuoteMap:
    """A map of market quotes in different currency conversions. The default map included is USD.

    Example:
        {'USD': {'volume_24h': 1418940000, 'last_updated': '2018-11-08T22:18:00.000Z', 'volume_24h_adjusted':
            1418940000, 'volume_7d': 3666423776, 'volume_30d': 21338299776, 'percent_change_volume_24h': -11.62,
            'percent_change_volume_7d': 67.21, 'percent_change_volume_30d': 0.0017, 'effective_liquidity_24h': 629.98}}

    """

    additional_properties: dict[str, ExchangeListingsLatestQuoteObject] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exchange_listings_latest_quote_object import ExchangeListingsLatestQuoteObject

        d = dict(src_dict)
        exchange_listings_latest_quote_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ExchangeListingsLatestQuoteObject.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        exchange_listings_latest_quote_map.additional_properties = additional_properties
        return exchange_listings_latest_quote_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ExchangeListingsLatestQuoteObject:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ExchangeListingsLatestQuoteObject) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
