from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cryptocurrencies_info_cryptocurrency_object_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint import (
        CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2Endpoint,
    )


T = TypeVar("T", bound="CryptocurrencyInfoResultsMap")


@_attrs_define
class CryptocurrencyInfoResultsMap:
    """Results of your query returned as an object map.

    Example:
        {'1': {'urls': {'website': ['https://bitcoin.org/'], 'technical_doc': ['https://bitcoin.org/bitcoin.pdf'],
            'twitter': [], 'reddit': ['https://reddit.com/r/bitcoin'], 'message_board': ['https://bitcointalk.org'],
            'announcement': [], 'chat': [], 'explorer': ['https://blockchain.coinmarketcap.com/chain/bitcoin',
            'https://blockchain.info/', 'https://live.blockcypher.com/btc/'], 'source_code':
            ['https://github.com/bitcoin/']}, 'logo': 'https://s2.coinmarketcap.com/static/img/coins/64x64/1.png', 'id': 1,
            'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'description': 'Bitcoin (BTC) is a consensus network that
            enables a new payment system and a completely digital currency. Powered by its users, it is a peer to peer
            payment network that requires no central authority to operate. On October 31st, 2008, an individual or group of
            individuals operating under the pseudonym "Satoshi Nakamoto" published the Bitcoin Whitepaper and described it
            as: "a purely peer-to-peer version of electronic cash would allow online payments to be sent directly from one
            party to another without going through a financial institution."', 'date_added': '2013-04-28T00:00:00.000Z',
            'date_launched': '2013-04-28T00:00:00.000Z', 'tags': ['mineable'], 'platform': None, 'category': 'coin'}}

    """

    additional_properties: dict[
        str,
        CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2Endpoint,
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrencies_info_cryptocurrency_object_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint import (
            CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2Endpoint,
        )

        d = dict(src_dict)
        cryptocurrency_info_results_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2Endpoint.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        cryptocurrency_info_results_map.additional_properties = additional_properties
        return cryptocurrency_info_results_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2Endpoint:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2Endpoint,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
