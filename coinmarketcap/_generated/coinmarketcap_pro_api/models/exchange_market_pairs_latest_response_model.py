from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.exchange_market_pairs_latest_results_object import ExchangeMarketPairsLatestResultsObject


T = TypeVar("T", bound="ExchangeMarketPairsLatestResponseModel")


@_attrs_define
class ExchangeMarketPairsLatestResponseModel:
    """
    Attributes:
        data (ExchangeMarketPairsLatestResultsObject): Results of your query returned as an object. Example: {'id': 270,
            'name': 'Binance', 'slug': 'binance', 'num_market_pairs': 473, 'volume_24h': 769291636.239632, 'market_pairs':
            [{'market_id': 9933, 'market_pair': 'BTC/USDT', 'category': 'spot', 'fee_type': 'percentage',
            'outlier_detected': 0, 'exclusions': None, 'market_pair_base': {'currency_id': 1, 'currency_symbol': 'BTC',
            'exchange_symbol': 'BTC', 'currency_type': 'cryptocurrency'}, 'market_pair_quote': {'currency_id': 825,
            'currency_symbol': 'USDT', 'exchange_symbol': 'USDT', 'currency_type': 'cryptocurrency'}, 'quote':
            {'exchange_reported': {'price': 7901.83, 'volume_24h_base': 47251.3345550653, 'volume_24h_quote':
            373372012.927251, 'volume_percentage': 19.4346563602467, 'last_updated': '2019-05-24T01:40:10.000Z'}, 'USD':
            {'price': 7933.66233493434, 'volume_24h': 374876133.234903, 'depth_negative_two': 40654.68019906,
            'depth_positive_two': 17352.9964811, 'last_updated': '2019-05-24T01:40:10.000Z'}}}, {'market_id': 36329,
            'market_pair': 'MATIC/BTC', 'category': 'spot', 'fee_type': 'percentage', 'outlier_detected': 0, 'exclusions':
            None, 'market_pair_base': {'currency_id': 3890, 'currency_symbol': 'MATIC', 'exchange_symbol': 'MATIC',
            'currency_type': 'cryptocurrency'}, 'market_pair_quote': {'currency_id': 1, 'currency_symbol': 'BTC',
            'exchange_symbol': 'BTC', 'currency_type': 'cryptocurrency'}, 'quote': {'exchange_reported': {'price': 3.4e-06,
            'volume_24h_base': 8773968381.05, 'volume_24h_quote': 29831.49249557, 'volume_percentage': 19.4346563602467,
            'last_updated': '2019-05-24T01:41:16.000Z'}, 'USD': {'price': 0.0269295015799739, 'volume_24h':
            236278595.380127, 'depth_negative_two': 40654.68019906, 'depth_positive_two': 17352.9964811, 'last_updated':
            '2019-05-24T01:41:16.000Z'}}}]}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: ExchangeMarketPairsLatestResultsObject
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
        from ..models.exchange_market_pairs_latest_results_object import ExchangeMarketPairsLatestResultsObject

        d = dict(src_dict)
        data = ExchangeMarketPairsLatestResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        exchange_market_pairs_latest_response_model = cls(
            data=data,
            status=status,
        )

        exchange_market_pairs_latest_response_model.additional_properties = d
        return exchange_market_pairs_latest_response_model

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
