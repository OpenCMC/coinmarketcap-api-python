from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DexMultiplierItemObject")


@_attrs_define
class DexMultiplierItemObject:
    """ERC-8056 multiplier information for a single token.

    Attributes:
        platform_id (int): Platform ID. Example: 14.
        platform (str): Platform name. Example: bsc.
        token_address (str): Token address. Example: 0x1234567890abcdef1234567890abcdef12345678.
        name (str): Token name. Example: Dogecoin.
        symbol (str): Token symbol. Example: DOGE.
        multiplier (float): ERC-8056 multiplier value. Example: 0.01.
        effective_at (str): Timestamp (ISO 8601) of when the current multiplier became effective. Example:
            2026-05-19T10:30:00Z.
    """

    platform_id: int
    platform: str
    token_address: str
    name: str
    symbol: str
    multiplier: float
    effective_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform_id = self.platform_id

        platform = self.platform

        token_address = self.token_address

        name = self.name

        symbol = self.symbol

        multiplier = self.multiplier

        effective_at = self.effective_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform_id": platform_id,
                "platform": platform,
                "token_address": token_address,
                "name": name,
                "symbol": symbol,
                "multiplier": multiplier,
                "effective_at": effective_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform_id = d.pop("platform_id")

        platform = d.pop("platform")

        token_address = d.pop("token_address")

        name = d.pop("name")

        symbol = d.pop("symbol")

        multiplier = d.pop("multiplier")

        effective_at = d.pop("effective_at")

        dex_multiplier_item_object = cls(
            platform_id=platform_id,
            platform=platform,
            token_address=token_address,
            name=name,
            symbol=symbol,
            multiplier=multiplier,
            effective_at=effective_at,
        )

        dex_multiplier_item_object.additional_properties = d
        return dex_multiplier_item_object

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
