from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rwa_info_results_object_rwa_assets_item import RWAInfoResultsObjectRwaAssetsItem


T = TypeVar("T", bound="RWAInfoResultsObject")


@_attrs_define
class RWAInfoResultsObject:
    """Results of your query returned as an object.

    Example:
        {'rwa_assets': [{'name': 'Gold', 'symbol': 'GOLD', 'slug': 'gold', 'website': None, 'employees': None,
            'founded': None, 'industry': None, 'cik': None, 'about': {'description': 'Gold is a physical commodity and
            monetary metal that has served as a store of value for thousands of years, widely regarded as a safe-haven asset
            that retains purchasing power during inflation and financial instability.', 'logo': None, 'website': None,
            'date_added': '2025-07-17T06:57:15.000Z'}, 'rwa_id': 1, 'asset_type': 'commodity', 'rwa_rank': 1, 'has_tokens':
            True, 'primary_exchange': None}, {'name': 'Nvidia Corp', 'symbol': 'NVDA', 'slug': 'nvidia', 'website':
            'https://www.nvidia.com', 'employees': 36000, 'founded': '1993-04-04', 'industry': 'Semiconductors & Related
            Devices', 'cik': '0001045810', 'about': {'description': 'NVIDIA is a U.S.-based semiconductor and computing
            company specializing in GPUs, AI hardware, and high-performance computing.', 'logo': None, 'website':
            'https://www.nvidia.com', 'date_added': '2025-07-17T06:35:44.000Z'}, 'rwa_id': 2, 'asset_type': 'stock',
            'rwa_rank': 2, 'has_tokens': True, 'primary_exchange': 'Nasdaq'}]}

    Attributes:
        rwa_assets (list[RWAInfoResultsObjectRwaAssetsItem] | Unset): Array of static-metadata objects, one per
            requested RWA asset.
    """

    rwa_assets: list[RWAInfoResultsObjectRwaAssetsItem] | Unset = UNSET
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
        from ..models.rwa_info_results_object_rwa_assets_item import RWAInfoResultsObjectRwaAssetsItem

        d = dict(src_dict)
        _rwa_assets = d.pop("rwa_assets", UNSET)
        rwa_assets: list[RWAInfoResultsObjectRwaAssetsItem] | Unset = UNSET
        if _rwa_assets is not UNSET:
            rwa_assets = []
            for rwa_assets_item_data in _rwa_assets:
                rwa_assets_item = RWAInfoResultsObjectRwaAssetsItem.from_dict(rwa_assets_item_data)

                rwa_assets.append(rwa_assets_item)

        rwa_info_results_object = cls(
            rwa_assets=rwa_assets,
        )

        rwa_info_results_object.additional_properties = d
        return rwa_info_results_object

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
