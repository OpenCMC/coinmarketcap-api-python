from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cryptocurrency_price_performance_stats_latest_quote_map import (
        CryptocurrencyPricePerformanceStatsLatestQuoteMap,
    )


T = TypeVar("T", bound="CryptocurrencyPricePerformanceStatsLatestPeriodObject")


@_attrs_define
class CryptocurrencyPricePerformanceStatsLatestPeriodObject:
    """A time period data object. `all_time` is the default.

    Attributes:
        open_timestamp (str): Timestamp (ISO 8601) of the start of this time period. Please note that this is a rolling
            period back from current time for time periods outside of `yesterday`. Example: 2013-04-28T00:00:00.000Z.
        high_timestamp (str): Timestamp (ISO 8601) of when this cryptocurrency achieved it's highest USD price during
            the requested time period. *Note: The `yesterday` period currently doesn't support this field and will return
            `null`.* Example: 2017-12-17T12:19:14.000Z.
        low_timestamp (str): Timestamp (ISO 8601) of when this cryptocurrency achieved it's lowest USD price during the
            requested time period. *Note: The `yesterday` period currently doesn't support this field and will return
            `null`.* Example: 2013-07-05T18:56:01.000Z.
        close_timestamp (str): Timestamp (ISO 8601) of the end of this time period. Please note that this is a rolling
            period back from current time for time periods outside of `yesterday`. Example: 2019-08-22T01:52:18.613Z.
        quote (CryptocurrencyPricePerformanceStatsLatestQuoteMap): An object map of time period quotes for each convert
            option requested. The default map included is USD.
    """

    open_timestamp: str
    high_timestamp: str
    low_timestamp: str
    close_timestamp: str
    quote: CryptocurrencyPricePerformanceStatsLatestQuoteMap
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_timestamp = self.open_timestamp

        high_timestamp = self.high_timestamp

        low_timestamp = self.low_timestamp

        close_timestamp = self.close_timestamp

        quote = self.quote.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "open_timestamp": open_timestamp,
                "high_timestamp": high_timestamp,
                "low_timestamp": low_timestamp,
                "close_timestamp": close_timestamp,
                "quote": quote,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_price_performance_stats_latest_quote_map import (
            CryptocurrencyPricePerformanceStatsLatestQuoteMap,
        )

        d = dict(src_dict)
        open_timestamp = d.pop("open_timestamp")

        high_timestamp = d.pop("high_timestamp")

        low_timestamp = d.pop("low_timestamp")

        close_timestamp = d.pop("close_timestamp")

        quote = CryptocurrencyPricePerformanceStatsLatestQuoteMap.from_dict(d.pop("quote"))

        cryptocurrency_price_performance_stats_latest_period_object = cls(
            open_timestamp=open_timestamp,
            high_timestamp=high_timestamp,
            low_timestamp=low_timestamp,
            close_timestamp=close_timestamp,
            quote=quote,
        )

        cryptocurrency_price_performance_stats_latest_period_object.additional_properties = d
        return cryptocurrency_price_performance_stats_latest_period_object

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
