from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cryptocurrency_quotes_historical_result_object import CryptocurrencyQuotesHistoricalResultObject


T = TypeVar("T", bound="CryptocurrencyQuotesHistoricalResultsMap")


@_attrs_define
class CryptocurrencyQuotesHistoricalResultsMap:
    """Results of your query returned as an object map.

    Example:
        {'1': {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'is_active': 1, 'is_fiat': 0, 'quotes': [{'timestamp':
            '2018-06-22T00:00:00.000Z', 'quote': {'USD': {'price': 6242.48, 'volume_24h': 4894120000, 'market_cap':
            107057808682, 'last_updated': '2018-06-22T00:04:16.000Z', 'volume_24hr': 4894120000, 'timestamp':
            '2018-06-22T00:04:16.000Z'}}}]}}

    """

    additional_properties: dict[str, CryptocurrencyQuotesHistoricalResultObject] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_quotes_historical_result_object import CryptocurrencyQuotesHistoricalResultObject

        d = dict(src_dict)
        cryptocurrency_quotes_historical_results_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CryptocurrencyQuotesHistoricalResultObject.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        cryptocurrency_quotes_historical_results_map.additional_properties = additional_properties
        return cryptocurrency_quotes_historical_results_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> CryptocurrencyQuotesHistoricalResultObject:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: CryptocurrencyQuotesHistoricalResultObject) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
