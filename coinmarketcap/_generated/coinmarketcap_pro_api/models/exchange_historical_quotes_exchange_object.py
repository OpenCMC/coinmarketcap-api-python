from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exchange_historical_quotes_nterval_quote_object import ExchangeHistoricalQuotesNtervalQuoteObject


T = TypeVar("T", bound="ExchangeHistoricalQuotesExchangeObject")


@_attrs_define
class ExchangeHistoricalQuotesExchangeObject:
    """An exchange object for each exchange requested. The map key being the id/slug used in the request.

    Attributes:
        id (int): The CoinMarketCap exchange ID. Example: 1.
        name (str): The exchange name. Example: Binance.
        slug (str): The exchange slug. Example: binance.
        quotes (list[ExchangeHistoricalQuotesNtervalQuoteObject]): An array of quotes for each interval for this
            exchange.
    """

    id: int
    name: str
    slug: str
    quotes: list[ExchangeHistoricalQuotesNtervalQuoteObject]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        quotes = []
        for componentsschemas_exchange_historical_quotes_interval_quotes_array_item_data in self.quotes:
            componentsschemas_exchange_historical_quotes_interval_quotes_array_item = (
                componentsschemas_exchange_historical_quotes_interval_quotes_array_item_data.to_dict()
            )
            quotes.append(componentsschemas_exchange_historical_quotes_interval_quotes_array_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "quotes": quotes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exchange_historical_quotes_nterval_quote_object import ExchangeHistoricalQuotesNtervalQuoteObject

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        quotes = []
        _quotes = d.pop("quotes")
        for componentsschemas_exchange_historical_quotes_interval_quotes_array_item_data in _quotes:
            componentsschemas_exchange_historical_quotes_interval_quotes_array_item = (
                ExchangeHistoricalQuotesNtervalQuoteObject.from_dict(
                    componentsschemas_exchange_historical_quotes_interval_quotes_array_item_data
                )
            )

            quotes.append(componentsschemas_exchange_historical_quotes_interval_quotes_array_item)

        exchange_historical_quotes_exchange_object = cls(
            id=id,
            name=name,
            slug=slug,
            quotes=quotes,
        )

        exchange_historical_quotes_exchange_object.additional_properties = d
        return exchange_historical_quotes_exchange_object

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
