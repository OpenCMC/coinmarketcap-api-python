from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RWAInfoResultsObjectRwaAssetsItemAbout")


@_attrs_define
class RWAInfoResultsObjectRwaAssetsItemAbout:
    """About block (descriptive static metadata).

    Attributes:
        description (None | str | Unset): Asset description (may contain Markdown). Example: NVIDIA is a U.S.-based
            semiconductor and computing company specializing in GPUs, AI hardware, and high-performance computing..
        logo (None | str | Unset): Single small-size logo URL; `null` when absent.
        website (None | str | Unset): Official asset/company website URL. `null` when absent. Example:
            https://www.nvidia.com.
        date_added (datetime.datetime | Unset): ISO 8601 date the asset was added to CoinMarketCap. Example:
            2025-07-17T06:35:44.000Z.
    """

    description: None | str | Unset = UNSET
    logo: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        logo: None | str | Unset
        if isinstance(self.logo, Unset):
            logo = UNSET
        else:
            logo = self.logo

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if logo is not UNSET:
            field_dict["logo"] = logo
        if website is not UNSET:
            field_dict["website"] = website
        if date_added is not UNSET:
            field_dict["date_added"] = date_added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_logo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo = _parse_logo(d.pop("logo", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        _date_added = d.pop("date_added", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        rwa_info_results_object_rwa_assets_item_about = cls(
            description=description,
            logo=logo,
            website=website,
            date_added=date_added,
        )

        rwa_info_results_object_rwa_assets_item_about.additional_properties = d
        return rwa_info_results_object_rwa_assets_item_about

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
