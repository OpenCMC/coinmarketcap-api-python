from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptocurrencyMultiplierItemObject")


@_attrs_define
class CryptocurrencyMultiplierItemObject:
    """Current ERC-8056 UI multiplier details for a single cryptocurrency.

    Attributes:
        crypto_id (int): CoinMarketCap cryptocurrency ID. Example: 1.
        crypto_slug (str): CoinMarketCap cryptocurrency slug. Example: bitcoin.
        name (str): Cryptocurrency name. Example: Bitcoin.
        symbol (str): Cryptocurrency symbol. Example: BTC.
        multiplier (float): Current effective UI multiplier. Example: 1.
        effective_at (str): Timestamp (ISO 8601) of when the current multiplier became effective. Example:
            2026-05-10T10:30:00Z.
        token_address (str | Unset): On-chain contract address from multiplier history. Omitted when the extra
            multiplier does not match the latest scheduled change, the scheduled change is not yet effective, or the value
            was changed administratively. Example: 0x2260fac5e5542a773aa44fbcfedf7c193bc2c599.
        platform_id (int | Unset): CoinMarketCap platform ID paired with `token_address`. Omitted under the same
            conditions as `token_address`. Example: 14.
    """

    crypto_id: int
    crypto_slug: str
    name: str
    symbol: str
    multiplier: float
    effective_at: str
    token_address: str | Unset = UNSET
    platform_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crypto_id = self.crypto_id

        crypto_slug = self.crypto_slug

        name = self.name

        symbol = self.symbol

        multiplier = self.multiplier

        effective_at = self.effective_at

        token_address = self.token_address

        platform_id = self.platform_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "crypto_id": crypto_id,
                "crypto_slug": crypto_slug,
                "name": name,
                "symbol": symbol,
                "multiplier": multiplier,
                "effective_at": effective_at,
            }
        )
        if token_address is not UNSET:
            field_dict["token_address"] = token_address
        if platform_id is not UNSET:
            field_dict["platform_id"] = platform_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        crypto_id = d.pop("crypto_id")

        crypto_slug = d.pop("crypto_slug")

        name = d.pop("name")

        symbol = d.pop("symbol")

        multiplier = d.pop("multiplier")

        effective_at = d.pop("effective_at")

        token_address = d.pop("token_address", UNSET)

        platform_id = d.pop("platform_id", UNSET)

        cryptocurrency_multiplier_item_object = cls(
            crypto_id=crypto_id,
            crypto_slug=crypto_slug,
            name=name,
            symbol=symbol,
            multiplier=multiplier,
            effective_at=effective_at,
            token_address=token_address,
            platform_id=platform_id,
        )

        cryptocurrency_multiplier_item_object.additional_properties = d
        return cryptocurrency_multiplier_item_object

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
