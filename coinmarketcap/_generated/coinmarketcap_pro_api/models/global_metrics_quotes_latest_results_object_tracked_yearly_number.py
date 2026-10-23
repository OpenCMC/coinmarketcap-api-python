from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalMetricsQuotesLatestResultsObjectTrackedYearlyNumber")


@_attrs_define
class GlobalMetricsQuotesLatestResultsObjectTrackedYearlyNumber:
    """The highest and lowest number of new cryptocurrencies and DEX tokens tracked in a single day over the past year.

    Attributes:
        max_incremental_number (int | Unset): Highest number of new assets tracked in a single day.
        min_incremental_number (int | Unset): Lowest number of new assets tracked in a single day.
        max_incremental_date (datetime.datetime | Unset): Date (ISO 8601) of the day with the highest number.
        min_incremental_date (datetime.datetime | Unset): Date (ISO 8601) of the day with the lowest number.
    """

    max_incremental_number: int | Unset = UNSET
    min_incremental_number: int | Unset = UNSET
    max_incremental_date: datetime.datetime | Unset = UNSET
    min_incremental_date: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_incremental_number = self.max_incremental_number

        min_incremental_number = self.min_incremental_number

        max_incremental_date: str | Unset = UNSET
        if not isinstance(self.max_incremental_date, Unset):
            max_incremental_date = self.max_incremental_date.isoformat()

        min_incremental_date: str | Unset = UNSET
        if not isinstance(self.min_incremental_date, Unset):
            min_incremental_date = self.min_incremental_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_incremental_number is not UNSET:
            field_dict["maxIncrementalNumber"] = max_incremental_number
        if min_incremental_number is not UNSET:
            field_dict["minIncrementalNumber"] = min_incremental_number
        if max_incremental_date is not UNSET:
            field_dict["maxIncrementalDate"] = max_incremental_date
        if min_incremental_date is not UNSET:
            field_dict["minIncrementalDate"] = min_incremental_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_incremental_number = d.pop("maxIncrementalNumber", UNSET)

        min_incremental_number = d.pop("minIncrementalNumber", UNSET)

        _max_incremental_date = d.pop("maxIncrementalDate", UNSET)
        max_incremental_date: datetime.datetime | Unset
        if isinstance(_max_incremental_date, Unset):
            max_incremental_date = UNSET
        else:
            max_incremental_date = isoparse(_max_incremental_date)

        _min_incremental_date = d.pop("minIncrementalDate", UNSET)
        min_incremental_date: datetime.datetime | Unset
        if isinstance(_min_incremental_date, Unset):
            min_incremental_date = UNSET
        else:
            min_incremental_date = isoparse(_min_incremental_date)

        global_metrics_quotes_latest_results_object_tracked_yearly_number = cls(
            max_incremental_number=max_incremental_number,
            min_incremental_number=min_incremental_number,
            max_incremental_date=max_incremental_date,
            min_incremental_date=min_incremental_date,
        )

        global_metrics_quotes_latest_results_object_tracked_yearly_number.additional_properties = d
        return global_metrics_quotes_latest_results_object_tracked_yearly_number

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
