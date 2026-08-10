from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tools_price_conversion_quotes_map_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint import (
        ToolsPriceConversionQuotesMapPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2Endpoint,
    )


T = TypeVar("T", bound="ToolsPriceConversionResultsObject")


@_attrs_define
class ToolsPriceConversionResultsObject:
    """Results object for your API call.

    Example:
        {'symbol': 'BTC', 'id': 1, 'name': 'Bitcoin', 'amount': 50, 'last_updated': '2018-06-06T08:04:36.000Z', 'quote':
            {'USD': {'price': 284656.08465608465, 'last_updated': '2018-06-06T06:00:00.000Z'}}}

    Attributes:
        id (int): The unique CoinMarketCap ID for your base currency. Example: 1.
        name (str): The name of your base currency. Example: Bitcoin.
        symbol (str): The symbol for your base currency. Example: BTC.
        amount (float): Amount of base currency to convert from. Example: 50.
        last_updated (str): Timestamp (ISO 8601) of when the referenced market value of the base currency was recorded.
            Example: 2018-06-02T00:00:00.000Z.
        quote (ToolsPriceConversionQuotesMapPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2Endpoint):
            An object map of price conversions.
    """

    id: int
    name: str
    symbol: str
    amount: float
    last_updated: str
    quote: ToolsPriceConversionQuotesMapPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2Endpoint
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        symbol = self.symbol

        amount = self.amount

        last_updated = self.last_updated

        quote = self.quote.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "symbol": symbol,
                "amount": amount,
                "last_updated": last_updated,
                "quote": quote,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tools_price_conversion_quotes_map_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint import (
            ToolsPriceConversionQuotesMapPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2Endpoint,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        symbol = d.pop("symbol")

        amount = d.pop("amount")

        last_updated = d.pop("last_updated")

        quote = ToolsPriceConversionQuotesMapPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2Endpoint.from_dict(
            d.pop("quote")
        )

        tools_price_conversion_results_object = cls(
            id=id,
            name=name,
            symbol=symbol,
            amount=amount,
            last_updated=last_updated,
            quote=quote,
        )

        tools_price_conversion_results_object.additional_properties = d
        return tools_price_conversion_results_object

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
