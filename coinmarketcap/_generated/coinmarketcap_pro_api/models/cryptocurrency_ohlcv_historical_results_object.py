from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cryptocurrency_ohlcv_historical_interval_quote_object import (
        CryptocurrencyOHLCVHistoricalIntervalQuoteObject,
    )


T = TypeVar("T", bound="CryptocurrencyOHLCVHistoricalResultsObject")


@_attrs_define
class CryptocurrencyOHLCVHistoricalResultsObject:
    """Results of your query returned as an object.

    Example:
        {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'quotes': [{'time_open': '2019-01-02T00:00:00.000Z', 'time_close':
            '2019-01-02T23:59:59.999Z', 'time_high': '2019-01-02T03:53:00.000Z', 'time_low': '2019-01-02T02:43:00.000Z',
            'quote': {'USD': {'open': 3849.21640853, 'high': 3947.9812729, 'low': 3817.40949569, 'close': 3943.40933686,
            'volume': 5244856835.70851, 'market_cap': 68849856731.6738, 'timestamp': '2019-01-02T23:59:59.999Z'}}},
            {'time_open': '2019-01-03T00:00:00.000Z', 'time_close': '2019-01-03T23:59:59.999Z', 'time_high':
            '2019-01-02T03:53:00.000Z', 'time_low': '2019-01-02T02:43:00.000Z', 'quote': {'USD': {'open': 3931.04863841,
            'high': 3935.68513083, 'low': 3826.22287069, 'close': 3836.74131867, 'volume': 4530215218.84018, 'market_cap':
            66994920902.7202, 'timestamp': '2019-01-03T23:59:59.999Z'}}}]}

    Attributes:
        id (int): The CoinMarketCap cryptocurrency ID. Example: 1.
        name (str): The cryptocurrency name. Example: Bitcoin.
        symbol (str): The cryptocurrency symbol. Example: BTC.
        quotes (list[CryptocurrencyOHLCVHistoricalIntervalQuoteObject]): An array of OHLCV quotes for the supplied
            interval.
    """

    id: int
    name: str
    symbol: str
    quotes: list[CryptocurrencyOHLCVHistoricalIntervalQuoteObject]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        symbol = self.symbol

        quotes = []
        for componentsschemas_cryptocurrency_ohlcv_historical_interval_quotes_array_item_data in self.quotes:
            componentsschemas_cryptocurrency_ohlcv_historical_interval_quotes_array_item = (
                componentsschemas_cryptocurrency_ohlcv_historical_interval_quotes_array_item_data.to_dict()
            )
            quotes.append(componentsschemas_cryptocurrency_ohlcv_historical_interval_quotes_array_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "symbol": symbol,
                "quotes": quotes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_ohlcv_historical_interval_quote_object import (
            CryptocurrencyOHLCVHistoricalIntervalQuoteObject,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        symbol = d.pop("symbol")

        quotes = []
        _quotes = d.pop("quotes")
        for componentsschemas_cryptocurrency_ohlcv_historical_interval_quotes_array_item_data in _quotes:
            componentsschemas_cryptocurrency_ohlcv_historical_interval_quotes_array_item = (
                CryptocurrencyOHLCVHistoricalIntervalQuoteObject.from_dict(
                    componentsschemas_cryptocurrency_ohlcv_historical_interval_quotes_array_item_data
                )
            )

            quotes.append(componentsschemas_cryptocurrency_ohlcv_historical_interval_quotes_array_item)

        cryptocurrency_ohlcv_historical_results_object = cls(
            id=id,
            name=name,
            symbol=symbol,
            quotes=quotes,
        )

        cryptocurrency_ohlcv_historical_results_object.additional_properties = d
        return cryptocurrency_ohlcv_historical_results_object

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
