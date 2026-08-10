from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.derivatives_exchanges_list_results_object_exchanges_item import (
        DerivativesExchangesListResultsObjectExchangesItem,
    )


T = TypeVar("T", bound="DerivativesExchangesListResultsObject")


@_attrs_define
class DerivativesExchangesListResultsObject:
    """Results of your query returned as an object.

    Example:
        {'exchanges': [{'exchange_id': 270, 'exchange_name': 'Binance', 'exchange_slug': 'binance', 'num_market_pairs':
            645, 'fiats': [], 'traffic_score': 1000, 'rank': 1, 'exchange_score': 7.82345678, 'liquidity_score': 9.8028,
            'last_updated': '2026-04-21T10:30:00.000Z', 'quotes': [{'convert_id': 2781, 'convert_symbol': 'USD',
            'open_interest': 23306624960.78, 'open_interest_usd': 23306624960.78, 'derivative_volume': 62828618628.85901,
            'derivative_volume_usd': 62828618628.85901, 'maker_fees': 0.04, 'taker_fees': 0.04, 'last_updated':
            '2026-04-21T10:30:00.000Z'}]}]}

    Attributes:
        exchanges (list[DerivativesExchangesListResultsObjectExchangesItem] | Unset): Array of derivatives exchanges,
            sorted per the `sort` and `sort_dir` parameters.
    """

    exchanges: list[DerivativesExchangesListResultsObjectExchangesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchanges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exchanges, Unset):
            exchanges = []
            for exchanges_item_data in self.exchanges:
                exchanges_item = exchanges_item_data.to_dict()
                exchanges.append(exchanges_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exchanges is not UNSET:
            field_dict["exchanges"] = exchanges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.derivatives_exchanges_list_results_object_exchanges_item import (
            DerivativesExchangesListResultsObjectExchangesItem,
        )

        d = dict(src_dict)
        _exchanges = d.pop("exchanges", UNSET)
        exchanges: list[DerivativesExchangesListResultsObjectExchangesItem] | Unset = UNSET
        if _exchanges is not UNSET:
            exchanges = []
            for exchanges_item_data in _exchanges:
                exchanges_item = DerivativesExchangesListResultsObjectExchangesItem.from_dict(exchanges_item_data)

                exchanges.append(exchanges_item)

        derivatives_exchanges_list_results_object = cls(
            exchanges=exchanges,
        )

        derivatives_exchanges_list_results_object.additional_properties = d
        return derivatives_exchanges_list_results_object

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
