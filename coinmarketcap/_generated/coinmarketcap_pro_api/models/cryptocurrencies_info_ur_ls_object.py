from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CryptocurrenciesInfoURLsObject")


@_attrs_define
class CryptocurrenciesInfoURLsObject:
    """An object containing various resource URLs for this cryptocurrency.

    Attributes:
        website (list[str]): Array of website URLs. Example: ['https://bitcoin.org/'].
        technical_doc (list[str]): Array of white paper or technical documentation URLs. Example:
            ['https://bitcoin.org/bitcoin.pdf'].
        explorer (list[str]): Array of block explorer URLs. Example:
            ['https://blockchain.coinmarketcap.com/chain/bitcoin', 'https://blockchain.info/',
            'https://live.blockcypher.com/btc/'].
        source_code (list[str]): Array of source code URLs. Example: ['https://github.com/bitcoin/'].
        message_board (list[str]): Array of message board URLs. Example: ['https://bitcointalk.org'].
        chat (list[str]): Array of chat service URLs.
        announcement (list[str]): Array of announcement URLs.
        reddit (list[str]): Array of Reddit community page URLs. Example: ['https://reddit.com/r/bitcoin'].
        twitter (list[str]): Array of official twitter profile URLs. Example: ['https://twitter.com/Bitcoin'].
    """

    website: list[str]
    technical_doc: list[str]
    explorer: list[str]
    source_code: list[str]
    message_board: list[str]
    chat: list[str]
    announcement: list[str]
    reddit: list[str]
    twitter: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        website = self.website

        technical_doc = self.technical_doc

        explorer = self.explorer

        source_code = self.source_code

        message_board = self.message_board

        chat = self.chat

        announcement = self.announcement

        reddit = self.reddit

        twitter = self.twitter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "website": website,
                "technical_doc": technical_doc,
                "explorer": explorer,
                "source_code": source_code,
                "message_board": message_board,
                "chat": chat,
                "announcement": announcement,
                "reddit": reddit,
                "twitter": twitter,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        website = cast(list[str], d.pop("website"))

        technical_doc = cast(list[str], d.pop("technical_doc"))

        explorer = cast(list[str], d.pop("explorer"))

        source_code = cast(list[str], d.pop("source_code"))

        message_board = cast(list[str], d.pop("message_board"))

        chat = cast(list[str], d.pop("chat"))

        announcement = cast(list[str], d.pop("announcement"))

        reddit = cast(list[str], d.pop("reddit"))

        twitter = cast(list[str], d.pop("twitter"))

        cryptocurrencies_info_ur_ls_object = cls(
            website=website,
            technical_doc=technical_doc,
            explorer=explorer,
            source_code=source_code,
            message_board=message_board,
            chat=chat,
            announcement=announcement,
            reddit=reddit,
            twitter=twitter,
        )

        cryptocurrencies_info_ur_ls_object.additional_properties = d
        return cryptocurrencies_info_ur_ls_object

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
