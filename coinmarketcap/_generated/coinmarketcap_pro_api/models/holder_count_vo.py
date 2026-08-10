from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HolderCountVO")


@_attrs_define
class HolderCountVO:
    """
    Attributes:
        platform_id (int | Unset):
        count (int | Unset):
        token_address (str | Unset):
    """

    platform_id: int | Unset = UNSET
    count: int | Unset = UNSET
    token_address: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform_id = self.platform_id

        count = self.count

        token_address = self.token_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform_id is not UNSET:
            field_dict["platformId"] = platform_id
        if count is not UNSET:
            field_dict["count"] = count
        if token_address is not UNSET:
            field_dict["tokenAddress"] = token_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform_id = d.pop("platformId", UNSET)

        count = d.pop("count", UNSET)

        token_address = d.pop("tokenAddress", UNSET)

        holder_count_vo = cls(
            platform_id=platform_id,
            count=count,
            token_address=token_address,
        )

        holder_count_vo.additional_properties = d
        return holder_count_vo

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
