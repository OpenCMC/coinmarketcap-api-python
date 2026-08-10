from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.v2_simple_price_item_object import V2SimplePriceItemObject


T = TypeVar("T", bound="V2SimplePriceResponseModel")


@_attrs_define
class V2SimplePriceResponseModel:
    """
    Example:
        {'data': [{'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'quotes': [{'symbol': 'USD', 'price':
            63319.879266088545, 'market_cap': 1270345579794.0115, 'volume_24h': 23424304928.73599, 'percent_change_24h':
            -3.03610139, 'last_updated': '2026-07-28T10:35:05.000Z'}]}, {'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH',
            'slug': 'ethereum', 'quotes': [{'symbol': 'USD', 'price': 1875.3832420347037, 'market_cap': 226326126225.45407,
            'volume_24h': 12578049044.855345, 'percent_change_24h': -4.60239011, 'last_updated':
            '2026-07-28T10:35:05.000Z'}]}], 'status': {'timestamp': '2026-07-28T10:38:38.654Z', 'error_code': '0',
            'error_message': '', 'elapsed': 10, 'credit_count': 1}}

    Attributes:
        data (list[V2SimplePriceItemObject]): Array of asset objects, one per resolved identifier. With
            `skip_invalid=true`, unresolved identifiers are simply absent.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: list[V2SimplePriceItemObject]
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

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
        from ..models.v2_simple_price_item_object import V2SimplePriceItemObject

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = V2SimplePriceItemObject.from_dict(data_item_data)

            data.append(data_item)

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        v2_simple_price_response_model = cls(
            data=data,
            status=status,
        )

        v2_simple_price_response_model.additional_properties = d
        return v2_simple_price_response_model

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
