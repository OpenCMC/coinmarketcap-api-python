from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.rwa_issuers_list_results_object import RWAIssuersListResultsObject


T = TypeVar("T", bound="RWAIssuersListResponseModel")


@_attrs_define
class RWAIssuersListResponseModel:
    """
    Attributes:
        data (RWAIssuersListResultsObject): Results of your query returned as an object. Example: {'issuers': [{'name':
            'Backed Assets', 'website': 'https://assets.backed.fi/', 'logo': None, 'issuer_id': '6878977dcbbf471de3366e85',
            'num_tokens': 147}, {'name': 'Backpack', 'website': 'https://backpack.exchange', 'logo':
            'https://s2.coinmarketcap.com/static/img/issuer/M7sS2GzR_400x400.png', 'issuer_id': '6a2d54b697c45356b1a634f4',
            'num_tokens': 1}, {'name': 'Bitget Assets', 'website': 'https://www.bitget.com/', 'logo': None, 'issuer_id':
            '68a80be20135f56ec3188cdc', 'num_tokens': 0}], 'total_size': 24, 'has_more': True}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: RWAIssuersListResultsObject
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
        from ..models.rwa_issuers_list_results_object import RWAIssuersListResultsObject

        d = dict(src_dict)
        data = RWAIssuersListResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        rwa_issuers_list_response_model = cls(
            data=data,
            status=status,
        )

        rwa_issuers_list_response_model.additional_properties = d
        return rwa_issuers_list_response_model

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
