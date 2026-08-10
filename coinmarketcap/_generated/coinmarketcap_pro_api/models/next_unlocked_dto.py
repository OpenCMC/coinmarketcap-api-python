from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NextUnlockedDTO")


@_attrs_define
class NextUnlockedDTO:
    """The breakdown of the next token unlock.

    Attributes:
        date (str | Unset): Timestamp (ISO 8601) of when the next token unlock is.
        token_amount (float | Unset): The amount of token that will be unlocked in terms of your specified currency.
            Only USD is supported at the moment.
        token_amount_by_base_asset (float | Unset): The amount of tokens that will be unlocked.
        token_amount_percentage (float | Unset): The percentage of the tokens that will be unlocked.
    """

    date: str | Unset = UNSET
    token_amount: float | Unset = UNSET
    token_amount_by_base_asset: float | Unset = UNSET
    token_amount_percentage: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        token_amount = self.token_amount

        token_amount_by_base_asset = self.token_amount_by_base_asset

        token_amount_percentage = self.token_amount_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if token_amount is not UNSET:
            field_dict["token_amount"] = token_amount
        if token_amount_by_base_asset is not UNSET:
            field_dict["token_amount_by_base_asset"] = token_amount_by_base_asset
        if token_amount_percentage is not UNSET:
            field_dict["token_amount_percentage"] = token_amount_percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        token_amount = d.pop("token_amount", UNSET)

        token_amount_by_base_asset = d.pop("token_amount_by_base_asset", UNSET)

        token_amount_percentage = d.pop("token_amount_percentage", UNSET)

        next_unlocked_dto = cls(
            date=date,
            token_amount=token_amount,
            token_amount_by_base_asset=token_amount_by_base_asset,
            token_amount_percentage=token_amount_percentage,
        )

        next_unlocked_dto.additional_properties = d
        return next_unlocked_dto

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
