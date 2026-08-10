from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exchange_historical_quotes_quote_currency_map import ExchangeHistoricalQuotesQuoteCurrencyMap


T = TypeVar("T", bound="ExchangeHistoricalQuotesNtervalQuoteObject")


@_attrs_define
class ExchangeHistoricalQuotesNtervalQuoteObject:
    """An object containing details for the current interval quote.

    Attributes:
        timestamp (str): Timestamp (ISO 8601) of when this historical quote was recorded. Example:
            2018-06-02T00:00:00.000Z.
        num_market_pairs (float): Number of market pairs available at the current historical interval. Example:
            123456789.
        quote (ExchangeHistoricalQuotesQuoteCurrencyMap): A map of market details for this quote in different currency
            conversions. The default map included is USD.
    """

    timestamp: str
    num_market_pairs: float
    quote: ExchangeHistoricalQuotesQuoteCurrencyMap
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        num_market_pairs = self.num_market_pairs

        quote = self.quote.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "num_market_pairs": num_market_pairs,
                "quote": quote,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exchange_historical_quotes_quote_currency_map import ExchangeHistoricalQuotesQuoteCurrencyMap

        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        num_market_pairs = d.pop("num_market_pairs")

        quote = ExchangeHistoricalQuotesQuoteCurrencyMap.from_dict(d.pop("quote"))

        exchange_historical_quotes_nterval_quote_object = cls(
            timestamp=timestamp,
            num_market_pairs=num_market_pairs,
            quote=quote,
        )

        exchange_historical_quotes_nterval_quote_object.additional_properties = d
        return exchange_historical_quotes_nterval_quote_object

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
