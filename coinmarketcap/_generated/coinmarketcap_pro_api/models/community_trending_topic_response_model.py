from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.community_trending_topic_results import CommunityTrendingTopicResults


T = TypeVar("T", bound="CommunityTrendingTopicResponseModel")


@_attrs_define
class CommunityTrendingTopicResponseModel:
    """
    Example:
        {'data': {'rank': 1, 'topic': 'Tether'}, 'status': {'timestamp': '2022-09-08T16:08:52.641Z', 'error_code': '0',
            'error_message': 'SUCCESS', 'elapsed': '0', 'credit_count': 0}}

    Attributes:
        data (CommunityTrendingTopicResults): Cntent objects.
    """

    data: CommunityTrendingTopicResults
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.community_trending_topic_results import CommunityTrendingTopicResults

        d = dict(src_dict)
        data = CommunityTrendingTopicResults.from_dict(d.pop("data"))

        community_trending_topic_response_model = cls(
            data=data,
        )

        community_trending_topic_response_model.additional_properties = d
        return community_trending_topic_response_model

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
