from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.fcas_listings_latest_cryptocurrency_object import FCASListingsLatestCryptocurrencyObject


T = TypeVar("T", bound="FCASListingsLatestResponseModel")


@_attrs_define
class FCASListingsLatestResponseModel:
    """
    Example:
        {'data': [{'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH', 'slug': 'ethereum', 'score': 971, 'grade': 'S',
            'last_updated': '2021-05-05T00:00:00Z'}, {'id': 2010, 'name': 'Cardano', 'symbol': 'ADA', 'slug': 'cardano',
            'score': 961, 'grade': 'S', 'last_updated': '2021-05-05T00:00:00Z'}], 'status': {'timestamp':
            '2018-06-02T22:51:28.209Z', 'error_code': 0, 'error_message': '', 'elapsed': 10, 'credit_count': 1}}

    Attributes:
        data (list[FCASListingsLatestCryptocurrencyObject]): Array of cryptocurrency objects matching the list options.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: list[FCASListingsLatestCryptocurrencyObject]
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for componentsschemas_fcas_listings_latest_results_array_item_data in self.data:
            componentsschemas_fcas_listings_latest_results_array_item = (
                componentsschemas_fcas_listings_latest_results_array_item_data.to_dict()
            )
            data.append(componentsschemas_fcas_listings_latest_results_array_item)

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
        from ..models.fcas_listings_latest_cryptocurrency_object import FCASListingsLatestCryptocurrencyObject

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for componentsschemas_fcas_listings_latest_results_array_item_data in _data:
            componentsschemas_fcas_listings_latest_results_array_item = (
                FCASListingsLatestCryptocurrencyObject.from_dict(
                    componentsschemas_fcas_listings_latest_results_array_item_data
                )
            )

            data.append(componentsschemas_fcas_listings_latest_results_array_item)

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        fcas_listings_latest_response_model = cls(
            data=data,
            status=status,
        )

        fcas_listings_latest_response_model.additional_properties = d
        return fcas_listings_latest_response_model

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
