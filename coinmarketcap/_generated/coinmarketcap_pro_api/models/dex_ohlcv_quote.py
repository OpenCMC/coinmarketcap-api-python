from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DexOhlcvQuote")


@_attrs_define
class DexOhlcvQuote:
    """DEX OHLCV (Open, High, Low, Close, Volume) quote data

    Attributes:
        open_ (float | Unset): Price from first datapoint of today in UTC time for the convert option requested.
        high (float | Unset): Highest price so far today in UTC time for the convert option requested.
        low (float | Unset): Lowest price today in UTC time for the convert option requested.
        close (float | Unset): Latest price today in UTC time for the convert option requested. This is not the final
            price during close as the current day period is not over.
        volume (float | Unset): Adjusted volume for this time series interval.
        convert_id (str | Unset): id of specified currency.
        last_updated (str | Unset): Timestamp (ISO 8601) of when the conversion currency's current value was referenced
            for this conversion.
        field_24h_buy_volume (float | Unset): 24 hours buy volume of the asset
        field_24h_sell_volume (float | Unset): 24 hours sell volume of the asset
    """

    open_: float | Unset = UNSET
    high: float | Unset = UNSET
    low: float | Unset = UNSET
    close: float | Unset = UNSET
    volume: float | Unset = UNSET
    convert_id: str | Unset = UNSET
    last_updated: str | Unset = UNSET
    field_24h_buy_volume: float | Unset = UNSET
    field_24h_sell_volume: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_ = self.open_

        high = self.high

        low = self.low

        close = self.close

        volume = self.volume

        convert_id = self.convert_id

        last_updated = self.last_updated

        field_24h_buy_volume = self.field_24h_buy_volume

        field_24h_sell_volume = self.field_24h_sell_volume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if open_ is not UNSET:
            field_dict["open"] = open_
        if high is not UNSET:
            field_dict["high"] = high
        if low is not UNSET:
            field_dict["low"] = low
        if close is not UNSET:
            field_dict["close"] = close
        if volume is not UNSET:
            field_dict["volume"] = volume
        if convert_id is not UNSET:
            field_dict["convert_id"] = convert_id
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if field_24h_buy_volume is not UNSET:
            field_dict["24h_buy_volume"] = field_24h_buy_volume
        if field_24h_sell_volume is not UNSET:
            field_dict["24h_sell_volume"] = field_24h_sell_volume

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        open_ = d.pop("open", UNSET)

        high = d.pop("high", UNSET)

        low = d.pop("low", UNSET)

        close = d.pop("close", UNSET)

        volume = d.pop("volume", UNSET)

        convert_id = d.pop("convert_id", UNSET)

        last_updated = d.pop("last_updated", UNSET)

        field_24h_buy_volume = d.pop("24h_buy_volume", UNSET)

        field_24h_sell_volume = d.pop("24h_sell_volume", UNSET)

        dex_ohlcv_quote = cls(
            open_=open_,
            high=high,
            low=low,
            close=close,
            volume=volume,
            convert_id=convert_id,
            last_updated=last_updated,
            field_24h_buy_volume=field_24h_buy_volume,
            field_24h_sell_volume=field_24h_sell_volume,
        )

        dex_ohlcv_quote.additional_properties = d
        return dex_ohlcv_quote

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
