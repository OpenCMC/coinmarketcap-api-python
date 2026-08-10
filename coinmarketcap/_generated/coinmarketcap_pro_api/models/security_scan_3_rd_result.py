from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SecurityScan3RdResult")


@_attrs_define
class SecurityScan3RdResult:
    """
    Attributes:
        open_source (bool | Unset):
        proxy (bool | Unset):
        mintable (bool | Unset):
        can_take_back_ownership (bool | Unset):
        owner_change_balance (bool | Unset):
        hidden_owner (bool | Unset):
        self_destruct (bool | Unset):
        external_call (bool | Unset):
        cannot_buy (bool | Unset):
        cannot_sell_all (bool | Unset):
        slippage_modifiable (bool | Unset):
        honeypot (bool | Unset):
        transfer_pausable (bool | Unset):
        blacklisted (bool | Unset):
        whitelisted (bool | Unset):
        in_dex (bool | Unset):
        anti_whale (bool | Unset):
        anti_whale_modifiable (bool | Unset):
        trading_cool_down (bool | Unset):
        personal_slippage_modifiable (bool | Unset):
        trust_list (bool | Unset):
        true_token (bool | Unset):
        airdrop_scam (bool | Unset):
    """

    open_source: bool | Unset = UNSET
    proxy: bool | Unset = UNSET
    mintable: bool | Unset = UNSET
    can_take_back_ownership: bool | Unset = UNSET
    owner_change_balance: bool | Unset = UNSET
    hidden_owner: bool | Unset = UNSET
    self_destruct: bool | Unset = UNSET
    external_call: bool | Unset = UNSET
    cannot_buy: bool | Unset = UNSET
    cannot_sell_all: bool | Unset = UNSET
    slippage_modifiable: bool | Unset = UNSET
    honeypot: bool | Unset = UNSET
    transfer_pausable: bool | Unset = UNSET
    blacklisted: bool | Unset = UNSET
    whitelisted: bool | Unset = UNSET
    in_dex: bool | Unset = UNSET
    anti_whale: bool | Unset = UNSET
    anti_whale_modifiable: bool | Unset = UNSET
    trading_cool_down: bool | Unset = UNSET
    personal_slippage_modifiable: bool | Unset = UNSET
    trust_list: bool | Unset = UNSET
    true_token: bool | Unset = UNSET
    airdrop_scam: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_source = self.open_source

        proxy = self.proxy

        mintable = self.mintable

        can_take_back_ownership = self.can_take_back_ownership

        owner_change_balance = self.owner_change_balance

        hidden_owner = self.hidden_owner

        self_destruct = self.self_destruct

        external_call = self.external_call

        cannot_buy = self.cannot_buy

        cannot_sell_all = self.cannot_sell_all

        slippage_modifiable = self.slippage_modifiable

        honeypot = self.honeypot

        transfer_pausable = self.transfer_pausable

        blacklisted = self.blacklisted

        whitelisted = self.whitelisted

        in_dex = self.in_dex

        anti_whale = self.anti_whale

        anti_whale_modifiable = self.anti_whale_modifiable

        trading_cool_down = self.trading_cool_down

        personal_slippage_modifiable = self.personal_slippage_modifiable

        trust_list = self.trust_list

        true_token = self.true_token

        airdrop_scam = self.airdrop_scam

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if open_source is not UNSET:
            field_dict["open_source"] = open_source
        if proxy is not UNSET:
            field_dict["proxy"] = proxy
        if mintable is not UNSET:
            field_dict["mintable"] = mintable
        if can_take_back_ownership is not UNSET:
            field_dict["can_take_back_ownership"] = can_take_back_ownership
        if owner_change_balance is not UNSET:
            field_dict["owner_change_balance"] = owner_change_balance
        if hidden_owner is not UNSET:
            field_dict["hidden_owner"] = hidden_owner
        if self_destruct is not UNSET:
            field_dict["self_destruct"] = self_destruct
        if external_call is not UNSET:
            field_dict["external_call"] = external_call
        if cannot_buy is not UNSET:
            field_dict["cannot_buy"] = cannot_buy
        if cannot_sell_all is not UNSET:
            field_dict["cannot_sell_all"] = cannot_sell_all
        if slippage_modifiable is not UNSET:
            field_dict["slippage_modifiable"] = slippage_modifiable
        if honeypot is not UNSET:
            field_dict["honeypot"] = honeypot
        if transfer_pausable is not UNSET:
            field_dict["transfer_pausable"] = transfer_pausable
        if blacklisted is not UNSET:
            field_dict["blacklisted"] = blacklisted
        if whitelisted is not UNSET:
            field_dict["whitelisted"] = whitelisted
        if in_dex is not UNSET:
            field_dict["in_dex"] = in_dex
        if anti_whale is not UNSET:
            field_dict["anti_whale"] = anti_whale
        if anti_whale_modifiable is not UNSET:
            field_dict["anti_whale_modifiable"] = anti_whale_modifiable
        if trading_cool_down is not UNSET:
            field_dict["trading_cool_down"] = trading_cool_down
        if personal_slippage_modifiable is not UNSET:
            field_dict["personal_slippage_modifiable"] = personal_slippage_modifiable
        if trust_list is not UNSET:
            field_dict["trust_list"] = trust_list
        if true_token is not UNSET:
            field_dict["true_token"] = true_token
        if airdrop_scam is not UNSET:
            field_dict["airdrop_scam"] = airdrop_scam

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        open_source = d.pop("open_source", UNSET)

        proxy = d.pop("proxy", UNSET)

        mintable = d.pop("mintable", UNSET)

        can_take_back_ownership = d.pop("can_take_back_ownership", UNSET)

        owner_change_balance = d.pop("owner_change_balance", UNSET)

        hidden_owner = d.pop("hidden_owner", UNSET)

        self_destruct = d.pop("self_destruct", UNSET)

        external_call = d.pop("external_call", UNSET)

        cannot_buy = d.pop("cannot_buy", UNSET)

        cannot_sell_all = d.pop("cannot_sell_all", UNSET)

        slippage_modifiable = d.pop("slippage_modifiable", UNSET)

        honeypot = d.pop("honeypot", UNSET)

        transfer_pausable = d.pop("transfer_pausable", UNSET)

        blacklisted = d.pop("blacklisted", UNSET)

        whitelisted = d.pop("whitelisted", UNSET)

        in_dex = d.pop("in_dex", UNSET)

        anti_whale = d.pop("anti_whale", UNSET)

        anti_whale_modifiable = d.pop("anti_whale_modifiable", UNSET)

        trading_cool_down = d.pop("trading_cool_down", UNSET)

        personal_slippage_modifiable = d.pop("personal_slippage_modifiable", UNSET)

        trust_list = d.pop("trust_list", UNSET)

        true_token = d.pop("true_token", UNSET)

        airdrop_scam = d.pop("airdrop_scam", UNSET)

        security_scan_3_rd_result = cls(
            open_source=open_source,
            proxy=proxy,
            mintable=mintable,
            can_take_back_ownership=can_take_back_ownership,
            owner_change_balance=owner_change_balance,
            hidden_owner=hidden_owner,
            self_destruct=self_destruct,
            external_call=external_call,
            cannot_buy=cannot_buy,
            cannot_sell_all=cannot_sell_all,
            slippage_modifiable=slippage_modifiable,
            honeypot=honeypot,
            transfer_pausable=transfer_pausable,
            blacklisted=blacklisted,
            whitelisted=whitelisted,
            in_dex=in_dex,
            anti_whale=anti_whale,
            anti_whale_modifiable=anti_whale_modifiable,
            trading_cool_down=trading_cool_down,
            personal_slippage_modifiable=personal_slippage_modifiable,
            trust_list=trust_list,
            true_token=true_token,
            airdrop_scam=airdrop_scam,
        )

        security_scan_3_rd_result.additional_properties = d
        return security_scan_3_rd_result

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
