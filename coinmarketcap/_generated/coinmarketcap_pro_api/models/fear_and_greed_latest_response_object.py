from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FearAndGreedLatestResponseObject")


@_attrs_define
class FearAndGreedLatestResponseObject:
    """The latest CMC Fear and Greed value.

    Example:
        {'value': 40, 'value_classification': 'Neutral', 'update_time': '2024-09-19T02:54:56.017Z'}

    Attributes:
        value (int): The value of CMC Fear and Greed.

            When the value is closer to 0, the market is in Extreme Fear, and investors have over-sold irrationally.

            When the value is closer to 100, the market is in Extreme Greed, indicating a likely market correction.
        value_classification (str): The value classication of CMC Fear and Greed.

            1 ≤ x < 20: Extreme Fear
            20 ≤ x < 40: Fear
            40 ≤ x < 60: Neutral
            60 ≤ x < 80: Greed
            80 ≤ x ≤ 100: Extreme Greed
        update_time (str): Timestamp (ISO 8601) of the last time this record was updated.
    """

    value: int
    value_classification: str
    update_time: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        value_classification = self.value_classification

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "value_classification": value_classification,
                "update_time": update_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        value_classification = d.pop("value_classification")

        update_time = d.pop("update_time")

        fear_and_greed_latest_response_object = cls(
            value=value,
            value_classification=value_classification,
            update_time=update_time,
        )

        fear_and_greed_latest_response_object.additional_properties = d
        return fear_and_greed_latest_response_object

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
