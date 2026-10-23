from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.exchange_historical_quotes_exchange_object import ExchangeHistoricalQuotesExchangeObject
    from ..models.exchange_historical_quotes_results_map import ExchangeHistoricalQuotesResultsMap


T = TypeVar("T", bound="ExchangeHistoricalQuotesResponseModel")


@_attrs_define
class ExchangeHistoricalQuotesResponseModel:
    """
    Attributes:
        data (ExchangeHistoricalQuotesExchangeObject | ExchangeHistoricalQuotesResultsMap): A single object when you
            request one exchange, and an object map keyed by exchange ID when you request several.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: ExchangeHistoricalQuotesExchangeObject | ExchangeHistoricalQuotesResultsMap
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.exchange_historical_quotes_results_map import ExchangeHistoricalQuotesResultsMap

        data: dict[str, Any]
        if isinstance(self.data, ExchangeHistoricalQuotesResultsMap):
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
        from ..models.exchange_historical_quotes_exchange_object import ExchangeHistoricalQuotesExchangeObject
        from ..models.exchange_historical_quotes_results_map import ExchangeHistoricalQuotesResultsMap

        d = dict(src_dict)

        def _parse_data(data: object) -> ExchangeHistoricalQuotesExchangeObject | ExchangeHistoricalQuotesResultsMap:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = ExchangeHistoricalQuotesResultsMap.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_1 = ExchangeHistoricalQuotesExchangeObject.from_dict(data)

            return data_type_1

        data = _parse_data(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        exchange_historical_quotes_response_model = cls(
            data=data,
            status=status,
        )

        exchange_historical_quotes_response_model.additional_properties = d
        return exchange_historical_quotes_response_model

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
