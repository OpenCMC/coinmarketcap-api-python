from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cryptocurrency_ohlcv_latest_cryptocurrency_object import CryptocurrencyOHLCVLatestCryptocurrencyObject


T = TypeVar("T", bound="CryptocurrencyOHLCVLatestCryptocurrencyResultsMap")


@_attrs_define
class CryptocurrencyOHLCVLatestCryptocurrencyResultsMap:
    """A map of cryptocurrency objects by ID or symbol (as passed in query parameters).

    Example:
        {'1': {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'last_updated': '2018-09-10T18:54:00.000Z', 'time_open':
            '2018-09-10T00:00:00.000Z', 'time_close': '2019-08-30T23:59:59.999Z', 'time_high': '2018-09-10T00:00:00.000Z',
            'time_low': '2018-09-10T00:00:00.000Z', 'quote': {'USD': {'open': 6301.57, 'high': 6374.98, 'low': 6292.76,
            'close': 6308.76, 'volume': 3786450000, 'last_updated': '2018-09-10T18:54:00.000Z'}}}}

    """

    additional_properties: dict[str, CryptocurrencyOHLCVLatestCryptocurrencyObject] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_ohlcv_latest_cryptocurrency_object import (
            CryptocurrencyOHLCVLatestCryptocurrencyObject,
        )

        d = dict(src_dict)
        cryptocurrency_ohlcv_latest_cryptocurrency_results_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CryptocurrencyOHLCVLatestCryptocurrencyObject.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        cryptocurrency_ohlcv_latest_cryptocurrency_results_map.additional_properties = additional_properties
        return cryptocurrency_ohlcv_latest_cryptocurrency_results_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> CryptocurrencyOHLCVLatestCryptocurrencyObject:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: CryptocurrencyOHLCVLatestCryptocurrencyObject) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
