from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dex_ohlcv_quote import DexOhlcvQuote


T = TypeVar("T", bound="DexPairsOhlcvHistoricalQuotes")


@_attrs_define
class DexPairsOhlcvHistoricalQuotes:
    """Historical OHLCV quotes data

    Attributes:
        quote (list[DexOhlcvQuote] | Unset): A map of market quotes in different currency conversions. The default map
            included is USD.
        time_open (datetime.datetime | Unset): Timestamp (ISO 8601) of the start of this OHLCV period.
        time_close (datetime.datetime | Unset): Timestamp (ISO 8601) of the end of this OHLCV period. Always null as the
            current day is incomplete. See last_updated for the last UTC time included in the current OHLCV calculation.
    """

    quote: list[DexOhlcvQuote] | Unset = UNSET
    time_open: datetime.datetime | Unset = UNSET
    time_close: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quote: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quote, Unset):
            quote = []
            for quote_item_data in self.quote:
                quote_item = quote_item_data.to_dict()
                quote.append(quote_item)

        time_open: str | Unset = UNSET
        if not isinstance(self.time_open, Unset):
            time_open = self.time_open.isoformat()

        time_close: str | Unset = UNSET
        if not isinstance(self.time_close, Unset):
            time_close = self.time_close.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quote is not UNSET:
            field_dict["quote"] = quote
        if time_open is not UNSET:
            field_dict["time_open"] = time_open
        if time_close is not UNSET:
            field_dict["time_close"] = time_close

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dex_ohlcv_quote import DexOhlcvQuote

        d = dict(src_dict)
        _quote = d.pop("quote", UNSET)
        quote: list[DexOhlcvQuote] | Unset = UNSET
        if _quote is not UNSET:
            quote = []
            for quote_item_data in _quote:
                quote_item = DexOhlcvQuote.from_dict(quote_item_data)

                quote.append(quote_item)

        _time_open = d.pop("time_open", UNSET)
        time_open: datetime.datetime | Unset
        if isinstance(_time_open, Unset):
            time_open = UNSET
        else:
            time_open = isoparse(_time_open)

        _time_close = d.pop("time_close", UNSET)
        time_close: datetime.datetime | Unset
        if isinstance(_time_close, Unset):
            time_close = UNSET
        else:
            time_close = isoparse(_time_close)

        dex_pairs_ohlcv_historical_quotes = cls(
            quote=quote,
            time_open=time_open,
            time_close=time_close,
        )

        dex_pairs_ohlcv_historical_quotes.additional_properties = d
        return dex_pairs_ohlcv_historical_quotes

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
