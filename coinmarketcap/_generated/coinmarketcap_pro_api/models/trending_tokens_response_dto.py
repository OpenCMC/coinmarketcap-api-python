from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.token_leaderboard_dto import TokenLeaderboardDTO


T = TypeVar("T", bound="TrendingTokensResponseDTO")


@_attrs_define
class TrendingTokensResponseDTO:
    """
    Attributes:
        total (int | Unset): Total number of tokens
        current_page (int | Unset): Current page index
        page_size (int | Unset): Number of tokens per page
        next_page_index (str | Unset): Next page index
        version (str | Unset): Version
        leaderboard_list (list[TokenLeaderboardDTO] | Unset): Token Leaderboard List
    """

    total: int | Unset = UNSET
    current_page: int | Unset = UNSET
    page_size: int | Unset = UNSET
    next_page_index: str | Unset = UNSET
    version: str | Unset = UNSET
    leaderboard_list: list[TokenLeaderboardDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        current_page = self.current_page

        page_size = self.page_size

        next_page_index = self.next_page_index

        version = self.version

        leaderboard_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.leaderboard_list, Unset):
            leaderboard_list = []
            for leaderboard_list_item_data in self.leaderboard_list:
                leaderboard_list_item = leaderboard_list_item_data.to_dict()
                leaderboard_list.append(leaderboard_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if next_page_index is not UNSET:
            field_dict["nextPageIndex"] = next_page_index
        if version is not UNSET:
            field_dict["version"] = version
        if leaderboard_list is not UNSET:
            field_dict["leaderboardList"] = leaderboard_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_leaderboard_dto import TokenLeaderboardDTO

        d = dict(src_dict)
        total = d.pop("total", UNSET)

        current_page = d.pop("currentPage", UNSET)

        page_size = d.pop("pageSize", UNSET)

        next_page_index = d.pop("nextPageIndex", UNSET)

        version = d.pop("version", UNSET)

        _leaderboard_list = d.pop("leaderboardList", UNSET)
        leaderboard_list: list[TokenLeaderboardDTO] | Unset = UNSET
        if _leaderboard_list is not UNSET:
            leaderboard_list = []
            for leaderboard_list_item_data in _leaderboard_list:
                leaderboard_list_item = TokenLeaderboardDTO.from_dict(leaderboard_list_item_data)

                leaderboard_list.append(leaderboard_list_item)

        trending_tokens_response_dto = cls(
            total=total,
            current_page=current_page,
            page_size=page_size,
            next_page_index=next_page_index,
            version=version,
            leaderboard_list=leaderboard_list,
        )

        trending_tokens_response_dto.additional_properties = d
        return trending_tokens_response_dto

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
