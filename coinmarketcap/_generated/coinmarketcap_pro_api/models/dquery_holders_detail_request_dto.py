from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DqueryHoldersDetailRequestDTO")


@_attrs_define
class DqueryHoldersDetailRequestDTO:
    """holders detail request

    Attributes:
        token_address (str | Unset): Token contract address Example: 0x1234567890abcdef1234567890abcdef12345678.
        wallet_address (str | Unset): Wallet address Example: 0xabcdef1234567890abcdef1234567890abcdef12.
        platform (str | Unset): Blockchain platform Example: ethereum.
        tag (str | Unset): tag enum [tag_all, tag_kol, tag_smart_money, tag_whale, tag_bot, tag_sniper, tag_dev]
            Example: tag_all.
    """

    token_address: str | Unset = UNSET
    wallet_address: str | Unset = UNSET
    platform: str | Unset = UNSET
    tag: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token_address = self.token_address

        wallet_address = self.wallet_address

        platform = self.platform

        tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token_address is not UNSET:
            field_dict["tokenAddress"] = token_address
        if wallet_address is not UNSET:
            field_dict["walletAddress"] = wallet_address
        if platform is not UNSET:
            field_dict["platform"] = platform
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token_address = d.pop("tokenAddress", UNSET)

        wallet_address = d.pop("walletAddress", UNSET)

        platform = d.pop("platform", UNSET)

        tag = d.pop("tag", UNSET)

        dquery_holders_detail_request_dto = cls(
            token_address=token_address,
            wallet_address=wallet_address,
            platform=platform,
            tag=tag,
        )

        dquery_holders_detail_request_dto.additional_properties = d
        return dquery_holders_detail_request_dto

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
