from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.categories_category_object import CategoriesCategoryObject


T = TypeVar("T", bound="CategoriesResponseModel")


@_attrs_define
class CategoriesResponseModel:
    """
    Example:
        {'data': [{'id': '605e2ce9d41eae1066535f7c', 'name': 'A16Z Portfolio', 'title': 'A16Z Portfolio', 'description':
            'A16Z Portfolio', 'num_tokens': 12, 'avg_price_change': 0.61305157, 'market_cap': 29429241867.031097,
            'market_cap_change': 3.049044106496, 'volume': 4103706600.0391645, 'volume_change': -10.538325849854,
            'last_updated': '2021-11-10T10:35:12.354Z'}], 'status': {'timestamp': '2021-08-01T22:51:28.209Z', 'error_code':
            0, 'error_message': '', 'elapsed': 3, 'credit_count': 1}}

    Attributes:
        data (list[CategoriesCategoryObject]): Results of your query returned as an object map.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: list[CategoriesCategoryObject]
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for componentsschemas_categories_results_map_item_data in self.data:
            componentsschemas_categories_results_map_item = componentsschemas_categories_results_map_item_data.to_dict()
            data.append(componentsschemas_categories_results_map_item)

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
        from ..models.categories_category_object import CategoriesCategoryObject

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for componentsschemas_categories_results_map_item_data in _data:
            componentsschemas_categories_results_map_item = CategoriesCategoryObject.from_dict(
                componentsschemas_categories_results_map_item_data
            )

            data.append(componentsschemas_categories_results_map_item)

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        categories_response_model = cls(
            data=data,
            status=status,
        )

        categories_response_model.additional_properties = d
        return categories_response_model

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
