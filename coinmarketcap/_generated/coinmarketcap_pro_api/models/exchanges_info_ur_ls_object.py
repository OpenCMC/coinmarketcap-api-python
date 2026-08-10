from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExchangesInfoURLsObject")


@_attrs_define
class ExchangesInfoURLsObject:
    """An object containing various resource URLs for this exchange.

    Attributes:
        website (list[str]): Official website URLs. Example: ['https://binance.com'].
        blog (list[str]): Official blog URLs. Example: ['https://blog.kraken.com/'].
        chat (list[str]): Official chat URLs. Example: ['https://t.me/coinbene'].
        fee (list[str]): Official web URLs covering exchange fees. Example: ['https://www.gdax.com/fees'].
        twitter (list[str]): Official twitter profile URLs. Example: ['https://twitter.com/Bitcoin'].
    """

    website: list[str]
    blog: list[str]
    chat: list[str]
    fee: list[str]
    twitter: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        website = self.website

        blog = self.blog

        chat = self.chat

        fee = self.fee

        twitter = self.twitter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "website": website,
                "blog": blog,
                "chat": chat,
                "fee": fee,
                "twitter": twitter,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        website = cast(list[str], d.pop("website"))

        blog = cast(list[str], d.pop("blog"))

        chat = cast(list[str], d.pop("chat"))

        fee = cast(list[str], d.pop("fee"))

        twitter = cast(list[str], d.pop("twitter"))

        exchanges_info_ur_ls_object = cls(
            website=website,
            blog=blog,
            chat=chat,
            fee=fee,
            twitter=twitter,
        )

        exchanges_info_ur_ls_object.additional_properties = d
        return exchanges_info_ur_ls_object

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
