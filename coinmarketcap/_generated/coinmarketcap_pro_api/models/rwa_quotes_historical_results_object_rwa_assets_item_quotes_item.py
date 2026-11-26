from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RWAQuotesHistoricalResultsObjectRwaAssetsItemQuotesItem")


@_attrs_define
class RWAQuotesHistoricalResultsObjectRwaAssetsItemQuotesItem:
    """
    Attributes:
        timestamp (datetime.datetime | Unset): Start of the interval period the data point belongs to (ISO 8601, UTC).
            Example: 2026-11-17T05:00:00.000Z.
        convert_id (int | Unset): CoinMarketCap ID of the convert currency (`2781` for USD). Example: 2781.
        convert_symbol (str | Unset): Symbol of the convert currency. Example: USD.
        average_tokenized_price (float | Unset): Aggregate price across the underlying tokens, in the convert currency.
            Example: 157.86910203115895.
        tokenized_market_cap (float | Unset): Aggregate tokenized market cap, in the convert currency. Example:
            362817204.1754513.
        tokenized_volume_24h (float | Unset): Aggregate trailing 24h tokenized volume, in the convert currency. Example:
            321224540.9867724.
    """

    timestamp: datetime.datetime | Unset = UNSET
    convert_id: int | Unset = UNSET
    convert_symbol: str | Unset = UNSET
    average_tokenized_price: float | Unset = UNSET
    tokenized_market_cap: float | Unset = UNSET
    tokenized_volume_24h: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        convert_id = self.convert_id

        convert_symbol = self.convert_symbol

        average_tokenized_price = self.average_tokenized_price

        tokenized_market_cap = self.tokenized_market_cap

        tokenized_volume_24h = self.tokenized_volume_24h

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if convert_id is not UNSET:
            field_dict["convert_id"] = convert_id
        if convert_symbol is not UNSET:
            field_dict["convert_symbol"] = convert_symbol
        if average_tokenized_price is not UNSET:
            field_dict["average_tokenized_price"] = average_tokenized_price
        if tokenized_market_cap is not UNSET:
            field_dict["tokenized_market_cap"] = tokenized_market_cap
        if tokenized_volume_24h is not UNSET:
            field_dict["tokenized_volume_24h"] = tokenized_volume_24h

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        convert_id = d.pop("convert_id", UNSET)

        convert_symbol = d.pop("convert_symbol", UNSET)

        average_tokenized_price = d.pop("average_tokenized_price", UNSET)

        tokenized_market_cap = d.pop("tokenized_market_cap", UNSET)

        tokenized_volume_24h = d.pop("tokenized_volume_24h", UNSET)

        rwa_quotes_historical_results_object_rwa_assets_item_quotes_item = cls(
            timestamp=timestamp,
            convert_id=convert_id,
            convert_symbol=convert_symbol,
            average_tokenized_price=average_tokenized_price,
            tokenized_market_cap=tokenized_market_cap,
            tokenized_volume_24h=tokenized_volume_24h,
        )

        rwa_quotes_historical_results_object_rwa_assets_item_quotes_item.additional_properties = d
        return rwa_quotes_historical_results_object_rwa_assets_item_quotes_item

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
