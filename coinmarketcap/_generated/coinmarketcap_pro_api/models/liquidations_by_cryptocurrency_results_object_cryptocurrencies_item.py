from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.liquidations_by_cryptocurrency_results_object_cryptocurrencies_item_quotes_item import (
        LiquidationsByCryptocurrencyResultsObjectCryptocurrenciesItemQuotesItem,
    )


T = TypeVar("T", bound="LiquidationsByCryptocurrencyResultsObjectCryptocurrenciesItem")


@_attrs_define
class LiquidationsByCryptocurrencyResultsObjectCryptocurrenciesItem:
    """
    Attributes:
        crypto_id (int | Unset): CoinMarketCap cryptocurrency ID. Example: 1.
        name (str | Unset): Cryptocurrency name. Example: Bitcoin.
        symbol (str | Unset): Cryptocurrency symbol. Example: BTC.
        slug (str | Unset): Cryptocurrency slug. Example: bitcoin.
        cmc_rank (int | Unset): The coin's CoinMarketCap market-cap rank. Example: 1.
        quotes (list[LiquidationsByCryptocurrencyResultsObjectCryptocurrenciesItemQuotesItem] | Unset): One entry per
            requested convert currency.
    """

    crypto_id: int | Unset = UNSET
    name: str | Unset = UNSET
    symbol: str | Unset = UNSET
    slug: str | Unset = UNSET
    cmc_rank: int | Unset = UNSET
    quotes: list[LiquidationsByCryptocurrencyResultsObjectCryptocurrenciesItemQuotesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crypto_id = self.crypto_id

        name = self.name

        symbol = self.symbol

        slug = self.slug

        cmc_rank = self.cmc_rank

        quotes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quotes, Unset):
            quotes = []
            for quotes_item_data in self.quotes:
                quotes_item = quotes_item_data.to_dict()
                quotes.append(quotes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crypto_id is not UNSET:
            field_dict["crypto_id"] = crypto_id
        if name is not UNSET:
            field_dict["name"] = name
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if slug is not UNSET:
            field_dict["slug"] = slug
        if cmc_rank is not UNSET:
            field_dict["cmc_rank"] = cmc_rank
        if quotes is not UNSET:
            field_dict["quotes"] = quotes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.liquidations_by_cryptocurrency_results_object_cryptocurrencies_item_quotes_item import (
            LiquidationsByCryptocurrencyResultsObjectCryptocurrenciesItemQuotesItem,
        )

        d = dict(src_dict)
        crypto_id = d.pop("crypto_id", UNSET)

        name = d.pop("name", UNSET)

        symbol = d.pop("symbol", UNSET)

        slug = d.pop("slug", UNSET)

        cmc_rank = d.pop("cmc_rank", UNSET)

        _quotes = d.pop("quotes", UNSET)
        quotes: list[LiquidationsByCryptocurrencyResultsObjectCryptocurrenciesItemQuotesItem] | Unset = UNSET
        if _quotes is not UNSET:
            quotes = []
            for quotes_item_data in _quotes:
                quotes_item = LiquidationsByCryptocurrencyResultsObjectCryptocurrenciesItemQuotesItem.from_dict(
                    quotes_item_data
                )

                quotes.append(quotes_item)

        liquidations_by_cryptocurrency_results_object_cryptocurrencies_item = cls(
            crypto_id=crypto_id,
            name=name,
            symbol=symbol,
            slug=slug,
            cmc_rank=cmc_rank,
            quotes=quotes,
        )

        liquidations_by_cryptocurrency_results_object_cryptocurrencies_item.additional_properties = d
        return liquidations_by_cryptocurrency_results_object_cryptocurrencies_item

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
