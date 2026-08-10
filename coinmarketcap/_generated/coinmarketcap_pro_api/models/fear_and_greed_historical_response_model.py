from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.fear_and_greed_historical_fear_and_greed_object import FearAndGreedHistoricalFearAndGreedObject


T = TypeVar("T", bound="FearAndGreedHistoricalResponseModel")


@_attrs_define
class FearAndGreedHistoricalResponseModel:
    """
    Attributes:
        data (list[FearAndGreedHistoricalFearAndGreedObject]): Fear and Greed Historical. Example: [{'timestamp':
            '1726617600', 'value': 38, 'value_classification': 'Fear'}, {'timestamp': '1726531200', 'value': 34,
            'value_classification': 'Fear'}, {'timestamp': '1726444800', 'value': 36, 'value_classification': 'Fear'},
            {'timestamp': '1726358400', 'value': 38, 'value_classification': 'Fear'}, {'timestamp': '1726272000', 'value':
            38, 'value_classification': 'Fear'}].
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: list[FearAndGreedHistoricalFearAndGreedObject]
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for componentsschemas_fear_and_greed_historical_results_map_item_data in self.data:
            componentsschemas_fear_and_greed_historical_results_map_item = (
                componentsschemas_fear_and_greed_historical_results_map_item_data.to_dict()
            )
            data.append(componentsschemas_fear_and_greed_historical_results_map_item)

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_status_object import APIStatusObject
        from ..models.fear_and_greed_historical_fear_and_greed_object import FearAndGreedHistoricalFearAndGreedObject

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for componentsschemas_fear_and_greed_historical_results_map_item_data in _data:
            componentsschemas_fear_and_greed_historical_results_map_item = (
                FearAndGreedHistoricalFearAndGreedObject.from_dict(
                    componentsschemas_fear_and_greed_historical_results_map_item_data
                )
            )

            data.append(componentsschemas_fear_and_greed_historical_results_map_item)

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        fear_and_greed_historical_response_model = cls(
            data=data,
            status=status,
        )

        fear_and_greed_historical_response_model.additional_properties = d
        return fear_and_greed_historical_response_model

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
