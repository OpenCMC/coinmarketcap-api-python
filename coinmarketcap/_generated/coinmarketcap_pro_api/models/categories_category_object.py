from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CategoriesCategoryObject")


@_attrs_define
class CategoriesCategoryObject:
    """A results object for each category requested. The map key being the id used in the request.

    Attributes:
        id (str): The unique ID of the category Example: fj3893983c1b42617d6dc0.
        avg_price_change (float): Average price change of coins within this categry Example: 0.03.
        market_cap (float): Market cap of coins within this categry Example: 121020662982.
        market_cap_change (float): Market cap change of coins within this categry Example: 0.03.
        volume (float): Volume of coins within this categry Example: 121020662982.
        volume_change (float): Volume change of coins within this categry Example: 0.03.
        last_updated (str): Timestamp (ISO 8601) of when this was last updated. Example: 2013-04-28T00:00:00.000Z.
        name (str | Unset): The name of the category Example: A16Z Portfolio.
        title (str | Unset): The title of the category Example: A16Z Portfolio.
        description (str | Unset): The description of the category Example: A16Z Portfolio.
        num_tokens (int | Unset):  Example: 12.
    """

    id: str
    avg_price_change: float
    market_cap: float
    market_cap_change: float
    volume: float
    volume_change: float
    last_updated: str
    name: str | Unset = UNSET
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    num_tokens: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        avg_price_change = self.avg_price_change

        market_cap = self.market_cap

        market_cap_change = self.market_cap_change

        volume = self.volume

        volume_change = self.volume_change

        last_updated = self.last_updated

        name = self.name

        title = self.title

        description = self.description

        num_tokens = self.num_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "avg_price_change": avg_price_change,
                "market_cap": market_cap,
                "market_cap_change": market_cap_change,
                "volume": volume,
                "volume_change": volume_change,
                "last_updated": last_updated,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if num_tokens is not UNSET:
            field_dict["num_tokens"] = num_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        avg_price_change = d.pop("avg_price_change")

        market_cap = d.pop("market_cap")

        market_cap_change = d.pop("market_cap_change")

        volume = d.pop("volume")

        volume_change = d.pop("volume_change")

        last_updated = d.pop("last_updated")

        name = d.pop("name", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        num_tokens = d.pop("num_tokens", UNSET)

        categories_category_object = cls(
            id=id,
            avg_price_change=avg_price_change,
            market_cap=market_cap,
            market_cap_change=market_cap_change,
            volume=volume,
            volume_change=volume_change,
            last_updated=last_updated,
            name=name,
            title=title,
            description=description,
            num_tokens=num_tokens,
        )

        categories_category_object.additional_properties = d
        return categories_category_object

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
