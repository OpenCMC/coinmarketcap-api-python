from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BnSecurityExtraInfoDTO")


@_attrs_define
class BnSecurityExtraInfoDTO:
    """Extra security metadata provided by external vendors or on-chain analysis

    Attributes:
        buy_tax (str | Unset): Buy tax
        sell_tax (str | Unset): Sell tax
        is_flagged_by_vendor (bool | Unset): Whether the token is flagged by third-party security vendors
        is_verified (bool | Unset): Whether the token contract is verified Example: True.
        is_reported (bool | Unset): Whether the token has been reported by users or security platforms
        source (str | Unset): Data source of the security information Example: GoPlus.
    """

    buy_tax: str | Unset = UNSET
    sell_tax: str | Unset = UNSET
    is_flagged_by_vendor: bool | Unset = UNSET
    is_verified: bool | Unset = UNSET
    is_reported: bool | Unset = UNSET
    source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buy_tax = self.buy_tax

        sell_tax = self.sell_tax

        is_flagged_by_vendor = self.is_flagged_by_vendor

        is_verified = self.is_verified

        is_reported = self.is_reported

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buy_tax is not UNSET:
            field_dict["buyTax"] = buy_tax
        if sell_tax is not UNSET:
            field_dict["sellTax"] = sell_tax
        if is_flagged_by_vendor is not UNSET:
            field_dict["isFlaggedByVendor"] = is_flagged_by_vendor
        if is_verified is not UNSET:
            field_dict["isVerified"] = is_verified
        if is_reported is not UNSET:
            field_dict["isReported"] = is_reported
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        buy_tax = d.pop("buyTax", UNSET)

        sell_tax = d.pop("sellTax", UNSET)

        is_flagged_by_vendor = d.pop("isFlaggedByVendor", UNSET)

        is_verified = d.pop("isVerified", UNSET)

        is_reported = d.pop("isReported", UNSET)

        source = d.pop("source", UNSET)

        bn_security_extra_info_dto = cls(
            buy_tax=buy_tax,
            sell_tax=sell_tax,
            is_flagged_by_vendor=is_flagged_by_vendor,
            is_verified=is_verified,
            is_reported=is_reported,
            source=source,
        )

        bn_security_extra_info_dto.additional_properties = d
        return bn_security_extra_info_dto

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
