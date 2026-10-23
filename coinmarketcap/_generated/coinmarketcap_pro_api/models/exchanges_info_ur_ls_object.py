from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

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
        actual (list[str] | Unset): Links to the exchange's main trading website.
        register (list[str] | Unset): Links to the exchange's sign-up page.
    """

    website: list[str]
    blog: list[str]
    chat: list[str]
    fee: list[str]
    twitter: list[str]
    actual: list[str] | Unset = UNSET
    register: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        website = self.website

        blog = self.blog

        chat = self.chat

        fee = self.fee

        twitter = self.twitter

        actual: list[str] | Unset = UNSET
        if not isinstance(self.actual, Unset):
            actual = self.actual

        register: list[str] | Unset = UNSET
        if not isinstance(self.register, Unset):
            register = self.register

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
        if actual is not UNSET:
            field_dict["actual"] = actual
        if register is not UNSET:
            field_dict["register"] = register

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        website = cast(list[str], d.pop("website"))

        blog = cast(list[str], d.pop("blog"))

        chat = cast(list[str], d.pop("chat"))

        fee = cast(list[str], d.pop("fee"))

        twitter = cast(list[str], d.pop("twitter"))

        actual = cast(list[str], d.pop("actual", UNSET))

        register = cast(list[str], d.pop("register", UNSET))

        exchanges_info_ur_ls_object = cls(
            website=website,
            blog=blog,
            chat=chat,
            fee=fee,
            twitter=twitter,
            actual=actual,
            register=register,
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
