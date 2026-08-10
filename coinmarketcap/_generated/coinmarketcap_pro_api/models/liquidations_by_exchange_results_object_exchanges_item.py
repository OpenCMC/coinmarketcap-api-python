from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.liquidations_by_exchange_results_object_exchanges_item_quotes_item import (
        LiquidationsByExchangeResultsObjectExchangesItemQuotesItem,
    )


T = TypeVar("T", bound="LiquidationsByExchangeResultsObjectExchangesItem")


@_attrs_define
class LiquidationsByExchangeResultsObjectExchangesItem:
    """
    Attributes:
        exchange_id (int | Unset): CoinMarketCap exchange ID. Example: 270.
        name (str | Unset): Exchange name. Example: Binance.
        slug (str | Unset): Exchange slug. Example: binance.
        quotes (list[LiquidationsByExchangeResultsObjectExchangesItemQuotesItem] | Unset): One entry per requested
            convert currency.
    """

    exchange_id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    quotes: list[LiquidationsByExchangeResultsObjectExchangesItemQuotesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange_id = self.exchange_id

        name = self.name

        slug = self.slug

        quotes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quotes, Unset):
            quotes = []
            for quotes_item_data in self.quotes:
                quotes_item = quotes_item_data.to_dict()
                quotes.append(quotes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exchange_id is not UNSET:
            field_dict["exchange_id"] = exchange_id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if quotes is not UNSET:
            field_dict["quotes"] = quotes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.liquidations_by_exchange_results_object_exchanges_item_quotes_item import (
            LiquidationsByExchangeResultsObjectExchangesItemQuotesItem,
        )

        d = dict(src_dict)
        exchange_id = d.pop("exchange_id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        _quotes = d.pop("quotes", UNSET)
        quotes: list[LiquidationsByExchangeResultsObjectExchangesItemQuotesItem] | Unset = UNSET
        if _quotes is not UNSET:
            quotes = []
            for quotes_item_data in _quotes:
                quotes_item = LiquidationsByExchangeResultsObjectExchangesItemQuotesItem.from_dict(quotes_item_data)

                quotes.append(quotes_item)

        liquidations_by_exchange_results_object_exchanges_item = cls(
            exchange_id=exchange_id,
            name=name,
            slug=slug,
            quotes=quotes,
        )

        liquidations_by_exchange_results_object_exchanges_item.additional_properties = d
        return liquidations_by_exchange_results_object_exchanges_item

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
