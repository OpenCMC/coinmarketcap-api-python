from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.exchange_map_exchange_object import ExchangeMapExchangeObject


T = TypeVar("T", bound="ExchangeMapResponseModel")


@_attrs_define
class ExchangeMapResponseModel:
    """
    Attributes:
        data (list[ExchangeMapExchangeObject]): Array of exchange object results.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: list[ExchangeMapExchangeObject]
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for componentsschemas_exchange_map_exchanges_array_item_data in self.data:
            componentsschemas_exchange_map_exchanges_array_item = (
                componentsschemas_exchange_map_exchanges_array_item_data.to_dict()
            )
            data.append(componentsschemas_exchange_map_exchanges_array_item)

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
        from ..models.exchange_map_exchange_object import ExchangeMapExchangeObject

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for componentsschemas_exchange_map_exchanges_array_item_data in _data:
            componentsschemas_exchange_map_exchanges_array_item = ExchangeMapExchangeObject.from_dict(
                componentsschemas_exchange_map_exchanges_array_item_data
            )

            data.append(componentsschemas_exchange_map_exchanges_array_item)

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        exchange_map_response_model = cls(
            data=data,
            status=status,
        )

        exchange_map_response_model.additional_properties = d
        return exchange_map_response_model

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
