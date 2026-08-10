from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptoQuoteDTO")


@_attrs_define
class CryptoQuoteDTO:
    """
    Attributes:
        score (int | Unset): Score value for sorting or ranking
        price (float | Unset): Current price in USD
        volume (float | Unset): 24-hour trading volume in USD
        market_cap (float | Unset): Market capitalization in USD
        total_supply (float | Unset): Total supply of the cryptocurrency
        circulating_supply (float | Unset): Circulating supply of the cryptocurrency
        percentage_change_price_usd_1_h (float | Unset): 1-hour percentage change in USD price
        percentage_change_price_usd_24_h (float | Unset): 24-hour percentage change in USD price
        percentage_change_price_usd_7_d (float | Unset): 7-day percentage change in USD price
        percentage_change_price_usd_30_d (float | Unset): 30-day percentage change in USD price
    """

    score: int | Unset = UNSET
    price: float | Unset = UNSET
    volume: float | Unset = UNSET
    market_cap: float | Unset = UNSET
    total_supply: float | Unset = UNSET
    circulating_supply: float | Unset = UNSET
    percentage_change_price_usd_1_h: float | Unset = UNSET
    percentage_change_price_usd_24_h: float | Unset = UNSET
    percentage_change_price_usd_7_d: float | Unset = UNSET
    percentage_change_price_usd_30_d: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        score = self.score

        price = self.price

        volume = self.volume

        market_cap = self.market_cap

        total_supply = self.total_supply

        circulating_supply = self.circulating_supply

        percentage_change_price_usd_1_h = self.percentage_change_price_usd_1_h

        percentage_change_price_usd_24_h = self.percentage_change_price_usd_24_h

        percentage_change_price_usd_7_d = self.percentage_change_price_usd_7_d

        percentage_change_price_usd_30_d = self.percentage_change_price_usd_30_d

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if score is not UNSET:
            field_dict["score"] = score
        if price is not UNSET:
            field_dict["price"] = price
        if volume is not UNSET:
            field_dict["volume"] = volume
        if market_cap is not UNSET:
            field_dict["marketCap"] = market_cap
        if total_supply is not UNSET:
            field_dict["totalSupply"] = total_supply
        if circulating_supply is not UNSET:
            field_dict["circulatingSupply"] = circulating_supply
        if percentage_change_price_usd_1_h is not UNSET:
            field_dict["percentageChangePriceUsd1h"] = percentage_change_price_usd_1_h
        if percentage_change_price_usd_24_h is not UNSET:
            field_dict["percentageChangePriceUsd24h"] = percentage_change_price_usd_24_h
        if percentage_change_price_usd_7_d is not UNSET:
            field_dict["percentageChangePriceUsd7d"] = percentage_change_price_usd_7_d
        if percentage_change_price_usd_30_d is not UNSET:
            field_dict["percentageChangePriceUsd30d"] = percentage_change_price_usd_30_d

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        score = d.pop("score", UNSET)

        price = d.pop("price", UNSET)

        volume = d.pop("volume", UNSET)

        market_cap = d.pop("marketCap", UNSET)

        total_supply = d.pop("totalSupply", UNSET)

        circulating_supply = d.pop("circulatingSupply", UNSET)

        percentage_change_price_usd_1_h = d.pop("percentageChangePriceUsd1h", UNSET)

        percentage_change_price_usd_24_h = d.pop("percentageChangePriceUsd24h", UNSET)

        percentage_change_price_usd_7_d = d.pop("percentageChangePriceUsd7d", UNSET)

        percentage_change_price_usd_30_d = d.pop("percentageChangePriceUsd30d", UNSET)

        crypto_quote_dto = cls(
            score=score,
            price=price,
            volume=volume,
            market_cap=market_cap,
            total_supply=total_supply,
            circulating_supply=circulating_supply,
            percentage_change_price_usd_1_h=percentage_change_price_usd_1_h,
            percentage_change_price_usd_24_h=percentage_change_price_usd_24_h,
            percentage_change_price_usd_7_d=percentage_change_price_usd_7_d,
            percentage_change_price_usd_30_d=percentage_change_price_usd_30_d,
        )

        crypto_quote_dto.additional_properties = d
        return crypto_quote_dto

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
