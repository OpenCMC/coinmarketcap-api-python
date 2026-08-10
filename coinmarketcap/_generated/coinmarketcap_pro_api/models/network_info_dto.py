from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkInfoDTO")


@_attrs_define
class NetworkInfoDTO:
    """
    Attributes:
        id (int | Unset): The unique CoinMarketCap ID for this network.
        name (str | Unset): The name of this network.
        alternative_name (str | Unset): The alternate name for this network.
        cryptocurrency_id (str | Unset): The unique CoinMarketCap identifier for the cryptocurrency associated with this
            network.
        cryptocurrency_slug (str | Unset): The slug(URL-friendly name) for the associated cryptocurrency
        wrapped_token_id (str | Unset): The unique identifier for the wrapped token on this network.
        wrapped_token_slug (str | Unset): The slug(URL-friendly name) for the wrapped token on this network.
        token_explorer_url (str | Unset): The URL for exploring tokens on this network.
        pool_explorer_url (str | Unset): The URL for exploring liquidity pools on this network.
        transaction_hash_url (str | Unset): The URL for exploring transaction hashes on this network.
        network_slug (str | Unset): The slug of the network the spot pair is on.
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    alternative_name: str | Unset = UNSET
    cryptocurrency_id: str | Unset = UNSET
    cryptocurrency_slug: str | Unset = UNSET
    wrapped_token_id: str | Unset = UNSET
    wrapped_token_slug: str | Unset = UNSET
    token_explorer_url: str | Unset = UNSET
    pool_explorer_url: str | Unset = UNSET
    transaction_hash_url: str | Unset = UNSET
    network_slug: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        alternative_name = self.alternative_name

        cryptocurrency_id = self.cryptocurrency_id

        cryptocurrency_slug = self.cryptocurrency_slug

        wrapped_token_id = self.wrapped_token_id

        wrapped_token_slug = self.wrapped_token_slug

        token_explorer_url = self.token_explorer_url

        pool_explorer_url = self.pool_explorer_url

        transaction_hash_url = self.transaction_hash_url

        network_slug = self.network_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if alternative_name is not UNSET:
            field_dict["alternativeName"] = alternative_name
        if cryptocurrency_id is not UNSET:
            field_dict["cryptocurrencyId"] = cryptocurrency_id
        if cryptocurrency_slug is not UNSET:
            field_dict["cryptocurrencySlug"] = cryptocurrency_slug
        if wrapped_token_id is not UNSET:
            field_dict["wrappedTokenId"] = wrapped_token_id
        if wrapped_token_slug is not UNSET:
            field_dict["wrappedTokenSlug"] = wrapped_token_slug
        if token_explorer_url is not UNSET:
            field_dict["tokenExplorerUrl"] = token_explorer_url
        if pool_explorer_url is not UNSET:
            field_dict["poolExplorerUrl"] = pool_explorer_url
        if transaction_hash_url is not UNSET:
            field_dict["transactionHashUrl"] = transaction_hash_url
        if network_slug is not UNSET:
            field_dict["network_slug"] = network_slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        alternative_name = d.pop("alternativeName", UNSET)

        cryptocurrency_id = d.pop("cryptocurrencyId", UNSET)

        cryptocurrency_slug = d.pop("cryptocurrencySlug", UNSET)

        wrapped_token_id = d.pop("wrappedTokenId", UNSET)

        wrapped_token_slug = d.pop("wrappedTokenSlug", UNSET)

        token_explorer_url = d.pop("tokenExplorerUrl", UNSET)

        pool_explorer_url = d.pop("poolExplorerUrl", UNSET)

        transaction_hash_url = d.pop("transactionHashUrl", UNSET)

        network_slug = d.pop("network_slug", UNSET)

        network_info_dto = cls(
            id=id,
            name=name,
            alternative_name=alternative_name,
            cryptocurrency_id=cryptocurrency_id,
            cryptocurrency_slug=cryptocurrency_slug,
            wrapped_token_id=wrapped_token_id,
            wrapped_token_slug=wrapped_token_slug,
            token_explorer_url=token_explorer_url,
            pool_explorer_url=pool_explorer_url,
            transaction_hash_url=transaction_hash_url,
            network_slug=network_slug,
        )

        network_info_dto.additional_properties = d
        return network_info_dto

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
