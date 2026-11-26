from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.cryptocurrency_quotes_historical_result_object import CryptocurrencyQuotesHistoricalResultObject
    from ..models.cryptocurrency_quotes_historical_results_map import CryptocurrencyQuotesHistoricalResultsMap


T = TypeVar("T", bound="CryptocurrencyQuotesHistoricalResponseModel")


@_attrs_define
class CryptocurrencyQuotesHistoricalResponseModel:
    """
    Attributes:
        data (CryptocurrencyQuotesHistoricalResultObject | CryptocurrencyQuotesHistoricalResultsMap): The shape depends
            on the endpoint version and on the identifiers you send:

            - **One cryptocurrency (v1 and v2)** - one `id`, or one `symbol` on v1, returns the cryptocurrency object
            itself.
            - **Object map** - several `id` or `symbol` values on v1 and v2, and every v3 request, return an object map
            keyed by the identifiers you sent (IDs or symbols).
            - **Symbol lookups (v2 and v3)** - each map value is an array of all cryptocurrencies that share the symbol,
            even when you send one symbol.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: CryptocurrencyQuotesHistoricalResultObject | CryptocurrencyQuotesHistoricalResultsMap
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cryptocurrency_quotes_historical_results_map import CryptocurrencyQuotesHistoricalResultsMap

        data: dict[str, Any]
        if isinstance(self.data, CryptocurrencyQuotesHistoricalResultsMap):
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
        from ..models.cryptocurrency_quotes_historical_result_object import CryptocurrencyQuotesHistoricalResultObject
        from ..models.cryptocurrency_quotes_historical_results_map import CryptocurrencyQuotesHistoricalResultsMap

        d = dict(src_dict)

        def _parse_data(
            data: object,
        ) -> CryptocurrencyQuotesHistoricalResultObject | CryptocurrencyQuotesHistoricalResultsMap:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = CryptocurrencyQuotesHistoricalResultsMap.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_1 = CryptocurrencyQuotesHistoricalResultObject.from_dict(data)

            return data_type_1

        data = _parse_data(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        cryptocurrency_quotes_historical_response_model = cls(
            data=data,
            status=status,
        )

        cryptocurrency_quotes_historical_response_model.additional_properties = d
        return cryptocurrency_quotes_historical_response_model

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
