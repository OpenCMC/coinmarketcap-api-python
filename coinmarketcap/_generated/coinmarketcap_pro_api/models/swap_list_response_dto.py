from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trade_history_dto import TradeHistoryDTO


T = TypeVar("T", bound="SwapListResponseDTO")


@_attrs_define
class SwapListResponseDTO:
    """Swap list response data

    Attributes:
        swaps (list[TradeHistoryDTO] | Unset): List of swap transactions
        last_id (str | Unset): Last ID for pagination
    """

    swaps: list[TradeHistoryDTO] | Unset = UNSET
    last_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        swaps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.swaps, Unset):
            swaps = []
            for swaps_item_data in self.swaps:
                swaps_item = swaps_item_data.to_dict()
                swaps.append(swaps_item)

        last_id = self.last_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if swaps is not UNSET:
            field_dict["swaps"] = swaps
        if last_id is not UNSET:
            field_dict["lastId"] = last_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trade_history_dto import TradeHistoryDTO

        d = dict(src_dict)
        _swaps = d.pop("swaps", UNSET)
        swaps: list[TradeHistoryDTO] | Unset = UNSET
        if _swaps is not UNSET:
            swaps = []
            for swaps_item_data in _swaps:
                swaps_item = TradeHistoryDTO.from_dict(swaps_item_data)

                swaps.append(swaps_item)

        last_id = d.pop("lastId", UNSET)

        swap_list_response_dto = cls(
            swaps=swaps,
            last_id=last_id,
        )

        swap_list_response_dto.additional_properties = d
        return swap_list_response_dto

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
