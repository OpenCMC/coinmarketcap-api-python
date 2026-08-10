from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.security_scan_3_rd_result import SecurityScan3RdResult
    from ..models.security_scan_aggregated_result import SecurityScanAggregatedResult


T = TypeVar("T", bound="SecurityScanResult")


@_attrs_define
class SecurityScanResult:
    """Security scan by Go+.


    All infomation and data relating to contract detection are based on public third party information. CoinMarketCap
    does not confirm or verify the accuracy or timeliness of such information and data.

    CoinMarketCap shall have no responsibility or liability for the accuracy of data, nor have the duty to review,
    confirm, verify or otherwise perform any inquiry or investigation as to the completeness, accuracy, sufficiency,
    integrity, reliability or timeliness of any such information or data provided.

    Only returned if passed in aux.

        Attributes:
            third_party (SecurityScan3RdResult | Unset):
            aggregated (SecurityScanAggregatedResult | Unset):
    """

    third_party: SecurityScan3RdResult | Unset = UNSET
    aggregated: SecurityScanAggregatedResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        third_party: dict[str, Any] | Unset = UNSET
        if not isinstance(self.third_party, Unset):
            third_party = self.third_party.to_dict()

        aggregated: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aggregated, Unset):
            aggregated = self.aggregated.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if third_party is not UNSET:
            field_dict["third_party"] = third_party
        if aggregated is not UNSET:
            field_dict["aggregated"] = aggregated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.security_scan_3_rd_result import SecurityScan3RdResult
        from ..models.security_scan_aggregated_result import SecurityScanAggregatedResult

        d = dict(src_dict)
        _third_party = d.pop("third_party", UNSET)
        third_party: SecurityScan3RdResult | Unset
        if isinstance(_third_party, Unset):
            third_party = UNSET
        else:
            third_party = SecurityScan3RdResult.from_dict(_third_party)

        _aggregated = d.pop("aggregated", UNSET)
        aggregated: SecurityScanAggregatedResult | Unset
        if isinstance(_aggregated, Unset):
            aggregated = UNSET
        else:
            aggregated = SecurityScanAggregatedResult.from_dict(_aggregated)

        security_scan_result = cls(
            third_party=third_party,
            aggregated=aggregated,
        )

        security_scan_result.additional_properties = d
        return security_scan_result

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
