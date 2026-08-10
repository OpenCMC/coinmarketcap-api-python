from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.holder_tag_item import HolderTagItem


T = TypeVar("T", bound="HolderTagCountVO")


@_attrs_define
class HolderTagCountVO:
    """
    Attributes:
        holders (list[HolderTagItem] | Unset):
        platform_id (int | Unset):
        token_address (str | Unset):
    """

    holders: list[HolderTagItem] | Unset = UNSET
    platform_id: int | Unset = UNSET
    token_address: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        holders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.holders, Unset):
            holders = []
            for holders_item_data in self.holders:
                holders_item = holders_item_data.to_dict()
                holders.append(holders_item)

        platform_id = self.platform_id

        token_address = self.token_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if holders is not UNSET:
            field_dict["holders"] = holders
        if platform_id is not UNSET:
            field_dict["platformId"] = platform_id
        if token_address is not UNSET:
            field_dict["tokenAddress"] = token_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.holder_tag_item import HolderTagItem

        d = dict(src_dict)
        _holders = d.pop("holders", UNSET)
        holders: list[HolderTagItem] | Unset = UNSET
        if _holders is not UNSET:
            holders = []
            for holders_item_data in _holders:
                holders_item = HolderTagItem.from_dict(holders_item_data)

                holders.append(holders_item)

        platform_id = d.pop("platformId", UNSET)

        token_address = d.pop("tokenAddress", UNSET)

        holder_tag_count_vo = cls(
            holders=holders,
            platform_id=platform_id,
            token_address=token_address,
        )

        holder_tag_count_vo.additional_properties = d
        return holder_tag_count_vo

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
