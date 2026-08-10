from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptoOhlcvQuoteDTO")


@_attrs_define
class CryptoOhlcvQuoteDTO:
    """
    Attributes:
        open_ (float | Unset): Open price
        high (float | Unset): High price
        low (float | Unset): Low price
        close (float | Unset): Close price
        volume (float | Unset): Volume
        score (int | Unset): Score
        market_cap (float | Unset): Market capitalization
        time_high (str | Unset): Time of high price
        time_low (str | Unset): Time of low price
        time_open (str | Unset): Time of open price
        time_close (str | Unset): Time of close price
    """

    open_: float | Unset = UNSET
    high: float | Unset = UNSET
    low: float | Unset = UNSET
    close: float | Unset = UNSET
    volume: float | Unset = UNSET
    score: int | Unset = UNSET
    market_cap: float | Unset = UNSET
    time_high: str | Unset = UNSET
    time_low: str | Unset = UNSET
    time_open: str | Unset = UNSET
    time_close: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_ = self.open_

        high = self.high

        low = self.low

        close = self.close

        volume = self.volume

        score = self.score

        market_cap = self.market_cap

        time_high = self.time_high

        time_low = self.time_low

        time_open = self.time_open

        time_close = self.time_close

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
        if score is not UNSET:
            field_dict["score"] = score
        if market_cap is not UNSET:
            field_dict["market_cap"] = market_cap
        if time_high is not UNSET:
            field_dict["time_high"] = time_high
        if time_low is not UNSET:
            field_dict["time_low"] = time_low
        if time_open is not UNSET:
            field_dict["time_open"] = time_open
        if time_close is not UNSET:
            field_dict["time_close"] = time_close

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        open_ = d.pop("open", UNSET)

        high = d.pop("high", UNSET)

        low = d.pop("low", UNSET)

        close = d.pop("close", UNSET)

        volume = d.pop("volume", UNSET)

        score = d.pop("score", UNSET)

        market_cap = d.pop("market_cap", UNSET)

        time_high = d.pop("time_high", UNSET)

        time_low = d.pop("time_low", UNSET)

        time_open = d.pop("time_open", UNSET)

        time_close = d.pop("time_close", UNSET)

        crypto_ohlcv_quote_dto = cls(
            open_=open_,
            high=high,
            low=low,
            close=close,
            volume=volume,
            score=score,
            market_cap=market_cap,
            time_high=time_high,
            time_low=time_low,
            time_open=time_open,
            time_close=time_close,
        )

        crypto_ohlcv_quote_dto.additional_properties = d
        return crypto_ohlcv_quote_dto

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
