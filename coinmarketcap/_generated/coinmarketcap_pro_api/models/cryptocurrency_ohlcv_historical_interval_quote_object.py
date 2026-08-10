from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cryptocurrency_ohlcv_historical_quote_map import CryptocurrencyOHLCVHistoricalQuoteMap


T = TypeVar("T", bound="CryptocurrencyOHLCVHistoricalIntervalQuoteObject")


@_attrs_define
class CryptocurrencyOHLCVHistoricalIntervalQuoteObject:
    """An OHLCV quote for the supplied interval.

    Attributes:
        time_open (str): Timestamp (ISO 8601) of the start of this time series interval. Example:
            2018-06-02T00:00:00.000Z.
        time_close (str): Timestamp (ISO 8601) of the end of this time series interval. Example:
            2018-06-02T23:59:59.999Z.
        time_high (str): Timestamp (ISO 8601) of the high of this time series interval. Example:
            2018-06-02T22:59:59.999Z.
        time_low (str): Timestamp (ISO 8601) of the low of this time series interval. Example: 2018-06-02T21:59:59.999Z.
        quote (CryptocurrencyOHLCVHistoricalQuoteMap): A map of market quotes in different currency conversions. The
            default map included is USD.
    """

    time_open: str
    time_close: str
    time_high: str
    time_low: str
    quote: CryptocurrencyOHLCVHistoricalQuoteMap
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_open = self.time_open

        time_close = self.time_close

        time_high = self.time_high

        time_low = self.time_low

        quote = self.quote.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time_open": time_open,
                "time_close": time_close,
                "time_high": time_high,
                "time_low": time_low,
                "quote": quote,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_ohlcv_historical_quote_map import CryptocurrencyOHLCVHistoricalQuoteMap

        d = dict(src_dict)
        time_open = d.pop("time_open")

        time_close = d.pop("time_close")

        time_high = d.pop("time_high")

        time_low = d.pop("time_low")

        quote = CryptocurrencyOHLCVHistoricalQuoteMap.from_dict(d.pop("quote"))

        cryptocurrency_ohlcv_historical_interval_quote_object = cls(
            time_open=time_open,
            time_close=time_close,
            time_high=time_high,
            time_low=time_low,
            quote=quote,
        )

        cryptocurrency_ohlcv_historical_interval_quote_object.additional_properties = d
        return cryptocurrency_ohlcv_historical_interval_quote_object

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
