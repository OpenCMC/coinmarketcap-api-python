from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.derivatives_exchanges_list_results_object import DerivativesExchangesListResultsObject


T = TypeVar("T", bound="DerivativesExchangesListResponseModel")


@_attrs_define
class DerivativesExchangesListResponseModel:
    """
    Attributes:
        data (DerivativesExchangesListResultsObject): Results of your query returned as an object. Example:
            {'exchanges': [{'exchange_id': 270, 'exchange_name': 'Binance', 'exchange_slug': 'binance', 'num_market_pairs':
            645, 'fiats': [], 'traffic_score': 1000, 'rank': 1, 'exchange_score': 7.82345678, 'liquidity_score': 9.8028,
            'last_updated': '2026-04-21T10:30:00.000Z', 'quotes': [{'convert_id': 2781, 'convert_symbol': 'USD',
            'open_interest': 23306624960.78, 'open_interest_usd': 23306624960.78, 'derivative_volume': 62828618628.85901,
            'derivative_volume_usd': 62828618628.85901, 'maker_fees': 0.04, 'taker_fees': 0.04, 'last_updated':
            '2026-04-21T10:30:00.000Z'}]}]}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: DerivativesExchangesListResultsObject
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
        from ..models.derivatives_exchanges_list_results_object import DerivativesExchangesListResultsObject

        d = dict(src_dict)
        data = DerivativesExchangesListResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        derivatives_exchanges_list_response_model = cls(
            data=data,
            status=status,
        )

        derivatives_exchanges_list_response_model.additional_properties = d
        return derivatives_exchanges_list_response_model

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
