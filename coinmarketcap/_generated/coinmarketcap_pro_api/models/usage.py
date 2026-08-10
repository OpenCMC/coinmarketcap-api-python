from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.current_day import CurrentDay
    from ..models.current_minute import CurrentMinute
    from ..models.current_month import CurrentMonth


T = TypeVar("T", bound="Usage")


@_attrs_define
class Usage:
    """Object containing live usage details about your API Key.

    Attributes:
        current_minute (CurrentMinute): Usage stats around the minute based rate limit.
        current_day (CurrentDay): Usage stats around the daily API credit limit.
        current_month (CurrentMonth): Usage stats around the monthly API credit limit.
    """

    current_minute: CurrentMinute
    current_day: CurrentDay
    current_month: CurrentMonth
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_minute = self.current_minute.to_dict()

        current_day = self.current_day.to_dict()

        current_month = self.current_month.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_minute": current_minute,
                "current_day": current_day,
                "current_month": current_month,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.current_day import CurrentDay
        from ..models.current_minute import CurrentMinute
        from ..models.current_month import CurrentMonth

        d = dict(src_dict)
        current_minute = CurrentMinute.from_dict(d.pop("current_minute"))

        current_day = CurrentDay.from_dict(d.pop("current_day"))

        current_month = CurrentMonth.from_dict(d.pop("current_month"))

        usage = cls(
            current_minute=current_minute,
            current_day=current_day,
            current_month=current_month,
        )

        usage.additional_properties = d
        return usage

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
