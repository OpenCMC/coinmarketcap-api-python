from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FearGreedLatestDTO")


@_attrs_define
class FearGreedLatestDTO:
    """
    Attributes:
        value (int | Unset):
        update_time (str | Unset):
        value_classification (str | Unset):
    """

    value: int | Unset = UNSET
    update_time: str | Unset = UNSET
    value_classification: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        update_time = self.update_time

        value_classification = self.value_classification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if value_classification is not UNSET:
            field_dict["value_classification"] = value_classification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        update_time = d.pop("update_time", UNSET)

        value_classification = d.pop("value_classification", UNSET)

        fear_greed_latest_dto = cls(
            value=value,
            update_time=update_time,
            value_classification=value_classification,
        )

        fear_greed_latest_dto.additional_properties = d
        return fear_greed_latest_dto

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
