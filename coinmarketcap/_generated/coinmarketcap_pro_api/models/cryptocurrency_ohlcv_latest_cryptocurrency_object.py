from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cryptocurrency_ohlcv_latest_quote_map import CryptocurrencyOHLCVLatestQuoteMap


T = TypeVar("T", bound="CryptocurrencyOHLCVLatestCryptocurrencyObject")


@_attrs_define
class CryptocurrencyOHLCVLatestCryptocurrencyObject:
    """A cryptocurrency object for each requested.

    Attributes:
        id (int): The unique CoinMarketCap ID for this cryptocurrency. Example: 1.
        name (str): The name of this cryptocurrency. Example: Bitcoin.
        symbol (str): The ticker symbol for this cryptocurrency. Example: BTC.
        last_updated (str): Timestamp (ISO 8601) of the lastest market value record included to generate the latest
            active day OHLCV values. Example: 2018-06-02T23:59:59.999Z.
        time_open (str): Timestamp (ISO 8601) of the start of this OHLCV period. Example: 2018-06-02T00:00:00.000Z.
        time_high (str): Timestamp (ISO 8601) of the high of this OHLCV period. Example: 2018-06-02T00:00:00.000Z.
        time_low (str): Timestamp (ISO 8601) of the low of this OHLCV period. Example: 2018-06-02T00:00:00.000Z.
        time_close (str): Timestamp (ISO 8601) of the end of this OHLCV period. Always `null` as the current day is
            incomplete. See `last_updated` for the last UTC time included in the current OHLCV calculation. Example: null.
        quote (CryptocurrencyOHLCVLatestQuoteMap): A map of market quotes in different currency conversions. The default
            map included is USD.
    """

    id: int
    name: str
    symbol: str
    last_updated: str
    time_open: str
    time_high: str
    time_low: str
    time_close: str
    quote: CryptocurrencyOHLCVLatestQuoteMap
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        symbol = self.symbol

        last_updated = self.last_updated

        time_open = self.time_open

        time_high = self.time_high

        time_low = self.time_low

        time_close = self.time_close

        quote = self.quote.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "symbol": symbol,
                "last_updated": last_updated,
                "time_open": time_open,
                "time_high": time_high,
                "time_low": time_low,
                "time_close": time_close,
                "quote": quote,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_ohlcv_latest_quote_map import CryptocurrencyOHLCVLatestQuoteMap

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        symbol = d.pop("symbol")

        last_updated = d.pop("last_updated")

        time_open = d.pop("time_open")

        time_high = d.pop("time_high")

        time_low = d.pop("time_low")

        time_close = d.pop("time_close")

        quote = CryptocurrencyOHLCVLatestQuoteMap.from_dict(d.pop("quote"))

        cryptocurrency_ohlcv_latest_cryptocurrency_object = cls(
            id=id,
            name=name,
            symbol=symbol,
            last_updated=last_updated,
            time_open=time_open,
            time_high=time_high,
            time_low=time_low,
            time_close=time_close,
            quote=quote,
        )

        cryptocurrency_ohlcv_latest_cryptocurrency_object.additional_properties = d
        return cryptocurrency_ohlcv_latest_cryptocurrency_object

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
