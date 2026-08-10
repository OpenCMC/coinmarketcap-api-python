from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.derivatives_crypto_market_pairs_list_latest_results_object_market_pairs_item_market_pair_base_currency_type import (
    DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBaseCurrencyType,
    check_derivatives_crypto_market_pairs_list_latest_results_object_market_pairs_item_market_pair_base_currency_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBase")


@_attrs_define
class DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBase:
    """Base currency of the market pair.

    Attributes:
        crypto_id (int | Unset): CoinMarketCap ID for the base currency. Example: 1.
        symbol (str | Unset): CoinMarketCap canonical symbol. Example: BTC.
        exchange_symbol (str | Unset): Symbol as listed on the exchange. Example: BTC.
        currency_type (DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBaseCurrencyType |
            Unset): Currency type. Example: cryptocurrency.
    """

    crypto_id: int | Unset = UNSET
    symbol: str | Unset = UNSET
    exchange_symbol: str | Unset = UNSET
    currency_type: (
        DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBaseCurrencyType | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crypto_id = self.crypto_id

        symbol = self.symbol

        exchange_symbol = self.exchange_symbol

        currency_type: str | Unset = UNSET
        if not isinstance(self.currency_type, Unset):
            currency_type = self.currency_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crypto_id is not UNSET:
            field_dict["crypto_id"] = crypto_id
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if exchange_symbol is not UNSET:
            field_dict["exchange_symbol"] = exchange_symbol
        if currency_type is not UNSET:
            field_dict["currency_type"] = currency_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        crypto_id = d.pop("crypto_id", UNSET)

        symbol = d.pop("symbol", UNSET)

        exchange_symbol = d.pop("exchange_symbol", UNSET)

        _currency_type = d.pop("currency_type", UNSET)
        currency_type: (
            DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBaseCurrencyType | Unset
        )
        if isinstance(_currency_type, Unset):
            currency_type = UNSET
        else:
            currency_type = check_derivatives_crypto_market_pairs_list_latest_results_object_market_pairs_item_market_pair_base_currency_type(
                _currency_type
            )

        derivatives_crypto_market_pairs_list_latest_results_object_market_pairs_item_market_pair_base = cls(
            crypto_id=crypto_id,
            symbol=symbol,
            exchange_symbol=exchange_symbol,
            currency_type=currency_type,
        )

        derivatives_crypto_market_pairs_list_latest_results_object_market_pairs_item_market_pair_base.additional_properties = d
        return derivatives_crypto_market_pairs_list_latest_results_object_market_pairs_item_market_pair_base

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
