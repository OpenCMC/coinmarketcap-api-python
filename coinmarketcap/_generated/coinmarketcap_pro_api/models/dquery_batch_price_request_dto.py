from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.platform_address import PlatformAddress


T = TypeVar("T", bound="DqueryBatchPriceRequestDTO")


@_attrs_define
class DqueryBatchPriceRequestDTO:
    """Batch price query request

    Attributes:
        tokens (list[PlatformAddress] | Unset): List of platform-address pairs
    """

    tokens: list[PlatformAddress] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tokens: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tokens, Unset):
            tokens = []
            for tokens_item_data in self.tokens:
                tokens_item = tokens_item_data.to_dict()
                tokens.append(tokens_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tokens is not UNSET:
            field_dict["tokens"] = tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.platform_address import PlatformAddress

        d = dict(src_dict)
        _tokens = d.pop("tokens", UNSET)
        tokens: list[PlatformAddress] | Unset = UNSET
        if _tokens is not UNSET:
            tokens = []
            for tokens_item_data in _tokens:
                tokens_item = PlatformAddress.from_dict(tokens_item_data)

                tokens.append(tokens_item)

        dquery_batch_price_request_dto = cls(
            tokens=tokens,
        )

        dquery_batch_price_request_dto.additional_properties = d
        return dquery_batch_price_request_dto

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
