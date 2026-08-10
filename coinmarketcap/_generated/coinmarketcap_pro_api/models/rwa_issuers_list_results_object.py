from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rwa_issuers_list_results_object_issuers_item import RWAIssuersListResultsObjectIssuersItem


T = TypeVar("T", bound="RWAIssuersListResultsObject")


@_attrs_define
class RWAIssuersListResultsObject:
    """Results of your query returned as an object.

    Example:
        {'issuers': [{'name': 'Backed Assets', 'website': 'https://assets.backed.fi/', 'logo': None, 'issuer_id':
            '6878977dcbbf471de3366e85', 'num_tokens': 147}, {'name': 'Backpack', 'website': 'https://backpack.exchange',
            'logo': 'https://s2.coinmarketcap.com/static/img/issuer/M7sS2GzR_400x400.png', 'issuer_id':
            '6a2d54b697c45356b1a634f4', 'num_tokens': 1}, {'name': 'Bitget Assets', 'website': 'https://www.bitget.com/',
            'logo': None, 'issuer_id': '68a80be20135f56ec3188cdc', 'num_tokens': 0}], 'total_size': 24, 'has_more': True}

    Attributes:
        issuers (list[RWAIssuersListResultsObjectIssuersItem] | Unset): Array of issuer objects.
        total_size (int | Unset): Total number of matching records across all pages. Example: 24.
        has_more (bool | Unset): `true` if more records exist beyond this page, else `false`. Example: True.
    """

    issuers: list[RWAIssuersListResultsObjectIssuersItem] | Unset = UNSET
    total_size: int | Unset = UNSET
    has_more: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issuers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.issuers, Unset):
            issuers = []
            for issuers_item_data in self.issuers:
                issuers_item = issuers_item_data.to_dict()
                issuers.append(issuers_item)

        total_size = self.total_size

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issuers is not UNSET:
            field_dict["issuers"] = issuers
        if total_size is not UNSET:
            field_dict["total_size"] = total_size
        if has_more is not UNSET:
            field_dict["has_more"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rwa_issuers_list_results_object_issuers_item import RWAIssuersListResultsObjectIssuersItem

        d = dict(src_dict)
        _issuers = d.pop("issuers", UNSET)
        issuers: list[RWAIssuersListResultsObjectIssuersItem] | Unset = UNSET
        if _issuers is not UNSET:
            issuers = []
            for issuers_item_data in _issuers:
                issuers_item = RWAIssuersListResultsObjectIssuersItem.from_dict(issuers_item_data)

                issuers.append(issuers_item)

        total_size = d.pop("total_size", UNSET)

        has_more = d.pop("has_more", UNSET)

        rwa_issuers_list_results_object = cls(
            issuers=issuers,
            total_size=total_size,
            has_more=has_more,
        )

        rwa_issuers_list_results_object.additional_properties = d
        return rwa_issuers_list_results_object

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
