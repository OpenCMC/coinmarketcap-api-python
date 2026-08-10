from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PlatformType0")


@_attrs_define
class PlatformType0:
    """Metadata about the parent cryptocurrency platform this cryptocurrency belongs to if it is a token, otherwise null.

    Attributes:
        id (int): The unique CoinMarketCap ID for the parent platform cryptocurrency. Example: 1.
        name (str): The name of the parent platform cryptocurrency. Example: Ethereum.
        symbol (str): The ticker symbol for the parent platform cryptocurrency. Example: ETH.
        slug (str): The web URL friendly shorthand version of the parent platform cryptocurrency name. Example:
            ethereum.
        token_address (str): The token address on the parent platform cryptocurrency. Example:
            0xe41d2489571d322189246dafa5ebde1f4699f498.
    """

    id: int
    name: str
    symbol: str
    slug: str
    token_address: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        symbol = self.symbol

        slug = self.slug

        token_address = self.token_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "symbol": symbol,
                "slug": slug,
                "token_address": token_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        symbol = d.pop("symbol")

        slug = d.pop("slug")

        token_address = d.pop("token_address")

        platform_type_0 = cls(
            id=id,
            name=name,
            symbol=symbol,
            slug=slug,
            token_address=token_address,
        )

        platform_type_0.additional_properties = d
        return platform_type_0

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
