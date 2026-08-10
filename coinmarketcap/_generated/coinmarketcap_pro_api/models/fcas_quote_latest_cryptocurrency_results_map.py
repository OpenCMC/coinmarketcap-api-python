from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.fcas_quote_latest_cryptocurrency_object import FCASQuoteLatestCryptocurrencyObject


T = TypeVar("T", bound="FCASQuoteLatestCryptocurrencyResultsMap")


@_attrs_define
class FCASQuoteLatestCryptocurrencyResultsMap:
    """A map of cryptocurrency objects by ID or symbol (as used in query parameters).

    Example:
        {'1': {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'score': 894, 'grade': 'A',
            'percent_change_24h': 0.56, 'point_change_24h': 5, 'last_updated': '2019-08-08T00:00:00Z'}}

    """

    additional_properties: dict[str, FCASQuoteLatestCryptocurrencyObject] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fcas_quote_latest_cryptocurrency_object import FCASQuoteLatestCryptocurrencyObject

        d = dict(src_dict)
        fcas_quote_latest_cryptocurrency_results_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = FCASQuoteLatestCryptocurrencyObject.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        fcas_quote_latest_cryptocurrency_results_map.additional_properties = additional_properties
        return fcas_quote_latest_cryptocurrency_results_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> FCASQuoteLatestCryptocurrencyObject:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: FCASQuoteLatestCryptocurrencyObject) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
