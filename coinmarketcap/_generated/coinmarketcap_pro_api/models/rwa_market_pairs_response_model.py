from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.rwa_market_pairs_results_object import RWAMarketPairsResultsObject


T = TypeVar("T", bound="RWAMarketPairsResponseModel")


@_attrs_define
class RWAMarketPairsResponseModel:
    """
    Attributes:
        data (RWAMarketPairsResultsObject): Results of your query returned as an object. Example: {'rwa_id': 2, 'name':
            'NVIDIA', 'symbol': 'NVDA', 'num_market_pairs': 1, 'market_pairs': [{'exchange': {'exchange_id': 270, 'name':
            'Binance', 'slug': 'binance'}, 'market_id': 99001, 'market_pair': 'NVDAX/USDT', 'category': 'spot', 'fee_type':
            'percentage', 'market_pair_base': {'crypto_id': 36992, 'symbol': 'NVDAX', 'exchange_symbol': 'NVDAX',
            'currency_type': 'cryptocurrency'}, 'market_pair_quote': {'crypto_id': 825, 'symbol': 'USDT', 'exchange_symbol':
            'USDT', 'currency_type': 'cryptocurrency'}, 'exchange_reported_quotes': [{'crypto_id': 2781, 'symbol': 'USD',
            'price': 211.33, 'volume_24h_base': 39290.12, 'volume_24h_quote': 8302814.85, 'last_updated':
            '2026-07-15T10:45:05.000Z'}], 'quotes': [{'crypto_id': 2781, 'symbol': 'USD', 'price': 211.33, 'volume_24h':
            8302814.85, 'last_updated': '2026-07-15T10:45:05.000Z'}]}], 'total_size': 1, 'has_more': False}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: RWAMarketPairsResultsObject
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
        from ..models.rwa_market_pairs_results_object import RWAMarketPairsResultsObject

        d = dict(src_dict)
        data = RWAMarketPairsResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        rwa_market_pairs_response_model = cls(
            data=data,
            status=status,
        )

        rwa_market_pairs_response_model.additional_properties = d
        return rwa_market_pairs_response_model

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
