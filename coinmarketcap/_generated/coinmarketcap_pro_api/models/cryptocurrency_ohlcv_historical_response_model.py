from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.cryptocurrency_ohlcv_historical_results_object import CryptocurrencyOHLCVHistoricalResultsObject


T = TypeVar("T", bound="CryptocurrencyOHLCVHistoricalResponseModel")


@_attrs_define
class CryptocurrencyOHLCVHistoricalResponseModel:
    """
    Attributes:
        data (CryptocurrencyOHLCVHistoricalResultsObject): Results of your query returned as an object. Example: {'id':
            1, 'name': 'Bitcoin', 'symbol': 'BTC', 'quotes': [{'time_open': '2019-01-02T00:00:00.000Z', 'time_close':
            '2019-01-02T23:59:59.999Z', 'time_high': '2019-01-02T03:53:00.000Z', 'time_low': '2019-01-02T02:43:00.000Z',
            'quote': {'USD': {'open': 3849.21640853, 'high': 3947.9812729, 'low': 3817.40949569, 'close': 3943.40933686,
            'volume': 5244856835.70851, 'market_cap': 68849856731.6738, 'timestamp': '2019-01-02T23:59:59.999Z'}}},
            {'time_open': '2019-01-03T00:00:00.000Z', 'time_close': '2019-01-03T23:59:59.999Z', 'time_high':
            '2019-01-02T03:53:00.000Z', 'time_low': '2019-01-02T02:43:00.000Z', 'quote': {'USD': {'open': 3931.04863841,
            'high': 3935.68513083, 'low': 3826.22287069, 'close': 3836.74131867, 'volume': 4530215218.84018, 'market_cap':
            66994920902.7202, 'timestamp': '2019-01-03T23:59:59.999Z'}}}]}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: CryptocurrencyOHLCVHistoricalResultsObject
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
        from ..models.cryptocurrency_ohlcv_historical_results_object import CryptocurrencyOHLCVHistoricalResultsObject

        d = dict(src_dict)
        data = CryptocurrencyOHLCVHistoricalResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        cryptocurrency_ohlcv_historical_response_model = cls(
            data=data,
            status=status,
        )

        cryptocurrency_ohlcv_historical_response_model.additional_properties = d
        return cryptocurrency_ohlcv_historical_response_model

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
