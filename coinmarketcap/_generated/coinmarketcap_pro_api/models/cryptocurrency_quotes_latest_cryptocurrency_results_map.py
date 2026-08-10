from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cryptocurrency_quotes_latest_cryptocurrency_object import (
        CryptocurrencyQuotesLatestCryptocurrencyObject,
    )


T = TypeVar("T", bound="CryptocurrencyQuotesLatestCryptocurrencyResultsMap")


@_attrs_define
class CryptocurrencyQuotesLatestCryptocurrencyResultsMap:
    """A map of cryptocurrency objects by ID, symbol, or slug (as used in query parameters).

    Example:
        {'1': {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'is_active': 1, 'is_fiat': 0,
            'circulating_supply': 17199862, 'total_supply': 17199862, 'max_supply': 21000000, 'date_added':
            '2013-04-28T00:00:00.000Z', 'num_market_pairs': 331, 'cmc_rank': 1, 'last_updated': '2018-08-09T21:56:28.000Z',
            'tags': ['mineable'], 'platform': None, 'self_reported_circulating_supply': None, 'self_reported_market_cap':
            None, 'minted_market_cap': 1802955697670.94, 'quote': {'USD': {'price': 6602.60701122, 'volume_24h':
            4314444687.5194, 'volume_change_24h': -0.152774, 'percent_change_1h': 0.988615, 'percent_change_24h': 4.37185,
            'percent_change_7d': -12.1352, 'percent_change_30d': -12.1352, 'market_cap': 852164659250.2758,
            'market_cap_dominance': 51, 'fully_diluted_market_cap': 952835089431.14, 'last_updated':
            '2018-08-09T21:56:28.000Z'}}}}

    """

    additional_properties: dict[str, CryptocurrencyQuotesLatestCryptocurrencyObject] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_quotes_latest_cryptocurrency_object import (
            CryptocurrencyQuotesLatestCryptocurrencyObject,
        )

        d = dict(src_dict)
        cryptocurrency_quotes_latest_cryptocurrency_results_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CryptocurrencyQuotesLatestCryptocurrencyObject.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        cryptocurrency_quotes_latest_cryptocurrency_results_map.additional_properties = additional_properties
        return cryptocurrency_quotes_latest_cryptocurrency_results_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> CryptocurrencyQuotesLatestCryptocurrencyObject:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: CryptocurrencyQuotesLatestCryptocurrencyObject) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
