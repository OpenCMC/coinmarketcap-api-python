from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="APIStatusObject")


@_attrs_define
class APIStatusObject:
    """Standardized status object for API calls.

    Attributes:
        timestamp (str): Current timestamp (ISO 8601) on the server. Example: 2026-03-05T22:43:48.471Z.
        error_code (int | str): An internal error code for the current error. If a unique platform error code is not
            available the HTTP status code is returned. `0` is returned if there is no error. Some endpoints return this
            code as a string, for example `"0"`.
        error_message (None | str): An error message to go along with the error code.
        elapsed (int): Number of milliseconds taken to generate this response. Example: 10.
        credit_count (int): Number of API call credits that were used for this call. Example: 1.
        notice (None | str | Unset): Optional notice about API key information.
        total_count (int | Unset): Total number of results available for this request. Only returned by some list
            endpoints. Example: 8128.
    """

    timestamp: str
    error_code: int | str
    error_message: None | str
    elapsed: int
    credit_count: int
    notice: None | str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        error_code: int | str
        error_code = self.error_code

        error_message: None | str
        error_message = self.error_message

        elapsed = self.elapsed

        credit_count = self.credit_count

        notice: None | str | Unset
        if isinstance(self.notice, Unset):
            notice = UNSET
        else:
            notice = self.notice

        total_count = self.total_count

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
        if notice is not UNSET:
            field_dict["notice"] = notice
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        def _parse_error_code(data: object) -> int | str:
            return cast(int | str, data)

        error_code = _parse_error_code(d.pop("error_code"))

        def _parse_error_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_message = _parse_error_message(d.pop("error_message"))

        elapsed = d.pop("elapsed")

        credit_count = d.pop("credit_count")

        def _parse_notice(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notice = _parse_notice(d.pop("notice", UNSET))

        total_count = d.pop("total_count", UNSET)

        api_status_object = cls(
            timestamp=timestamp,
            error_code=error_code,
            error_message=error_message,
            elapsed=elapsed,
            credit_count=credit_count,
            notice=notice,
            total_count=total_count,
        )

        api_status_object.additional_properties = d
        return api_status_object

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
