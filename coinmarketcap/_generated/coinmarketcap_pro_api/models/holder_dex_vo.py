from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.holder_detail_vo import HolderDetailVO


T = TypeVar("T", bound="HolderDexVO")


@_attrs_define
class HolderDexVO:
    """
    Attributes:
        holders (list[HolderDetailVO] | Unset):
    """

    holders: list[HolderDetailVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        holders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.holders, Unset):
            holders = []
            for holders_item_data in self.holders:
                holders_item = holders_item_data.to_dict()
                holders.append(holders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if holders is not UNSET:
            field_dict["holders"] = holders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.holder_detail_vo import HolderDetailVO

        d = dict(src_dict)
        _holders = d.pop("holders", UNSET)
        holders: list[HolderDetailVO] | Unset = UNSET
        if _holders is not UNSET:
            holders = []
            for holders_item_data in _holders:
                holders_item = HolderDetailVO.from_dict(holders_item_data)

                holders.append(holders_item)

        holder_dex_vo = cls(
            holders=holders,
        )

        holder_dex_vo.additional_properties = d
        return holder_dex_vo

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
