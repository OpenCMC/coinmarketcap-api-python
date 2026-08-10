from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RWAAssetListResultsObjectRwaAssetsItemQuotesItem")


@_attrs_define
class RWAAssetListResultsObjectRwaAssetsItemQuotesItem:
    """
    Attributes:
        crypto_id (int | Unset): CoinMarketCap ID of the quote currency. Example: 2781.
        symbol (str | Unset): Symbol of the quote currency. Example: USD.
        average_tokenized_price (float | Unset): Aggregate tokenized price in the converted currency.
        tokenized_market_cap (float | Unset): Aggregate tokenized market cap in the converted currency.
        tokenized_volume_24h (float | Unset): Aggregate 24h tokenized volume in the converted currency.
        last_updated (datetime.datetime | Unset): ISO 8601 timestamp of the quote.
    """

    crypto_id: int | Unset = UNSET
    symbol: str | Unset = UNSET
    average_tokenized_price: float | Unset = UNSET
    tokenized_market_cap: float | Unset = UNSET
    tokenized_volume_24h: float | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crypto_id = self.crypto_id

        symbol = self.symbol

        average_tokenized_price = self.average_tokenized_price

        tokenized_market_cap = self.tokenized_market_cap

        tokenized_volume_24h = self.tokenized_volume_24h

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
        if average_tokenized_price is not UNSET:
            field_dict["average_tokenized_price"] = average_tokenized_price
        if tokenized_market_cap is not UNSET:
            field_dict["tokenized_market_cap"] = tokenized_market_cap
        if tokenized_volume_24h is not UNSET:
            field_dict["tokenized_volume_24h"] = tokenized_volume_24h
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        crypto_id = d.pop("crypto_id", UNSET)

        symbol = d.pop("symbol", UNSET)

        average_tokenized_price = d.pop("average_tokenized_price", UNSET)

        tokenized_market_cap = d.pop("tokenized_market_cap", UNSET)

        tokenized_volume_24h = d.pop("tokenized_volume_24h", UNSET)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        rwa_asset_list_results_object_rwa_assets_item_quotes_item = cls(
            crypto_id=crypto_id,
            symbol=symbol,
            average_tokenized_price=average_tokenized_price,
            tokenized_market_cap=tokenized_market_cap,
            tokenized_volume_24h=tokenized_volume_24h,
            last_updated=last_updated,
        )

        rwa_asset_list_results_object_rwa_assets_item_quotes_item.additional_properties = d
        return rwa_asset_list_results_object_rwa_assets_item_quotes_item

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
