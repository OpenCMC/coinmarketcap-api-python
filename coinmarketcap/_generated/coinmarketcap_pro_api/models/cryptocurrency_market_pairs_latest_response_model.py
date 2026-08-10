from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.cryptocurrency_market_pairs_latest_results_object import CryptocurrencyMarketPairsLatestResultsObject


T = TypeVar("T", bound="CryptocurrencyMarketPairsLatestResponseModel")


@_attrs_define
class CryptocurrencyMarketPairsLatestResponseModel:
    """
    Attributes:
        data (CryptocurrencyMarketPairsLatestResultsObject): Results of your query returned as an object. Example:
            {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'num_market_pairs': 7526, 'market_pairs': [{'exchange': {'id':
            157, 'name': 'BitMEX', 'slug': 'bitmex'}, 'market_id': 4902, 'market_pair': 'BTC/USD', 'category':
            'derivatives', 'fee_type': 'no-fees', 'market_pair_base': {'currency_id': 1, 'currency_symbol': 'BTC',
            'exchange_symbol': 'XBT', 'currency_type': 'cryptocurrency'}, 'market_pair_quote': {'currency_id': 2781,
            'currency_symbol': 'USD', 'exchange_symbol': 'USD', 'currency_type': 'fiat'}, 'quote': {'exchange_reported':
            {'price': 7839, 'volume_24h_base': 434215.85308502, 'volume_24h_quote': 3403818072.33347, 'last_updated':
            '2019-05-24T02:39:00.000Z'}, 'USD': {'price': 7839, 'volume_24h': 3403818072.33347, 'last_updated':
            '2019-05-24T02:39:00.000Z'}}}, {'exchange': {'id': 108, 'name': 'Negocie Coins', 'slug': 'negocie-coins'},
            'market_id': 3377, 'market_pair': 'BTC/BRL', 'category': 'spot', 'fee_type': 'percentage', 'market_pair_base':
            {'currency_id': 1, 'currency_symbol': 'BTC', 'exchange_symbol': 'BTC', 'currency_type': 'cryptocurrency'},
            'market_pair_quote': {'currency_id': 2783, 'currency_symbol': 'BRL', 'exchange_symbol': 'BRL', 'currency_type':
            'fiat'}, 'quote': {'exchange_reported': {'price': 33002.11, 'volume_24h_base': 336699.03559957,
            'volume_24h_quote': 11111778609.7509, 'last_updated': '2019-05-24T02:39:00.000Z'}, 'USD': {'price':
            8165.02539531659, 'volume_24h': 2749156176.2491, 'last_updated': '2019-05-24T02:39:00.000Z'}}}]}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: CryptocurrencyMarketPairsLatestResultsObject
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
        from ..models.cryptocurrency_market_pairs_latest_results_object import (
            CryptocurrencyMarketPairsLatestResultsObject,
        )

        d = dict(src_dict)
        data = CryptocurrencyMarketPairsLatestResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        cryptocurrency_market_pairs_latest_response_model = cls(
            data=data,
            status=status,
        )

        cryptocurrency_market_pairs_latest_response_model.additional_properties = d
        return cryptocurrency_market_pairs_latest_response_model

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
