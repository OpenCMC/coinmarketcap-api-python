from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptoSnapshotDTO")


@_attrs_define
class CryptoSnapshotDTO:
    """
    Attributes:
        symbol (str | Unset): Cryptocurrency symbol
        name (str | Unset): Cryptocurrency name
        slug (str | Unset): Cryptocurrency slug
        rank (int | Unset): Cryptocurrency rank
        id (int | Unset): Cryptocurrency ID
        tag_names (str | Unset): Tag names
        tag_groups (str | Unset): Tag groups
        num_market_pairs (int | Unset): Number of market pairs
        target_date (str | Unset): Target date
        last_update (str | Unset): Last update time
        price_usd (float | Unset): Price in USD
        max_supply (float | Unset): Max supply
        volume_usd (float | Unset): Volume in USD
        available_supply (float | Unset): Available supply
        total_supply (float | Unset): Total supply
        market_cap (float | Unset): Market capitalization
        percentage_change_price_usd_1h (float | Unset): Percentage change in price USD in 1 hour
        percentage_change_price_usd_24h (float | Unset): Percentage change in price USD in 24 hours
        percentage_change_price_usd_7d (float | Unset): Percentage change in price USD in 7 days
    """

    symbol: str | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    rank: int | Unset = UNSET
    id: int | Unset = UNSET
    tag_names: str | Unset = UNSET
    tag_groups: str | Unset = UNSET
    num_market_pairs: int | Unset = UNSET
    target_date: str | Unset = UNSET
    last_update: str | Unset = UNSET
    price_usd: float | Unset = UNSET
    max_supply: float | Unset = UNSET
    volume_usd: float | Unset = UNSET
    available_supply: float | Unset = UNSET
    total_supply: float | Unset = UNSET
    market_cap: float | Unset = UNSET
    percentage_change_price_usd_1h: float | Unset = UNSET
    percentage_change_price_usd_24h: float | Unset = UNSET
    percentage_change_price_usd_7d: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        name = self.name

        slug = self.slug

        rank = self.rank

        id = self.id

        tag_names = self.tag_names

        tag_groups = self.tag_groups

        num_market_pairs = self.num_market_pairs

        target_date = self.target_date

        last_update = self.last_update

        price_usd = self.price_usd

        max_supply = self.max_supply

        volume_usd = self.volume_usd

        available_supply = self.available_supply

        total_supply = self.total_supply

        market_cap = self.market_cap

        percentage_change_price_usd_1h = self.percentage_change_price_usd_1h

        percentage_change_price_usd_24h = self.percentage_change_price_usd_24h

        percentage_change_price_usd_7d = self.percentage_change_price_usd_7d

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if rank is not UNSET:
            field_dict["rank"] = rank
        if id is not UNSET:
            field_dict["id"] = id
        if tag_names is not UNSET:
            field_dict["tag_names"] = tag_names
        if tag_groups is not UNSET:
            field_dict["tag_groups"] = tag_groups
        if num_market_pairs is not UNSET:
            field_dict["num_market_pairs"] = num_market_pairs
        if target_date is not UNSET:
            field_dict["target_date"] = target_date
        if last_update is not UNSET:
            field_dict["last_update"] = last_update
        if price_usd is not UNSET:
            field_dict["price_usd"] = price_usd
        if max_supply is not UNSET:
            field_dict["max_supply"] = max_supply
        if volume_usd is not UNSET:
            field_dict["volume_usd"] = volume_usd
        if available_supply is not UNSET:
            field_dict["available_supply"] = available_supply
        if total_supply is not UNSET:
            field_dict["total_supply"] = total_supply
        if market_cap is not UNSET:
            field_dict["market_cap"] = market_cap
        if percentage_change_price_usd_1h is not UNSET:
            field_dict["percentage_change_price_usd_1h"] = percentage_change_price_usd_1h
        if percentage_change_price_usd_24h is not UNSET:
            field_dict["percentage_change_price_usd_24h"] = percentage_change_price_usd_24h
        if percentage_change_price_usd_7d is not UNSET:
            field_dict["percentage_change_price_usd_7d"] = percentage_change_price_usd_7d

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        symbol = d.pop("symbol", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        rank = d.pop("rank", UNSET)

        id = d.pop("id", UNSET)

        tag_names = d.pop("tag_names", UNSET)

        tag_groups = d.pop("tag_groups", UNSET)

        num_market_pairs = d.pop("num_market_pairs", UNSET)

        target_date = d.pop("target_date", UNSET)

        last_update = d.pop("last_update", UNSET)

        price_usd = d.pop("price_usd", UNSET)

        max_supply = d.pop("max_supply", UNSET)

        volume_usd = d.pop("volume_usd", UNSET)

        available_supply = d.pop("available_supply", UNSET)

        total_supply = d.pop("total_supply", UNSET)

        market_cap = d.pop("market_cap", UNSET)

        percentage_change_price_usd_1h = d.pop("percentage_change_price_usd_1h", UNSET)

        percentage_change_price_usd_24h = d.pop("percentage_change_price_usd_24h", UNSET)

        percentage_change_price_usd_7d = d.pop("percentage_change_price_usd_7d", UNSET)

        crypto_snapshot_dto = cls(
            symbol=symbol,
            name=name,
            slug=slug,
            rank=rank,
            id=id,
            tag_names=tag_names,
            tag_groups=tag_groups,
            num_market_pairs=num_market_pairs,
            target_date=target_date,
            last_update=last_update,
            price_usd=price_usd,
            max_supply=max_supply,
            volume_usd=volume_usd,
            available_supply=available_supply,
            total_supply=total_supply,
            market_cap=market_cap,
            percentage_change_price_usd_1h=percentage_change_price_usd_1h,
            percentage_change_price_usd_24h=percentage_change_price_usd_24h,
            percentage_change_price_usd_7d=percentage_change_price_usd_7d,
        )

        crypto_snapshot_dto.additional_properties = d
        return crypto_snapshot_dto

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
