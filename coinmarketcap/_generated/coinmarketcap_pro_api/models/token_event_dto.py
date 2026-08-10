from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.next_unlocked_detail_dto import NextUnlockedDetailDTO


T = TypeVar("T", bound="TokenEventDTO")


@_attrs_define
class TokenEventDTO:
    """The breakdown of the next token unlock.

    Attributes:
        time (datetime.datetime | Unset): Timestamp (ISO 8601) of when the next token unlock is.
        allocations (list[NextUnlockedDetailDTO] | Unset): The details of the allocations.
        total_token_amount (float | Unset): The amount of token that will be unlocked in terms of your specified
            currency. Only USD is supported at the moment.
        total_token_amount_by_base_asset (float | Unset): The amount of tokens that will be unlocked.
    """

    time: datetime.datetime | Unset = UNSET
    allocations: list[NextUnlockedDetailDTO] | Unset = UNSET
    total_token_amount: float | Unset = UNSET
    total_token_amount_by_base_asset: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        allocations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allocations, Unset):
            allocations = []
            for allocations_item_data in self.allocations:
                allocations_item = allocations_item_data.to_dict()
                allocations.append(allocations_item)

        total_token_amount = self.total_token_amount

        total_token_amount_by_base_asset = self.total_token_amount_by_base_asset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if allocations is not UNSET:
            field_dict["allocations"] = allocations
        if total_token_amount is not UNSET:
            field_dict["total_token_amount"] = total_token_amount
        if total_token_amount_by_base_asset is not UNSET:
            field_dict["total_token_amount_by_base_asset"] = total_token_amount_by_base_asset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.next_unlocked_detail_dto import NextUnlockedDetailDTO

        d = dict(src_dict)
        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        _allocations = d.pop("allocations", UNSET)
        allocations: list[NextUnlockedDetailDTO] | Unset = UNSET
        if _allocations is not UNSET:
            allocations = []
            for allocations_item_data in _allocations:
                allocations_item = NextUnlockedDetailDTO.from_dict(allocations_item_data)

                allocations.append(allocations_item)

        total_token_amount = d.pop("total_token_amount", UNSET)

        total_token_amount_by_base_asset = d.pop("total_token_amount_by_base_asset", UNSET)

        token_event_dto = cls(
            time=time,
            allocations=allocations,
            total_token_amount=total_token_amount,
            total_token_amount_by_base_asset=total_token_amount_by_base_asset,
        )

        token_event_dto.additional_properties = d
        return token_event_dto

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
