from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.plan import Plan
    from ..models.usage import Usage


T = TypeVar("T", bound="AccountInfoResponseObject")


@_attrs_define
class AccountInfoResponseObject:
    """Details about your API key are returned in this object.

    Attributes:
        plan (Plan): Object containing rate limit and daily/monthly credit limit details for your API Key.
        usage (Usage): Object containing live usage details about your API Key.
    """

    plan: Plan
    usage: Usage
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan = self.plan.to_dict()

        usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plan": plan,
                "usage": usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plan import Plan
        from ..models.usage import Usage

        d = dict(src_dict)
        plan = Plan.from_dict(d.pop("plan"))

        usage = Usage.from_dict(d.pop("usage"))

        account_info_response_object = cls(
            plan=plan,
            usage=usage,
        )

        account_info_response_object.additional_properties = d
        return account_info_response_object

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
