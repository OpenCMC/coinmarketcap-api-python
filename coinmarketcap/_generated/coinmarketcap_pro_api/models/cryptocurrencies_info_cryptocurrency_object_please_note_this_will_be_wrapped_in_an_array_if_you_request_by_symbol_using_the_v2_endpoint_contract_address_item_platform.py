from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cryptocurrencies_info_cryptocurrency_object_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint_contract_address_item_platform_coin import (
        CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2EndpointContractAddressItemPlatformCoin,
    )


T = TypeVar(
    "T",
    bound="CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2EndpointContractAddressItemPlatform",
)


@_attrs_define
class CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2EndpointContractAddressItemPlatform:
    """The platform this contract address belongs to.

    Attributes:
        name (str | Unset): Platform name.
        coin (CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2
            EndpointContractAddressItemPlatformCoin | Unset): The platform's native cryptocurrency.
    """

    name: str | Unset = UNSET
    coin: (
        CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2EndpointContractAddressItemPlatformCoin
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        coin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coin, Unset):
            coin = self.coin.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if coin is not UNSET:
            field_dict["coin"] = coin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrencies_info_cryptocurrency_object_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint_contract_address_item_platform_coin import (
            CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2EndpointContractAddressItemPlatformCoin,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _coin = d.pop("coin", UNSET)
        coin: (
            CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2EndpointContractAddressItemPlatformCoin
            | Unset
        )
        if isinstance(_coin, Unset):
            coin = UNSET
        else:
            coin = CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2EndpointContractAddressItemPlatformCoin.from_dict(
                _coin
            )

        cryptocurrencies_info_cryptocurrency_object_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint_contract_address_item_platform = cls(
            name=name,
            coin=coin,
        )

        cryptocurrencies_info_cryptocurrency_object_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint_contract_address_item_platform.additional_properties = d
        return cryptocurrencies_info_cryptocurrency_object_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint_contract_address_item_platform

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
