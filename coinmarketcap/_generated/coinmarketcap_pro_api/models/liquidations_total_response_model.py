from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.liquidations_total_results_object import LiquidationsTotalResultsObject


T = TypeVar("T", bound="LiquidationsTotalResponseModel")


@_attrs_define
class LiquidationsTotalResponseModel:
    """
    Attributes:
        data (LiquidationsTotalResultsObject): Results of your query returned as an object. Example: {'quotes':
            [{'symbol': 'USD', 'crypto_id': 2781, 'total_liquidations_1h': 4615261.252240025, 'long_liquidations_1h':
            3506917.9880817593, 'short_liquidations_1h': 1108343.264158266, 'total_liquidations_4h': 12888989.407139461,
            'long_liquidations_4h': 9462596.325027341, 'short_liquidations_4h': 3426393.0821121223,
            'total_liquidations_24h': 519760825.61196995, 'long_liquidations_24h': 451643104.8996174,
            'short_liquidations_24h': 68117720.71235262, 'last_updated': '2026-07-28T10:36:00.000Z'}]}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: LiquidationsTotalResultsObject
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
        from ..models.liquidations_total_results_object import LiquidationsTotalResultsObject

        d = dict(src_dict)
        data = LiquidationsTotalResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        liquidations_total_response_model = cls(
            data=data,
            status=status,
        )

        liquidations_total_response_model.additional_properties = d
        return liquidations_total_response_model

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
