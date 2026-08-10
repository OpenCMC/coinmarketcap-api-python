from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_result_dto import SearchResultDTO


T = TypeVar("T", bound="SearchResponseDTO")


@_attrs_define
class SearchResponseDTO:
    """
    Attributes:
        total (int | Unset):
        tks (list[SearchResultDTO] | Unset):
    """

    total: int | Unset = UNSET
    tks: list[SearchResultDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        tks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tks, Unset):
            tks = []
            for tks_item_data in self.tks:
                tks_item = tks_item_data.to_dict()
                tks.append(tks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if tks is not UNSET:
            field_dict["tks"] = tks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_result_dto import SearchResultDTO

        d = dict(src_dict)
        total = d.pop("total", UNSET)

        _tks = d.pop("tks", UNSET)
        tks: list[SearchResultDTO] | Unset = UNSET
        if _tks is not UNSET:
            tks = []
            for tks_item_data in _tks:
                tks_item = SearchResultDTO.from_dict(tks_item_data)

                tks.append(tks_item)

        search_response_dto = cls(
            total=total,
            tks=tks,
        )

        search_response_dto.additional_properties = d
        return search_response_dto

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
