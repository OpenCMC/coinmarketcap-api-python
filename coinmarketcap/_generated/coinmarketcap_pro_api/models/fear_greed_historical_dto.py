from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FearGreedHistoricalDTO")


@_attrs_define
class FearGreedHistoricalDTO:
    """
    Attributes:
        timestamp (str | Unset):
        value (int | Unset):
        value_classification (str | Unset):
    """

    timestamp: str | Unset = UNSET
    value: int | Unset = UNSET
    value_classification: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        value = self.value

        value_classification = self.value_classification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if value is not UNSET:
            field_dict["value"] = value
        if value_classification is not UNSET:
            field_dict["value_classification"] = value_classification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp", UNSET)

        value = d.pop("value", UNSET)

        value_classification = d.pop("value_classification", UNSET)

        fear_greed_historical_dto = cls(
            timestamp=timestamp,
            value=value,
            value_classification=value_classification,
        )

        fear_greed_historical_dto.additional_properties = d
        return fear_greed_historical_dto

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
