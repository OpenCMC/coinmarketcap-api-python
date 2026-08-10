from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rwa_issuer_results_object_tokens_item import RWAIssuerResultsObjectTokensItem


T = TypeVar("T", bound="RWAIssuerResultsObject")


@_attrs_define
class RWAIssuerResultsObject:
    """Results of your query returned as an object.

    Example:
        {'name': 'Backpack', 'website': 'https://backpack.exchange', 'logo':
            'https://s2.coinmarketcap.com/static/img/issuer/M7sS2GzR_400x400.png', 'tokens': [{'name': 'SpaceX tokenized
            stock (Backpack)', 'symbol': 'SPCX', 'crypto_id': 40238, 'rwa_id': 9}], 'issuer_id': '6a2d54b697c45356b1a634f4',
            'num_tokens': 1, 'total_size': 1, 'has_more': False}

    Attributes:
        name (str | Unset): Issuer display name. Example: Backpack.
        website (None | str | Unset): Issuer website; `null` when absent. Example: https://backpack.exchange.
        logo (None | str | Unset): Single small-size logo URL; `null` when the issuer has no logo. Example:
            https://s2.coinmarketcap.com/static/img/issuer/M7sS2GzR_400x400.png.
        tokens (list[RWAIssuerResultsObjectTokensItem] | Unset): Tokens issued by this issuer.
        issuer_id (str | Unset): Issuer ID (24-char hex). Example: 6a2d54b697c45356b1a634f4.
        num_tokens (int | Unset): Total linked tokens for this issuer. Example: 1.
        total_size (int | Unset): Total number of matching records across all pages. Example: 1.
        has_more (bool | Unset): `true` if more records exist beyond this page, else `false`.
    """

    name: str | Unset = UNSET
    website: None | str | Unset = UNSET
    logo: None | str | Unset = UNSET
    tokens: list[RWAIssuerResultsObjectTokensItem] | Unset = UNSET
    issuer_id: str | Unset = UNSET
    num_tokens: int | Unset = UNSET
    total_size: int | Unset = UNSET
    has_more: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        logo: None | str | Unset
        if isinstance(self.logo, Unset):
            logo = UNSET
        else:
            logo = self.logo

        tokens: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tokens, Unset):
            tokens = []
            for tokens_item_data in self.tokens:
                tokens_item = tokens_item_data.to_dict()
                tokens.append(tokens_item)

        issuer_id = self.issuer_id

        num_tokens = self.num_tokens

        total_size = self.total_size

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if website is not UNSET:
            field_dict["website"] = website
        if logo is not UNSET:
            field_dict["logo"] = logo
        if tokens is not UNSET:
            field_dict["tokens"] = tokens
        if issuer_id is not UNSET:
            field_dict["issuer_id"] = issuer_id
        if num_tokens is not UNSET:
            field_dict["num_tokens"] = num_tokens
        if total_size is not UNSET:
            field_dict["total_size"] = total_size
        if has_more is not UNSET:
            field_dict["has_more"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rwa_issuer_results_object_tokens_item import RWAIssuerResultsObjectTokensItem

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_logo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo = _parse_logo(d.pop("logo", UNSET))

        _tokens = d.pop("tokens", UNSET)
        tokens: list[RWAIssuerResultsObjectTokensItem] | Unset = UNSET
        if _tokens is not UNSET:
            tokens = []
            for tokens_item_data in _tokens:
                tokens_item = RWAIssuerResultsObjectTokensItem.from_dict(tokens_item_data)

                tokens.append(tokens_item)

        issuer_id = d.pop("issuer_id", UNSET)

        num_tokens = d.pop("num_tokens", UNSET)

        total_size = d.pop("total_size", UNSET)

        has_more = d.pop("has_more", UNSET)

        rwa_issuer_results_object = cls(
            name=name,
            website=website,
            logo=logo,
            tokens=tokens,
            issuer_id=issuer_id,
            num_tokens=num_tokens,
            total_size=total_size,
            has_more=has_more,
        )

        rwa_issuer_results_object.additional_properties = d
        return rwa_issuer_results_object

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
