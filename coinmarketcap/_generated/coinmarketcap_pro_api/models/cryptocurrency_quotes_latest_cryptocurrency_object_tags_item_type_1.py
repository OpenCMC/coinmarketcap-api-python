from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptocurrencyQuotesLatestCryptocurrencyObjectTagsItemType1")


@_attrs_define
class CryptocurrencyQuotesLatestCryptocurrencyObjectTagsItemType1:
    """
    Attributes:
        slug (str | Unset): Tag slug.
        name (str | Unset): Tag name.
        category (str | Unset): Tag category, for example `ALGORITHM` or `CATEGORY`.
    """

    slug: str | Unset = UNSET
    name: str | Unset = UNSET
    category: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        name = self.name

        category = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        category = d.pop("category", UNSET)

        cryptocurrency_quotes_latest_cryptocurrency_object_tags_item_type_1 = cls(
            slug=slug,
            name=name,
            category=category,
        )

        cryptocurrency_quotes_latest_cryptocurrency_object_tags_item_type_1.additional_properties = d
        return cryptocurrency_quotes_latest_cryptocurrency_object_tags_item_type_1

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
