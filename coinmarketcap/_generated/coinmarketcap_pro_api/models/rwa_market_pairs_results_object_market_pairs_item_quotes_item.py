from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RWAMarketPairsResultsObjectMarketPairsItemQuotesItem")


@_attrs_define
class RWAMarketPairsResultsObjectMarketPairsItemQuotesItem:
    """
    Attributes:
        crypto_id (int | Unset): CoinMarketCap ID of the quote currency. Example: 2781.
        symbol (str | Unset): Symbol of the quote currency. Example: USD.
        price (float | Unset): Converted price.
        volume_24h (float | Unset): Converted 24h volume.
        last_updated (datetime.datetime | Unset): ISO 8601 timestamp.
    """

    crypto_id: int | Unset = UNSET
    symbol: str | Unset = UNSET
    price: float | Unset = UNSET
    volume_24h: float | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crypto_id = self.crypto_id

        symbol = self.symbol

        price = self.price

        volume_24h = self.volume_24h

        last_updated: str | Unset = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crypto_id is not UNSET:
            field_dict["crypto_id"] = crypto_id
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if price is not UNSET:
            field_dict["price"] = price
        if volume_24h is not UNSET:
            field_dict["volume_24h"] = volume_24h
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        crypto_id = d.pop("crypto_id", UNSET)

        symbol = d.pop("symbol", UNSET)

        price = d.pop("price", UNSET)

        volume_24h = d.pop("volume_24h", UNSET)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        rwa_market_pairs_results_object_market_pairs_item_quotes_item = cls(
            crypto_id=crypto_id,
            symbol=symbol,
            price=price,
            volume_24h=volume_24h,
            last_updated=last_updated,
        )

        rwa_market_pairs_results_object_market_pairs_item_quotes_item.additional_properties = d
        return rwa_market_pairs_results_object_market_pairs_item_quotes_item

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
