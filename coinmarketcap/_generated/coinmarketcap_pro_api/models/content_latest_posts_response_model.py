from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.content_top_posts_results import ContentTopPostsResults


T = TypeVar("T", bound="ContentLatestPostsResponseModel")


@_attrs_define
class ContentLatestPostsResponseModel:
    """
    Example:
        {'data': {'list': [{'post_id': '123456789', 'comments_url':
            '{{baseUrl}}/v1/content/posts/comments?post_id=123456789', 'owner': {'nickname': 'CoinMarketCap', 'avatar_url':
            'https://s3.coinmarketcap.com/static/img/portraits/621c22097aafe46422aa1161.png'}, 'text_content': '$ETH
            regardless of merging or not merging...', 'photos':
            ['https://s3.coinmarketcap.com/static/img/portraits/621c22097aafe46422aa1161.png'], 'comment_count': '5',
            'like_count': '5', 'post_time': '1662643031298', 'currencies': [{'id': 1027, 'symbol': 'ETH', 'slug':
            'ethereum'}], 'language_code': 'en'}, {'post_id': '123456790', 'comments_url':
            '{{baseUrl}}/v1/content/posts/comments?post_id=123456790', 'owner': {'nickname': 'John', 'avatar_url':
            'https://s3.coinmarketcap.com/static/img/portraits/61b9aaca1d79d0637758fdeb.png'}, 'text_content': '$ETH The
            success and the failure are almost...', 'photos':
            ['https://s3.coinmarketcap.com/static/img/portraits/621c22097aafe46422aa1161.png'], 'comment_count': '6',
            'like_count': '60', 'post_time': '1662612816768', 'currencies': [{'id': 1027, 'symbol': 'ETH', 'slug':
            'ethereum'}], 'repost_count': '0', 'language_code': 'en'}], 'last_score': '1662903634322'}}

    Attributes:
        data (ContentTopPostsResults): Cntent objects.
    """

    data: ContentTopPostsResults
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
        from ..models.content_top_posts_results import ContentTopPostsResults

        d = dict(src_dict)
        data = ContentTopPostsResults.from_dict(d.pop("data"))

        content_latest_posts_response_model = cls(
            data=data,
        )

        content_latest_posts_response_model.additional_properties = d
        return content_latest_posts_response_model

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
