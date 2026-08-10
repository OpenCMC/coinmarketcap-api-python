from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.cryptocurrency_info_results_map import CryptocurrencyInfoResultsMap


T = TypeVar("T", bound="CryptocurrenciesInfoResponseModel")


@_attrs_define
class CryptocurrenciesInfoResponseModel:
    """
    Attributes:
        data (CryptocurrencyInfoResultsMap): Results of your query returned as an object map. Example: {'1': {'urls':
            {'website': ['https://bitcoin.org/'], 'technical_doc': ['https://bitcoin.org/bitcoin.pdf'], 'twitter': [],
            'reddit': ['https://reddit.com/r/bitcoin'], 'message_board': ['https://bitcointalk.org'], 'announcement': [],
            'chat': [], 'explorer': ['https://blockchain.coinmarketcap.com/chain/bitcoin', 'https://blockchain.info/',
            'https://live.blockcypher.com/btc/'], 'source_code': ['https://github.com/bitcoin/']}, 'logo':
            'https://s2.coinmarketcap.com/static/img/coins/64x64/1.png', 'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC',
            'slug': 'bitcoin', 'description': 'Bitcoin (BTC) is a consensus network that enables a new payment system and a
            completely digital currency. Powered by its users, it is a peer to peer payment network that requires no central
            authority to operate. On October 31st, 2008, an individual or group of individuals operating under the pseudonym
            "Satoshi Nakamoto" published the Bitcoin Whitepaper and described it as: "a purely peer-to-peer version of
            electronic cash would allow online payments to be sent directly from one party to another without going through
            a financial institution."', 'date_added': '2013-04-28T00:00:00.000Z', 'date_launched':
            '2013-04-28T00:00:00.000Z', 'tags': ['mineable'], 'platform': None, 'category': 'coin'}}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: CryptocurrencyInfoResultsMap
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_status_object import APIStatusObject
        from ..models.cryptocurrency_info_results_map import CryptocurrencyInfoResultsMap

        d = dict(src_dict)
        data = CryptocurrencyInfoResultsMap.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        cryptocurrencies_info_response_model = cls(
            data=data,
            status=status,
        )

        cryptocurrencies_info_response_model.additional_properties = d
        return cryptocurrencies_info_response_model

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
