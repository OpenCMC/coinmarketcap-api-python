from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dex_multiplier_item_object import DexMultiplierItemObject


T = TypeVar("T", bound="DexMultiplierDataObject")


@_attrs_define
class DexMultiplierDataObject:
    """Paginated ERC-8056 multiplier results.

    Attributes:
        total_size (int): Total number of results before pagination. Example: 2.
        items (list[DexMultiplierItemObject]):
        has_more (bool): Whether more results exist beyond the current page.
    """

    total_size: int
    items: list[DexMultiplierItemObject]
    has_more: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_size = self.total_size

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_size": total_size,
                "items": items,
                "has_more": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dex_multiplier_item_object import DexMultiplierItemObject

        d = dict(src_dict)
        total_size = d.pop("total_size")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = DexMultiplierItemObject.from_dict(items_item_data)

            items.append(items_item)

        has_more = d.pop("has_more")

        dex_multiplier_data_object = cls(
            total_size=total_size,
            items=items,
            has_more=has_more,
        )

        dex_multiplier_data_object.additional_properties = d
        return dex_multiplier_data_object

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
