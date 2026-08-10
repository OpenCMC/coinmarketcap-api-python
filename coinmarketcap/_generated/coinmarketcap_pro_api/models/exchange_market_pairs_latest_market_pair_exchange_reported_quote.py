from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExchangeMarketPairsLatestMarketPairExchangeReportedQuote")


@_attrs_define
class ExchangeMarketPairsLatestMarketPairExchangeReportedQuote:
    """A default exchange reported quote containing raw exchange reported values.

    Attributes:
        price (float): The last exchange reported price for this market pair in quote currency units. Example: 8000.23.
        volume_24h_base (float): The last exchange reported 24 hour volume for this market pair in base cryptocurrency
            units. Example: 30768.
        volume_24h_quote (float): The last exchange reported 24 hour volume for this market pair in quote cryptocurrency
            units. Example: 250448443.2.
        volume_percentage (float): Percentage of total exchange volume_24h Example: 0.03.
        last_updated (str): Timestamp (ISO 8601) of the last time this market data was updated. Example:
            2018-06-02T23:59:59.999Z.
    """

    price: float
    volume_24h_base: float
    volume_24h_quote: float
    volume_percentage: float
    last_updated: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price = self.price

        volume_24h_base = self.volume_24h_base

        volume_24h_quote = self.volume_24h_quote

        volume_percentage = self.volume_percentage

        last_updated = self.last_updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "price": price,
                "volume_24h_base": volume_24h_base,
                "volume_24h_quote": volume_24h_quote,
                "volume_percentage": volume_percentage,
                "last_updated": last_updated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price = d.pop("price")

        volume_24h_base = d.pop("volume_24h_base")

        volume_24h_quote = d.pop("volume_24h_quote")

        volume_percentage = d.pop("volume_percentage")

        last_updated = d.pop("last_updated")

        exchange_market_pairs_latest_market_pair_exchange_reported_quote = cls(
            price=price,
            volume_24h_base=volume_24h_base,
            volume_24h_quote=volume_24h_quote,
            volume_percentage=volume_percentage,
            last_updated=last_updated,
        )

        exchange_market_pairs_latest_market_pair_exchange_reported_quote.additional_properties = d
        return exchange_market_pairs_latest_market_pair_exchange_reported_quote

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
