from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cmc20_index_latest_dto import CMC20IndexLatestDTO
    from ..models.pro_api_response_status import ProApiResponseStatus


T = TypeVar("T", bound="ApiResponseOfCMC20IndexLatestResponseDTO")


@_attrs_define
class ApiResponseOfCMC20IndexLatestResponseDTO:
    """
    Attributes:
        data (CMC20IndexLatestDTO): The latest CoinMarketCap 20 Index value is returned in this object.
        status (ProApiResponseStatus | Unset):
    """

    data: CMC20IndexLatestDTO
    status: ProApiResponseStatus | Unset = UNSET
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
        from ..models.cmc20_index_latest_dto import CMC20IndexLatestDTO
        from ..models.pro_api_response_status import ProApiResponseStatus

        d = dict(src_dict)
        data = CMC20IndexLatestDTO.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: ProApiResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ProApiResponseStatus.from_dict(_status)

        api_response_of_cmc20_index_latest_response_dto = cls(
            data=data,
            status=status,
        )

        api_response_of_cmc20_index_latest_response_dto.additional_properties = d
        return api_response_of_cmc20_index_latest_response_dto

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
