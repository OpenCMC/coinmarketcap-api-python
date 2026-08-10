from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.exchange_historical_quotes_results_map import ExchangeHistoricalQuotesResultsMap


T = TypeVar("T", bound="ExchangeHistoricalQuotesResponseModel")


@_attrs_define
class ExchangeHistoricalQuotesResponseModel:
    """
    Attributes:
        data (ExchangeHistoricalQuotesResultsMap): Results of your query returned as an object map. Example: {'1':
            {'id': 270, 'name': 'Binance', 'slug': 'binance', 'quotes': [{'timestamp': '2018-06-03T00:00:00.000Z', 'quote':
            {'USD': {'volume_24h': 1632390000, 'timestamp': '2018-06-03T00:00:00.000Z'}}, 'num_market_pairs': 338},
            {'timestamp': '2018-06-10T00:00:00.000Z', 'quote': {'USD': {'volume_24h': 1034720000, 'timestamp':
            '2018-06-10T00:00:00.000Z'}}, 'num_market_pairs': 349}, {'timestamp': '2018-06-17T00:00:00.000Z', 'quote':
            {'USD': {'volume_24h': 883885000, 'timestamp': '2018-06-17T00:00:00.000Z'}}, 'num_market_pairs': 357}]}}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: ExchangeHistoricalQuotesResultsMap
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
        from ..models.exchange_historical_quotes_results_map import ExchangeHistoricalQuotesResultsMap

        d = dict(src_dict)
        data = ExchangeHistoricalQuotesResultsMap.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        exchange_historical_quotes_response_model = cls(
            data=data,
            status=status,
        )

        exchange_historical_quotes_response_model.additional_properties = d
        return exchange_historical_quotes_response_model

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
