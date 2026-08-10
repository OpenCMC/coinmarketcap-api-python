from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Status3")


@_attrs_define
class Status3:
    """
    Attributes:
        timestamp (str): Current ISO 8601 timestamp on the server. Example: 2018-06-02T22:51:28.209Z.
        error_code (int): An internal error code string for the current error. If a unique platform error code is not
            available the HTTP status code is returned. Default: 429. Example: 1008.
        error_message (str): An error message to go along with the error code. Example: You've exceeded your API Key's
            HTTP request rate limit. Rate limits reset every minute..
        elapsed (int): Number of milliseconds taken to generate this response Example: 10.
        credit_count (int): Number of API call credits required for this call. Always 0 for errors.
    """

    timestamp: str
    error_message: str
    elapsed: int
    credit_count: int
    error_code: int = 429
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        error_code = self.error_code

        error_message = self.error_message

        elapsed = self.elapsed

        credit_count = self.credit_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "error_code": error_code,
                "error_message": error_message,
                "elapsed": elapsed,
                "credit_count": credit_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        error_code = d.pop("error_code")

        error_message = d.pop("error_message")

        elapsed = d.pop("elapsed")

        credit_count = d.pop("credit_count")

        status_3 = cls(
            timestamp=timestamp,
            error_code=error_code,
            error_message=error_message,
            elapsed=elapsed,
            credit_count=credit_count,
        )

        status_3.additional_properties = d
        return status_3

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
