from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.category_cryptocurrency_object import CategoryCryptocurrencyObject


T = TypeVar("T", bound="CategoryResultsMap")


@_attrs_define
class CategoryResultsMap:
    """Results of your query returned as an object map.

    Example:
        {'1': {'id': '605e2ce9d41eae1066535f7c', 'name': 'A16Z Portfolio', 'title': 'A16Z Portfolio', 'description':
            'A16Z Portfolio', 'num_tokens': 12, 'avg_price_change': 0.61305157, 'market_cap': 29429241867.031097,
            'market_cap_change': 3.049044106496, 'volume': 4103706600.0391645, 'volume_change': -10.538325849854, 'coins':
            [{'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'cmc_rank': 5, 'num_market_pairs': 500,
            'circulating_supply': 16950100, 'total_supply': 16950100, 'max_supply': 21000000, 'last_updated':
            '2018-06-02T22:51:28.209Z', 'date_added': '2013-04-28T00:00:00.000Z', 'tags': ['mineable'], 'platform': None,
            'quote': {'USD': {'price': 9283.92, 'volume_24h': 7155680000, 'percent_change_1h': -0.152774,
            'percent_change_24h': 0.518894, 'percent_change_7d': 0.986573, 'market_cap': 158055024432, 'last_updated':
            '2018-08-09T22:53:32.000Z'}}}, {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum',
            'num_market_pairs': 6360, 'circulating_supply': 16950100, 'total_supply': 16950100, 'max_supply': 21000000,
            'last_updated': '2018-06-02T22:51:28.209Z', 'date_added': '2013-04-28T00:00:00.000Z', 'tags': ['mineable'],
            'platform': None, 'quote': {'USD': {'price': 1283.92, 'volume_24h': 7155680000, 'percent_change_1h': -0.152774,
            'percent_change_24h': 0.518894, 'percent_change_7d': 0.986573, 'market_cap': 158055024432, 'last_updated':
            '2018-08-09T22:53:32.000Z'}}}], 'last_updated': '2021-11-10T10:35:12.354Z'}}

    """

    additional_properties: dict[str, CategoryCryptocurrencyObject] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_cryptocurrency_object import CategoryCryptocurrencyObject

        d = dict(src_dict)
        category_results_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CategoryCryptocurrencyObject.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        category_results_map.additional_properties = additional_properties
        return category_results_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> CategoryCryptocurrencyObject:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: CategoryCryptocurrencyObject) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
