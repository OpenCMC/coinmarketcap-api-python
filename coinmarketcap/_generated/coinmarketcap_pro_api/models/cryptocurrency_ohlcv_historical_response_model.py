from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.cryptocurrency_ohlcv_historical_response_model_object_map import (
        CryptocurrencyOHLCVHistoricalResponseModelObjectMap,
    )
    from ..models.cryptocurrency_ohlcv_historical_results_object import CryptocurrencyOHLCVHistoricalResultsObject


T = TypeVar("T", bound="CryptocurrencyOHLCVHistoricalResponseModel")


@_attrs_define
class CryptocurrencyOHLCVHistoricalResponseModel:
    """
    Attributes:
        data (CryptocurrencyOHLCVHistoricalResponseModelObjectMap | CryptocurrencyOHLCVHistoricalResultsObject): The
            shape depends on the identifiers you send:

            - **One cryptocurrency** - one `id` or `slug` (or one `symbol` on v1) returns the cryptocurrency object itself.
            - **Object map** - several `id`, `slug` or `symbol` values return an object map keyed by the identifiers you
            sent (IDs, slugs or symbols).
            - **Symbol lookups (v2)** - every v2 `symbol` request returns an object map keyed by symbol, and each value is
            an array of all cryptocurrencies that share the symbol, even when you send one symbol.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: CryptocurrencyOHLCVHistoricalResponseModelObjectMap | CryptocurrencyOHLCVHistoricalResultsObject
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cryptocurrency_ohlcv_historical_response_model_object_map import (
            CryptocurrencyOHLCVHistoricalResponseModelObjectMap,
        )

        data: dict[str, Any]
        if isinstance(self.data, CryptocurrencyOHLCVHistoricalResponseModelObjectMap):
            data = self.data.to_dict()
        else:
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
        from ..models.cryptocurrency_ohlcv_historical_response_model_object_map import (
            CryptocurrencyOHLCVHistoricalResponseModelObjectMap,
        )
        from ..models.cryptocurrency_ohlcv_historical_results_object import CryptocurrencyOHLCVHistoricalResultsObject

        d = dict(src_dict)

        def _parse_data(
            data: object,
        ) -> CryptocurrencyOHLCVHistoricalResponseModelObjectMap | CryptocurrencyOHLCVHistoricalResultsObject:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_object_map = CryptocurrencyOHLCVHistoricalResponseModelObjectMap.from_dict(data)

                return data_object_map
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_1 = CryptocurrencyOHLCVHistoricalResultsObject.from_dict(data)

            return data_type_1

        data = _parse_data(d.pop("data"))

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
