from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.model_1 import Model1


T = TypeVar("T", bound="ContentLatestResponseModel")


@_attrs_define
class ContentLatestResponseModel:
    """
    Example:
        {'data': [{'cover': 'https://academy-public.coinmarketcap.com/optimized-
            uploads/0aec0502868046419ceace229f92601f.gif', 'assets': [{'id': 1027, 'name': 'Ethereum', 'symbol': 'ETH',
            'slug': 'ethereum'}], 'created_at': '2021-05-05T00:00:00Z', 'released_at': '2021-05-05T00:00:00Z', 'title':
            'Article Title', 'subtitle': 'Article Subtitle', 'type': 'alexandria', 'source_name': 'Connor Sephton',
            'source_url': 'https://coinmarketcap.com/alexandria/article/coinmarketcap-news-august-9-u-s-comes-for-tornado-
            cash'}], 'status': {'timestamp': '2018-06-02T22:51:28.209Z', 'error_code': 0, 'error_message': '', 'elapsed':
            10, 'credit_count': 1}}

    Attributes:
        data (list[Model1]): Array of content objects.
        status (APIStatusObject): Standardized status object for API calls.
    """

    data: list[Model1]
    status: APIStatusObject
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for componentsschemas_content_latest_results_array_item_data in self.data:
            componentsschemas_content_latest_results_array_item = (
                componentsschemas_content_latest_results_array_item_data.to_dict()
            )
            data.append(componentsschemas_content_latest_results_array_item)

        status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_status_object import APIStatusObject
        from ..models.model_1 import Model1

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for componentsschemas_content_latest_results_array_item_data in _data:
            componentsschemas_content_latest_results_array_item = Model1.from_dict(
                componentsschemas_content_latest_results_array_item_data
            )

            data.append(componentsschemas_content_latest_results_array_item)

        status = APIStatusObject.from_dict(d.pop("status"))

        content_latest_response_model = cls(
            data=data,
            status=status,
        )

        content_latest_response_model.additional_properties = d
        return content_latest_response_model

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
