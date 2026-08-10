from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenLiquiditySnapshotDTO")


@_attrs_define
class TokenLiquiditySnapshotDTO:
    """
    Attributes:
        snapshot_time (int | Unset):
        liquidity_usd (float | Unset):
        liquidity (float | Unset):
    """

    snapshot_time: int | Unset = UNSET
    liquidity_usd: float | Unset = UNSET
    liquidity: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot_time = self.snapshot_time

        liquidity_usd = self.liquidity_usd

        liquidity = self.liquidity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if snapshot_time is not UNSET:
            field_dict["snapshotTime"] = snapshot_time
        if liquidity_usd is not UNSET:
            field_dict["liquidityUsd"] = liquidity_usd
        if liquidity is not UNSET:
            field_dict["liquidity"] = liquidity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        snapshot_time = d.pop("snapshotTime", UNSET)

        liquidity_usd = d.pop("liquidityUsd", UNSET)

        liquidity = d.pop("liquidity", UNSET)

        token_liquidity_snapshot_dto = cls(
            snapshot_time=snapshot_time,
            liquidity_usd=liquidity_usd,
            liquidity=liquidity,
        )

        token_liquidity_snapshot_dto.additional_properties = d
        return token_liquidity_snapshot_dto

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
