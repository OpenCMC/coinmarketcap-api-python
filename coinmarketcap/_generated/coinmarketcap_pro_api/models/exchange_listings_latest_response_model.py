from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.exchange_listings_latest_exchange_object import ExchangeListingsLatestExchangeObject


T = TypeVar("T", bound="ExchangeListingsLatestResponseModel")


@_attrs_define
class ExchangeListingsLatestResponseModel:
    """
    Attributes:
        data (list[ExchangeListingsLatestExchangeObject]): Array of exchange objects matching the list options. Example:
            [{'id': 270, 'name': 'Binance', 'slug': 'binance', 'num_market_pairs': 1214, 'fiats': ['AED', 'USD'],
            'traffic_score': 1000, 'rank': 1, 'exchange_score': 9.8, 'liquidity_score': 9.8028, 'last_updated':
            '2018-11-08T22:18:00.000Z', 'quote': {'USD': {'volume_24h': 769291636.239632, 'volume_24h_adjusted':
            769291636.239632, 'volume_7d': 3666423776, 'volume_30d': 21338299776, 'percent_change_volume_24h': -11.6153,
            'percent_change_volume_7d': 67.2055, 'percent_change_volume_30d': 0.00169339, 'effective_liquidity_24h':
            629.9774, 'derivative_volume_usd': 62828618628.85901, 'spot_volume_usd': 39682580614.8572, 'last_updated':
            '2018-11-08T22:18:00.000Z'}}}, {'id': 294, 'name': 'OKEx', 'slug': 'okex', 'num_market_pairs': 385, 'fiats':
            ['AED', 'USD'], 'traffic_score': 845.1565, 'rank': 1, 'exchange_score': 8.5, 'liquidity_score': 9.8028,
            'last_updated': '2018-11-08T22:18:00.000Z', 'quote': {'USD': {'volume_24h': 677439315.721563,
            'volume_24h_adjusted': 677439315.721563, 'volume_7d': 3506137120, 'volume_30d': 14418225072,
            'percent_change_volume_24h': -13.9256, 'percent_change_volume_7d': 60.0461, 'percent_change_volume_30d':
            67.2225, 'effective_liquidity_24h': 629.9774, 'derivative_volume_usd': 62828618628.85901, 'spot_volume_usd':
            39682580614.8572, 'last_updated': '2018-11-08T22:18:00.000Z'}}}].
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: list[ExchangeListingsLatestExchangeObject]
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for componentsschemas_exchange_listings_latest_results_array_item_data in self.data:
            componentsschemas_exchange_listings_latest_results_array_item = (
                componentsschemas_exchange_listings_latest_results_array_item_data.to_dict()
            )
            data.append(componentsschemas_exchange_listings_latest_results_array_item)

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
        from ..models.exchange_listings_latest_exchange_object import ExchangeListingsLatestExchangeObject

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for componentsschemas_exchange_listings_latest_results_array_item_data in _data:
            componentsschemas_exchange_listings_latest_results_array_item = (
                ExchangeListingsLatestExchangeObject.from_dict(
                    componentsschemas_exchange_listings_latest_results_array_item_data
                )
            )

            data.append(componentsschemas_exchange_listings_latest_results_array_item)

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        exchange_listings_latest_response_model = cls(
            data=data,
            status=status,
        )

        exchange_listings_latest_response_model.additional_properties = d
        return exchange_listings_latest_response_model

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
