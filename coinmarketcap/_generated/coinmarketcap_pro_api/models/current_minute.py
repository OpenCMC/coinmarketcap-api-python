from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CurrentMinute")


@_attrs_define
class CurrentMinute:
    """Usage stats around the minute based rate limit.

    Attributes:
        requests_made (float): The number of API calls that have been made in the current UTC minute. Example: 1.
        requests_left (float): The number of remaining API calls that can be made in the current UTC minute before
            receiving a HTTP 429 rate limit error. This limit resets each UTC minute. Example: 59.
    """

    requests_made: float
    requests_left: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requests_made = self.requests_made

        requests_left = self.requests_left

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requests_made": requests_made,
                "requests_left": requests_left,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        requests_made = d.pop("requests_made")

        requests_left = d.pop("requests_left")

        current_minute = cls(
            requests_made=requests_made,
            requests_left=requests_left,
        )

        current_minute.additional_properties = d
        return current_minute

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
