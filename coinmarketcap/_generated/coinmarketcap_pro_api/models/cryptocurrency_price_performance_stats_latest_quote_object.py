from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CryptocurrencyPricePerformanceStatsLatestQuoteObject")


@_attrs_define
class CryptocurrencyPricePerformanceStatsLatestQuoteObject:
    """A time period quote in the currency conversion option.

    Attributes:
        open_ (float): Cryptocurrency price at the start of the requested time period historically converted into units
            of the convert currency. Example: 135.3000030517578.
        open_timestamp (str): Timestamp (ISO 8601) of the closest convert currency reference price used during `open`
            price conversion. Example: 2013-04-28T00:00:00.000Z.
        high (float): Highest USD price achieved within the requested time period historically converted into units of
            the convert currency. Example: 20088.99609375.
        high_timestamp (str): Timestamp (ISO 8601) of the closest convert currency reference price used during `high`
            price conversion. *For `yesterday` UTC close will be used.* Example: 2017-12-17T12:19:14.000Z.
        low (float): Lowest USD price achieved within the requested time period historically converted into units of the
            convert currency. Example: 65.5260009765625.
        low_timestamp (str): Timestamp (ISO 8601) of the closest convert currency reference price used during `low`
            price conversion. *For `yesterday` UTC close will be used.* Example: 2013-07-05T18:56:01.000Z.
        close (float): Cryptocurrency price at the end of the requested time period historically converted into units of
            the convert currency. Example: 9908.99193585.
        close_timestamp (str): Timestamp (ISO 8601) of the closest convert currency reference price used during `close`
            price conversion. Example: 2019-08-22T01:52:18.618Z.
        percent_change (float): The approximate percentage change (ROI) if purchased at the start of the time period.
            This is the time of launch or earliest known price for the `all_time` period. This value includes historical
            change in market rate for the specified convert currency. Example: 7223.718930042746.
        price_change (float): The actual price change between the start of the time period and end. This is the time of
            launch or earliest known price for the `all_time` period. This value includes historical change in market rate
            for the specified convert currency. Example: 9773.691932798241.
    """

    open_: float
    open_timestamp: str
    high: float
    high_timestamp: str
    low: float
    low_timestamp: str
    close: float
    close_timestamp: str
    percent_change: float
    price_change: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_ = self.open_

        open_timestamp = self.open_timestamp

        high = self.high

        high_timestamp = self.high_timestamp

        low = self.low

        low_timestamp = self.low_timestamp

        close = self.close

        close_timestamp = self.close_timestamp

        percent_change = self.percent_change

        price_change = self.price_change

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "open": open_,
                "open_timestamp": open_timestamp,
                "high": high,
                "high_timestamp": high_timestamp,
                "low": low,
                "low_timestamp": low_timestamp,
                "close": close,
                "close_timestamp": close_timestamp,
                "percent_change": percent_change,
                "price_change": price_change,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        open_ = d.pop("open")

        open_timestamp = d.pop("open_timestamp")

        high = d.pop("high")

        high_timestamp = d.pop("high_timestamp")

        low = d.pop("low")

        low_timestamp = d.pop("low_timestamp")

        close = d.pop("close")

        close_timestamp = d.pop("close_timestamp")

        percent_change = d.pop("percent_change")

        price_change = d.pop("price_change")

        cryptocurrency_price_performance_stats_latest_quote_object = cls(
            open_=open_,
            open_timestamp=open_timestamp,
            high=high,
            high_timestamp=high_timestamp,
            low=low,
            low_timestamp=low_timestamp,
            close=close,
            close_timestamp=close_timestamp,
            percent_change=percent_change,
            price_change=price_change,
        )

        cryptocurrency_price_performance_stats_latest_quote_object.additional_properties = d
        return cryptocurrency_price_performance_stats_latest_quote_object

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
