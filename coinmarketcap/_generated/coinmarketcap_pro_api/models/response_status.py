from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseStatus")


@_attrs_define
class ResponseStatus:
    """
    Attributes:
        timestamp (str | Unset):
        error_code (str | Unset):
        error_message (str | Unset):
        elapsed (int | Unset):
        credit_count (int | Unset):
    """

    timestamp: str | Unset = UNSET
    error_code: str | Unset = UNSET
    error_message: str | Unset = UNSET
    elapsed: int | Unset = UNSET
    credit_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        error_code = self.error_code

        error_message = self.error_message

        elapsed = self.elapsed

        credit_count = self.credit_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if elapsed is not UNSET:
            field_dict["elapsed"] = elapsed
        if credit_count is not UNSET:
            field_dict["credit_count"] = credit_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp", UNSET)

        error_code = d.pop("error_code", UNSET)

        error_message = d.pop("error_message", UNSET)

        elapsed = d.pop("elapsed", UNSET)

        credit_count = d.pop("credit_count", UNSET)

        response_status = cls(
            timestamp=timestamp,
            error_code=error_code,
            error_message=error_message,
            elapsed=elapsed,
            credit_count=credit_count,
        )

        response_status.additional_properties = d
        return response_status

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
