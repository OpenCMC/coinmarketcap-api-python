from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProApiResponseStatus")


@_attrs_define
class ProApiResponseStatus:
    """
    Attributes:
        credit_count (int | Unset): Number of credits used for the request
        elapsed (int | Unset): Time taken to process the request
        error_code (str | Unset): Error code of the response
        error_message (str | Unset): Error message of the response, if any
        notice (str | Unset): Api notice message of the response
        timestamp (datetime.datetime | Unset): Timestamp of the response
        total_count (int | Unset): Number of data size
    """

    credit_count: int | Unset = UNSET
    elapsed: int | Unset = UNSET
    error_code: str | Unset = UNSET
    error_message: str | Unset = UNSET
    notice: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credit_count = self.credit_count

        elapsed = self.elapsed

        error_code = self.error_code

        error_message = self.error_message

        notice = self.notice

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credit_count is not UNSET:
            field_dict["credit_count"] = credit_count
        if elapsed is not UNSET:
            field_dict["elapsed"] = elapsed
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if notice is not UNSET:
            field_dict["notice"] = notice
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credit_count = d.pop("credit_count", UNSET)

        elapsed = d.pop("elapsed", UNSET)

        error_code = d.pop("error_code", UNSET)

        error_message = d.pop("error_message", UNSET)

        notice = d.pop("notice", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        total_count = d.pop("total_count", UNSET)

        pro_api_response_status = cls(
            credit_count=credit_count,
            elapsed=elapsed,
            error_code=error_code,
            error_message=error_message,
            notice=notice,
            timestamp=timestamp,
            total_count=total_count,
        )

        pro_api_response_status.additional_properties = d
        return pro_api_response_status

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
