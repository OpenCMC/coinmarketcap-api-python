from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.airdrop_results_map import AirdropResultsMap
    from ..models.api_status_object import APIStatusObject


T = TypeVar("T", bound="AirdropResponseModel")


@_attrs_define
class AirdropResponseModel:
    """
    Attributes:
        data (AirdropResultsMap): Results of your query returned as an object map. Example: {'1': {'id':
            '60e59b99c8ca1d58514a2322', 'project_name': 'DeRace Airdrop', 'description': 'For 7 days starting from August
            15, 2021, CoinMarketCap will host an Airdrop event...', 'status': 'UPCOMING', 'coin': {'id': 10744, 'name':
            'DeRace', 'slug': 'derace', 'symbol': 'DERC'}, 'start_date': '2021-06-01T22:11:00.000Z', 'end_date':
            '2021-07-01T22:11:00.000Z', 'total_prize': 20000000000, 'winner_count': 1000, 'link':
            'https://coinmarketcap.com/currencies/derace/airdrop/'}}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: AirdropResultsMap
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
        from ..models.airdrop_results_map import AirdropResultsMap
        from ..models.api_status_object import APIStatusObject

        d = dict(src_dict)
        data = AirdropResultsMap.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        airdrop_response_model = cls(
            data=data,
            status=status,
        )

        airdrop_response_model.additional_properties = d
        return airdrop_response_model

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
