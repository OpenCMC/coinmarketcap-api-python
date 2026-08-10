from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DisplayItem")


@_attrs_define
class DisplayItem:
    """Security item display flags for EVM or Solana

    Attributes:
        honeypot_status (str | Unset): EVM - Honeypot status Example: Safe.
        unverified_contract_status (str | Unset): EVM - Unverified contract status Example: Verified.
        mintable_status (str | Unset): Solana - Mintable token status Example: Non-mintable.
        freezable_status (str | Unset): Solana - Freezable status Example: Non-freezable.
        rug_pull_status (str | Unset): Solana - Rug pull detection Example: No risk.
        fake_token_status (str | Unset): Solana - Fake token detection Example: Genuine.
    """

    honeypot_status: str | Unset = UNSET
    unverified_contract_status: str | Unset = UNSET
    mintable_status: str | Unset = UNSET
    freezable_status: str | Unset = UNSET
    rug_pull_status: str | Unset = UNSET
    fake_token_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        honeypot_status = self.honeypot_status

        unverified_contract_status = self.unverified_contract_status

        mintable_status = self.mintable_status

        freezable_status = self.freezable_status

        rug_pull_status = self.rug_pull_status

        fake_token_status = self.fake_token_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if honeypot_status is not UNSET:
            field_dict["honeypotStatus"] = honeypot_status
        if unverified_contract_status is not UNSET:
            field_dict["unverifiedContractStatus"] = unverified_contract_status
        if mintable_status is not UNSET:
            field_dict["mintableStatus"] = mintable_status
        if freezable_status is not UNSET:
            field_dict["freezableStatus"] = freezable_status
        if rug_pull_status is not UNSET:
            field_dict["rugPullStatus"] = rug_pull_status
        if fake_token_status is not UNSET:
            field_dict["fakeTokenStatus"] = fake_token_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        honeypot_status = d.pop("honeypotStatus", UNSET)

        unverified_contract_status = d.pop("unverifiedContractStatus", UNSET)

        mintable_status = d.pop("mintableStatus", UNSET)

        freezable_status = d.pop("freezableStatus", UNSET)

        rug_pull_status = d.pop("rugPullStatus", UNSET)

        fake_token_status = d.pop("fakeTokenStatus", UNSET)

        display_item = cls(
            honeypot_status=honeypot_status,
            unverified_contract_status=unverified_contract_status,
            mintable_status=mintable_status,
            freezable_status=freezable_status,
            rug_pull_status=rug_pull_status,
            fake_token_status=fake_token_status,
        )

        display_item.additional_properties = d
        return display_item

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
