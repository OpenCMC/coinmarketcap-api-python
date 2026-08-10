from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rwa_market_pairs_results_object_market_pairs_item import RWAMarketPairsResultsObjectMarketPairsItem


T = TypeVar("T", bound="RWAMarketPairsResultsObject")


@_attrs_define
class RWAMarketPairsResultsObject:
    """Results of your query returned as an object.

    Example:
        {'rwa_id': 2, 'name': 'NVIDIA', 'symbol': 'NVDA', 'num_market_pairs': 1, 'market_pairs': [{'exchange':
            {'exchange_id': 270, 'name': 'Binance', 'slug': 'binance'}, 'market_id': 99001, 'market_pair': 'NVDAX/USDT',
            'category': 'spot', 'fee_type': 'percentage', 'market_pair_base': {'crypto_id': 36992, 'symbol': 'NVDAX',
            'exchange_symbol': 'NVDAX', 'currency_type': 'cryptocurrency'}, 'market_pair_quote': {'crypto_id': 825,
            'symbol': 'USDT', 'exchange_symbol': 'USDT', 'currency_type': 'cryptocurrency'}, 'exchange_reported_quotes':
            [{'crypto_id': 2781, 'symbol': 'USD', 'price': 211.33, 'volume_24h_base': 39290.12, 'volume_24h_quote':
            8302814.85, 'last_updated': '2026-07-15T10:45:05.000Z'}], 'quotes': [{'crypto_id': 2781, 'symbol': 'USD',
            'price': 211.33, 'volume_24h': 8302814.85, 'last_updated': '2026-07-15T10:45:05.000Z'}]}], 'total_size': 1,
            'has_more': False}

    Attributes:
        rwa_id (int | Unset): The RWA asset the market pairs belong to. Example: 2.
        name (str | Unset): Asset display name. Example: NVIDIA.
        symbol (str | Unset): Asset symbol / ticker. Example: NVDA.
        num_market_pairs (int | Unset): Total number of active market pairs for the asset. Example: 1.
        market_pairs (list[RWAMarketPairsResultsObjectMarketPairsItem] | Unset): Array of market pair objects.
        total_size (int | Unset): Total number of matching records across all pages. Example: 1.
        has_more (bool | Unset): `true` if more records exist beyond this page, else `false`.
    """

    rwa_id: int | Unset = UNSET
    name: str | Unset = UNSET
    symbol: str | Unset = UNSET
    num_market_pairs: int | Unset = UNSET
    market_pairs: list[RWAMarketPairsResultsObjectMarketPairsItem] | Unset = UNSET
    total_size: int | Unset = UNSET
    has_more: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rwa_id = self.rwa_id

        name = self.name

        symbol = self.symbol

        num_market_pairs = self.num_market_pairs

        market_pairs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.market_pairs, Unset):
            market_pairs = []
            for market_pairs_item_data in self.market_pairs:
                market_pairs_item = market_pairs_item_data.to_dict()
                market_pairs.append(market_pairs_item)

        total_size = self.total_size

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rwa_id is not UNSET:
            field_dict["rwa_id"] = rwa_id
        if name is not UNSET:
            field_dict["name"] = name
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if num_market_pairs is not UNSET:
            field_dict["num_market_pairs"] = num_market_pairs
        if market_pairs is not UNSET:
            field_dict["market_pairs"] = market_pairs
        if total_size is not UNSET:
            field_dict["total_size"] = total_size
        if has_more is not UNSET:
            field_dict["has_more"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rwa_market_pairs_results_object_market_pairs_item import (
            RWAMarketPairsResultsObjectMarketPairsItem,
        )

        d = dict(src_dict)
        rwa_id = d.pop("rwa_id", UNSET)

        name = d.pop("name", UNSET)

        symbol = d.pop("symbol", UNSET)

        num_market_pairs = d.pop("num_market_pairs", UNSET)

        _market_pairs = d.pop("market_pairs", UNSET)
        market_pairs: list[RWAMarketPairsResultsObjectMarketPairsItem] | Unset = UNSET
        if _market_pairs is not UNSET:
            market_pairs = []
            for market_pairs_item_data in _market_pairs:
                market_pairs_item = RWAMarketPairsResultsObjectMarketPairsItem.from_dict(market_pairs_item_data)

                market_pairs.append(market_pairs_item)

        total_size = d.pop("total_size", UNSET)

        has_more = d.pop("has_more", UNSET)

        rwa_market_pairs_results_object = cls(
            rwa_id=rwa_id,
            name=name,
            symbol=symbol,
            num_market_pairs=num_market_pairs,
            market_pairs=market_pairs,
            total_size=total_size,
            has_more=has_more,
        )

        rwa_market_pairs_results_object.additional_properties = d
        return rwa_market_pairs_results_object

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
