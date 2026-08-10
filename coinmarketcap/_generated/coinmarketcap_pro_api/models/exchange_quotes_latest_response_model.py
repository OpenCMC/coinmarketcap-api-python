from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.exchange_quotes_latest_exchange_results_map import ExchangeQuotesLatestExchangeResultsMap


T = TypeVar("T", bound="ExchangeQuotesLatestResponseModel")


@_attrs_define
class ExchangeQuotesLatestResponseModel:
    """
    Attributes:
        data (ExchangeQuotesLatestExchangeResultsMap): A map of exchange objects by ID or slugs (as used in query
            parameters). Example: {'1': {'id': 270, 'name': 'Binance', 'slug': 'binance', 'num_coins': 132,
            'num_market_pairs': 385, 'last_updated': '2018-11-08T22:11:00.000Z', 'traffic_score': 1000, 'rank': 1,
            'exchange_score': 9.8, 'liquidity_score': 9.8028, 'quote': {'USD': {'volume_24h': 768478308.529847,
            'volume_24h_adjusted': 768478308.529847, 'volume_7d': 3666423776, 'volume_30d': 21338299776,
            'percent_change_volume_24h': -11.8232, 'percent_change_volume_7d': 67.0306, 'percent_change_volume_30d':
            -0.0821558, 'effective_liquidity_24h': 629.9774, 'last_updated': '2018-11-08T22:18:00.000Z'}}}}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: ExchangeQuotesLatestExchangeResultsMap
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
        from ..models.exchange_quotes_latest_exchange_results_map import ExchangeQuotesLatestExchangeResultsMap

        d = dict(src_dict)
        data = ExchangeQuotesLatestExchangeResultsMap.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        exchange_quotes_latest_response_model = cls(
            data=data,
            status=status,
        )

        exchange_quotes_latest_response_model.additional_properties = d
        return exchange_quotes_latest_response_model

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
