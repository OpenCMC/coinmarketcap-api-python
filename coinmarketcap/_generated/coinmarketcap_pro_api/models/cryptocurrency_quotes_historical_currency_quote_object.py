from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptocurrencyQuotesHistoricalCurrencyQuoteObject")


@_attrs_define
class CryptocurrencyQuotesHistoricalCurrencyQuoteObject:
    """The market details for the current interval and currency conversion option. The map key being the curency symbol.

    Attributes:
        price (float): Price at this interval quote. Example: 1235000.
        volume_24h (float): Aggregate 24 hour adjusted volume for all market pairs tracked for this cryptocurrency at
            the current historical interval. Example: 1235000.
        market_cap (float): Number of market pairs available at the current historical interval. Example: 123456789.
        timestamp (str): Timestamp (ISO 8601) of when the conversion currency's current value was referenced for this
            conversion. Example: 2018-06-02T22:51:28.209Z.
        percent_change_1h (float | Unset): 1 hour price change as a percentage, at the time of this quote.
        percent_change_24h (float | Unset): 24 hour price change as a percentage, at the time of this quote.
        percent_change_7d (float | Unset): 7 day price change as a percentage, at the time of this quote.
        percent_change_30d (float | Unset): 30 day price change as a percentage, at the time of this quote.
        circulating_supply (float | Unset): Circulating supply at the time of this quote.
        total_supply (float | Unset): Total supply at the time of this quote.
    """

    price: float
    volume_24h: float
    market_cap: float
    timestamp: str
    percent_change_1h: float | Unset = UNSET
    percent_change_24h: float | Unset = UNSET
    percent_change_7d: float | Unset = UNSET
    percent_change_30d: float | Unset = UNSET
    circulating_supply: float | Unset = UNSET
    total_supply: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price = self.price

        volume_24h = self.volume_24h

        market_cap = self.market_cap

        timestamp = self.timestamp

        percent_change_1h = self.percent_change_1h

        percent_change_24h = self.percent_change_24h

        percent_change_7d = self.percent_change_7d

        percent_change_30d = self.percent_change_30d

        circulating_supply = self.circulating_supply

        total_supply = self.total_supply

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "price": price,
                "volume_24h": volume_24h,
                "market_cap": market_cap,
                "timestamp": timestamp,
            }
        )
        if percent_change_1h is not UNSET:
            field_dict["percent_change_1h"] = percent_change_1h
        if percent_change_24h is not UNSET:
            field_dict["percent_change_24h"] = percent_change_24h
        if percent_change_7d is not UNSET:
            field_dict["percent_change_7d"] = percent_change_7d
        if percent_change_30d is not UNSET:
            field_dict["percent_change_30d"] = percent_change_30d
        if circulating_supply is not UNSET:
            field_dict["circulating_supply"] = circulating_supply
        if total_supply is not UNSET:
            field_dict["total_supply"] = total_supply

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price = d.pop("price")

        volume_24h = d.pop("volume_24h")

        market_cap = d.pop("market_cap")

        timestamp = d.pop("timestamp")

        percent_change_1h = d.pop("percent_change_1h", UNSET)

        percent_change_24h = d.pop("percent_change_24h", UNSET)

        percent_change_7d = d.pop("percent_change_7d", UNSET)

        percent_change_30d = d.pop("percent_change_30d", UNSET)

        circulating_supply = d.pop("circulating_supply", UNSET)

        total_supply = d.pop("total_supply", UNSET)

        cryptocurrency_quotes_historical_currency_quote_object = cls(
            price=price,
            volume_24h=volume_24h,
            market_cap=market_cap,
            timestamp=timestamp,
            percent_change_1h=percent_change_1h,
            percent_change_24h=percent_change_24h,
            percent_change_7d=percent_change_7d,
            percent_change_30d=percent_change_30d,
            circulating_supply=circulating_supply,
            total_supply=total_supply,
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
