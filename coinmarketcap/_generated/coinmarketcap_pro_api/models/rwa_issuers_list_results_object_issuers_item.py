from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RWAIssuersListResultsObjectIssuersItem")


@_attrs_define
class RWAIssuersListResultsObjectIssuersItem:
    """
    Attributes:
        name (str | Unset): Issuer display name (e.g. `Backpack`). Example: Backpack.
        website (None | str | Unset): Issuer website; `null` when absent. Example: https://backpack.exchange.
        logo (None | str | Unset): Single small-size logo URL; `null` when the issuer has no logo. Example:
            https://s2.coinmarketcap.com/static/img/issuer/M7sS2GzR_400x400.png.
        issuer_id (str | Unset): Issuer ID (24-char hex), the stable identifier for issuer lookups. Example:
            6a2d54b697c45356b1a634f4.
        num_tokens (int | Unset): Number of linked tokens (cryptos) for this issuer; may be `0`. Example: 1.
    """

    name: str | Unset = UNSET
    website: None | str | Unset = UNSET
    logo: None | str | Unset = UNSET
    issuer_id: str | Unset = UNSET
    num_tokens: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        logo: None | str | Unset
        if isinstance(self.logo, Unset):
            logo = UNSET
        else:
            logo = self.logo

        issuer_id = self.issuer_id

        num_tokens = self.num_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if website is not UNSET:
            field_dict["website"] = website
        if logo is not UNSET:
            field_dict["logo"] = logo
        if issuer_id is not UNSET:
            field_dict["issuer_id"] = issuer_id
        if num_tokens is not UNSET:
            field_dict["num_tokens"] = num_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_logo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo = _parse_logo(d.pop("logo", UNSET))

        issuer_id = d.pop("issuer_id", UNSET)

        num_tokens = d.pop("num_tokens", UNSET)

        rwa_issuers_list_results_object_issuers_item = cls(
            name=name,
            website=website,
            logo=logo,
            issuer_id=issuer_id,
            num_tokens=num_tokens,
        )

        rwa_issuers_list_results_object_issuers_item.additional_properties = d
        return rwa_issuers_list_results_object_issuers_item

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
