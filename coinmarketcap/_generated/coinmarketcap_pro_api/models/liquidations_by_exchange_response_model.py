from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.liquidations_by_exchange_results_object import LiquidationsByExchangeResultsObject


T = TypeVar("T", bound="LiquidationsByExchangeResponseModel")


@_attrs_define
class LiquidationsByExchangeResponseModel:
    """
    Attributes:
        data (LiquidationsByExchangeResultsObject): Results of your query returned as an object. Example: {'exchanges':
            [{'name': 'Binance', 'slug': 'binance', 'quotes': [{'symbol': 'USD', 'crypto_id': 2781, 'total_liquidations_1h':
            3419396.41473615, 'long_liquidations_1h': 2539954.62605147, 'short_liquidations_1h': 879441.78868468,
            'total_liquidations_4h': 8461178.33919474, 'long_liquidations_4h': 6216074.5828236, 'short_liquidations_4h':
            2245103.75637114, 'total_liquidations_24h': 237863442.34358633, 'long_liquidations_24h': 207991776.57081032,
            'short_liquidations_24h': 29871665.77277603, 'last_updated': '2026-07-28T10:38:00.000Z'}], 'exchange_id': 270},
            {'name': 'Hyperliquid', 'slug': 'hyperliquid', 'quotes': [{'symbol': 'USD', 'crypto_id': 2781,
            'total_liquidations_1h': 65760.566551, 'long_liquidations_1h': 65708.762741, 'short_liquidations_1h': 51.80381,
            'total_liquidations_4h': 922900.157248, 'long_liquidations_4h': 876782.844196, 'short_liquidations_4h':
            46117.313052, 'total_liquidations_24h': 118872754.545678, 'long_liquidations_24h': 113352963.292567,
            'short_liquidations_24h': 5519791.253111, 'last_updated': '2026-07-28T10:38:00.000Z'}], 'exchange_id': 8112},
            {'name': 'OKX', 'slug': 'okx', 'quotes': [{'symbol': 'USD', 'crypto_id': 2781, 'total_liquidations_1h':
            348581.89193, 'long_liquidations_1h': 326089.92823, 'short_liquidations_1h': 22491.9637,
            'total_liquidations_4h': 1335101.94926, 'long_liquidations_4h': 970497.7628, 'short_liquidations_4h':
            364604.18646, 'total_liquidations_24h': 62512691.315803, 'long_liquidations_24h': 50876917.340933,
            'short_liquidations_24h': 11635773.97487, 'last_updated': '2026-07-28T10:38:00.000Z'}], 'exchange_id': 294}],
            'total_size': 11, 'has_more': True}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: LiquidationsByExchangeResultsObject
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
        from ..models.liquidations_by_exchange_results_object import LiquidationsByExchangeResultsObject

        d = dict(src_dict)
        data = LiquidationsByExchangeResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        liquidations_by_exchange_response_model = cls(
            data=data,
            status=status,
        )

        liquidations_by_exchange_response_model.additional_properties = d
        return liquidations_by_exchange_response_model

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
