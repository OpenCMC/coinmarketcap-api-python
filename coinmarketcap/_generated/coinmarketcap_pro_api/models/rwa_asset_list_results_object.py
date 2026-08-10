from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rwa_asset_list_results_object_rwa_assets_item import RWAAssetListResultsObjectRwaAssetsItem


T = TypeVar("T", bound="RWAAssetListResultsObject")


@_attrs_define
class RWAAssetListResultsObject:
    """Results of your query returned as an object.

    Example:
        {'total_size': 2, 'has_more': False, 'rwa_assets': [{'name': 'GOLD', 'symbol': 'GOLD', 'slug': 'gold', 'quotes':
            [{'symbol': 'USD', 'crypto_id': 2781, 'average_tokenized_price': 4018.181479970762, 'tokenized_market_cap':
            1884879975.1722481, 'tokenized_volume_24h': 139285845.12748477, 'last_updated': '2026-07-15T10:45:05.000Z'}],
            'rwa_id': 1, 'asset_type': 'commodity', 'rwa_rank': 1, 'has_tokens': True, 'average_tokenized_price':
            4018.181479970762, 'tokenized_market_cap': 1884879975.1722481, 'tokenized_volume_24h': 139285845.12748477,
            'last_updated': '2026-07-15T10:13:26.000Z'}, {'name': 'NVIDIA', 'symbol': 'NVDA', 'slug': 'nvidia', 'quotes':
            [{'symbol': 'USD', 'crypto_id': 2781, 'average_tokenized_price': 211.04769840665475, 'tokenized_market_cap':
            3726091.2870977107, 'tokenized_volume_24h': 7654132.31153204, 'last_updated': '2026-07-15T10:45:05.000Z'}],
            'rwa_id': 2, 'asset_type': 'stock', 'rwa_rank': 2, 'has_tokens': True, 'average_tokenized_price':
            211.04769840665475, 'tokenized_market_cap': 3726091.2870977107, 'tokenized_volume_24h': 7654132.31153204,
            'last_updated': '2026-07-15T10:13:26.000Z'}]}

    Attributes:
        rwa_assets (list[RWAAssetListResultsObjectRwaAssetsItem] | Unset): Array of RWA asset objects (market data),
            sorted per the `sort` parameter.
        total_size (int | Unset): Total number of matching records across all pages. Example: 2.
        has_more (bool | Unset): `true` if more records exist beyond this page, else `false`.
    """

    rwa_assets: list[RWAAssetListResultsObjectRwaAssetsItem] | Unset = UNSET
    total_size: int | Unset = UNSET
    has_more: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rwa_assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rwa_assets, Unset):
            rwa_assets = []
            for rwa_assets_item_data in self.rwa_assets:
                rwa_assets_item = rwa_assets_item_data.to_dict()
                rwa_assets.append(rwa_assets_item)

        total_size = self.total_size

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rwa_assets is not UNSET:
            field_dict["rwa_assets"] = rwa_assets
        if total_size is not UNSET:
            field_dict["total_size"] = total_size
        if has_more is not UNSET:
            field_dict["has_more"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rwa_asset_list_results_object_rwa_assets_item import RWAAssetListResultsObjectRwaAssetsItem

        d = dict(src_dict)
        _rwa_assets = d.pop("rwa_assets", UNSET)
        rwa_assets: list[RWAAssetListResultsObjectRwaAssetsItem] | Unset = UNSET
        if _rwa_assets is not UNSET:
            rwa_assets = []
            for rwa_assets_item_data in _rwa_assets:
                rwa_assets_item = RWAAssetListResultsObjectRwaAssetsItem.from_dict(rwa_assets_item_data)

                rwa_assets.append(rwa_assets_item)

        total_size = d.pop("total_size", UNSET)

        has_more = d.pop("has_more", UNSET)

        rwa_asset_list_results_object = cls(
            rwa_assets=rwa_assets,
            total_size=total_size,
            has_more=has_more,
        )

        rwa_asset_list_results_object.additional_properties = d
        return rwa_asset_list_results_object

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
