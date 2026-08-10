from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SecurityItem")


@_attrs_define
class SecurityItem:
    """Detailed security item

    Attributes:
        code (str | Unset): Rule code
        risk_code (str | Unset): Risk classification code
        risky_level (str | Unset): Risk level
        is_hit (bool | Unset): Whether the risk was hit Example: True.
        order (int | Unset): Display order
        des (str | Unset): Risk description
        group_id (str | Unset): Group ID for categorization
    """

    code: str | Unset = UNSET
    risk_code: str | Unset = UNSET
    risky_level: str | Unset = UNSET
    is_hit: bool | Unset = UNSET
    order: int | Unset = UNSET
    des: str | Unset = UNSET
    group_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        risk_code = self.risk_code

        risky_level = self.risky_level

        is_hit = self.is_hit

        order = self.order

        des = self.des

        group_id = self.group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if risk_code is not UNSET:
            field_dict["riskCode"] = risk_code
        if risky_level is not UNSET:
            field_dict["riskyLevel"] = risky_level
        if is_hit is not UNSET:
            field_dict["isHit"] = is_hit
        if order is not UNSET:
            field_dict["order"] = order
        if des is not UNSET:
            field_dict["des"] = des
        if group_id is not UNSET:
            field_dict["groupId"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        risk_code = d.pop("riskCode", UNSET)

        risky_level = d.pop("riskyLevel", UNSET)

        is_hit = d.pop("isHit", UNSET)

        order = d.pop("order", UNSET)

        des = d.pop("des", UNSET)

        group_id = d.pop("groupId", UNSET)

        security_item = cls(
            code=code,
            risk_code=risk_code,
            risky_level=risky_level,
            is_hit=is_hit,
            order=order,
            des=des,
            group_id=group_id,
        )

        security_item.additional_properties = d
        return security_item

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
