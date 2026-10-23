from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meme_coin_result_dto import MemeCoinResultDTO


T = TypeVar("T", bound="MemeCoinResponseDTO")


@_attrs_define
class MemeCoinResponseDTO:
    """Response object containing categorized meme coin results

    Attributes:
        new_creations (list[MemeCoinResultDTO] | Unset):
        about_graduates (list[MemeCoinResultDTO] | Unset):
        graduates (list[MemeCoinResultDTO] | Unset):
    """

    new_creations: list[MemeCoinResultDTO] | Unset = UNSET
    about_graduates: list[MemeCoinResultDTO] | Unset = UNSET
    graduates: list[MemeCoinResultDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_creations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.new_creations, Unset):
            new_creations = []
            for new_creations_item_data in self.new_creations:
                new_creations_item = new_creations_item_data.to_dict()
                new_creations.append(new_creations_item)

        about_graduates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.about_graduates, Unset):
            about_graduates = []
            for about_graduates_item_data in self.about_graduates:
                about_graduates_item = about_graduates_item_data.to_dict()
                about_graduates.append(about_graduates_item)

        graduates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.graduates, Unset):
            graduates = []
            for graduates_item_data in self.graduates:
                graduates_item = graduates_item_data.to_dict()
                graduates.append(graduates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_creations is not UNSET:
            field_dict["newCreations"] = new_creations
        if about_graduates is not UNSET:
            field_dict["aboutGraduates"] = about_graduates
        if graduates is not UNSET:
            field_dict["graduates"] = graduates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meme_coin_result_dto import MemeCoinResultDTO

        d = dict(src_dict)
        _new_creations = d.pop("newCreations", UNSET)
        new_creations: list[MemeCoinResultDTO] | Unset = UNSET
        if _new_creations is not UNSET:
            new_creations = []
            for new_creations_item_data in _new_creations:
                new_creations_item = MemeCoinResultDTO.from_dict(new_creations_item_data)

                new_creations.append(new_creations_item)

        _about_graduates = d.pop("aboutGraduates", UNSET)
        about_graduates: list[MemeCoinResultDTO] | Unset = UNSET
        if _about_graduates is not UNSET:
            about_graduates = []
            for about_graduates_item_data in _about_graduates:
                about_graduates_item = MemeCoinResultDTO.from_dict(about_graduates_item_data)

                about_graduates.append(about_graduates_item)

        _graduates = d.pop("graduates", UNSET)
        graduates: list[MemeCoinResultDTO] | Unset = UNSET
        if _graduates is not UNSET:
            graduates = []
            for graduates_item_data in _graduates:
                graduates_item = MemeCoinResultDTO.from_dict(graduates_item_data)

                graduates.append(graduates_item)

        meme_coin_response_dto = cls(
            new_creations=new_creations,
            about_graduates=about_graduates,
            graduates=graduates,
        )

        meme_coin_response_dto.additional_properties = d
        return meme_coin_response_dto

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
