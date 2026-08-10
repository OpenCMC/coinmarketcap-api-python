from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dex_urls import DexUrls


T = TypeVar("T", bound="DexCommonInfoDTO")


@_attrs_define
class DexCommonInfoDTO:
    """
    Attributes:
        id (int | Unset): The unique CoinMarketCap ID for this exchange.
        name (str | Unset): The name of this exchange.
        slug (str | Unset): The web URL friendly shorthand version of this exchange name.
        logo (str | Unset): Link to a CoinMarketCap hosted logo png for this exchange. 64px is default size returned.
            Replace "64x64" in the image path with these alternative sizes: 16, 32, 64, 128, 200
        status (str | Unset): Current status of the DEX. Can be "active" or "inactive".
        description (str | Unset): A CoinMarketCap supplied brief description of this DEX pair. This field will return
            null if a description is not available.
        notice (str | Unset): A Markdown formatted message outlining a condition that is impacting the availability of
            the exchange's market data or the secure use of the exchange, otherwise null. This may include a maintenance
            event on the exchange's end or CoinMarketCap's end, an alert about reported issues with withdrawls from this
            exchange, or another condition that may be impacting the exchange and it's markets. If present, this notice is
            also displayed in an alert banner at the top of the exchange's page on coinmarketcap.com.
        urls (DexUrls | Unset): An object containing various resource URLs for this exchange.
        date_launched (datetime.datetime | Unset): Timestamp (ISO 8601) of the date this exchange launched. This field
            is only returned if requested through the aux request parameter.
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    logo: str | Unset = UNSET
    status: str | Unset = UNSET
    description: str | Unset = UNSET
    notice: str | Unset = UNSET
    urls: DexUrls | Unset = UNSET
    date_launched: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        logo = self.logo

        status = self.status

        description = self.description

        notice = self.notice

        urls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls.to_dict()

        date_launched: str | Unset = UNSET
        if not isinstance(self.date_launched, Unset):
            date_launched = self.date_launched.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if logo is not UNSET:
            field_dict["logo"] = logo
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if notice is not UNSET:
            field_dict["notice"] = notice
        if urls is not UNSET:
            field_dict["urls"] = urls
        if date_launched is not UNSET:
            field_dict["date_launched"] = date_launched

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dex_urls import DexUrls

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        logo = d.pop("logo", UNSET)

        status = d.pop("status", UNSET)

        description = d.pop("description", UNSET)

        notice = d.pop("notice", UNSET)

        _urls = d.pop("urls", UNSET)
        urls: DexUrls | Unset
        if isinstance(_urls, Unset):
            urls = UNSET
        else:
            urls = DexUrls.from_dict(_urls)

        _date_launched = d.pop("date_launched", UNSET)
        date_launched: datetime.datetime | Unset
        if isinstance(_date_launched, Unset):
            date_launched = UNSET
        else:
            date_launched = isoparse(_date_launched)

        dex_common_info_dto = cls(
            id=id,
            name=name,
            slug=slug,
            logo=logo,
            status=status,
            description=description,
            notice=notice,
            urls=urls,
            date_launched=date_launched,
        )

        dex_common_info_dto.additional_properties = d
        return dex_common_info_dto

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
