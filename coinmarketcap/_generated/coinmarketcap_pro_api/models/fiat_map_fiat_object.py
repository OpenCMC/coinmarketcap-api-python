from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FiatMapFiatObject")


@_attrs_define
class FiatMapFiatObject:
    """Fiat object for each result

    Attributes:
        id (int): The unique CoinMarketCap ID for this asset. Example: 2781.
        name (str): The name of this asset. Example: United States Dollar.
        sign (str): The currency sign for this asset. Example: $.
        symbol (str): The ticker symbol for this asset, always in all caps. Example: USD.
    """

    id: int
    name: str
    sign: str
    symbol: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        sign = self.sign

        symbol = self.symbol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "sign": sign,
                "symbol": symbol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        sign = d.pop("sign")

        symbol = d.pop("symbol")

        fiat_map_fiat_object = cls(
            id=id,
            name=name,
            sign=sign,
            symbol=symbol,
        )

        fiat_map_fiat_object.additional_properties = d
        return fiat_map_fiat_object

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
