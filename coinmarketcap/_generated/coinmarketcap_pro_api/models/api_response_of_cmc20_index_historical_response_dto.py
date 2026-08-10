from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cmc20_index_historical_dto import CMC20IndexHistoricalDTO
    from ..models.pro_api_response_status import ProApiResponseStatus


T = TypeVar("T", bound="ApiResponseOfCMC20IndexHistoricalResponseDTO")


@_attrs_define
class ApiResponseOfCMC20IndexHistoricalResponseDTO:
    """
    Attributes:
        data (list[CMC20IndexHistoricalDTO] | Unset):
        status (ProApiResponseStatus | Unset):
    """

    data: list[CMC20IndexHistoricalDTO] | Unset = UNSET
    status: ProApiResponseStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for componentsschemas_cmc20_index_historical_dps_dto_item_data in self.data:
                componentsschemas_cmc20_index_historical_dps_dto_item = (
                    componentsschemas_cmc20_index_historical_dps_dto_item_data.to_dict()
                )
                data.append(componentsschemas_cmc20_index_historical_dps_dto_item)

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cmc20_index_historical_dto import CMC20IndexHistoricalDTO
        from ..models.pro_api_response_status import ProApiResponseStatus

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[CMC20IndexHistoricalDTO] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for componentsschemas_cmc20_index_historical_dps_dto_item_data in _data:
                componentsschemas_cmc20_index_historical_dps_dto_item = CMC20IndexHistoricalDTO.from_dict(
                    componentsschemas_cmc20_index_historical_dps_dto_item_data
                )

                data.append(componentsschemas_cmc20_index_historical_dps_dto_item)

        _status = d.pop("status", UNSET)
        status: ProApiResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ProApiResponseStatus.from_dict(_status)

        api_response_of_cmc20_index_historical_response_dto = cls(
            data=data,
            status=status,
        )

        api_response_of_cmc20_index_historical_response_dto.additional_properties = d
        return api_response_of_cmc20_index_historical_response_dto

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
