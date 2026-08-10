from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.community_trending_token_results_object import CommunityTrendingTokenResultsObject


T = TypeVar("T", bound="CommunityTrendingTokenResponseModel")


@_attrs_define
class CommunityTrendingTokenResponseModel:
    """
    Example:
        {'data': [{'id': 7102, 'name': 'Linear Finance', 'symbol': 'LINA', 'slug': 'linear', 'cmc_rank': 461, 'rank':
            1}, {'id': 26265, 'name': 'NiHao', 'symbol': 'NIHAO', 'slug': 'nihao', 'cmc_rank': 5000, 'rank': 2}, {'id':
            22538, 'name': 'T-mac DAO', 'symbol': 'TMG', 'slug': 't-mac-dao', 'cmc_rank': 4802, 'rank': 3}, {'id': 2398,
            'name': 'SelfKey', 'symbol': 'KEY', 'slug': 'selfkey', 'cmc_rank': 753, 'rank': 4}, {'id': 3437, 'name': 'ABBC
            Coin', 'symbol': 'ABBC', 'slug': 'abbc-coin', 'cmc_rank': 178, 'rank': 5}]}

    Attributes:
        data (list[CommunityTrendingTokenResultsObject]): Cntent objects.
    """

    data: list[CommunityTrendingTokenResultsObject]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for componentsschemas_community_trending_token_results_item_data in self.data:
            componentsschemas_community_trending_token_results_item = (
                componentsschemas_community_trending_token_results_item_data.to_dict()
            )
            data.append(componentsschemas_community_trending_token_results_item)

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
        from ..models.community_trending_token_results_object import CommunityTrendingTokenResultsObject

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for componentsschemas_community_trending_token_results_item_data in _data:
            componentsschemas_community_trending_token_results_item = CommunityTrendingTokenResultsObject.from_dict(
                componentsschemas_community_trending_token_results_item_data
            )

            data.append(componentsschemas_community_trending_token_results_item)

        community_trending_token_response_model = cls(
            data=data,
        )

        community_trending_token_response_model.additional_properties = d
        return community_trending_token_response_model

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
