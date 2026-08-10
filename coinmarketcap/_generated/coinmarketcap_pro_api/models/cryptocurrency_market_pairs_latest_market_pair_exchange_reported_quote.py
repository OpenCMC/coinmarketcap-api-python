from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptocurrencyMarketPairsLatestMarketPairExchangeReportedQuote")


@_attrs_define
class CryptocurrencyMarketPairsLatestMarketPairExchangeReportedQuote:
    """A default exchange reported quote containing raw exchange reported values.

    Attributes:
        price (float): The lastest exchange reported price for this market pair in quote currency units. Example:
            8000.23.
        volume_24h_base (float): The latest exchange reported 24 hour rolling volume for this market pair in base
            cryptocurrency units. Example: 30768.
        volume_24h_quote (float): The latest exchange reported 24 hour rolling volume for this market pair in quote
            cryptocurrency units. Example: 250448443.2.
        last_updated (str): Timestamp (ISO 8601) of the last time this market data was updated. Example:
            2018-06-02T23:59:59.999Z.
        effective_liquidity (str | Unset):
        market_score (str | Unset):
        market_reputation (str | Unset):
    """

    price: float
    volume_24h_base: float
    volume_24h_quote: float
    last_updated: str
    effective_liquidity: str | Unset = UNSET
    market_score: str | Unset = UNSET
    market_reputation: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price = self.price

        volume_24h_base = self.volume_24h_base

        volume_24h_quote = self.volume_24h_quote

        last_updated = self.last_updated

        effective_liquidity = self.effective_liquidity

        market_score = self.market_score

        market_reputation = self.market_reputation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "price": price,
                "volume_24h_base": volume_24h_base,
                "volume_24h_quote": volume_24h_quote,
                "last_updated": last_updated,
            }
        )
        if effective_liquidity is not UNSET:
            field_dict["effective_liquidity"] = effective_liquidity
        if market_score is not UNSET:
            field_dict["market_score"] = market_score
        if market_reputation is not UNSET:
            field_dict["market_reputation"] = market_reputation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price = d.pop("price")

        volume_24h_base = d.pop("volume_24h_base")

        volume_24h_quote = d.pop("volume_24h_quote")

        last_updated = d.pop("last_updated")

        effective_liquidity = d.pop("effective_liquidity", UNSET)

        market_score = d.pop("market_score", UNSET)

        market_reputation = d.pop("market_reputation", UNSET)

        cryptocurrency_market_pairs_latest_market_pair_exchange_reported_quote = cls(
            price=price,
            volume_24h_base=volume_24h_base,
            volume_24h_quote=volume_24h_quote,
            last_updated=last_updated,
            effective_liquidity=effective_liquidity,
            market_score=market_score,
            market_reputation=market_reputation,
        )

        cryptocurrency_market_pairs_latest_market_pair_exchange_reported_quote.additional_properties = d
        return cryptocurrency_market_pairs_latest_market_pair_exchange_reported_quote

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
