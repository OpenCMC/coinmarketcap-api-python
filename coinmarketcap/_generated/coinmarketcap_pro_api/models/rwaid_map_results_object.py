from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rwaid_map_results_object_rwa_assets_item import RWAIDMapResultsObjectRwaAssetsItem


T = TypeVar("T", bound="RWAIDMapResultsObject")


@_attrs_define
class RWAIDMapResultsObject:
    """Results of your query returned as an object.

    Example:
        {'rwa_assets': [{'name': 'Gold', 'symbol': 'GOLD', 'slug': 'gold', 'rwa_id': 1, 'asset_type': 'commodity',
            'rwa_rank': 1, 'has_tokens': True, 'first_historical_data': '2009-09-27T00:00:00.000Z', 'last_historical_data':
            '2026-07-08T10:29:00.000Z'}, {'name': 'Nvidia Corp', 'symbol': 'NVDA', 'slug': 'nvidia', 'rwa_id': 2,
            'asset_type': 'stock', 'rwa_rank': 2, 'has_tokens': True, 'first_historical_data': '2003-09-07T04:00:00.000Z',
            'last_historical_data': '2026-07-08T10:29:00.000Z'}], 'total_size': 7805, 'has_more': True}

    Attributes:
        rwa_assets (list[RWAIDMapResultsObjectRwaAssetsItem] | Unset): Array of RWA asset map objects, sorted per the
            `sort` parameter.
        total_size (int | Unset): Total number of matching records across all pages. Example: 7805.
        has_more (bool | Unset): `true` if more records exist beyond this page, else `false`. Example: True.
    """

    rwa_assets: list[RWAIDMapResultsObjectRwaAssetsItem] | Unset = UNSET
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
        from ..models.rwaid_map_results_object_rwa_assets_item import RWAIDMapResultsObjectRwaAssetsItem

        d = dict(src_dict)
        _rwa_assets = d.pop("rwa_assets", UNSET)
        rwa_assets: list[RWAIDMapResultsObjectRwaAssetsItem] | Unset = UNSET
        if _rwa_assets is not UNSET:
            rwa_assets = []
            for rwa_assets_item_data in _rwa_assets:
                rwa_assets_item = RWAIDMapResultsObjectRwaAssetsItem.from_dict(rwa_assets_item_data)

                rwa_assets.append(rwa_assets_item)

        total_size = d.pop("total_size", UNSET)

        has_more = d.pop("has_more", UNSET)

        rwaid_map_results_object = cls(
            rwa_assets=rwa_assets,
            total_size=total_size,
            has_more=has_more,
        )

        rwaid_map_results_object.additional_properties = d
        return rwaid_map_results_object

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
