from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.derivatives_market_pairs_list_latest_results_object_market_pairs_item_market_pair_quote_currency_type import (
    DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuoteCurrencyType,
    check_derivatives_market_pairs_list_latest_results_object_market_pairs_item_market_pair_quote_currency_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuote")


@_attrs_define
class DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuote:
    """Quote currency of the market pair.

    Attributes:
        exchange_symbol (str | Unset): Symbol as listed on the exchange. Example: USDT.
        symbol (str | Unset): CoinMarketCap canonical symbol. Example: USDT.
        crypto_id (int | Unset): CoinMarketCap ID for the quote currency. Example: 825.
        currency_type (DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuoteCurrencyType | Unset):
            Currency type. Example: cryptocurrency.
    """

    exchange_symbol: str | Unset = UNSET
    symbol: str | Unset = UNSET
    crypto_id: int | Unset = UNSET
    currency_type: DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuoteCurrencyType | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange_symbol = self.exchange_symbol

        symbol = self.symbol

        crypto_id = self.crypto_id

        currency_type: str | Unset = UNSET
        if not isinstance(self.currency_type, Unset):
            currency_type = self.currency_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exchange_symbol is not UNSET:
            field_dict["exchange_symbol"] = exchange_symbol
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if crypto_id is not UNSET:
            field_dict["crypto_id"] = crypto_id
        if currency_type is not UNSET:
            field_dict["currency_type"] = currency_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exchange_symbol = d.pop("exchange_symbol", UNSET)

        symbol = d.pop("symbol", UNSET)

        crypto_id = d.pop("crypto_id", UNSET)

        _currency_type = d.pop("currency_type", UNSET)
        currency_type: DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuoteCurrencyType | Unset
        if isinstance(_currency_type, Unset):
            currency_type = UNSET
        else:
            currency_type = check_derivatives_market_pairs_list_latest_results_object_market_pairs_item_market_pair_quote_currency_type(
                _currency_type
            )

        derivatives_market_pairs_list_latest_results_object_market_pairs_item_market_pair_quote = cls(
            exchange_symbol=exchange_symbol,
            symbol=symbol,
            crypto_id=crypto_id,
            currency_type=currency_type,
        )

        derivatives_market_pairs_list_latest_results_object_market_pairs_item_market_pair_quote.additional_properties = d
        return derivatives_market_pairs_list_latest_results_object_market_pairs_item_market_pair_quote

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
