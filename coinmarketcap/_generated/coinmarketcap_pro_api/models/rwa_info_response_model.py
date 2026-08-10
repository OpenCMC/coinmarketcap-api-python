from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.rwa_info_results_object import RWAInfoResultsObject


T = TypeVar("T", bound="RWAInfoResponseModel")


@_attrs_define
class RWAInfoResponseModel:
    """
    Attributes:
        data (RWAInfoResultsObject): Results of your query returned as an object. Example: {'rwa_assets': [{'name':
            'Gold', 'symbol': 'GOLD', 'slug': 'gold', 'website': None, 'employees': None, 'founded': None, 'industry': None,
            'cik': None, 'about': {'description': 'Gold is a physical commodity and monetary metal that has served as a
            store of value for thousands of years, widely regarded as a safe-haven asset that retains purchasing power
            during inflation and financial instability.', 'logo': None, 'website': None, 'date_added':
            '2025-07-17T06:57:15.000Z'}, 'rwa_id': 1, 'asset_type': 'commodity', 'rwa_rank': 1, 'has_tokens': True,
            'primary_exchange': None}, {'name': 'Nvidia Corp', 'symbol': 'NVDA', 'slug': 'nvidia', 'website':
            'https://www.nvidia.com', 'employees': 36000, 'founded': '1993-04-04', 'industry': 'Semiconductors & Related
            Devices', 'cik': '0001045810', 'about': {'description': 'NVIDIA is a U.S.-based semiconductor and computing
            company specializing in GPUs, AI hardware, and high-performance computing.', 'logo': None, 'website':
            'https://www.nvidia.com', 'date_added': '2025-07-17T06:35:44.000Z'}, 'rwa_id': 2, 'asset_type': 'stock',
            'rwa_rank': 2, 'has_tokens': True, 'primary_exchange': 'Nasdaq'}]}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: RWAInfoResultsObject
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
        from ..models.rwa_info_results_object import RWAInfoResultsObject

        d = dict(src_dict)
        data = RWAInfoResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        rwa_info_response_model = cls(
            data=data,
            status=status,
        )

        rwa_info_response_model.additional_properties = d
        return rwa_info_response_model

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
