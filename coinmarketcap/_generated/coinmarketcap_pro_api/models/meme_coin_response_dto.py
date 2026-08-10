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
        new_creations (MemeCoinResultDTO | Unset): List of meme coins that have graduated
        about_graduates (MemeCoinResultDTO | Unset): List of meme coins that have graduated
        graduates (MemeCoinResultDTO | Unset): List of meme coins that have graduated
    """

    new_creations: MemeCoinResultDTO | Unset = UNSET
    about_graduates: MemeCoinResultDTO | Unset = UNSET
    graduates: MemeCoinResultDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_creations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_creations, Unset):
            new_creations = self.new_creations.to_dict()

        about_graduates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.about_graduates, Unset):
            about_graduates = self.about_graduates.to_dict()

        graduates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.graduates, Unset):
            graduates = self.graduates.to_dict()

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
        new_creations: MemeCoinResultDTO | Unset
        if isinstance(_new_creations, Unset):
            new_creations = UNSET
        else:
            new_creations = MemeCoinResultDTO.from_dict(_new_creations)

        _about_graduates = d.pop("aboutGraduates", UNSET)
        about_graduates: MemeCoinResultDTO | Unset
        if isinstance(_about_graduates, Unset):
            about_graduates = UNSET
        else:
            about_graduates = MemeCoinResultDTO.from_dict(_about_graduates)

        _graduates = d.pop("graduates", UNSET)
        graduates: MemeCoinResultDTO | Unset
        if isinstance(_graduates, Unset):
            graduates = UNSET
        else:
            graduates = MemeCoinResultDTO.from_dict(_graduates)

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
