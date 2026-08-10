from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.index_detail_dto import IndexDetailDTO


T = TypeVar("T", bound="IndexHistoricalDTO")


@_attrs_define
class IndexHistoricalDTO:
    """
    Attributes:
        constituents (list[IndexDetailDTO] | Unset): Array detailing the list of constituents and their weightage.
        update_time (str | Unset): Timestamp (ISO 8601) of the time this record was updated.
        value (float | Unset): Value of CoinMarketCap 100 Index.
    """

    constituents: list[IndexDetailDTO] | Unset = UNSET
    update_time: str | Unset = UNSET
    value: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constituents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.constituents, Unset):
            constituents = []
            for constituents_item_data in self.constituents:
                constituents_item = constituents_item_data.to_dict()
                constituents.append(constituents_item)

        update_time = self.update_time

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if constituents is not UNSET:
            field_dict["constituents"] = constituents
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.index_detail_dto import IndexDetailDTO

        d = dict(src_dict)
        _constituents = d.pop("constituents", UNSET)
        constituents: list[IndexDetailDTO] | Unset = UNSET
        if _constituents is not UNSET:
            constituents = []
            for constituents_item_data in _constituents:
                constituents_item = IndexDetailDTO.from_dict(constituents_item_data)

                constituents.append(constituents_item)

        update_time = d.pop("update_time", UNSET)

        value = d.pop("value", UNSET)

        index_historical_dto = cls(
            constituents=constituents,
            update_time=update_time,
            value=value,
        )

        index_historical_dto.additional_properties = d
        return index_historical_dto

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
