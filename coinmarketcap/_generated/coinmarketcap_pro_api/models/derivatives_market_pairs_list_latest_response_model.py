from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.derivatives_market_pairs_list_latest_results_object import (
        DerivativesMarketPairsListLatestResultsObject,
    )


T = TypeVar("T", bound="DerivativesMarketPairsListLatestResponseModel")


@_attrs_define
class DerivativesMarketPairsListLatestResponseModel:
    """
    Attributes:
        data (DerivativesMarketPairsListLatestResultsObject): Results of your query returned as an object. Example:
            {'exchange_id': 270, 'exchange_name': 'Binance', 'exchange_slug': 'binance', 'num_market_pairs': 2045,
            'volume_24h': 69306677552.93349, 'market_pairs': [{'market_id': 47150, 'market_pair': 'BTC/USDT', 'category':
            'perpetual', 'fee_type': 'percentage', 'outlier_detected': False, 'exclusions': None, 'market_pair_base':
            {'exchange_symbol': 'BTC', 'symbol': 'BTC', 'crypto_id': 1, 'currency_type': 'cryptocurrency'},
            'market_pair_quote': {'exchange_symbol': 'USDT', 'symbol': 'USDT', 'crypto_id': 825, 'currency_type':
            'cryptocurrency'}, 'exchange_reported_quotes': [{'crypto_id': 2781, 'symbol': 'USD', 'price': 80521.2,
            'volume_24h_base': 184589.83976729, 'volume_24h_quote': 14863395405.87, 'open_interest': 5000000, 'index_price':
            80498.5, 'index_basis': 0.0023, 'funding_rate': 0.0001, 'last_updated': '2026-05-15T06:54:18.743Z',
            'volume_percentage': 21.441131937316662}], 'quotes': [{'crypto_id': 2781, 'symbol': 'USD', 'price':
            80504.01770192, 'volume_24h': 14860136175.4951, 'open_interest': 5000000, 'last_updated':
            '2026-05-15T06:54:18.743Z'}]}]}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: DerivativesMarketPairsListLatestResultsObject
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
        from ..models.derivatives_market_pairs_list_latest_results_object import (
            DerivativesMarketPairsListLatestResultsObject,
        )

        d = dict(src_dict)
        data = DerivativesMarketPairsListLatestResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        derivatives_market_pairs_list_latest_response_model = cls(
            data=data,
            status=status,
        )

        derivatives_market_pairs_list_latest_response_model.additional_properties = d
        return derivatives_market_pairs_list_latest_response_model

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
