from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DexUrls")


@_attrs_define
class DexUrls:
    """An object containing various resource URLs for this exchange.

    Attributes:
        website (list[str] | Unset): Official website URLs.
        blog (list[str] | Unset): Official blog URLs.
        chat (list[str] | Unset): Official chat URLs.
        fee (list[str] | Unset): Official web URLs covering exchange fees.
        twitter (list[str] | Unset): Official twitter profile URLs.
    """

    website: list[str] | Unset = UNSET
    blog: list[str] | Unset = UNSET
    chat: list[str] | Unset = UNSET
    fee: list[str] | Unset = UNSET
    twitter: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        website: list[str] | Unset = UNSET
        if not isinstance(self.website, Unset):
            website = self.website

        blog: list[str] | Unset = UNSET
        if not isinstance(self.blog, Unset):
            blog = self.blog

        chat: list[str] | Unset = UNSET
        if not isinstance(self.chat, Unset):
            chat = self.chat

        fee: list[str] | Unset = UNSET
        if not isinstance(self.fee, Unset):
            fee = self.fee

        twitter: list[str] | Unset = UNSET
        if not isinstance(self.twitter, Unset):
            twitter = self.twitter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if website is not UNSET:
            field_dict["website"] = website
        if blog is not UNSET:
            field_dict["blog"] = blog
        if chat is not UNSET:
            field_dict["chat"] = chat
        if fee is not UNSET:
            field_dict["fee"] = fee
        if twitter is not UNSET:
            field_dict["twitter"] = twitter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        website = cast(list[str], d.pop("website", UNSET))

        blog = cast(list[str], d.pop("blog", UNSET))

        chat = cast(list[str], d.pop("chat", UNSET))

        fee = cast(list[str], d.pop("fee", UNSET))

        twitter = cast(list[str], d.pop("twitter", UNSET))

        dex_urls = cls(
            website=website,
            blog=blog,
            chat=chat,
            fee=fee,
            twitter=twitter,
        )

        dex_urls.additional_properties = d
        return dex_urls

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
