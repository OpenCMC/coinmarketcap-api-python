from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DerivativesMarketPairsListLatestResultsObjectMarketPairsItemExchangeReportedQuotesItem")


@_attrs_define
class DerivativesMarketPairsListLatestResultsObjectMarketPairsItemExchangeReportedQuotesItem:
    """
    Attributes:
        crypto_id (int | Unset): CoinMarketCap ID of the conversion currency. Example: 2781.
        symbol (str | Unset): Symbol of the conversion currency. Example: USD.
        price (float | Unset): Last reported price in the conversion currency. Example: 80521.2.
        volume_24h_base (float | Unset): 24h trade volume denominated in the base currency. Example: 184589.83976729.
        volume_24h_quote (float | Unset): 24h trade volume denominated in the conversion currency. Example:
            14863395405.87.
        open_interest (float | Unset): Open interest in the conversion currency. Example: 5000000.
        index_price (float | Unset): Index price the exchange uses for this contract. Example: 80498.5.
        index_basis (float | Unset): Spread between the contract price and the index price (basis). Example: 0.0023.
        funding_rate (float | Unset): Current funding rate (perpetuals only). Example: 0.0001.
        last_updated (datetime.datetime | Unset): Timestamp (RFC 3339 UTC) of the last update from the exchange.
            Example: 2026-05-15T06:54:18.743Z.
        volume_percentage (float | Unset): Share of this market pair in the exchange's total 24h derivative volume.
            Example: 21.441131937316662.
    """

    crypto_id: int | Unset = UNSET
    symbol: str | Unset = UNSET
    price: float | Unset = UNSET
    volume_24h_base: float | Unset = UNSET
    volume_24h_quote: float | Unset = UNSET
    open_interest: float | Unset = UNSET
    index_price: float | Unset = UNSET
    index_basis: float | Unset = UNSET
    funding_rate: float | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    volume_percentage: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crypto_id = self.crypto_id

        symbol = self.symbol

        price = self.price

        volume_24h_base = self.volume_24h_base

        volume_24h_quote = self.volume_24h_quote

        open_interest = self.open_interest

        index_price = self.index_price

        index_basis = self.index_basis

        funding_rate = self.funding_rate

        last_updated: str | Unset = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        volume_percentage = self.volume_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crypto_id is not UNSET:
            field_dict["crypto_id"] = crypto_id
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if price is not UNSET:
            field_dict["price"] = price
        if volume_24h_base is not UNSET:
            field_dict["volume_24h_base"] = volume_24h_base
        if volume_24h_quote is not UNSET:
            field_dict["volume_24h_quote"] = volume_24h_quote
        if open_interest is not UNSET:
            field_dict["open_interest"] = open_interest
        if index_price is not UNSET:
            field_dict["index_price"] = index_price
        if index_basis is not UNSET:
            field_dict["index_basis"] = index_basis
        if funding_rate is not UNSET:
            field_dict["funding_rate"] = funding_rate
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if volume_percentage is not UNSET:
            field_dict["volume_percentage"] = volume_percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        crypto_id = d.pop("crypto_id", UNSET)

        symbol = d.pop("symbol", UNSET)

        price = d.pop("price", UNSET)

        volume_24h_base = d.pop("volume_24h_base", UNSET)

        volume_24h_quote = d.pop("volume_24h_quote", UNSET)

        open_interest = d.pop("open_interest", UNSET)

        index_price = d.pop("index_price", UNSET)

        index_basis = d.pop("index_basis", UNSET)

        funding_rate = d.pop("funding_rate", UNSET)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        volume_percentage = d.pop("volume_percentage", UNSET)

        derivatives_market_pairs_list_latest_results_object_market_pairs_item_exchange_reported_quotes_item = cls(
            crypto_id=crypto_id,
            symbol=symbol,
            price=price,
            volume_24h_base=volume_24h_base,
            volume_24h_quote=volume_24h_quote,
            open_interest=open_interest,
            index_price=index_price,
            index_basis=index_basis,
            funding_rate=funding_rate,
            last_updated=last_updated,
            volume_percentage=volume_percentage,
        )

        derivatives_market_pairs_list_latest_results_object_market_pairs_item_exchange_reported_quotes_item.additional_properties = d
        return derivatives_market_pairs_list_latest_results_object_market_pairs_item_exchange_reported_quotes_item

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
