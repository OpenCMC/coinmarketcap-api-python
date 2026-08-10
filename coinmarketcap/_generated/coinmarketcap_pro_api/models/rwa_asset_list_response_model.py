from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.rwa_asset_list_results_object import RWAAssetListResultsObject


T = TypeVar("T", bound="RWAAssetListResponseModel")


@_attrs_define
class RWAAssetListResponseModel:
    """
    Attributes:
        data (RWAAssetListResultsObject): Results of your query returned as an object. Example: {'total_size': 2,
            'has_more': False, 'rwa_assets': [{'name': 'GOLD', 'symbol': 'GOLD', 'slug': 'gold', 'quotes': [{'symbol':
            'USD', 'crypto_id': 2781, 'average_tokenized_price': 4018.181479970762, 'tokenized_market_cap':
            1884879975.1722481, 'tokenized_volume_24h': 139285845.12748477, 'last_updated': '2026-07-15T10:45:05.000Z'}],
            'rwa_id': 1, 'asset_type': 'commodity', 'rwa_rank': 1, 'has_tokens': True, 'average_tokenized_price':
            4018.181479970762, 'tokenized_market_cap': 1884879975.1722481, 'tokenized_volume_24h': 139285845.12748477,
            'last_updated': '2026-07-15T10:13:26.000Z'}, {'name': 'NVIDIA', 'symbol': 'NVDA', 'slug': 'nvidia', 'quotes':
            [{'symbol': 'USD', 'crypto_id': 2781, 'average_tokenized_price': 211.04769840665475, 'tokenized_market_cap':
            3726091.2870977107, 'tokenized_volume_24h': 7654132.31153204, 'last_updated': '2026-07-15T10:45:05.000Z'}],
            'rwa_id': 2, 'asset_type': 'stock', 'rwa_rank': 2, 'has_tokens': True, 'average_tokenized_price':
            211.04769840665475, 'tokenized_market_cap': 3726091.2870977107, 'tokenized_volume_24h': 7654132.31153204,
            'last_updated': '2026-07-15T10:13:26.000Z'}]}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: RWAAssetListResultsObject
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_status_object import APIStatusObject
        from ..models.rwa_asset_list_results_object import RWAAssetListResultsObject

        d = dict(src_dict)
        data = RWAAssetListResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        rwa_asset_list_response_model = cls(
            data=data,
            status=status,
        )

        rwa_asset_list_response_model.additional_properties = d
        return rwa_asset_list_response_model

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
