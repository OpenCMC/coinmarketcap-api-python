from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.model_2 import Model2


T = TypeVar("T", bound="ContentPostCommentsResponseModel")


@_attrs_define
class ContentPostCommentsResponseModel:
    """
    Example:
        {'data': [{'post_id': '317807035', 'owner': {'nickname': 'Amy', 'avatar_url':
            'https://s3.coinmarketcap.com/static/img/portraits/61359449293ccc2c4bcf07c7.png'}, 'text_content': "Someone's
            working on it!!", 'photos': [], 'comment_count': '0', 'like_count': '0', 'post_time': '1662640110429',
            'language_code': 'en'}, {'post_id': '317807862', 'owner': {'nickname': 'Wanda', 'avatar_url':
            'https://s3.coinmarketcap.com/static/img/portraits/6136cf1015b8f3308e283073.png'}, 'text_content': 'yes sir!!',
            'photos': [], 'comment_count': '0', 'like_count': '0', 'post_time': '1662635039889', 'language_code': 'en'}],
            'status': {'timestamp': '2022-09-08T16:07:30.033Z', 'error_code': 0, 'error_message': 'SUCCESS', 'elapsed': 10,
            'credit_count': 0}}

    Attributes:
        data (list[Model2]): Array of content objects.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: list[Model2]
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for componentsschemas_content_post_comments_results_array_item_data in self.data:
            componentsschemas_content_post_comments_results_array_item = (
                componentsschemas_content_post_comments_results_array_item_data.to_dict()
            )
            data.append(componentsschemas_content_post_comments_results_array_item)

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
        from ..models.model_2 import Model2

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for componentsschemas_content_post_comments_results_array_item_data in _data:
            componentsschemas_content_post_comments_results_array_item = Model2.from_dict(
                componentsschemas_content_post_comments_results_array_item_data
            )

            data.append(componentsschemas_content_post_comments_results_array_item)

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        content_post_comments_response_model = cls(
            data=data,
            status=status,
        )

        content_post_comments_response_model.additional_properties = d
        return content_post_comments_response_model

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
