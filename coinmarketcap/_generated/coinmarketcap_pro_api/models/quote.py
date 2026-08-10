from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Quote")


@_attrs_define
class Quote:
    """
    Attributes:
        id (int | Unset): Currency ID
        symbol (str | Unset): Currency symbol
        price (float | Unset): Current price in the specified currency
        volume_24h (float | Unset): 24-hour trading volume
        cex_volume_24h (float | Unset): 24-hour trading volume from centralized exchanges
        dex_volume_24h (float | Unset): 24-hour trading volume from decentralized exchanges
        volume_24h_reported (float | Unset): Reported 24-hour trading volume
        volume_7d (float | Unset): 7-day trading volume
        volume_7d_reported (float | Unset): Reported 7-day trading volume
        volume_30d (float | Unset): 30-day trading volume
        volume_30d_reported (float | Unset): Reported 30-day trading volume
        volume_change_24h (float | Unset): 24-hour volume change percentage
        percent_change_1h (float | Unset): 1-hour percentage change
        percent_change_24h (float | Unset): 24-hour percentage change
        percent_change_7d (float | Unset): 7-day percentage change
        percent_change_30d (float | Unset): 30-day percentage change
        percent_change_60d (float | Unset): 60-day percentage change
        percent_change_90d (float | Unset): 90-day percentage change
        market_cap (float | Unset): Current market capitalization
        market_cap_dominance (float | Unset): Market cap dominance percentage
        fully_diluted_market_cap (float | Unset): Fully diluted market capitalization
        minted_market_cap (float | Unset): Minted market capitalization
        tvl (float | Unset): Total Value Locked
        market_cap_by_total_supply (float | Unset): Market cap calculated by total supply
        last_updated (str | Unset): Last updated timestamp
    """

    id: int | Unset = UNSET
    symbol: str | Unset = UNSET
    price: float | Unset = UNSET
    volume_24h: float | Unset = UNSET
    cex_volume_24h: float | Unset = UNSET
    dex_volume_24h: float | Unset = UNSET
    volume_24h_reported: float | Unset = UNSET
    volume_7d: float | Unset = UNSET
    volume_7d_reported: float | Unset = UNSET
    volume_30d: float | Unset = UNSET
    volume_30d_reported: float | Unset = UNSET
    volume_change_24h: float | Unset = UNSET
    percent_change_1h: float | Unset = UNSET
    percent_change_24h: float | Unset = UNSET
    percent_change_7d: float | Unset = UNSET
    percent_change_30d: float | Unset = UNSET
    percent_change_60d: float | Unset = UNSET
    percent_change_90d: float | Unset = UNSET
    market_cap: float | Unset = UNSET
    market_cap_dominance: float | Unset = UNSET
    fully_diluted_market_cap: float | Unset = UNSET
    minted_market_cap: float | Unset = UNSET
    tvl: float | Unset = UNSET
    market_cap_by_total_supply: float | Unset = UNSET
    last_updated: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        symbol = self.symbol

        price = self.price

        volume_24h = self.volume_24h

        cex_volume_24h = self.cex_volume_24h

        dex_volume_24h = self.dex_volume_24h

        volume_24h_reported = self.volume_24h_reported

        volume_7d = self.volume_7d

        volume_7d_reported = self.volume_7d_reported

        volume_30d = self.volume_30d

        volume_30d_reported = self.volume_30d_reported

        volume_change_24h = self.volume_change_24h

        percent_change_1h = self.percent_change_1h

        percent_change_24h = self.percent_change_24h

        percent_change_7d = self.percent_change_7d

        percent_change_30d = self.percent_change_30d

        percent_change_60d = self.percent_change_60d

        percent_change_90d = self.percent_change_90d

        market_cap = self.market_cap

        market_cap_dominance = self.market_cap_dominance

        fully_diluted_market_cap = self.fully_diluted_market_cap

        minted_market_cap = self.minted_market_cap

        tvl = self.tvl

        market_cap_by_total_supply = self.market_cap_by_total_supply

        last_updated = self.last_updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if price is not UNSET:
            field_dict["price"] = price
        if volume_24h is not UNSET:
            field_dict["volume_24h"] = volume_24h
        if cex_volume_24h is not UNSET:
            field_dict["cex_volume_24h"] = cex_volume_24h
        if dex_volume_24h is not UNSET:
            field_dict["dex_volume_24h"] = dex_volume_24h
        if volume_24h_reported is not UNSET:
            field_dict["volume_24h_reported"] = volume_24h_reported
        if volume_7d is not UNSET:
            field_dict["volume_7d"] = volume_7d
        if volume_7d_reported is not UNSET:
            field_dict["volume_7d_reported"] = volume_7d_reported
        if volume_30d is not UNSET:
            field_dict["volume_30d"] = volume_30d
        if volume_30d_reported is not UNSET:
            field_dict["volume_30d_reported"] = volume_30d_reported
        if volume_change_24h is not UNSET:
            field_dict["volume_change_24h"] = volume_change_24h
        if percent_change_1h is not UNSET:
            field_dict["percent_change_1h"] = percent_change_1h
        if percent_change_24h is not UNSET:
            field_dict["percent_change_24h"] = percent_change_24h
        if percent_change_7d is not UNSET:
            field_dict["percent_change_7d"] = percent_change_7d
        if percent_change_30d is not UNSET:
            field_dict["percent_change_30d"] = percent_change_30d
        if percent_change_60d is not UNSET:
            field_dict["percent_change_60d"] = percent_change_60d
        if percent_change_90d is not UNSET:
            field_dict["percent_change_90d"] = percent_change_90d
        if market_cap is not UNSET:
            field_dict["market_cap"] = market_cap
        if market_cap_dominance is not UNSET:
            field_dict["market_cap_dominance"] = market_cap_dominance
        if fully_diluted_market_cap is not UNSET:
            field_dict["fully_diluted_market_cap"] = fully_diluted_market_cap
        if minted_market_cap is not UNSET:
            field_dict["minted_market_cap"] = minted_market_cap
        if tvl is not UNSET:
            field_dict["tvl"] = tvl
        if market_cap_by_total_supply is not UNSET:
            field_dict["market_cap_by_total_supply"] = market_cap_by_total_supply
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        symbol = d.pop("symbol", UNSET)

        price = d.pop("price", UNSET)

        volume_24h = d.pop("volume_24h", UNSET)

        cex_volume_24h = d.pop("cex_volume_24h", UNSET)

        dex_volume_24h = d.pop("dex_volume_24h", UNSET)

        volume_24h_reported = d.pop("volume_24h_reported", UNSET)

        volume_7d = d.pop("volume_7d", UNSET)

        volume_7d_reported = d.pop("volume_7d_reported", UNSET)

        volume_30d = d.pop("volume_30d", UNSET)

        volume_30d_reported = d.pop("volume_30d_reported", UNSET)

        volume_change_24h = d.pop("volume_change_24h", UNSET)

        percent_change_1h = d.pop("percent_change_1h", UNSET)

        percent_change_24h = d.pop("percent_change_24h", UNSET)

        percent_change_7d = d.pop("percent_change_7d", UNSET)

        percent_change_30d = d.pop("percent_change_30d", UNSET)

        percent_change_60d = d.pop("percent_change_60d", UNSET)

        percent_change_90d = d.pop("percent_change_90d", UNSET)

        market_cap = d.pop("market_cap", UNSET)

        market_cap_dominance = d.pop("market_cap_dominance", UNSET)

        fully_diluted_market_cap = d.pop("fully_diluted_market_cap", UNSET)

        minted_market_cap = d.pop("minted_market_cap", UNSET)

        tvl = d.pop("tvl", UNSET)

        market_cap_by_total_supply = d.pop("market_cap_by_total_supply", UNSET)

        last_updated = d.pop("last_updated", UNSET)

        quote = cls(
            id=id,
            symbol=symbol,
            price=price,
            volume_24h=volume_24h,
            cex_volume_24h=cex_volume_24h,
            dex_volume_24h=dex_volume_24h,
            volume_24h_reported=volume_24h_reported,
            volume_7d=volume_7d,
            volume_7d_reported=volume_7d_reported,
            volume_30d=volume_30d,
            volume_30d_reported=volume_30d_reported,
            volume_change_24h=volume_change_24h,
            percent_change_1h=percent_change_1h,
            percent_change_24h=percent_change_24h,
            percent_change_7d=percent_change_7d,
            percent_change_30d=percent_change_30d,
            percent_change_60d=percent_change_60d,
            percent_change_90d=percent_change_90d,
            market_cap=market_cap,
            market_cap_dominance=market_cap_dominance,
            fully_diluted_market_cap=fully_diluted_market_cap,
            minted_market_cap=minted_market_cap,
            tvl=tvl,
            market_cap_by_total_supply=market_cap_by_total_supply,
            last_updated=last_updated,
        )

        quote.additional_properties = d
        return quote

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
