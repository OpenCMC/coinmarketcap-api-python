from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexDetailDTO")


@_attrs_define
class IndexDetailDTO:
    """
    Attributes:
        id (int | Unset): The unique CoinMarketCap ID for this cryptocurrency.
        name (str | Unset): The name of this cryptocurrency.
        symbol (str | Unset): The ticker symbol for this cryptocurrency.
        url (str | Unset): The URL of the detail page on CoinMarketCap for this cryptocurrency.
        weight (float | Unset): The relative proportion of this constituent within the index expressed as a percentage.
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    symbol: str | Unset = UNSET
    url: str | Unset = UNSET
    weight: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        symbol = self.symbol

        url = self.url

        weight = self.weight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if url is not UNSET:
            field_dict["url"] = url
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        symbol = d.pop("symbol", UNSET)

        url = d.pop("url", UNSET)

        weight = d.pop("weight", UNSET)

        index_detail_dto = cls(
            id=id,
            name=name,
            symbol=symbol,
            url=url,
            weight=weight,
        )

        index_detail_dto.additional_properties = d
        return index_detail_dto

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
