from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LiquidationsByExchangeResultsObjectExchangesItemQuotesItem")


@_attrs_define
class LiquidationsByExchangeResultsObjectExchangesItemQuotesItem:
    """
    Attributes:
        crypto_id (int | Unset): CoinMarketCap ID of the convert currency (e.g. `2781` for USD). Always present.
            Example: 2781.
        symbol (str | Unset): Symbol of the convert currency (e.g. `USD`). Always present. Example: USD.
        total_liquidations_1h (float | Unset): Total notional liquidated in the rolling 1h window, in the convert
            currency.
        long_liquidations_1h (float | Unset): Longs liquidated (forced sells) in the rolling 1h window.
        short_liquidations_1h (float | Unset): Shorts liquidated (forced buys) in the rolling 1h window.
        total_liquidations_4h (float | Unset): Total notional liquidated in the rolling 4h window.
        long_liquidations_4h (float | Unset): Longs liquidated (forced sells) in the rolling 4h window.
        short_liquidations_4h (float | Unset): Shorts liquidated (forced buys) in the rolling 4h window.
        total_liquidations_24h (float | Unset): Total notional liquidated in the rolling 24h window.
        long_liquidations_24h (float | Unset): Longs liquidated (forced sells) in the rolling 24h window.
        short_liquidations_24h (float | Unset): Shorts liquidated (forced buys) in the rolling 24h window.
        last_updated (datetime.datetime | Unset): ISO 8601 timestamp of the last aggregation for this quote.
    """

    crypto_id: int | Unset = UNSET
    symbol: str | Unset = UNSET
    total_liquidations_1h: float | Unset = UNSET
    long_liquidations_1h: float | Unset = UNSET
    short_liquidations_1h: float | Unset = UNSET
    total_liquidations_4h: float | Unset = UNSET
    long_liquidations_4h: float | Unset = UNSET
    short_liquidations_4h: float | Unset = UNSET
    total_liquidations_24h: float | Unset = UNSET
    long_liquidations_24h: float | Unset = UNSET
    short_liquidations_24h: float | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crypto_id = self.crypto_id

        symbol = self.symbol

        total_liquidations_1h = self.total_liquidations_1h

        long_liquidations_1h = self.long_liquidations_1h

        short_liquidations_1h = self.short_liquidations_1h

        total_liquidations_4h = self.total_liquidations_4h

        long_liquidations_4h = self.long_liquidations_4h

        short_liquidations_4h = self.short_liquidations_4h

        total_liquidations_24h = self.total_liquidations_24h

        long_liquidations_24h = self.long_liquidations_24h

        short_liquidations_24h = self.short_liquidations_24h

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
        if total_liquidations_1h is not UNSET:
            field_dict["total_liquidations_1h"] = total_liquidations_1h
        if long_liquidations_1h is not UNSET:
            field_dict["long_liquidations_1h"] = long_liquidations_1h
        if short_liquidations_1h is not UNSET:
            field_dict["short_liquidations_1h"] = short_liquidations_1h
        if total_liquidations_4h is not UNSET:
            field_dict["total_liquidations_4h"] = total_liquidations_4h
        if long_liquidations_4h is not UNSET:
            field_dict["long_liquidations_4h"] = long_liquidations_4h
        if short_liquidations_4h is not UNSET:
            field_dict["short_liquidations_4h"] = short_liquidations_4h
        if total_liquidations_24h is not UNSET:
            field_dict["total_liquidations_24h"] = total_liquidations_24h
        if long_liquidations_24h is not UNSET:
            field_dict["long_liquidations_24h"] = long_liquidations_24h
        if short_liquidations_24h is not UNSET:
            field_dict["short_liquidations_24h"] = short_liquidations_24h
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        crypto_id = d.pop("crypto_id", UNSET)

        symbol = d.pop("symbol", UNSET)

        total_liquidations_1h = d.pop("total_liquidations_1h", UNSET)

        long_liquidations_1h = d.pop("long_liquidations_1h", UNSET)

        short_liquidations_1h = d.pop("short_liquidations_1h", UNSET)

        total_liquidations_4h = d.pop("total_liquidations_4h", UNSET)

        long_liquidations_4h = d.pop("long_liquidations_4h", UNSET)

        short_liquidations_4h = d.pop("short_liquidations_4h", UNSET)

        total_liquidations_24h = d.pop("total_liquidations_24h", UNSET)

        long_liquidations_24h = d.pop("long_liquidations_24h", UNSET)

        short_liquidations_24h = d.pop("short_liquidations_24h", UNSET)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        liquidations_by_exchange_results_object_exchanges_item_quotes_item = cls(
            crypto_id=crypto_id,
            symbol=symbol,
            total_liquidations_1h=total_liquidations_1h,
            long_liquidations_1h=long_liquidations_1h,
            short_liquidations_1h=short_liquidations_1h,
            total_liquidations_4h=total_liquidations_4h,
            long_liquidations_4h=long_liquidations_4h,
            short_liquidations_4h=short_liquidations_4h,
            total_liquidations_24h=total_liquidations_24h,
            long_liquidations_24h=long_liquidations_24h,
            short_liquidations_24h=short_liquidations_24h,
            last_updated=last_updated,
        )

        liquidations_by_exchange_results_object_exchanges_item_quotes_item.additional_properties = d
        return liquidations_by_exchange_results_object_exchanges_item_quotes_item

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
