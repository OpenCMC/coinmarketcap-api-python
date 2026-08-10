from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exchange_historical_quotes_exchange_object import ExchangeHistoricalQuotesExchangeObject


T = TypeVar("T", bound="ExchangeHistoricalQuotesResultsMap")


@_attrs_define
class ExchangeHistoricalQuotesResultsMap:
    """Results of your query returned as an object map.

    Example:
        {'1': {'id': 270, 'name': 'Binance', 'slug': 'binance', 'quotes': [{'timestamp': '2018-06-03T00:00:00.000Z',
            'quote': {'USD': {'volume_24h': 1632390000, 'timestamp': '2018-06-03T00:00:00.000Z'}}, 'num_market_pairs': 338},
            {'timestamp': '2018-06-10T00:00:00.000Z', 'quote': {'USD': {'volume_24h': 1034720000, 'timestamp':
            '2018-06-10T00:00:00.000Z'}}, 'num_market_pairs': 349}, {'timestamp': '2018-06-17T00:00:00.000Z', 'quote':
            {'USD': {'volume_24h': 883885000, 'timestamp': '2018-06-17T00:00:00.000Z'}}, 'num_market_pairs': 357}]}}

    """

    additional_properties: dict[str, ExchangeHistoricalQuotesExchangeObject] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exchange_historical_quotes_exchange_object import ExchangeHistoricalQuotesExchangeObject

        d = dict(src_dict)
        exchange_historical_quotes_results_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ExchangeHistoricalQuotesExchangeObject.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        exchange_historical_quotes_results_map.additional_properties = additional_properties
        return exchange_historical_quotes_results_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ExchangeHistoricalQuotesExchangeObject:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ExchangeHistoricalQuotesExchangeObject) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
