from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HolderTagItem")


@_attrs_define
class HolderTagItem:
    """
    Attributes:
        tag (str | Unset):
        hc (str | Unset):
        tb (str | Unset):
        hr (str | Unset):
    """

    tag: str | Unset = UNSET
    hc: str | Unset = UNSET
    tb: str | Unset = UNSET
    hr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag = self.tag

        hc = self.hc

        tb = self.tb

        hr = self.hr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tag is not UNSET:
            field_dict["tag"] = tag
        if hc is not UNSET:
            field_dict["hc"] = hc
        if tb is not UNSET:
            field_dict["tb"] = tb
        if hr is not UNSET:
            field_dict["hr"] = hr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tag = d.pop("tag", UNSET)

        hc = d.pop("hc", UNSET)

        tb = d.pop("tb", UNSET)

        hr = d.pop("hr", UNSET)

        holder_tag_item = cls(
            tag=tag,
            hc=hc,
            tb=tb,
            hr=hr,
        )

        holder_tag_item.additional_properties = d
        return holder_tag_item

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
