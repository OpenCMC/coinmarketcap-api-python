from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GlobalMetricsQuotesHistoricCurrencyQuoteObject")


@_attrs_define
class GlobalMetricsQuotesHistoricCurrencyQuoteObject:
    """The market details for the current interval and currency conversion option. The map key being the curency symbol.

    Attributes:
        total_market_cap (float): The sum of all individual cryptocurrency market capitalizations at the given point in
            time, historically converted into units of the requested currency. Example: 375179000000.
        total_volume_24h (float): The sum of rolling 24 hour adjusted volume (as outlined in our methodology) for all
            cryptocurrencies at the given point in time, historically converted into units of the requested currency.
            Example: 19918400000.
        total_volume_24h_reported (float): The sum of rolling 24 hour reported volume for all cryptocurrencies at the
            given point in time, historically converted into units of the requested currency. *Note: This field is only
            available after 2019-05-10 and will return `null` prior to that time.* Example: 19918400000.
        altcoin_market_cap (float): The sum of rolling 24 hour adjusted volume (as outlined in our methodology) for all
            cryptocurrencies excluding Bitcoin at the given point in time, historically converted into units of the
            requested currency. Example: 187589500000.
        altcoin_volume_24h (float): The sum of all individual cryptocurrency market capitalizations excluding Bitcoin at
            the given point in time, historically converted into units of the requested currency. Example: 19918400000.
        altcoin_volume_24h_reported (float): The sum of rolling 24 hour reported volume for all cryptocurrencies
            excluding Bitcoin at the given point in time, historically converted into units of the requested currency.
            *Note: This field is only available after 2019-05-10 and will return `null` prior to that time.* Example:
            19918400000.
        timestamp (str): Timestamp (ISO 8601) of when the conversion currency's current value was referenced for this
            conversion. Example: 2018-06-02T22:51:28.209Z.
    """

    total_market_cap: float
    total_volume_24h: float
    total_volume_24h_reported: float
    altcoin_market_cap: float
    altcoin_volume_24h: float
    altcoin_volume_24h_reported: float
    timestamp: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_market_cap = self.total_market_cap

        total_volume_24h = self.total_volume_24h

        total_volume_24h_reported = self.total_volume_24h_reported

        altcoin_market_cap = self.altcoin_market_cap

        altcoin_volume_24h = self.altcoin_volume_24h

        altcoin_volume_24h_reported = self.altcoin_volume_24h_reported

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_market_cap": total_market_cap,
                "total_volume_24h": total_volume_24h,
                "total_volume_24h_reported": total_volume_24h_reported,
                "altcoin_market_cap": altcoin_market_cap,
                "altcoin_volume_24h": altcoin_volume_24h,
                "altcoin_volume_24h_reported": altcoin_volume_24h_reported,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_market_cap = d.pop("total_market_cap")

        total_volume_24h = d.pop("total_volume_24h")

        total_volume_24h_reported = d.pop("total_volume_24h_reported")

        altcoin_market_cap = d.pop("altcoin_market_cap")

        altcoin_volume_24h = d.pop("altcoin_volume_24h")

        altcoin_volume_24h_reported = d.pop("altcoin_volume_24h_reported")

        timestamp = d.pop("timestamp")

        global_metrics_quotes_historic_currency_quote_object = cls(
            total_market_cap=total_market_cap,
            total_volume_24h=total_volume_24h,
            total_volume_24h_reported=total_volume_24h_reported,
            altcoin_market_cap=altcoin_market_cap,
            altcoin_volume_24h=altcoin_volume_24h,
            altcoin_volume_24h_reported=altcoin_volume_24h_reported,
            timestamp=timestamp,
        )

        global_metrics_quotes_historic_currency_quote_object.additional_properties = d
        return global_metrics_quotes_historic_currency_quote_object

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
