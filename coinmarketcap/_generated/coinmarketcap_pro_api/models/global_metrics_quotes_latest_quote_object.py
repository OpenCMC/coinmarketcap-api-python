from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GlobalMetricsQuotesLatestQuoteObject")


@_attrs_define
class GlobalMetricsQuotesLatestQuoteObject:
    """A market quote in the currency conversion option.

    Attributes:
        total_market_cap (float): The sum of all individual cryptocurrency market capitalizations in the requested
            currency. Example: 250385096532.124.
        total_volume_24h (float): The sum of rolling 24 hour adjusted volume (as outlined in our methodology) for all
            cryptocurrencies in the requested currency. Example: 119270642406.968.
        total_volume_24h_reported (float): The sum of rolling 24 hour reported volume for all cryptocurrencies in the
            requested currency. Example: 1514905418.39087.
        altcoin_volume_24h (float): The sum of rolling 24 hour adjusted volume (as outlined in our methodology) for all
            cryptocurrencies excluding Bitcoin in the requested currency. Example: 119270642406.968.
        altcoin_volume_24h_reported (float): The sum of rolling 24 hour reported volume for all cryptocurrencies
            excluding Bitcoin in the requested currency. Example: 1514905418.39087.
        altcoin_market_cap (float): The sum of all individual cryptocurrency market capitalizations excluding Bitcoin in
            the requested currency. Example: 250385096532.124.
        last_updated (str): Timestamp (ISO 8601) of when the conversion currency's current value was referenced.
            Example: 2019-05-16T18:47:00.000Z.
    """

    total_market_cap: float
    total_volume_24h: float
    total_volume_24h_reported: float
    altcoin_volume_24h: float
    altcoin_volume_24h_reported: float
    altcoin_market_cap: float
    last_updated: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_market_cap = self.total_market_cap

        total_volume_24h = self.total_volume_24h

        total_volume_24h_reported = self.total_volume_24h_reported

        altcoin_volume_24h = self.altcoin_volume_24h

        altcoin_volume_24h_reported = self.altcoin_volume_24h_reported

        altcoin_market_cap = self.altcoin_market_cap

        last_updated = self.last_updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_market_cap": total_market_cap,
                "total_volume_24h": total_volume_24h,
                "total_volume_24h_reported": total_volume_24h_reported,
                "altcoin_volume_24h": altcoin_volume_24h,
                "altcoin_volume_24h_reported": altcoin_volume_24h_reported,
                "altcoin_market_cap": altcoin_market_cap,
                "last_updated": last_updated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_market_cap = d.pop("total_market_cap")

        total_volume_24h = d.pop("total_volume_24h")

        total_volume_24h_reported = d.pop("total_volume_24h_reported")

        altcoin_volume_24h = d.pop("altcoin_volume_24h")

        altcoin_volume_24h_reported = d.pop("altcoin_volume_24h_reported")

        altcoin_market_cap = d.pop("altcoin_market_cap")

        last_updated = d.pop("last_updated")

        global_metrics_quotes_latest_quote_object = cls(
            total_market_cap=total_market_cap,
            total_volume_24h=total_volume_24h,
            total_volume_24h_reported=total_volume_24h_reported,
            altcoin_volume_24h=altcoin_volume_24h,
            altcoin_volume_24h_reported=altcoin_volume_24h_reported,
            altcoin_market_cap=altcoin_market_cap,
            last_updated=last_updated,
        )

        global_metrics_quotes_latest_quote_object.additional_properties = d
        return global_metrics_quotes_latest_quote_object

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
