from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.derivatives_exchanges_list_results_object_exchanges_item_quotes_item import (
        DerivativesExchangesListResultsObjectExchangesItemQuotesItem,
    )


T = TypeVar("T", bound="DerivativesExchangesListResultsObjectExchangesItem")


@_attrs_define
class DerivativesExchangesListResultsObjectExchangesItem:
    """
    Attributes:
        exchange_id (int | Unset): The CoinMarketCap ID for this exchange. Example: 270.
        exchange_name (str | Unset): The name of this exchange. Example: Binance.
        exchange_slug (str | Unset): The slug for this exchange. Example: binance.
        num_market_pairs (int | Unset): Number of active derivative market pairs CoinMarketCap tracks for this exchange.
            Example: 645.
        fiats (list[str] | Unset): Fiat currencies accepted by this exchange.
        traffic_score (float | Unset): CoinMarketCap's traffic score for this exchange. Example: 1000.
        rank (int | Unset): CoinMarketCap derivative-volume rank for this exchange (lower is higher). Example: 1.
        exchange_score (float | Unset): CoinMarketCap's overall exchange score. Example: 7.82345678.
        liquidity_score (float | Unset): CoinMarketCap's liquidity score for this exchange's derivatives markets.
            Example: 9.8028.
        last_updated (datetime.datetime | Unset): Timestamp (RFC 3339 UTC) of the last update for this exchange's
            aggregate stats. Example: 2026-04-21T10:30:00.000Z.
        quotes (list[DerivativesExchangesListResultsObjectExchangesItemQuotesItem] | Unset): Per-conversion-currency
            aggregate quotes, one entry per requested `convert` / `convert_id`.
    """

    exchange_id: int | Unset = UNSET
    exchange_name: str | Unset = UNSET
    exchange_slug: str | Unset = UNSET
    num_market_pairs: int | Unset = UNSET
    fiats: list[str] | Unset = UNSET
    traffic_score: float | Unset = UNSET
    rank: int | Unset = UNSET
    exchange_score: float | Unset = UNSET
    liquidity_score: float | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    quotes: list[DerivativesExchangesListResultsObjectExchangesItemQuotesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange_id = self.exchange_id

        exchange_name = self.exchange_name

        exchange_slug = self.exchange_slug

        num_market_pairs = self.num_market_pairs

        fiats: list[str] | Unset = UNSET
        if not isinstance(self.fiats, Unset):
            fiats = self.fiats

        traffic_score = self.traffic_score

        rank = self.rank

        exchange_score = self.exchange_score

        liquidity_score = self.liquidity_score

        last_updated: str | Unset = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        quotes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quotes, Unset):
            quotes = []
            for quotes_item_data in self.quotes:
                quotes_item = quotes_item_data.to_dict()
                quotes.append(quotes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exchange_id is not UNSET:
            field_dict["exchange_id"] = exchange_id
        if exchange_name is not UNSET:
            field_dict["exchange_name"] = exchange_name
        if exchange_slug is not UNSET:
            field_dict["exchange_slug"] = exchange_slug
        if num_market_pairs is not UNSET:
            field_dict["num_market_pairs"] = num_market_pairs
        if fiats is not UNSET:
            field_dict["fiats"] = fiats
        if traffic_score is not UNSET:
            field_dict["traffic_score"] = traffic_score
        if rank is not UNSET:
            field_dict["rank"] = rank
        if exchange_score is not UNSET:
            field_dict["exchange_score"] = exchange_score
        if liquidity_score is not UNSET:
            field_dict["liquidity_score"] = liquidity_score
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if quotes is not UNSET:
            field_dict["quotes"] = quotes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.derivatives_exchanges_list_results_object_exchanges_item_quotes_item import (
            DerivativesExchangesListResultsObjectExchangesItemQuotesItem,
        )

        d = dict(src_dict)
        exchange_id = d.pop("exchange_id", UNSET)

        exchange_name = d.pop("exchange_name", UNSET)

        exchange_slug = d.pop("exchange_slug", UNSET)

        num_market_pairs = d.pop("num_market_pairs", UNSET)

        fiats = cast(list[str], d.pop("fiats", UNSET))

        traffic_score = d.pop("traffic_score", UNSET)

        rank = d.pop("rank", UNSET)

        exchange_score = d.pop("exchange_score", UNSET)

        liquidity_score = d.pop("liquidity_score", UNSET)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _quotes = d.pop("quotes", UNSET)
        quotes: list[DerivativesExchangesListResultsObjectExchangesItemQuotesItem] | Unset = UNSET
        if _quotes is not UNSET:
            quotes = []
            for quotes_item_data in _quotes:
                quotes_item = DerivativesExchangesListResultsObjectExchangesItemQuotesItem.from_dict(quotes_item_data)

                quotes.append(quotes_item)

        derivatives_exchanges_list_results_object_exchanges_item = cls(
            exchange_id=exchange_id,
            exchange_name=exchange_name,
            exchange_slug=exchange_slug,
            num_market_pairs=num_market_pairs,
            fiats=fiats,
            traffic_score=traffic_score,
            rank=rank,
            exchange_score=exchange_score,
            liquidity_score=liquidity_score,
            last_updated=last_updated,
            quotes=quotes,
        )

        derivatives_exchanges_list_results_object_exchanges_item.additional_properties = d
        return derivatives_exchanges_list_results_object_exchanges_item

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
