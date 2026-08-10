from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NextUnlockedDetailDTO")


@_attrs_define
class NextUnlockedDetailDTO:
    """Timestamp (ISO 8601) of when this was last updated.

    Attributes:
        allocation_name (str | Unset): The name of the allocation.
        vesting_type (str | Unset): The type of vesting schedule. One of these 4:

            Cliff = single event where some tokens are released.
            Linear = when the same amount of tokens is released with a certain frequency until a certain date.
            Inflationary = when an increasing amount of tokens is released with a certain rate and frequency until a certain
            date.
            Deflationary = when a decreasing amount of tokens is released with a certain rate and frequency until a certain
            date.
        token_amount (float | Unset): The amount of token that will be unlocked in terms of your specified currency.
            Only USD is supported at the moment.
        token_amount_by_base_asset (float | Unset): The amount of token that will be unlocked.
    """

    allocation_name: str | Unset = UNSET
    vesting_type: str | Unset = UNSET
    token_amount: float | Unset = UNSET
    token_amount_by_base_asset: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allocation_name = self.allocation_name

        vesting_type = self.vesting_type

        token_amount = self.token_amount

        token_amount_by_base_asset = self.token_amount_by_base_asset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocation_name is not UNSET:
            field_dict["allocation_name"] = allocation_name
        if vesting_type is not UNSET:
            field_dict["vesting_type"] = vesting_type
        if token_amount is not UNSET:
            field_dict["token_amount"] = token_amount
        if token_amount_by_base_asset is not UNSET:
            field_dict["token_amount_by_base_asset"] = token_amount_by_base_asset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allocation_name = d.pop("allocation_name", UNSET)

        vesting_type = d.pop("vesting_type", UNSET)

        token_amount = d.pop("token_amount", UNSET)

        token_amount_by_base_asset = d.pop("token_amount_by_base_asset", UNSET)

        next_unlocked_detail_dto = cls(
            allocation_name=allocation_name,
            vesting_type=vesting_type,
            token_amount=token_amount,
            token_amount_by_base_asset=token_amount_by_base_asset,
        )

        next_unlocked_detail_dto.additional_properties = d
        return next_unlocked_detail_dto

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
