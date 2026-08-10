from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cmc20_index_detail_dto import CMC20IndexDetailDTO


T = TypeVar("T", bound="CMC20IndexLatestDTO")


@_attrs_define
class CMC20IndexLatestDTO:
    """The latest CoinMarketCap 20 Index value is returned in this object.

    Attributes:
        constituents (list[CMC20IndexDetailDTO] | Unset): Array detailing the list of constituents and their weightage.
        last_update (datetime.date | Unset): Timestamp (ISO 8601) of the last time this record was updated.
        next_update (str | Unset): Timestamp (ISO 8601) of the next time this record will be updated.
        value (float | Unset): Current value of CoinMarketCap 20 Index.
        value_24h_percentage_change (float | Unset): Percentage change of the CoinMarketCap 20 Index over the past 24h.
    """

    constituents: list[CMC20IndexDetailDTO] | Unset = UNSET
    last_update: datetime.date | Unset = UNSET
    next_update: str | Unset = UNSET
    value: float | Unset = UNSET
    value_24h_percentage_change: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constituents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.constituents, Unset):
            constituents = []
            for constituents_item_data in self.constituents:
                constituents_item = constituents_item_data.to_dict()
                constituents.append(constituents_item)

        last_update: str | Unset = UNSET
        if not isinstance(self.last_update, Unset):
            last_update = self.last_update.isoformat()

        next_update = self.next_update

        value = self.value

        value_24h_percentage_change = self.value_24h_percentage_change

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if constituents is not UNSET:
            field_dict["constituents"] = constituents
        if last_update is not UNSET:
            field_dict["last_update"] = last_update
        if next_update is not UNSET:
            field_dict["next_update"] = next_update
        if value is not UNSET:
            field_dict["value"] = value
        if value_24h_percentage_change is not UNSET:
            field_dict["value_24h_percentage_change"] = value_24h_percentage_change

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cmc20_index_detail_dto import CMC20IndexDetailDTO

        d = dict(src_dict)
        _constituents = d.pop("constituents", UNSET)
        constituents: list[CMC20IndexDetailDTO] | Unset = UNSET
        if _constituents is not UNSET:
            constituents = []
            for constituents_item_data in _constituents:
                constituents_item = CMC20IndexDetailDTO.from_dict(constituents_item_data)

                constituents.append(constituents_item)

        _last_update = d.pop("last_update", UNSET)
        last_update: datetime.date | Unset
        if isinstance(_last_update, Unset):
            last_update = UNSET
        else:
            last_update = isoparse(_last_update).date()

        next_update = d.pop("next_update", UNSET)

        value = d.pop("value", UNSET)

        value_24h_percentage_change = d.pop("value_24h_percentage_change", UNSET)

        cmc20_index_latest_dto = cls(
            constituents=constituents,
            last_update=last_update,
            next_update=next_update,
            value=value,
            value_24h_percentage_change=value_24h_percentage_change,
        )

        cmc20_index_latest_dto.additional_properties = d
        return cmc20_index_latest_dto

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
