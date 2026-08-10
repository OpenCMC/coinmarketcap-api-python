from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExchangeMarketPairsLatestMarketPairQuote")


@_attrs_define
class ExchangeMarketPairsLatestMarketPairQuote:
    """One or more market quotes where $key is the conversion currency requested, ex. USD

    Attributes:
        price (float): The last reported exchange price for this market pair converted into the requested convert
            currency. Example: 8000.23.
        volume_24h (float): The last reported exchange volume for this market pair converted into the requested convert
            currency. Example: 1600000.
        last_updated (str): Timestamp (ISO 8601) of when the conversion currency's current value was referenced for this
            conversion. Example: 2018-06-02T23:59:59.999Z.
        price_quote (float | Unset): The latest exchange reported price in base units converted into the requested
            convert currency. *This field is only returned if requested through the `aux` request parameter.* Example:
            8000.23.
        depth_negative_two (float | Unset): -2% Depth in the specified currency. Example: 1600000.
        depth_positive_two (float | Unset): +2% Depth in the specified currency. Example: 1600000.
        effective_liquidity (str | Unset):
        market_score (str | Unset):
        market_reputation (str | Unset):
    """

    price: float
    volume_24h: float
    last_updated: str
    price_quote: float | Unset = UNSET
    depth_negative_two: float | Unset = UNSET
    depth_positive_two: float | Unset = UNSET
    effective_liquidity: str | Unset = UNSET
    market_score: str | Unset = UNSET
    market_reputation: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price = self.price

        volume_24h = self.volume_24h

        last_updated = self.last_updated

        price_quote = self.price_quote

        depth_negative_two = self.depth_negative_two

        depth_positive_two = self.depth_positive_two

        effective_liquidity = self.effective_liquidity

        market_score = self.market_score

        market_reputation = self.market_reputation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "price": price,
                "volume_24h": volume_24h,
                "last_updated": last_updated,
            }
        )
        if price_quote is not UNSET:
            field_dict["price_quote"] = price_quote
        if depth_negative_two is not UNSET:
            field_dict["depth_negative_two"] = depth_negative_two
        if depth_positive_two is not UNSET:
            field_dict["depth_positive_two"] = depth_positive_two
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

        volume_24h = d.pop("volume_24h")

        last_updated = d.pop("last_updated")

        price_quote = d.pop("price_quote", UNSET)

        depth_negative_two = d.pop("depth_negative_two", UNSET)

        depth_positive_two = d.pop("depth_positive_two", UNSET)

        effective_liquidity = d.pop("effective_liquidity", UNSET)

        market_score = d.pop("market_score", UNSET)

        market_reputation = d.pop("market_reputation", UNSET)

        exchange_market_pairs_latest_market_pair_quote = cls(
            price=price,
            volume_24h=volume_24h,
            last_updated=last_updated,
            price_quote=price_quote,
            depth_negative_two=depth_negative_two,
            depth_positive_two=depth_positive_two,
            effective_liquidity=effective_liquidity,
            market_score=market_score,
            market_reputation=market_reputation,
        )

        exchange_market_pairs_latest_market_pair_quote.additional_properties = d
        return exchange_market_pairs_latest_market_pair_quote

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
