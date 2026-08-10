from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meme_coin_filter_dto import MemeCoinFilterDTO


T = TypeVar("T", bound="DqueryMemeRequestDTO")


@_attrs_define
class DqueryMemeRequestDTO:
    """Meme coin request

    Attributes:
        protocol (int | Unset): Protocol code
        exclusive (int | Unset): Binance exclusive flag
        limit (int | Unset): Result limit
        new_creation_filter (MemeCoinFilterDTO | Unset): Filter criteria for meme coins
        about_graduate_filter (MemeCoinFilterDTO | Unset): Filter criteria for meme coins
        graduate_filter (MemeCoinFilterDTO | Unset): Filter criteria for meme coins
    """

    protocol: int | Unset = UNSET
    exclusive: int | Unset = UNSET
    limit: int | Unset = UNSET
    new_creation_filter: MemeCoinFilterDTO | Unset = UNSET
    about_graduate_filter: MemeCoinFilterDTO | Unset = UNSET
    graduate_filter: MemeCoinFilterDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        protocol = self.protocol

        exclusive = self.exclusive

        limit = self.limit

        new_creation_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_creation_filter, Unset):
            new_creation_filter = self.new_creation_filter.to_dict()

        about_graduate_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.about_graduate_filter, Unset):
            about_graduate_filter = self.about_graduate_filter.to_dict()

        graduate_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.graduate_filter, Unset):
            graduate_filter = self.graduate_filter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if exclusive is not UNSET:
            field_dict["exclusive"] = exclusive
        if limit is not UNSET:
            field_dict["limit"] = limit
        if new_creation_filter is not UNSET:
            field_dict["newCreationFilter"] = new_creation_filter
        if about_graduate_filter is not UNSET:
            field_dict["aboutGraduateFilter"] = about_graduate_filter
        if graduate_filter is not UNSET:
            field_dict["graduateFilter"] = graduate_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meme_coin_filter_dto import MemeCoinFilterDTO

        d = dict(src_dict)
        protocol = d.pop("protocol", UNSET)

        exclusive = d.pop("exclusive", UNSET)

        limit = d.pop("limit", UNSET)

        _new_creation_filter = d.pop("newCreationFilter", UNSET)
        new_creation_filter: MemeCoinFilterDTO | Unset
        if isinstance(_new_creation_filter, Unset):
            new_creation_filter = UNSET
        else:
            new_creation_filter = MemeCoinFilterDTO.from_dict(_new_creation_filter)

        _about_graduate_filter = d.pop("aboutGraduateFilter", UNSET)
        about_graduate_filter: MemeCoinFilterDTO | Unset
        if isinstance(_about_graduate_filter, Unset):
            about_graduate_filter = UNSET
        else:
            about_graduate_filter = MemeCoinFilterDTO.from_dict(_about_graduate_filter)

        _graduate_filter = d.pop("graduateFilter", UNSET)
        graduate_filter: MemeCoinFilterDTO | Unset
        if isinstance(_graduate_filter, Unset):
            graduate_filter = UNSET
        else:
            graduate_filter = MemeCoinFilterDTO.from_dict(_graduate_filter)

        dquery_meme_request_dto = cls(
            protocol=protocol,
            exclusive=exclusive,
            limit=limit,
            new_creation_filter=new_creation_filter,
            about_graduate_filter=about_graduate_filter,
            graduate_filter=graduate_filter,
        )

        dquery_meme_request_dto.additional_properties = d
        return dquery_meme_request_dto

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
