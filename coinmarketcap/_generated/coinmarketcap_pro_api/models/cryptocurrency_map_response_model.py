from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.cryptocurrency_map_cryotocurrency_object import CryptocurrencyMapCryotocurrencyObject


T = TypeVar("T", bound="CryptocurrencyMapResponseModel")


@_attrs_define
class CryptocurrencyMapResponseModel:
    """
    Example:
        {'data': [{'id': 1, 'rank': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'is_active': 1,
            'first_historical_data': '2013-04-28T18:47:21.000Z', 'last_historical_data': '2020-05-05T20:44:01.000Z',
            'platform': None}, {'id': 1839, 'rank': 3, 'name': 'Binance Coin', 'symbol': 'BNB', 'slug': 'binance-coin',
            'is_active': 1, 'first_historical_data': '2017-07-25T04:30:05.000Z', 'last_historical_data':
            '2020-05-05T20:44:02.000Z', 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum',
            'token_address': '0xB8c77482e45F1F44dE1745F52C74426C631bDD52'}}, {'id': 825, 'rank': 5, 'name': 'Tether',
            'symbol': 'USDT', 'slug': 'tether', 'is_active': 1, 'first_historical_data': '2015-02-25T13:34:26.000Z',
            'last_historical_data': '2020-05-05T20:44:01.000Z', 'platform': {'id': 1027, 'name': 'Ethereum', 'symbol':
            'ETH', 'slug': 'ethereum', 'token_address': '0xdac17f958d2ee523a2206206994597c13d831ec7'}}], 'status':
            {'timestamp': '2018-06-02T22:51:28.209Z', 'error_code': 0, 'error_message': '', 'elapsed': 10, 'credit_count':
            1}}

    Attributes:
        data (list[CryptocurrencyMapCryotocurrencyObject]): Array of cryptocurrency object results.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: list[CryptocurrencyMapCryotocurrencyObject]
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for componentsschemas_cryptocurrency_map_cryptocurrency_array_item_data in self.data:
            componentsschemas_cryptocurrency_map_cryptocurrency_array_item = (
                componentsschemas_cryptocurrency_map_cryptocurrency_array_item_data.to_dict()
            )
            data.append(componentsschemas_cryptocurrency_map_cryptocurrency_array_item)

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
        from ..models.cryptocurrency_map_cryotocurrency_object import CryptocurrencyMapCryotocurrencyObject

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for componentsschemas_cryptocurrency_map_cryptocurrency_array_item_data in _data:
            componentsschemas_cryptocurrency_map_cryptocurrency_array_item = (
                CryptocurrencyMapCryotocurrencyObject.from_dict(
                    componentsschemas_cryptocurrency_map_cryptocurrency_array_item_data
                )
            )

            data.append(componentsschemas_cryptocurrency_map_cryptocurrency_array_item)

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        cryptocurrency_map_response_model = cls(
            data=data,
            status=status,
        )

        cryptocurrency_map_response_model.additional_properties = d
        return cryptocurrency_map_response_model

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
