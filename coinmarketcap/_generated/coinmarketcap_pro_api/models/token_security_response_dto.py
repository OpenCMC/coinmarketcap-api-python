from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bn_security_extra_info_dto import BnSecurityExtraInfoDTO
    from ..models.display_item import DisplayItem
    from ..models.security_item import SecurityItem


T = TypeVar("T", bound="TokenSecurityResponseDTO")


@_attrs_define
class TokenSecurityResponseDTO:
    """Token security response

    Attributes:
        platform_name (str | Unset): Platform name Example: ethereum.
        platform_id (int | Unset): Platform ID Example: 1.
        token_contract_address (str | Unset): Token contract address Example: 0xabc123....
        security_level (str | Unset): Overall security level
        category_level (str | Unset): Overall category level
        security_batch_level (int | Unset): Overall security batch level
        extra (BnSecurityExtraInfoDTO | Unset): Extra security metadata provided by external vendors or on-chain
            analysis
        security_items (list[SecurityItem] | Unset): Detailed security items
        evm_display (DisplayItem | Unset): Security item display flags for EVM or Solana
        solana_display (DisplayItem | Unset): Security item display flags for EVM or Solana
        exist (bool | Unset): token security exist
        tags (list[str] | Unset): token security exist
    """

    platform_name: str | Unset = UNSET
    platform_id: int | Unset = UNSET
    token_contract_address: str | Unset = UNSET
    security_level: str | Unset = UNSET
    category_level: str | Unset = UNSET
    security_batch_level: int | Unset = UNSET
    extra: BnSecurityExtraInfoDTO | Unset = UNSET
    security_items: list[SecurityItem] | Unset = UNSET
    evm_display: DisplayItem | Unset = UNSET
    solana_display: DisplayItem | Unset = UNSET
    exist: bool | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform_name = self.platform_name

        platform_id = self.platform_id

        token_contract_address = self.token_contract_address

        security_level = self.security_level

        category_level = self.category_level

        security_batch_level = self.security_batch_level

        extra: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extra, Unset):
            extra = self.extra.to_dict()

        security_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.security_items, Unset):
            security_items = []
            for security_items_item_data in self.security_items:
                security_items_item = security_items_item_data.to_dict()
                security_items.append(security_items_item)

        evm_display: dict[str, Any] | Unset = UNSET
        if not isinstance(self.evm_display, Unset):
            evm_display = self.evm_display.to_dict()

        solana_display: dict[str, Any] | Unset = UNSET
        if not isinstance(self.solana_display, Unset):
            solana_display = self.solana_display.to_dict()

        exist = self.exist

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform_name is not UNSET:
            field_dict["platformName"] = platform_name
        if platform_id is not UNSET:
            field_dict["platformId"] = platform_id
        if token_contract_address is not UNSET:
            field_dict["tokenContractAddress"] = token_contract_address
        if security_level is not UNSET:
            field_dict["securityLevel"] = security_level
        if category_level is not UNSET:
            field_dict["categoryLevel"] = category_level
        if security_batch_level is not UNSET:
            field_dict["securityBatchLevel"] = security_batch_level
        if extra is not UNSET:
            field_dict["extra"] = extra
        if security_items is not UNSET:
            field_dict["securityItems"] = security_items
        if evm_display is not UNSET:
            field_dict["evmDisplay"] = evm_display
        if solana_display is not UNSET:
            field_dict["solanaDisplay"] = solana_display
        if exist is not UNSET:
            field_dict["exist"] = exist
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bn_security_extra_info_dto import BnSecurityExtraInfoDTO
        from ..models.display_item import DisplayItem
        from ..models.security_item import SecurityItem

        d = dict(src_dict)
        platform_name = d.pop("platformName", UNSET)

        platform_id = d.pop("platformId", UNSET)

        token_contract_address = d.pop("tokenContractAddress", UNSET)

        security_level = d.pop("securityLevel", UNSET)

        category_level = d.pop("categoryLevel", UNSET)

        security_batch_level = d.pop("securityBatchLevel", UNSET)

        _extra = d.pop("extra", UNSET)
        extra: BnSecurityExtraInfoDTO | Unset
        if isinstance(_extra, Unset):
            extra = UNSET
        else:
            extra = BnSecurityExtraInfoDTO.from_dict(_extra)

        _security_items = d.pop("securityItems", UNSET)
        security_items: list[SecurityItem] | Unset = UNSET
        if _security_items is not UNSET:
            security_items = []
            for security_items_item_data in _security_items:
                security_items_item = SecurityItem.from_dict(security_items_item_data)

                security_items.append(security_items_item)

        _evm_display = d.pop("evmDisplay", UNSET)
        evm_display: DisplayItem | Unset
        if isinstance(_evm_display, Unset):
            evm_display = UNSET
        else:
            evm_display = DisplayItem.from_dict(_evm_display)

        _solana_display = d.pop("solanaDisplay", UNSET)
        solana_display: DisplayItem | Unset
        if isinstance(_solana_display, Unset):
            solana_display = UNSET
        else:
            solana_display = DisplayItem.from_dict(_solana_display)

        exist = d.pop("exist", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        token_security_response_dto = cls(
            platform_name=platform_name,
            platform_id=platform_id,
            token_contract_address=token_contract_address,
            security_level=security_level,
            category_level=category_level,
            security_batch_level=security_batch_level,
            extra=extra,
            security_items=security_items,
            evm_display=evm_display,
            solana_display=solana_display,
            exist=exist,
            tags=tags,
        )

        token_security_response_dto.additional_properties = d
        return token_security_response_dto

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
