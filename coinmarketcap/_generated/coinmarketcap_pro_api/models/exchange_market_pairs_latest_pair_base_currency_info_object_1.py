from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.exchange_market_pairs_latest_pair_base_currency_info_object_1_currency_type import (
    ExchangeMarketPairsLatestPairBaseCurrencyInfoObject1CurrencyType,
    check_exchange_market_pairs_latest_pair_base_currency_info_object_1_currency_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExchangeMarketPairsLatestPairBaseCurrencyInfoObject1")


@_attrs_define
class ExchangeMarketPairsLatestPairBaseCurrencyInfoObject1:
    """Quote (secondary) currency details object for this market pair

    Attributes:
        currency_id (int): The CoinMarketCap ID for the quote (secondary) currency in this market pair. Example: 2781.
        currency_symbol (str): The symbol for the quote (secondary) currency in this market pair. Example: USD.
        exchange_symbol (str): The exchange reported symbol for the quote (secondary) currency in this market pair. In
            most cases this is identical to CoinMarketCap's symbol but it may differ if the exchange uses an outdated or
            contentious symbol that contrasts with the majority of other markets. Example: USD.
        currency_type (ExchangeMarketPairsLatestPairBaseCurrencyInfoObject1CurrencyType): The currency type for the
            quote (secondary) currency in this market pair. Example: fiat.
        currency_name (str | Unset): The name of this cryptocurrency. *This field is only returned if requested through
            the `aux` request parameter.* Example: Bitcoin.
        currency_slug (str | Unset): The web URL friendly shorthand version of this cryptocurrency name. *This field is
            only returned if requested through the `aux` request parameter.* Example: bitcoin.
    """

    currency_id: int
    currency_symbol: str
    exchange_symbol: str
    currency_type: ExchangeMarketPairsLatestPairBaseCurrencyInfoObject1CurrencyType
    currency_name: str | Unset = UNSET
    currency_slug: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_id = self.currency_id

        currency_symbol = self.currency_symbol

        exchange_symbol = self.exchange_symbol

        currency_type: str = self.currency_type

        currency_name = self.currency_name

        currency_slug = self.currency_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency_id": currency_id,
                "currency_symbol": currency_symbol,
                "exchange_symbol": exchange_symbol,
                "currency_type": currency_type,
            }
        )
        if currency_name is not UNSET:
            field_dict["currency_name"] = currency_name
        if currency_slug is not UNSET:
            field_dict["currency_slug"] = currency_slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency_id = d.pop("currency_id")

        currency_symbol = d.pop("currency_symbol")

        exchange_symbol = d.pop("exchange_symbol")

        currency_type = check_exchange_market_pairs_latest_pair_base_currency_info_object_1_currency_type(
            d.pop("currency_type")
        )

        currency_name = d.pop("currency_name", UNSET)

        currency_slug = d.pop("currency_slug", UNSET)

        exchange_market_pairs_latest_pair_base_currency_info_object_1 = cls(
            currency_id=currency_id,
            currency_symbol=currency_symbol,
            exchange_symbol=exchange_symbol,
            currency_type=currency_type,
            currency_name=currency_name,
            currency_slug=currency_slug,
        )

        exchange_market_pairs_latest_pair_base_currency_info_object_1.additional_properties = d
        return exchange_market_pairs_latest_pair_base_currency_info_object_1

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
