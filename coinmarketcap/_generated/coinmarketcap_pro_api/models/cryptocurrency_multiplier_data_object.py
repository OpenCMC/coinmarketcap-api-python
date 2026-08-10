from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cryptocurrency_multiplier_item_object import CryptocurrencyMultiplierItemObject


T = TypeVar("T", bound="CryptocurrencyMultiplierDataObject")


@_attrs_define
class CryptocurrencyMultiplierDataObject:
    """Paginated multiplier results.

    Attributes:
        total_size (int): Total number of results before pagination. Example: 21.
        has_more (bool): Whether additional candidate IDs remain after the current `start` and `limit` window. Example:
            True.
        items (list[CryptocurrencyMultiplierItemObject]): Multiplier records for the current page.
    """

    total_size: int
    has_more: bool
    items: list[CryptocurrencyMultiplierItemObject]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_size = self.total_size

        has_more = self.has_more

        items = []
        for componentsschemas_cryptocurrency_multiplier_items_array_item_data in self.items:
            componentsschemas_cryptocurrency_multiplier_items_array_item = (
                componentsschemas_cryptocurrency_multiplier_items_array_item_data.to_dict()
            )
            items.append(componentsschemas_cryptocurrency_multiplier_items_array_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_size": total_size,
                "has_more": has_more,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_multiplier_item_object import CryptocurrencyMultiplierItemObject

        d = dict(src_dict)
        total_size = d.pop("total_size")

        has_more = d.pop("has_more")

        items = []
        _items = d.pop("items")
        for componentsschemas_cryptocurrency_multiplier_items_array_item_data in _items:
            componentsschemas_cryptocurrency_multiplier_items_array_item = CryptocurrencyMultiplierItemObject.from_dict(
                componentsschemas_cryptocurrency_multiplier_items_array_item_data
            )

            items.append(componentsschemas_cryptocurrency_multiplier_items_array_item)

        cryptocurrency_multiplier_data_object = cls(
            total_size=total_size,
            has_more=has_more,
            items=items,
        )

        cryptocurrency_multiplier_data_object.additional_properties = d
        return cryptocurrency_multiplier_data_object

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
