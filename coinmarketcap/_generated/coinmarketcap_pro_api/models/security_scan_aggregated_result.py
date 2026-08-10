from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SecurityScanAggregatedResult")


@_attrs_define
class SecurityScanAggregatedResult:
    """
    Attributes:
        contract_verified (bool | Unset):
        honeypot (bool | Unset):
    """

    contract_verified: bool | Unset = UNSET
    honeypot: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contract_verified = self.contract_verified

        honeypot = self.honeypot

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contract_verified is not UNSET:
            field_dict["contract_verified"] = contract_verified
        if honeypot is not UNSET:
            field_dict["honeypot"] = honeypot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contract_verified = d.pop("contract_verified", UNSET)

        honeypot = d.pop("honeypot", UNSET)

        security_scan_aggregated_result = cls(
            contract_verified=contract_verified,
            honeypot=honeypot,
        )

        security_scan_aggregated_result.additional_properties = d
        return security_scan_aggregated_result

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
