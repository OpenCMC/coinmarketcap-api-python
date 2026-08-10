from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cryptocurrency_quotes_historical_interval_quote_object import (
        CryptocurrencyQuotesHistoricalIntervalQuoteObject,
    )


T = TypeVar("T", bound="CryptocurrencyQuotesHistoricalResultObject")


@_attrs_define
class CryptocurrencyQuotesHistoricalResultObject:
    """A results object for each cryptocurrency requested. The map key being the id/symbol used in the request.

    Attributes:
        id (int): The CoinMarketCap cryptocurrency ID. Example: 1.
        name (str): The cryptocurrency name. Example: Bitcoin.
        symbol (str): The cryptocurrency symbol. Example: BTC.
        quotes (list[CryptocurrencyQuotesHistoricalIntervalQuoteObject]): An array of quotes for each interval for this
            cryptocurrency.
        is_active (int | Unset): 1 if this cryptocurrency has at least 1 active market currently being tracked by the
            platform, otherwise 0. A value of 1 is analogous with `listing_status=active`. Example: 1.
        is_fiat (int | Unset): 1 if this is a fiat Example: 1.
    """

    id: int
    name: str
    symbol: str
    quotes: list[CryptocurrencyQuotesHistoricalIntervalQuoteObject]
    is_active: int | Unset = UNSET
    is_fiat: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        symbol = self.symbol

        quotes = []
        for componentsschemas_cryptocurrency_quotes_historical_interval_quotes_array_item_data in self.quotes:
            componentsschemas_cryptocurrency_quotes_historical_interval_quotes_array_item = (
                componentsschemas_cryptocurrency_quotes_historical_interval_quotes_array_item_data.to_dict()
            )
            quotes.append(componentsschemas_cryptocurrency_quotes_historical_interval_quotes_array_item)

        is_active = self.is_active

        is_fiat = self.is_fiat

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
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_fiat is not UNSET:
            field_dict["is_fiat"] = is_fiat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_quotes_historical_interval_quote_object import (
            CryptocurrencyQuotesHistoricalIntervalQuoteObject,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        symbol = d.pop("symbol")

        quotes = []
        _quotes = d.pop("quotes")
        for componentsschemas_cryptocurrency_quotes_historical_interval_quotes_array_item_data in _quotes:
            componentsschemas_cryptocurrency_quotes_historical_interval_quotes_array_item = (
                CryptocurrencyQuotesHistoricalIntervalQuoteObject.from_dict(
                    componentsschemas_cryptocurrency_quotes_historical_interval_quotes_array_item_data
                )
            )

            quotes.append(componentsschemas_cryptocurrency_quotes_historical_interval_quotes_array_item)

        is_active = d.pop("is_active", UNSET)

        is_fiat = d.pop("is_fiat", UNSET)

        cryptocurrency_quotes_historical_result_object = cls(
            id=id,
            name=name,
            symbol=symbol,
            quotes=quotes,
            is_active=is_active,
            is_fiat=is_fiat,
        )

        cryptocurrency_quotes_historical_result_object.additional_properties = d
        return cryptocurrency_quotes_historical_result_object

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
