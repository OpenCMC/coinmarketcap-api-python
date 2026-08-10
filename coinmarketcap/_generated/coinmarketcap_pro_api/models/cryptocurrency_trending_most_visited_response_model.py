from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.cryptocurrency_cryptocurrency_object import CryptocurrencyCryptocurrencyObject


T = TypeVar("T", bound="CryptocurrencyTrendingMostVisitedResponseModel")


@_attrs_define
class CryptocurrencyTrendingMostVisitedResponseModel:
    """
    Example:
        {'data': [{'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'cmc_rank': 5, 'num_market_pairs':
            500, 'circulating_supply': 16950100, 'total_supply': 16950100, 'max_supply': 21000000, 'last_updated':
            '2018-06-02T22:51:28.209Z', 'date_added': '2013-04-28T00:00:00.000Z', 'tags': ['mineable'], 'platform': None,
            'quote': {'USD': {'price': 9283.92, 'volume_24h': 7155680000, 'percent_change_1h': -0.152774,
            'percent_change_24h': 0.518894, 'percent_change_7d': 0.986573, 'market_cap': 158055024432, 'last_updated':
            '2018-08-09T22:53:32.000Z'}}}, {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum',
            'num_market_pairs': 6360, 'circulating_supply': 16950100, 'total_supply': 16950100, 'max_supply': 21000000,
            'last_updated': '2018-06-02T22:51:28.209Z', 'date_added': '2013-04-28T00:00:00.000Z', 'tags': ['mineable'],
            'platform': None, 'quote': {'USD': {'price': 1283.92, 'volume_24h': 7155680000, 'percent_change_1h': -0.152774,
            'percent_change_24h': 0.518894, 'percent_change_7d': 0.986573, 'market_cap': 158055024432, 'last_updated':
            '2018-08-09T22:53:32.000Z'}}}], 'status': {'timestamp': '2018-06-02T22:51:28.209Z', 'error_code': 0,
            'error_message': '', 'elapsed': 10, 'credit_count': 1}}

    Attributes:
        data (list[CryptocurrencyCryptocurrencyObject]): Array of cryptocurrency objects matching the list options.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: list[CryptocurrencyCryptocurrencyObject]
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for componentsschemas_cryptocurrency_trending_most_visited_results_array_item_data in self.data:
            componentsschemas_cryptocurrency_trending_most_visited_results_array_item = (
                componentsschemas_cryptocurrency_trending_most_visited_results_array_item_data.to_dict()
            )
            data.append(componentsschemas_cryptocurrency_trending_most_visited_results_array_item)

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
        from ..models.cryptocurrency_cryptocurrency_object import CryptocurrencyCryptocurrencyObject

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for componentsschemas_cryptocurrency_trending_most_visited_results_array_item_data in _data:
            componentsschemas_cryptocurrency_trending_most_visited_results_array_item = (
                CryptocurrencyCryptocurrencyObject.from_dict(
                    componentsschemas_cryptocurrency_trending_most_visited_results_array_item_data
                )
            )

            data.append(componentsschemas_cryptocurrency_trending_most_visited_results_array_item)

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        cryptocurrency_trending_most_visited_response_model = cls(
            data=data,
            status=status,
        )

        cryptocurrency_trending_most_visited_response_model.additional_properties = d
        return cryptocurrency_trending_most_visited_response_model

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
