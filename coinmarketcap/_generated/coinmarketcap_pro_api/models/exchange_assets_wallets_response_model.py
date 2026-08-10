from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.the_blockchain_platform_where_the_assets_are_held_on import (
        TheBlockchainPlatformWhereTheAssetsAreHeldOn,
    )
    from ..models.the_cryptocurrency_of_the_holdings_in_the_wallet import TheCryptocurrencyOfTheHoldingsInTheWallet


T = TypeVar("T", bound="ExchangeAssetsWalletsResponseModel")


@_attrs_define
class ExchangeAssetsWalletsResponseModel:
    """
    Attributes:
        wallet_address (str): The address of the wallet Example: 0x5a52e96bacdabb82fd05763e25335261b270efcb.
        balance (float): The amount of coins/tokens held in this wallet Example: 1000.
        platform (TheBlockchainPlatformWhereTheAssetsAreHeldOn):
        currency (TheCryptocurrencyOfTheHoldingsInTheWallet):
    """

    wallet_address: str
    balance: float
    platform: TheBlockchainPlatformWhereTheAssetsAreHeldOn
    currency: TheCryptocurrencyOfTheHoldingsInTheWallet
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wallet_address = self.wallet_address

        balance = self.balance

        platform = self.platform.to_dict()

        currency = self.currency.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wallet_address": wallet_address,
                "balance": balance,
                "platform": platform,
                "currency": currency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.the_blockchain_platform_where_the_assets_are_held_on import (
            TheBlockchainPlatformWhereTheAssetsAreHeldOn,
        )
        from ..models.the_cryptocurrency_of_the_holdings_in_the_wallet import TheCryptocurrencyOfTheHoldingsInTheWallet

        d = dict(src_dict)
        wallet_address = d.pop("wallet_address")

        balance = d.pop("balance")

        platform = TheBlockchainPlatformWhereTheAssetsAreHeldOn.from_dict(d.pop("platform"))

        currency = TheCryptocurrencyOfTheHoldingsInTheWallet.from_dict(d.pop("currency"))

        exchange_assets_wallets_response_model = cls(
            wallet_address=wallet_address,
            balance=balance,
            platform=platform,
            currency=currency,
        )

        exchange_assets_wallets_response_model.additional_properties = d
        return exchange_assets_wallets_response_model

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
