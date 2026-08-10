from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cryptocurrency_price_performance_stats_latest_cryptocurrency_object import (
        CryptocurrencyPricePerformanceStatsLatestCryptocurrencyObject,
    )


T = TypeVar("T", bound="CryptocurrencyPricePerformanceStatsLatestCryptocurrencyResultsMap")


@_attrs_define
class CryptocurrencyPricePerformanceStatsLatestCryptocurrencyResultsMap:
    """An object map of cryptocurrency objects by ID, slug, or symbol (as used in query parameters).

    Example:
        {'1': {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'last_updated':
            '2019-08-22T01:51:32.000Z', 'periods': {'USD': {'open_timestamp': '2013-04-28T00:00:00.000Z', 'high_timestamp':
            '2017-12-17T12:19:14.000Z', 'low_timestamp': '2013-07-05T18:56:01.000Z', 'close_timestamp':
            '2019-08-22T01:52:18.613Z', 'quote': {'USD': {'open': 135.3000030517578, 'open_timestamp':
            '2013-04-28T00:00:00.000Z', 'high': 20088.99609375, 'high_timestamp': '2017-12-17T12:19:14.000Z', 'low':
            65.5260009765625, 'low_timestamp': '2013-07-05T18:56:01.000Z', 'close': 65.5260009765625, 'close_timestamp':
            '2019-08-22T01:52:18.618Z', 'percent_change': 7223.718930042746, 'price_change': 9773.691932798241}}}}}}

    """

    additional_properties: dict[str, CryptocurrencyPricePerformanceStatsLatestCryptocurrencyObject] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_price_performance_stats_latest_cryptocurrency_object import (
            CryptocurrencyPricePerformanceStatsLatestCryptocurrencyObject,
        )

        d = dict(src_dict)
        cryptocurrency_price_performance_stats_latest_cryptocurrency_results_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CryptocurrencyPricePerformanceStatsLatestCryptocurrencyObject.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        cryptocurrency_price_performance_stats_latest_cryptocurrency_results_map.additional_properties = (
            additional_properties
        )
        return cryptocurrency_price_performance_stats_latest_cryptocurrency_results_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> CryptocurrencyPricePerformanceStatsLatestCryptocurrencyObject:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: CryptocurrencyPricePerformanceStatsLatestCryptocurrencyObject) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
