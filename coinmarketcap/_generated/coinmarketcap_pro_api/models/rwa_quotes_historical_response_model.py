from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.rwa_quotes_historical_results_object import RWAQuotesHistoricalResultsObject


T = TypeVar("T", bound="RWAQuotesHistoricalResponseModel")


@_attrs_define
class RWAQuotesHistoricalResponseModel:
    """
    Attributes:
        data (RWAQuotesHistoricalResultsObject): Results of your query returned as an object. Example: {'rwa_assets':
            [{'name': 'Nvidia Corp', 'symbol': 'NVDA', 'slug': 'nvidia', 'quotes': [{'timestamp':
            '2026-11-17T05:00:00.000Z', 'convert_id': 2781, 'convert_symbol': 'USD', 'average_tokenized_price':
            157.86910203115895, 'tokenized_market_cap': 362817204.1754513, 'tokenized_volume_24h': 321224540.9867724},
            {'timestamp': '2026-11-18T05:00:00.000Z', 'convert_id': 2781, 'convert_symbol': 'USD',
            'average_tokenized_price': 157.31123163132813, 'tokenized_market_cap': 392273916.1191814,
            'tokenized_volume_24h': 473033580.56851166}, {'timestamp': '2026-11-19T05:00:00.000Z', 'convert_id': 2781,
            'convert_symbol': 'USD', 'average_tokenized_price': 152.06295777583813, 'tokenized_market_cap':
            383038734.34426445, 'tokenized_volume_24h': 356263300.4355586}], 'rwa_id': 2, 'asset_type': 'stock', 'rwa_rank':
            4, 'has_tokens': True}]}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: RWAQuotesHistoricalResultsObject
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
        from ..models.rwa_quotes_historical_results_object import RWAQuotesHistoricalResultsObject

        d = dict(src_dict)
        data = RWAQuotesHistoricalResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        rwa_quotes_historical_response_model = cls(
            data=data,
            status=status,
        )

        rwa_quotes_historical_response_model.additional_properties = d
        return rwa_quotes_historical_response_model

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
