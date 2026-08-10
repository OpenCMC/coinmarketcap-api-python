from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.token_leaderboard_dto import TokenLeaderboardDTO


T = TypeVar("T", bound="GainerLeaderBoardResponseDTO")


@_attrs_define
class GainerLeaderBoardResponseDTO:
    """Response object for the Gainer Leaderboard API

    Attributes:
        leaderboard_list (list[TokenLeaderboardDTO] | Unset): List of token leaderboard entries
        page_num (int | Unset): Current page number
        page_size (int | Unset): Number of entries per page
        total (int | Unset): Total number of matching entries
        has_next_page (bool | Unset): Whether there is another page after the current one
        last_update_time (int | Unset): Timestamp (in milliseconds) when the data was last updated
        next_page_index (str | Unset): Cursor to be used for fetching the next page
    """

    leaderboard_list: list[TokenLeaderboardDTO] | Unset = UNSET
    page_num: int | Unset = UNSET
    page_size: int | Unset = UNSET
    total: int | Unset = UNSET
    has_next_page: bool | Unset = UNSET
    last_update_time: int | Unset = UNSET
    next_page_index: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        leaderboard_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.leaderboard_list, Unset):
            leaderboard_list = []
            for leaderboard_list_item_data in self.leaderboard_list:
                leaderboard_list_item = leaderboard_list_item_data.to_dict()
                leaderboard_list.append(leaderboard_list_item)

        page_num = self.page_num

        page_size = self.page_size

        total = self.total

        has_next_page = self.has_next_page

        last_update_time = self.last_update_time

        next_page_index = self.next_page_index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if leaderboard_list is not UNSET:
            field_dict["leaderboardList"] = leaderboard_list
        if page_num is not UNSET:
            field_dict["pageNum"] = page_num
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if total is not UNSET:
            field_dict["total"] = total
        if has_next_page is not UNSET:
            field_dict["hasNextPage"] = has_next_page
        if last_update_time is not UNSET:
            field_dict["lastUpdateTime"] = last_update_time
        if next_page_index is not UNSET:
            field_dict["nextPageIndex"] = next_page_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_leaderboard_dto import TokenLeaderboardDTO

        d = dict(src_dict)
        _leaderboard_list = d.pop("leaderboardList", UNSET)
        leaderboard_list: list[TokenLeaderboardDTO] | Unset = UNSET
        if _leaderboard_list is not UNSET:
            leaderboard_list = []
            for leaderboard_list_item_data in _leaderboard_list:
                leaderboard_list_item = TokenLeaderboardDTO.from_dict(leaderboard_list_item_data)

                leaderboard_list.append(leaderboard_list_item)

        page_num = d.pop("pageNum", UNSET)

        page_size = d.pop("pageSize", UNSET)

        total = d.pop("total", UNSET)

        has_next_page = d.pop("hasNextPage", UNSET)

        last_update_time = d.pop("lastUpdateTime", UNSET)

        next_page_index = d.pop("nextPageIndex", UNSET)

        gainer_leader_board_response_dto = cls(
            leaderboard_list=leaderboard_list,
            page_num=page_num,
            page_size=page_size,
            total=total,
            has_next_page=has_next_page,
            last_update_time=last_update_time,
            next_page_index=next_page_index,
        )

        gainer_leader_board_response_dto.additional_properties = d
        return gainer_leader_board_response_dto

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
