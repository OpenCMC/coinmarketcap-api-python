from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.rwaid_map_results_object import RWAIDMapResultsObject


T = TypeVar("T", bound="RWAIDMapResponseModel")


@_attrs_define
class RWAIDMapResponseModel:
    """
    Attributes:
        data (RWAIDMapResultsObject): Results of your query returned as an object. Example: {'rwa_assets': [{'name':
            'Gold', 'symbol': 'GOLD', 'slug': 'gold', 'rwa_id': 1, 'asset_type': 'commodity', 'rwa_rank': 1, 'has_tokens':
            True, 'first_historical_data': '2009-09-27T00:00:00.000Z', 'last_historical_data': '2026-07-08T10:29:00.000Z'},
            {'name': 'Nvidia Corp', 'symbol': 'NVDA', 'slug': 'nvidia', 'rwa_id': 2, 'asset_type': 'stock', 'rwa_rank': 2,
            'has_tokens': True, 'first_historical_data': '2003-09-07T04:00:00.000Z', 'last_historical_data':
            '2026-07-08T10:29:00.000Z'}], 'total_size': 7805, 'has_more': True}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: RWAIDMapResultsObject
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

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
        from ..models.rwaid_map_results_object import RWAIDMapResultsObject

        d = dict(src_dict)
        data = RWAIDMapResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        rwaid_map_response_model = cls(
            data=data,
            status=status,
        )

        rwaid_map_response_model.additional_properties = d
        return rwaid_map_response_model

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
