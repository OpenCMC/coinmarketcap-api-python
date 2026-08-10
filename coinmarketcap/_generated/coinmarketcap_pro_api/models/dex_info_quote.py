from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DexInfoQuote")


@_attrs_define
class DexInfoQuote:
    """DEX exchange quote information

    Attributes:
        convert_id (str | Unset): id of specified currency.
        market_type (str | Unset): Type of market data being returned, such as Spot, Perpetual, and Futures.
        last_updated (datetime.datetime | Unset): Timestamp (ISO 8601) of when the conversion currency's current value
            was referenced for this conversion.
        volume_24h (float | Unset): Reported 24 hour volume in the specified currency.
        percent_change_volume_24h (float | Unset): 24 hour volume change percentage in the specified currency. Only
            applicable for fiat conversions.
        num_transactions_24h (float | Unset): Total number of transactions in the past 24 hours. This field will return
            null if not available.
    """

    convert_id: str | Unset = UNSET
    market_type: str | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    volume_24h: float | Unset = UNSET
    percent_change_volume_24h: float | Unset = UNSET
    num_transactions_24h: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        convert_id = self.convert_id

        market_type = self.market_type

        last_updated: str | Unset = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        volume_24h = self.volume_24h

        percent_change_volume_24h = self.percent_change_volume_24h

        num_transactions_24h = self.num_transactions_24h

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if convert_id is not UNSET:
            field_dict["convert_id"] = convert_id
        if market_type is not UNSET:
            field_dict["market_type"] = market_type
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if volume_24h is not UNSET:
            field_dict["volume_24h"] = volume_24h
        if percent_change_volume_24h is not UNSET:
            field_dict["percent_change_volume_24h"] = percent_change_volume_24h
        if num_transactions_24h is not UNSET:
            field_dict["num_transactions_24h"] = num_transactions_24h

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        convert_id = d.pop("convert_id", UNSET)

        market_type = d.pop("market_type", UNSET)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        volume_24h = d.pop("volume_24h", UNSET)

        percent_change_volume_24h = d.pop("percent_change_volume_24h", UNSET)

        num_transactions_24h = d.pop("num_transactions_24h", UNSET)

        dex_info_quote = cls(
            convert_id=convert_id,
            market_type=market_type,
            last_updated=last_updated,
            volume_24h=volume_24h,
            percent_change_volume_24h=percent_change_volume_24h,
            num_transactions_24h=num_transactions_24h,
        )

        dex_info_quote.additional_properties = d
        return dex_info_quote

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
