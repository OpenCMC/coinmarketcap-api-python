from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cryptocurrency_listings_latest_quote_object import CryptocurrencyListingsLatestQuoteObject


T = TypeVar("T", bound="CryptocurrencyListingsLatestQuoteMap")


@_attrs_define
class CryptocurrencyListingsLatestQuoteMap:
    """A map of market quotes in different currency conversions. The default map included is USD.

    Example:
        {'USD': {'price': 9283.92, 'volume_24h': 7155680000, 'percent_change_1h': -0.152774, 'percent_change_24h':
            0.518894, 'percent_change_7d': 0.986573, 'market_cap': 158055024432, 'last_updated':
            '2018-08-09T22:53:32.000Z'}}

    """

    additional_properties: dict[str, CryptocurrencyListingsLatestQuoteObject] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_listings_latest_quote_object import CryptocurrencyListingsLatestQuoteObject

        d = dict(src_dict)
        cryptocurrency_listings_latest_quote_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CryptocurrencyListingsLatestQuoteObject.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        cryptocurrency_listings_latest_quote_map.additional_properties = additional_properties
        return cryptocurrency_listings_latest_quote_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> CryptocurrencyListingsLatestQuoteObject:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: CryptocurrencyListingsLatestQuoteObject) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
