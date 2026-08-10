from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CryptocurrencyOHLCVHistoricalQuoteObject")


@_attrs_define
class CryptocurrencyOHLCVHistoricalQuoteObject:
    """A market quote in each currency conversion option.

    Attributes:
        open_ (float): Opening price for time series interval. Example: 3849.21640853.
        high (float): Highest price during this time series interval. Example: 3947.9812729.
        low (float): Lowest price during this time series interval. Example: 3817.40949569.
        close (float): Closing price for this time series interval. Example: 3943.40933686.
        volume (float): Adjusted volume for this time series interval. Volume is not currently supported for hourly
            OHLCV intervals before 2020-09-22. Example: 5244856835.70851.
        market_cap (float): Market cap by circulating supply for this time series interval. Example: 68849856731.6738.
        timestamp (str): Timestamp (ISO 8601) of when the conversion currency's current value was referenced for this
            conversion. Example: 2019-01-02T23:59:59.999Z.
    """

    open_: float
    high: float
    low: float
    close: float
    volume: float
    market_cap: float
    timestamp: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_ = self.open_

        high = self.high

        low = self.low

        close = self.close

        volume = self.volume

        market_cap = self.market_cap

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "open": open_,
                "high": high,
                "low": low,
                "close": close,
                "volume": volume,
                "market_cap": market_cap,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        open_ = d.pop("open")

        high = d.pop("high")

        low = d.pop("low")

        close = d.pop("close")

        volume = d.pop("volume")

        market_cap = d.pop("market_cap")

        timestamp = d.pop("timestamp")

        cryptocurrency_ohlcv_historical_quote_object = cls(
            open_=open_,
            high=high,
            low=low,
            close=close,
            volume=volume,
            market_cap=market_cap,
            timestamp=timestamp,
        )

        cryptocurrency_ohlcv_historical_quote_object.additional_properties = d
        return cryptocurrency_ohlcv_historical_quote_object

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
