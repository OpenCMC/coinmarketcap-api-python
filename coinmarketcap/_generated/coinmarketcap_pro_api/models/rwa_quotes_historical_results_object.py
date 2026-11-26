from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rwa_quotes_historical_results_object_rwa_assets_item import (
        RWAQuotesHistoricalResultsObjectRwaAssetsItem,
    )


T = TypeVar("T", bound="RWAQuotesHistoricalResultsObject")


@_attrs_define
class RWAQuotesHistoricalResultsObject:
    """Results of your query returned as an object.

    Example:
        {'rwa_assets': [{'name': 'Nvidia Corp', 'symbol': 'NVDA', 'slug': 'nvidia', 'quotes': [{'timestamp':
            '2026-11-17T05:00:00.000Z', 'convert_id': 2781, 'convert_symbol': 'USD', 'average_tokenized_price':
            157.86910203115895, 'tokenized_market_cap': 362817204.1754513, 'tokenized_volume_24h': 321224540.9867724},
            {'timestamp': '2026-11-18T05:00:00.000Z', 'convert_id': 2781, 'convert_symbol': 'USD',
            'average_tokenized_price': 157.31123163132813, 'tokenized_market_cap': 392273916.1191814,
            'tokenized_volume_24h': 473033580.56851166}, {'timestamp': '2026-11-19T05:00:00.000Z', 'convert_id': 2781,
            'convert_symbol': 'USD', 'average_tokenized_price': 152.06295777583813, 'tokenized_market_cap':
            383038734.34426445, 'tokenized_volume_24h': 356263300.4355586}], 'rwa_id': 2, 'asset_type': 'stock', 'rwa_rank':
            4, 'has_tokens': True}]}

    Attributes:
        rwa_assets (list[RWAQuotesHistoricalResultsObjectRwaAssetsItem] | Unset): One object per requested RWA asset, in
            the order requested.
    """

    rwa_assets: list[RWAQuotesHistoricalResultsObjectRwaAssetsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rwa_assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rwa_assets, Unset):
            rwa_assets = []
            for rwa_assets_item_data in self.rwa_assets:
                rwa_assets_item = rwa_assets_item_data.to_dict()
                rwa_assets.append(rwa_assets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rwa_assets is not UNSET:
            field_dict["rwa_assets"] = rwa_assets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rwa_quotes_historical_results_object_rwa_assets_item import (
            RWAQuotesHistoricalResultsObjectRwaAssetsItem,
        )

        d = dict(src_dict)
        _rwa_assets = d.pop("rwa_assets", UNSET)
        rwa_assets: list[RWAQuotesHistoricalResultsObjectRwaAssetsItem] | Unset = UNSET
        if _rwa_assets is not UNSET:
            rwa_assets = []
            for rwa_assets_item_data in _rwa_assets:
                rwa_assets_item = RWAQuotesHistoricalResultsObjectRwaAssetsItem.from_dict(rwa_assets_item_data)

                rwa_assets.append(rwa_assets_item)

        rwa_quotes_historical_results_object = cls(
            rwa_assets=rwa_assets,
        )

        rwa_quotes_historical_results_object.additional_properties = d
        return rwa_quotes_historical_results_object

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
