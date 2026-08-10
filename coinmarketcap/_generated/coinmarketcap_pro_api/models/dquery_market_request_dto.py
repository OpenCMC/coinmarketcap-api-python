from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.leaderboard_filter_dto import LeaderboardFilterDTO


T = TypeVar("T", bound="DqueryMarketRequestDTO")


@_attrs_define
class DqueryMarketRequestDTO:
    """Market list request

    Attributes:
        platform_ids (str | Unset): Platform IDs, comma separated
        interval (str | Unset): Time interval
        next_page_index (str | Unset): Next page cursor
        page_size (int | Unset): Page size
        filter_ (LeaderboardFilterDTO | Unset): The request parameters for querying the token leaderboard
        sort_by (str | Unset): Sort field
        sort_type (str | Unset): Sort type: asc or desc
    """

    platform_ids: str | Unset = UNSET
    interval: str | Unset = UNSET
    next_page_index: str | Unset = UNSET
    page_size: int | Unset = UNSET
    filter_: LeaderboardFilterDTO | Unset = UNSET
    sort_by: str | Unset = UNSET
    sort_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform_ids = self.platform_ids

        interval = self.interval

        next_page_index = self.next_page_index

        page_size = self.page_size

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        sort_by = self.sort_by

        sort_type = self.sort_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform_ids is not UNSET:
            field_dict["platformIds"] = platform_ids
        if interval is not UNSET:
            field_dict["interval"] = interval
        if next_page_index is not UNSET:
            field_dict["nextPageIndex"] = next_page_index
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if sort_by is not UNSET:
            field_dict["sortBy"] = sort_by
        if sort_type is not UNSET:
            field_dict["sortType"] = sort_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.leaderboard_filter_dto import LeaderboardFilterDTO

        d = dict(src_dict)
        platform_ids = d.pop("platformIds", UNSET)

        interval = d.pop("interval", UNSET)

        next_page_index = d.pop("nextPageIndex", UNSET)

        page_size = d.pop("pageSize", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: LeaderboardFilterDTO | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = LeaderboardFilterDTO.from_dict(_filter_)

        sort_by = d.pop("sortBy", UNSET)

        sort_type = d.pop("sortType", UNSET)

        dquery_market_request_dto = cls(
            platform_ids=platform_ids,
            interval=interval,
            next_page_index=next_page_index,
            page_size=page_size,
            filter_=filter_,
            sort_by=sort_by,
            sort_type=sort_type,
        )

        dquery_market_request_dto.additional_properties = d
        return dquery_market_request_dto

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
