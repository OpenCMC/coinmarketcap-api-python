from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CryptocurrencyOHLCVLatestQuoteObject")


@_attrs_define
class CryptocurrencyOHLCVLatestQuoteObject:
    """A market quote in each currency conversion option.

    Attributes:
        open_ (float): Price from first datapoint of today in UTC time for the convert option requested. Example:
            966.34.
        high (float): Highest price so far today in UTC time for the convert option requested. Example: 1005.
        low (float): Lowest price today in UTC time for the convert option requested. Example: 960.53.
        close (float): Latest price today in UTC time for the convert option requested. This is not the final price
            during close as the current day period is not over. Example: 997.75.
        volume (float): Aggregate 24 hour adjusted volume for the convert option requested. Please note, this is a
            rolling 24 hours back from the current time. Example: 6850.59330859.
        last_updated (str): Timestamp (ISO 8601) of when the conversion currency's current value was last updated when
            referenced for this conversion. Example: 2018-06-02T00:00:00.000Z.
    """

    open_: float
    high: float
    low: float
    close: float
    volume: float
    last_updated: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_ = self.open_

        high = self.high

        low = self.low

        close = self.close

        volume = self.volume

        last_updated = self.last_updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "open": open_,
                "high": high,
                "low": low,
                "close": close,
                "volume": volume,
                "last_updated": last_updated,
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

        last_updated = d.pop("last_updated")

        cryptocurrency_ohlcv_latest_quote_object = cls(
            open_=open_,
            high=high,
            low=low,
            close=close,
            volume=volume,
            last_updated=last_updated,
        )

        cryptocurrency_ohlcv_latest_quote_object.additional_properties = d
        return cryptocurrency_ohlcv_latest_quote_object

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
