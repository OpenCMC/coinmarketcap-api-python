from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.category_results_map import CategoryResultsMap


T = TypeVar("T", bound="CategoryResponseModel")


@_attrs_define
class CategoryResponseModel:
    """
    Attributes:
        data (CategoryResultsMap): Results of your query returned as an object map. Example: {'1': {'id':
            '605e2ce9d41eae1066535f7c', 'name': 'A16Z Portfolio', 'title': 'A16Z Portfolio', 'description': 'A16Z
            Portfolio', 'num_tokens': 12, 'avg_price_change': 0.61305157, 'market_cap': 29429241867.031097,
            'market_cap_change': 3.049044106496, 'volume': 4103706600.0391645, 'volume_change': -10.538325849854, 'coins':
            [{'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'cmc_rank': 5, 'num_market_pairs': 500,
            'circulating_supply': 16950100, 'total_supply': 16950100, 'max_supply': 21000000, 'last_updated':
            '2018-06-02T22:51:28.209Z', 'date_added': '2013-04-28T00:00:00.000Z', 'tags': ['mineable'], 'platform': None,
            'quote': {'USD': {'price': 9283.92, 'volume_24h': 7155680000, 'percent_change_1h': -0.152774,
            'percent_change_24h': 0.518894, 'percent_change_7d': 0.986573, 'market_cap': 158055024432, 'last_updated':
            '2018-08-09T22:53:32.000Z'}}}, {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum',
            'num_market_pairs': 6360, 'circulating_supply': 16950100, 'total_supply': 16950100, 'max_supply': 21000000,
            'last_updated': '2018-06-02T22:51:28.209Z', 'date_added': '2013-04-28T00:00:00.000Z', 'tags': ['mineable'],
            'platform': None, 'quote': {'USD': {'price': 1283.92, 'volume_24h': 7155680000, 'percent_change_1h': -0.152774,
            'percent_change_24h': 0.518894, 'percent_change_7d': 0.986573, 'market_cap': 158055024432, 'last_updated':
            '2018-08-09T22:53:32.000Z'}}}], 'last_updated': '2021-11-10T10:35:12.354Z'}}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: CategoryResultsMap
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
        from ..models.category_results_map import CategoryResultsMap

        d = dict(src_dict)
        data = CategoryResultsMap.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        category_response_model = cls(
            data=data,
            status=status,
        )

        category_response_model.additional_properties = d
        return category_response_model

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
