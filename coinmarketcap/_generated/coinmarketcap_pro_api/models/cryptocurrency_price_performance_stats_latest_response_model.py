from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.cryptocurrency_price_performance_stats_latest_cryptocurrency_results_map import (
        CryptocurrencyPricePerformanceStatsLatestCryptocurrencyResultsMap,
    )


T = TypeVar("T", bound="CryptocurrencyPricePerformanceStatsLatestResponseModel")


@_attrs_define
class CryptocurrencyPricePerformanceStatsLatestResponseModel:
    """
    Attributes:
        data (CryptocurrencyPricePerformanceStatsLatestCryptocurrencyResultsMap): An object map of cryptocurrency
            objects by ID, slug, or symbol (as used in query parameters). Example: {'1': {'id': 1, 'name': 'Bitcoin',
            'symbol': 'BTC', 'slug': 'bitcoin', 'last_updated': '2019-08-22T01:51:32.000Z', 'periods': {'USD':
            {'open_timestamp': '2013-04-28T00:00:00.000Z', 'high_timestamp': '2017-12-17T12:19:14.000Z', 'low_timestamp':
            '2013-07-05T18:56:01.000Z', 'close_timestamp': '2019-08-22T01:52:18.613Z', 'quote': {'USD': {'open':
            135.3000030517578, 'open_timestamp': '2013-04-28T00:00:00.000Z', 'high': 20088.99609375, 'high_timestamp':
            '2017-12-17T12:19:14.000Z', 'low': 65.5260009765625, 'low_timestamp': '2013-07-05T18:56:01.000Z', 'close':
            65.5260009765625, 'close_timestamp': '2019-08-22T01:52:18.618Z', 'percent_change': 7223.718930042746,
            'price_change': 9773.691932798241}}}}}}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: CryptocurrencyPricePerformanceStatsLatestCryptocurrencyResultsMap
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
        from ..models.cryptocurrency_price_performance_stats_latest_cryptocurrency_results_map import (
            CryptocurrencyPricePerformanceStatsLatestCryptocurrencyResultsMap,
        )

        d = dict(src_dict)
        data = CryptocurrencyPricePerformanceStatsLatestCryptocurrencyResultsMap.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        cryptocurrency_price_performance_stats_latest_response_model = cls(
            data=data,
            status=status,
        )

        cryptocurrency_price_performance_stats_latest_response_model.additional_properties = d
        return cryptocurrency_price_performance_stats_latest_response_model

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
