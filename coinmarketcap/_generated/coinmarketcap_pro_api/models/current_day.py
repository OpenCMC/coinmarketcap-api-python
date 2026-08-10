from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CurrentDay")


@_attrs_define
class CurrentDay:
    """Usage stats around the daily API credit limit.

    Attributes:
        credits_used (float): The number of API credits used during the current daily period. Example: 1.
        credits_left (float): The number of remaining API credits that can be used during the current daily period
            before receiving a HTTP 429 rate limit error. This limit resets at the end of each daily period. Example: 3999.
    """

    credits_used: float
    credits_left: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credits_used = self.credits_used

        credits_left = self.credits_left

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credits_used": credits_used,
                "credits_left": credits_left,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credits_used = d.pop("credits_used")

        credits_left = d.pop("credits_left")

        current_day = cls(
            credits_used=credits_used,
            credits_left=credits_left,
        )

        current_day.additional_properties = d
        return current_day

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
