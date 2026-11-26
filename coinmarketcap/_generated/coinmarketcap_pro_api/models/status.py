from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Status")


@_attrs_define
class Status:
    r"""
    Attributes:
        timestamp (str): Current ISO 8601 timestamp on the server. Example: 2018-06-02T22:51:28.209Z.
        error_code (int | str): An internal error code for the current error. If a unique platform error code is not
            available the HTTP status code is returned. Some endpoints return this code as a string, for example `"4001"`.
            Default: 400. Example: 400.
        error_message (str): An error message to go along with the error code. Example: Invalid value for \"id\".
        elapsed (int): Number of milliseconds taken to generate this response Example: 10.
        credit_count (int): Number of API call credits required for this call. Always 0 for errors.
        category (str | Unset): Error category on some v5 endpoints, for example `VALIDATION` for an invalid parameter
            or `AUTH` for a plan limit. Example: VALIDATION.
        error_detail (None | str | Unset): On some v5 endpoints, a more specific explanation of the error, such as the
            parameter that was rejected. Example: convert is not supported by this endpoint..
    """

    timestamp: str
    error_message: str
    elapsed: int
    credit_count: int
    error_code: int | str = 400
    category: str | Unset = UNSET
    error_detail: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        error_code: int | str
        error_code = self.error_code

        error_message = self.error_message

        elapsed = self.elapsed

        credit_count = self.credit_count

        category = self.category

        error_detail: None | str | Unset
        if isinstance(self.error_detail, Unset):
            error_detail = UNSET
        else:
            error_detail = self.error_detail

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
        if category is not UNSET:
            field_dict["category"] = category
        if error_detail is not UNSET:
            field_dict["error_detail"] = error_detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        def _parse_error_code(data: object) -> int | str:
            return cast(int | str, data)

        error_code = _parse_error_code(d.pop("error_code"))

        error_message = d.pop("error_message")

        elapsed = d.pop("elapsed")

        credit_count = d.pop("credit_count")

        category = d.pop("category", UNSET)

        def _parse_error_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_detail = _parse_error_detail(d.pop("error_detail", UNSET))

        status = cls(
            timestamp=timestamp,
            error_code=error_code,
            error_message=error_message,
            elapsed=elapsed,
            credit_count=credit_count,
            category=category,
            error_detail=error_detail,
        )

        status.additional_properties = d
        return status

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
