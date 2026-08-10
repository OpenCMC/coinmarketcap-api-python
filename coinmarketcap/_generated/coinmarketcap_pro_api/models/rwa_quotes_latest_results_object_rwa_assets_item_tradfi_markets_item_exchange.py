from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RWAQuotesLatestResultsObjectRwaAssetsItemTradfiMarketsItemExchange")


@_attrs_define
class RWAQuotesLatestResultsObjectRwaAssetsItemTradfiMarketsItemExchange:
    """Exchange listing the market.

    Attributes:
        exchange_id (int | Unset): CoinMarketCap exchange ID. Example: 270.
        name (str | Unset): Exchange name. Example: Binance.
        slug (str | Unset): Exchange slug. Example: binance.
    """

    exchange_id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange_id = self.exchange_id

        name = self.name

        slug = self.slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exchange_id is not UNSET:
            field_dict["exchange_id"] = exchange_id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exchange_id = d.pop("exchange_id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        rwa_quotes_latest_results_object_rwa_assets_item_tradfi_markets_item_exchange = cls(
            exchange_id=exchange_id,
            name=name,
            slug=slug,
        )

        rwa_quotes_latest_results_object_rwa_assets_item_tradfi_markets_item_exchange.additional_properties = d
        return rwa_quotes_latest_results_object_rwa_assets_item_tradfi_markets_item_exchange

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
