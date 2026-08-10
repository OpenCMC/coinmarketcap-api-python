from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemExchange")


@_attrs_define
class DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItemExchange:
    """Exchange this market pair is listed on.

    Attributes:
        exchange_id (int | Unset): CoinMarketCap ID for the exchange. Example: 270.
        exchange_name (str | Unset): Exchange name. Example: Binance.
        exchange_slug (str | Unset): Exchange slug. Example: binance.
    """

    exchange_id: int | Unset = UNSET
    exchange_name: str | Unset = UNSET
    exchange_slug: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange_id = self.exchange_id

        exchange_name = self.exchange_name

        exchange_slug = self.exchange_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exchange_id is not UNSET:
            field_dict["exchange_id"] = exchange_id
        if exchange_name is not UNSET:
            field_dict["exchange_name"] = exchange_name
        if exchange_slug is not UNSET:
            field_dict["exchange_slug"] = exchange_slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exchange_id = d.pop("exchange_id", UNSET)

        exchange_name = d.pop("exchange_name", UNSET)

        exchange_slug = d.pop("exchange_slug", UNSET)

        derivatives_crypto_market_pairs_list_latest_results_object_market_pairs_item_exchange = cls(
            exchange_id=exchange_id,
            exchange_name=exchange_name,
            exchange_slug=exchange_slug,
        )

        derivatives_crypto_market_pairs_list_latest_results_object_market_pairs_item_exchange.additional_properties = d
        return derivatives_crypto_market_pairs_list_latest_results_object_market_pairs_item_exchange

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
