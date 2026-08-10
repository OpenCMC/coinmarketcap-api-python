from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExchangeHistoricalQuotesCurrencyQuoteObject")


@_attrs_define
class ExchangeHistoricalQuotesCurrencyQuoteObject:
    """The market details for the current interval and currency conversion option. The map key being the curency symbol.

    Attributes:
        volume_24h (float): Combined 24 hour volume for all market pairs on this exchange at the current historical
            interval. Example: 1235000.
        timestamp (str): Timestamp (ISO 8601) of when the conversion currency's current value was referenced for this
            conversion. Example: 2018-06-02T22:51:28.209Z.
    """

    volume_24h: float
    timestamp: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volume_24h = self.volume_24h

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "volume_24h": volume_24h,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        volume_24h = d.pop("volume_24h")

        timestamp = d.pop("timestamp")

        exchange_historical_quotes_currency_quote_object = cls(
            volume_24h=volume_24h,
            timestamp=timestamp,
        )

        exchange_historical_quotes_currency_quote_object.additional_properties = d
        return exchange_historical_quotes_currency_quote_object

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
