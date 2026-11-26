from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject


T = TypeVar("T", bound="CryptocurrencyOHLCVHistoricalV5ResponseModel")


@_attrs_define
class CryptocurrencyOHLCVHistoricalV5ResponseModel:
    """
    Example:
        {'data': [[78559.1131265811, 78748.50143864893, 78549.03085271013, 78727.98306878311, 30034635342.11,
            1580696743839.83, '2026-09-01T00:00:00.000Z', '2026-09-01T00:12:00.000Z', '2026-09-01T00:01:00.000Z',
            '2026-09-01T00:14:59.999Z'], [78737.76559810448, 78881.55883757334, 78737.76559810448, 78854.57252549069,
            30041940429.35, 1583238401001.9, '2026-09-01T00:15:00.000Z', '2026-09-01T00:28:00.000Z',
            '2026-09-01T00:15:00.000Z', '2026-09-01T00:29:59.999Z'], [78845.01243441102, 78845.01243441102,
            78684.2224550443, 78684.2224550443, 29878468702.82, 1579819536609.93, '2026-09-01T00:30:00.000Z',
            '2026-09-01T00:30:00.000Z', '2026-09-01T00:44:00.000Z', '2026-09-01T00:44:59.999Z']], 'status': {'timestamp':
            '2026-11-11T10:18:24.323Z', 'error_code': '0', 'error_message': '', 'elapsed': 31, 'credit_count': 1}}

    Attributes:
        data (list[list[float | None | str]]): Candles, oldest first. Empty when the window has no data.

            Each candle is an array of 10 values. Read them by index:

            | Index | Value |
            |---|---|
            | 0 | Open price |
            | 1 | High price |
            | 2 | Low price |
            | 3 | Close price |
            | 4 | Volume |
            | 5 | Market cap |
            | 6 | Open time - start of the period (ISO 8601, UTC) |
            | 7 | High time - time of the high price |
            | 8 | Low time - time of the low price |
            | 9 | Close time - end of the period |
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: list[list[float | None | str]]
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = []
            for componentsschemas_cryptocurrency_ohlcv_historical_v_5_candle_item_data in data_item_data:
                componentsschemas_cryptocurrency_ohlcv_historical_v_5_candle_item: float | None | str
                componentsschemas_cryptocurrency_ohlcv_historical_v_5_candle_item = (
                    componentsschemas_cryptocurrency_ohlcv_historical_v_5_candle_item_data
                )
                data_item.append(componentsschemas_cryptocurrency_ohlcv_historical_v_5_candle_item)

            data.append(data_item)

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

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = []
            _data_item = data_item_data
            for componentsschemas_cryptocurrency_ohlcv_historical_v_5_candle_item_data in _data_item:

                def _parse_componentsschemas_cryptocurrency_ohlcv_historical_v_5_candle_item(
                    data: object,
                ) -> float | None | str:
                    if data is None:
                        return data
                    return cast(float | None | str, data)

                componentsschemas_cryptocurrency_ohlcv_historical_v_5_candle_item = (
                    _parse_componentsschemas_cryptocurrency_ohlcv_historical_v_5_candle_item(
                        componentsschemas_cryptocurrency_ohlcv_historical_v_5_candle_item_data
                    )
                )

                data_item.append(componentsschemas_cryptocurrency_ohlcv_historical_v_5_candle_item)

            data.append(data_item)

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        cryptocurrency_ohlcv_historical_v5_response_model = cls(
            data=data,
            status=status,
        )

        cryptocurrency_ohlcv_historical_v5_response_model.additional_properties = d
        return cryptocurrency_ohlcv_historical_v5_response_model

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
