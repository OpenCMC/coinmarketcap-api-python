from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cryptocurrency_quotes_historical_quote_currency_map import (
        CryptocurrencyQuotesHistoricalQuoteCurrencyMap,
    )


T = TypeVar("T", bound="CryptocurrencyQuotesHistoricalIntervalQuoteObject")


@_attrs_define
class CryptocurrencyQuotesHistoricalIntervalQuoteObject:
    """An object containing details for the current interval quote.

    Attributes:
        timestamp (str): Timestamp of when this historical quote was recorded. Example: 2018-06-02T23:59:59.999Z.
        quote (CryptocurrencyQuotesHistoricalQuoteCurrencyMap): A map of market details for this quote in different
            currency conversions. The default map included is USD.
        search_interval (str | Unset): The interval timestamp for the search period that this historical quote was
            located against. *This field is only returned if requested through the `aux` request parameter.* Example:
            2018-06-02T00:00:00.000Z.
    """

    timestamp: str
    quote: CryptocurrencyQuotesHistoricalQuoteCurrencyMap
    search_interval: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        quote = self.quote.to_dict()

        search_interval = self.search_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "quote": quote,
            }
        )
        if search_interval is not UNSET:
            field_dict["search_interval"] = search_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_quotes_historical_quote_currency_map import (
            CryptocurrencyQuotesHistoricalQuoteCurrencyMap,
        )

        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        quote = CryptocurrencyQuotesHistoricalQuoteCurrencyMap.from_dict(d.pop("quote"))

        search_interval = d.pop("search_interval", UNSET)

        cryptocurrency_quotes_historical_interval_quote_object = cls(
            timestamp=timestamp,
            quote=quote,
            search_interval=search_interval,
        )

        cryptocurrency_quotes_historical_interval_quote_object.additional_properties = d
        return cryptocurrency_quotes_historical_interval_quote_object

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
