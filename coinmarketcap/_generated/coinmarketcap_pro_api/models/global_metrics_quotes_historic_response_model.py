from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.global_metrics_quotes_historic_results_object import GlobalMetricsQuotesHistoricResultsObject


T = TypeVar("T", bound="GlobalMetricsQuotesHistoricResponseModel")


@_attrs_define
class GlobalMetricsQuotesHistoricResponseModel:
    """
    Attributes:
        data (GlobalMetricsQuotesHistoricResultsObject): Results of your query returned as an object. Example:
            {'quotes': [{'timestamp': '2018-07-31T00:02:00.000Z', 'eth_dominance': 16.099, 'btc_dominance': 47.9949,
            'active_cryptocurrencies': 2500, 'active_exchanges': 600, 'active_market_pairs': 1000, 'quote': {'USD':
            {'total_market_cap': 292863223827.394, 'total_volume_24h': 17692152629.7864, 'total_volume_24h_reported':
            375179000000, 'altcoin_market_cap': 187589500000, 'altcoin_volume_24h': 375179000000,
            'altcoin_volume_24h_reported': 375179000000, 'timestamp': '2018-07-31T00:02:00.000Z'}}}, {'timestamp':
            '2018-08-01T00:02:00.000Z', 'eth_dominance': 16.099, 'btc_dominance': 48.0585, 'active_cryptocurrencies': 2500,
            'active_exchanges': 600, 'active_market_pairs': 1000, 'quote': {'USD': {'total_market_cap': 277770824530.303,
            'total_volume_24h': 15398085549.0344, 'total_volume_24h_reported': 375179000000, 'altcoin_market_cap':
            187589500000, 'altcoin_volume_24h': 375179000000, 'altcoin_volume_24h_reported': 375179000000, 'timestamp':
            '2018-07-31T00:02:00.000Z'}}}, {'timestamp': '2018-08-02T00:02:00.000Z', 'eth_dominance': 16.099,
            'btc_dominance': 48.041, 'active_cryptocurrencies': 2500, 'active_exchanges': 600, 'active_market_pairs': 1000,
            'quote': {'USD': {'total_market_cap': 273078776005.223, 'total_volume_24h': 14300071695.0547,
            'total_volume_24h_reported': 375179000000, 'altcoin_market_cap': 187589500000, 'altcoin_volume_24h':
            375179000000, 'altcoin_volume_24h_reported': 375179000000, 'timestamp': '2018-07-31T00:02:00.000Z'}}}]}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: GlobalMetricsQuotesHistoricResultsObject
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
        from ..models.global_metrics_quotes_historic_results_object import GlobalMetricsQuotesHistoricResultsObject

        d = dict(src_dict)
        data = GlobalMetricsQuotesHistoricResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        global_metrics_quotes_historic_response_model = cls(
            data=data,
            status=status,
        )

        global_metrics_quotes_historic_response_model.additional_properties = d
        return global_metrics_quotes_historic_response_model

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
