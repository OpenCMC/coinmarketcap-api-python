from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TheCryptocurrencyOfTheHoldingsInTheWallet")


@_attrs_define
class TheCryptocurrencyOfTheHoldingsInTheWallet:
    """
    Attributes:
        crypto_id (int | Unset): The CoinMarketCap ID for the coin/token used for this wallet Example: 1027.
        symbol (str | Unset): The symbol for the coin/token used for this wallet Example: ETH.
        name (str | Unset): The name for the coin/token used for this wallet Example: Ethereum.
        price_usd (float | Unset): The price in USD for 1 coin/token Example: 1200.055.
    """

    crypto_id: int | Unset = UNSET
    symbol: str | Unset = UNSET
    name: str | Unset = UNSET
    price_usd: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crypto_id = self.crypto_id

        symbol = self.symbol

        name = self.name

        price_usd = self.price_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crypto_id is not UNSET:
            field_dict["crypto_id"] = crypto_id
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if name is not UNSET:
            field_dict["name"] = name
        if price_usd is not UNSET:
            field_dict["price_usd"] = price_usd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        crypto_id = d.pop("crypto_id", UNSET)

        symbol = d.pop("symbol", UNSET)

        name = d.pop("name", UNSET)

        price_usd = d.pop("price_usd", UNSET)

        the_cryptocurrency_of_the_holdings_in_the_wallet = cls(
            crypto_id=crypto_id,
            symbol=symbol,
            name=name,
            price_usd=price_usd,
        )

        the_cryptocurrency_of_the_holdings_in_the_wallet.additional_properties = d
        return the_cryptocurrency_of_the_holdings_in_the_wallet

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
