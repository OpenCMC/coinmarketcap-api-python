from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.liquidity_change_dto import LiquidityChangeDTO


T = TypeVar("T", bound="LiquidityChangeListResponseDTO")


@_attrs_define
class LiquidityChangeListResponseDTO:
    """Swap list response data

    Attributes:
        last_id (str | Unset): Last ID for pagination
        lcs (list[LiquidityChangeDTO] | Unset): List of liquidity change transactions
        tlu (float | Unset): total liquidity usd value
        lpc (int | Unset): liquidity pool count
    """

    last_id: str | Unset = UNSET
    lcs: list[LiquidityChangeDTO] | Unset = UNSET
    tlu: float | Unset = UNSET
    lpc: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_id = self.last_id

        lcs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lcs, Unset):
            lcs = []
            for lcs_item_data in self.lcs:
                lcs_item = lcs_item_data.to_dict()
                lcs.append(lcs_item)

        tlu = self.tlu

        lpc = self.lpc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_id is not UNSET:
            field_dict["lastId"] = last_id
        if lcs is not UNSET:
            field_dict["lcs"] = lcs
        if tlu is not UNSET:
            field_dict["tlu"] = tlu
        if lpc is not UNSET:
            field_dict["lpc"] = lpc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.liquidity_change_dto import LiquidityChangeDTO

        d = dict(src_dict)
        last_id = d.pop("lastId", UNSET)

        _lcs = d.pop("lcs", UNSET)
        lcs: list[LiquidityChangeDTO] | Unset = UNSET
        if _lcs is not UNSET:
            lcs = []
            for lcs_item_data in _lcs:
                lcs_item = LiquidityChangeDTO.from_dict(lcs_item_data)

                lcs.append(lcs_item)

        tlu = d.pop("tlu", UNSET)

        lpc = d.pop("lpc", UNSET)

        liquidity_change_list_response_dto = cls(
            last_id=last_id,
            lcs=lcs,
            tlu=tlu,
            lpc=lpc,
        )

        liquidity_change_list_response_dto.additional_properties = d
        return liquidity_change_list_response_dto

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
