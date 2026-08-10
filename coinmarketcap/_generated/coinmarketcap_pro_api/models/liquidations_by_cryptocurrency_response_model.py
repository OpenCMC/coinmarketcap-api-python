from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.liquidations_by_cryptocurrency_results_object import LiquidationsByCryptocurrencyResultsObject


T = TypeVar("T", bound="LiquidationsByCryptocurrencyResponseModel")


@_attrs_define
class LiquidationsByCryptocurrencyResponseModel:
    """
    Attributes:
        data (LiquidationsByCryptocurrencyResultsObject): Results of your query returned as an object. Example:
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
            'cmc_rank': 2}], 'total_size': 805, 'has_more': True}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: LiquidationsByCryptocurrencyResultsObject
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
        from ..models.liquidations_by_cryptocurrency_results_object import LiquidationsByCryptocurrencyResultsObject

        d = dict(src_dict)
        data = LiquidationsByCryptocurrencyResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        liquidations_by_cryptocurrency_response_model = cls(
            data=data,
            status=status,
        )

        liquidations_by_cryptocurrency_response_model.additional_properties = d
        return liquidations_by_cryptocurrency_response_model

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
