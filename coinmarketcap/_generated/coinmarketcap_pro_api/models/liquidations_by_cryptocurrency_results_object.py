from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.liquidations_by_cryptocurrency_results_object_cryptocurrencies_item import (
        LiquidationsByCryptocurrencyResultsObjectCryptocurrenciesItem,
    )


T = TypeVar("T", bound="LiquidationsByCryptocurrencyResultsObject")


@_attrs_define
class LiquidationsByCryptocurrencyResultsObject:
    """Results of your query returned as an object.

    Example:
        {'cryptocurrencies': [{'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'quotes': [{'symbol': 'USD',
            'crypto_id': 2781, 'total_liquidations_1h': 409828.32216, 'long_liquidations_1h': 315044.32766,
            'short_liquidations_1h': 94783.9945, 'total_liquidations_4h': 582070.15453, 'long_liquidations_4h':
            406032.34715, 'short_liquidations_4h': 176037.80738, 'total_liquidations_24h': 136257955.96593451,
            'long_liquidations_24h': 121265024.55953953, 'short_liquidations_24h': 14992931.406395, 'last_updated':
            '2026-07-28T10:38:00.000Z'}], 'crypto_id': 1, 'cmc_rank': 1}, {'name': 'Ethereum', 'symbol': 'ETH', 'slug':
            'ethereum', 'quotes': [{'symbol': 'USD', 'crypto_id': 2781, 'total_liquidations_1h': 1024702.24571,
            'long_liquidations_1h': 885316.5256, 'short_liquidations_1h': 139385.72011, 'total_liquidations_4h':
            1195480.61418, 'long_liquidations_4h': 970511.89739, 'short_liquidations_4h': 224968.71679,
            'total_liquidations_24h': 85919188.88445781, 'long_liquidations_24h': 65191933.69474781,
            'short_liquidations_24h': 20727255.18971, 'last_updated': '2026-07-28T10:38:00.000Z'}], 'crypto_id': 1027,
            'cmc_rank': 2}], 'total_size': 805, 'has_more': True}

    Attributes:
        cryptocurrencies (list[LiquidationsByCryptocurrencyResultsObjectCryptocurrenciesItem] | Unset): One object per
            cryptocurrency, ordered by `sort` / `sort_dir`. Never a bare array at `data`.
        total_size (int | Unset): Total number of matching cryptocurrencies across all pages. Placed after the
            `cryptocurrencies[]` array. Example: 805.
        has_more (bool | Unset): `true` if more records exist beyond this page, else `false`. Placed after the
            `cryptocurrencies[]` array. Example: True.
    """

    cryptocurrencies: list[LiquidationsByCryptocurrencyResultsObjectCryptocurrenciesItem] | Unset = UNSET
    total_size: int | Unset = UNSET
    has_more: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cryptocurrencies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cryptocurrencies, Unset):
            cryptocurrencies = []
            for cryptocurrencies_item_data in self.cryptocurrencies:
                cryptocurrencies_item = cryptocurrencies_item_data.to_dict()
                cryptocurrencies.append(cryptocurrencies_item)

        total_size = self.total_size

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cryptocurrencies is not UNSET:
            field_dict["cryptocurrencies"] = cryptocurrencies
        if total_size is not UNSET:
            field_dict["total_size"] = total_size
        if has_more is not UNSET:
            field_dict["has_more"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.liquidations_by_cryptocurrency_results_object_cryptocurrencies_item import (
            LiquidationsByCryptocurrencyResultsObjectCryptocurrenciesItem,
        )

        d = dict(src_dict)
        _cryptocurrencies = d.pop("cryptocurrencies", UNSET)
        cryptocurrencies: list[LiquidationsByCryptocurrencyResultsObjectCryptocurrenciesItem] | Unset = UNSET
        if _cryptocurrencies is not UNSET:
            cryptocurrencies = []
            for cryptocurrencies_item_data in _cryptocurrencies:
                cryptocurrencies_item = LiquidationsByCryptocurrencyResultsObjectCryptocurrenciesItem.from_dict(
                    cryptocurrencies_item_data
                )

                cryptocurrencies.append(cryptocurrencies_item)

        total_size = d.pop("total_size", UNSET)

        has_more = d.pop("has_more", UNSET)

        liquidations_by_cryptocurrency_results_object = cls(
            cryptocurrencies=cryptocurrencies,
            total_size=total_size,
            has_more=has_more,
        )

        liquidations_by_cryptocurrency_results_object.additional_properties = d
        return liquidations_by_cryptocurrency_results_object

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
