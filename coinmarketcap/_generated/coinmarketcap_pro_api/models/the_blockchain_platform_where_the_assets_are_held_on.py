from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TheBlockchainPlatformWhereTheAssetsAreHeldOn")


@_attrs_define
class TheBlockchainPlatformWhereTheAssetsAreHeldOn:
    """
    Attributes:
        crypto_id (int | Unset): The CoinMarketCap ID for the blockchain platform where the assets are held on Example:
            1027.
        symbol (str | Unset): The symbol for the blockchain platform where the assets are held on Example: ETH.
        name (str | Unset): The name for the blockchain platform where the assets are held on Example: Ethereum.
    """

    crypto_id: int | Unset = UNSET
    symbol: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crypto_id = self.crypto_id

        symbol = self.symbol

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crypto_id is not UNSET:
            field_dict["crypto_id"] = crypto_id
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        crypto_id = d.pop("crypto_id", UNSET)

        symbol = d.pop("symbol", UNSET)

        name = d.pop("name", UNSET)

        the_blockchain_platform_where_the_assets_are_held_on = cls(
            crypto_id=crypto_id,
            symbol=symbol,
            name=name,
        )

        the_blockchain_platform_where_the_assets_are_held_on.additional_properties = d
        return the_blockchain_platform_where_the_assets_are_held_on

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
