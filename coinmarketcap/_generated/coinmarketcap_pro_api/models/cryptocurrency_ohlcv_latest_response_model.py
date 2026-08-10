from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.cryptocurrency_ohlcv_latest_cryptocurrency_results_map import (
        CryptocurrencyOHLCVLatestCryptocurrencyResultsMap,
    )


T = TypeVar("T", bound="CryptocurrencyOHLCVLatestResponseModel")


@_attrs_define
class CryptocurrencyOHLCVLatestResponseModel:
    """
    Attributes:
        data (CryptocurrencyOHLCVLatestCryptocurrencyResultsMap): A map of cryptocurrency objects by ID or symbol (as
            passed in query parameters). Example: {'1': {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'last_updated':
            '2018-09-10T18:54:00.000Z', 'time_open': '2018-09-10T00:00:00.000Z', 'time_close': '2019-08-30T23:59:59.999Z',
            'time_high': '2018-09-10T00:00:00.000Z', 'time_low': '2018-09-10T00:00:00.000Z', 'quote': {'USD': {'open':
            6301.57, 'high': 6374.98, 'low': 6292.76, 'close': 6308.76, 'volume': 3786450000, 'last_updated':
            '2018-09-10T18:54:00.000Z'}}}}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: CryptocurrencyOHLCVLatestCryptocurrencyResultsMap
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
        from ..models.cryptocurrency_ohlcv_latest_cryptocurrency_results_map import (
            CryptocurrencyOHLCVLatestCryptocurrencyResultsMap,
        )

        d = dict(src_dict)
        data = CryptocurrencyOHLCVLatestCryptocurrencyResultsMap.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        cryptocurrency_ohlcv_latest_response_model = cls(
            data=data,
            status=status,
        )

        cryptocurrency_ohlcv_latest_response_model.additional_properties = d
        return cryptocurrency_ohlcv_latest_response_model

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
