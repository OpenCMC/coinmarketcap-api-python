from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CryptocurrencyQuotesHistoricalCurrencyQuoteObject")


@_attrs_define
class CryptocurrencyQuotesHistoricalCurrencyQuoteObject:
    """The market details for the current interval and currency conversion option. The map key being the curency symbol.

    Attributes:
        price (float): Price at this interval quote. Example: 1235000.
        volume_24hr (float): Aggregate 24 hour adjusted volume for all market pairs tracked for this cryptocurrency at
            the current historical interval. Example: 1235000.
        market_cap (float): Number of market pairs available at the current historical interval. Example: 123456789.
        timestamp (str): Timestamp (ISO 8601) of when the conversion currency's current value was referenced for this
            conversion. Example: 2018-06-02T22:51:28.209Z.
    """

    price: float
    volume_24hr: float
    market_cap: float
    timestamp: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price = self.price

        volume_24hr = self.volume_24hr

        market_cap = self.market_cap

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "price": price,
                "volume_24hr": volume_24hr,
                "market_cap": market_cap,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price = d.pop("price")

        volume_24hr = d.pop("volume_24hr")

        market_cap = d.pop("market_cap")

        timestamp = d.pop("timestamp")

        cryptocurrency_quotes_historical_currency_quote_object = cls(
            price=price,
            volume_24hr=volume_24hr,
            market_cap=market_cap,
            timestamp=timestamp,
        )

        cryptocurrency_quotes_historical_currency_quote_object.additional_properties = d
        return cryptocurrency_quotes_historical_currency_quote_object

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
