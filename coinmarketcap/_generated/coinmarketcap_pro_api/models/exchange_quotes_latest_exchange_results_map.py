from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exchange_quotes_latest_exchange_object import ExchangeQuotesLatestExchangeObject


T = TypeVar("T", bound="ExchangeQuotesLatestExchangeResultsMap")


@_attrs_define
class ExchangeQuotesLatestExchangeResultsMap:
    """A map of exchange objects by ID or slugs (as used in query parameters).

    Example:
        {'1': {'id': 270, 'name': 'Binance', 'slug': 'binance', 'num_coins': 132, 'num_market_pairs': 385,
            'last_updated': '2018-11-08T22:11:00.000Z', 'traffic_score': 1000, 'rank': 1, 'exchange_score': 9.8,
            'liquidity_score': 9.8028, 'quote': {'USD': {'volume_24h': 768478308.529847, 'volume_24h_adjusted':
            768478308.529847, 'volume_7d': 3666423776, 'volume_30d': 21338299776, 'percent_change_volume_24h': -11.8232,
            'percent_change_volume_7d': 67.0306, 'percent_change_volume_30d': -0.0821558, 'effective_liquidity_24h':
            629.9774, 'last_updated': '2018-11-08T22:18:00.000Z'}}}}

    """

    additional_properties: dict[str, ExchangeQuotesLatestExchangeObject] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exchange_quotes_latest_exchange_object import ExchangeQuotesLatestExchangeObject

        d = dict(src_dict)
        exchange_quotes_latest_exchange_results_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ExchangeQuotesLatestExchangeObject.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        exchange_quotes_latest_exchange_results_map.additional_properties = additional_properties
        return exchange_quotes_latest_exchange_results_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ExchangeQuotesLatestExchangeObject:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ExchangeQuotesLatestExchangeObject) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
