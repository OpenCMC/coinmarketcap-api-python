from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.global_metrics_quotes_historic_interval_quote_object import (
        GlobalMetricsQuotesHistoricIntervalQuoteObject,
    )


T = TypeVar("T", bound="GlobalMetricsQuotesHistoricResultsObject")


@_attrs_define
class GlobalMetricsQuotesHistoricResultsObject:
    """Results of your query returned as an object.

    Example:
        {'quotes': [{'timestamp': '2018-07-31T00:02:00.000Z', 'eth_dominance': 16.099, 'btc_dominance': 47.9949,
            'active_cryptocurrencies': 2500, 'active_exchanges': 600, 'active_market_pairs': 1000, 'quote': {'USD':
            {'total_market_cap': 292863223827.394, 'total_volume_24h': 17692152629.7864, 'total_volume_24h_reported':
            375179000000, 'altcoin_market_cap': 187589500000, 'altcoin_volume_24h': 375179000000,
            'altcoin_volume_24h_reported': 375179000000, 'timestamp': '2018-07-31T00:02:00.000Z'}}}, {'timestamp':
            '2018-08-01T00:02:00.000Z', 'eth_dominance': 16.099, 'btc_dominance': 48.0585, 'active_cryptocurrencies': 2500,
            'active_exchanges': 600, 'active_market_pairs': 1000, 'quote': {'USD': {'total_market_cap': 277770824530.303,
            'total_volume_24h': 15398085549.0344, 'total_volume_24h_reported': 375179000000, 'altcoin_market_cap':
            187589500000, 'altcoin_volume_24h': 375179000000, 'altcoin_volume_24h_reported': 375179000000, 'timestamp':
            '2018-07-31T00:02:00.000Z'}}}, {'timestamp': '2018-08-02T00:02:00.000Z', 'eth_dominance': 16.099,
            'btc_dominance': 48.041, 'active_cryptocurrencies': 2500, 'active_exchanges': 600, 'active_market_pairs': 1000,
            'quote': {'USD': {'total_market_cap': 273078776005.223, 'total_volume_24h': 14300071695.0547,
            'total_volume_24h_reported': 375179000000, 'altcoin_market_cap': 187589500000, 'altcoin_volume_24h':
            375179000000, 'altcoin_volume_24h_reported': 375179000000, 'timestamp': '2018-07-31T00:02:00.000Z'}}}]}

    Attributes:
        quotes (list[GlobalMetricsQuotesHistoricIntervalQuoteObject]): An array of aggregate market quotes for each
            interval.
    """

    quotes: list[GlobalMetricsQuotesHistoricIntervalQuoteObject]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quotes = []
        for componentsschemas_global_metrics_quotes_historic_interval_quotes_array_item_data in self.quotes:
            componentsschemas_global_metrics_quotes_historic_interval_quotes_array_item = (
                componentsschemas_global_metrics_quotes_historic_interval_quotes_array_item_data.to_dict()
            )
            quotes.append(componentsschemas_global_metrics_quotes_historic_interval_quotes_array_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quotes": quotes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.global_metrics_quotes_historic_interval_quote_object import (
            GlobalMetricsQuotesHistoricIntervalQuoteObject,
        )

        d = dict(src_dict)
        quotes = []
        _quotes = d.pop("quotes")
        for componentsschemas_global_metrics_quotes_historic_interval_quotes_array_item_data in _quotes:
            componentsschemas_global_metrics_quotes_historic_interval_quotes_array_item = (
                GlobalMetricsQuotesHistoricIntervalQuoteObject.from_dict(
                    componentsschemas_global_metrics_quotes_historic_interval_quotes_array_item_data
                )
            )

            quotes.append(componentsschemas_global_metrics_quotes_historic_interval_quotes_array_item)

        global_metrics_quotes_historic_results_object = cls(
            quotes=quotes,
        )

        global_metrics_quotes_historic_results_object.additional_properties = d
        return global_metrics_quotes_historic_results_object

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
