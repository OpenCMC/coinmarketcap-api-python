from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.global_metrics_quotes_latest_quote_object import GlobalMetricsQuotesLatestQuoteObject


T = TypeVar("T", bound="GlobalMetricsQuotesLatestQuoteMap")


@_attrs_define
class GlobalMetricsQuotesLatestQuoteMap:
    """A map of market quotes in different currency conversions. The default map included is USD.

    Example:
        {'USD': {'total_market_cap': 250284668020.67, 'total_volume_24h': 16903498628.86, 'total_volume_24h_reported':
            16903498628.86, 'altcoin_volume_24h': 11883384723.14, 'altcoin_volume_24h_reported': 11883384723.14,
            'altcoin_market_cap': 119597549931.01, 'last_updated': '2018-06-02T23:46:14.000Z'}}

    """

    additional_properties: dict[str, GlobalMetricsQuotesLatestQuoteObject] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.global_metrics_quotes_latest_quote_object import GlobalMetricsQuotesLatestQuoteObject

        d = dict(src_dict)
        global_metrics_quotes_latest_quote_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = GlobalMetricsQuotesLatestQuoteObject.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        global_metrics_quotes_latest_quote_map.additional_properties = additional_properties
        return global_metrics_quotes_latest_quote_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> GlobalMetricsQuotesLatestQuoteObject:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: GlobalMetricsQuotesLatestQuoteObject) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
