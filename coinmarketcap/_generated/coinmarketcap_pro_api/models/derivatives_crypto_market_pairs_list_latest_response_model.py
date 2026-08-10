from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.derivatives_crypto_market_pairs_list_latest_results_object import (
        DerivativesCryptoMarketPairsListLatestResultsObject,
    )


T = TypeVar("T", bound="DerivativesCryptoMarketPairsListLatestResponseModel")


@_attrs_define
class DerivativesCryptoMarketPairsListLatestResponseModel:
    """
    Attributes:
        data (DerivativesCryptoMarketPairsListLatestResultsObject): Results of your query returned as an object.
            Example: {'crypto_id': 1, 'crypto_name': 'Bitcoin', 'symbol': 'BTC', 'num_market_pairs': 5, 'market_pairs':
            [{'market_id': 79477, 'market_pair': 'BTC/USDT', 'category': 'perpetual', 'fee_type': 'percentage',
            'outlier_detected': False, 'exclusions': None, 'exchange': {'exchange_id': 270, 'exchange_name': 'Binance',
            'exchange_slug': 'binance'}, 'market_pair_base': {'crypto_id': 1, 'symbol': 'BTC', 'exchange_symbol': 'BTC',
            'currency_type': 'cryptocurrency'}, 'market_pair_quote': {'crypto_id': 825, 'symbol': 'USDT', 'exchange_symbol':
            'USDT', 'currency_type': 'cryptocurrency'}, 'exchange_reported_quotes': [{'crypto_id': 2781, 'symbol': 'USD',
            'price': 80496.6, 'volume_24h_base': 686357.90331837, 'volume_24h_quote': 55249477600.25728, 'open_interest':
            5000000, 'index_price': 80498.5, 'index_basis': 0.0023, 'funding_rate': 0.0001, 'last_updated':
            '2026-05-15T06:36:15.586Z'}], 'quotes': [{'crypto_id': 2781, 'symbol': 'USD', 'price': 80470.69372308,
            'volume_24h': 55231696622.35106, 'open_interest': 5000000, 'last_updated': '2026-05-15T06:36:15.586Z'}]}]}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: DerivativesCryptoMarketPairsListLatestResultsObject
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
        from ..models.derivatives_crypto_market_pairs_list_latest_results_object import (
            DerivativesCryptoMarketPairsListLatestResultsObject,
        )

        d = dict(src_dict)
        data = DerivativesCryptoMarketPairsListLatestResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        derivatives_crypto_market_pairs_list_latest_response_model = cls(
            data=data,
            status=status,
        )

        derivatives_crypto_market_pairs_list_latest_response_model.additional_properties = d
        return derivatives_crypto_market_pairs_list_latest_response_model

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
