from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.v2_simple_price_item_object_quotes_item import V2SimplePriceItemObjectQuotesItem


T = TypeVar("T", bound="V2SimplePriceItemObject")


@_attrs_define
class V2SimplePriceItemObject:
    """Latest-price entry for a single cryptocurrency.

    Attributes:
        id (int): CoinMarketCap cryptocurrency ID. Example: 1.
        name (str): Cryptocurrency name. Example: Bitcoin.
        symbol (str): Cryptocurrency symbol. Example: BTC.
        slug (str): Cryptocurrency slug. Example: bitcoin.
        quotes (list[V2SimplePriceItemObjectQuotesItem]): One quote object per `convert` / `convert_id` currency
            requested.
    """

    id: int
    name: str
    symbol: str
    slug: str
    quotes: list[V2SimplePriceItemObjectQuotesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        symbol = self.symbol

        slug = self.slug

        quotes = []
        for quotes_item_data in self.quotes:
            quotes_item = quotes_item_data.to_dict()
            quotes.append(quotes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "symbol": symbol,
                "slug": slug,
                "quotes": quotes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v2_simple_price_item_object_quotes_item import V2SimplePriceItemObjectQuotesItem

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        symbol = d.pop("symbol")

        slug = d.pop("slug")

        quotes = []
        _quotes = d.pop("quotes")
        for quotes_item_data in _quotes:
            quotes_item = V2SimplePriceItemObjectQuotesItem.from_dict(quotes_item_data)

            quotes.append(quotes_item)

        v2_simple_price_item_object = cls(
            id=id,
            name=name,
            symbol=symbol,
            slug=slug,
            quotes=quotes,
        )

        v2_simple_price_item_object.additional_properties = d
        return v2_simple_price_item_object

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
