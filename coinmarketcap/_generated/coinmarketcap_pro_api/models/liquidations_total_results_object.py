from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.liquidations_total_results_object_quotes_item import LiquidationsTotalResultsObjectQuotesItem


T = TypeVar("T", bound="LiquidationsTotalResultsObject")


@_attrs_define
class LiquidationsTotalResultsObject:
    """Results of your query returned as an object.

    Example:
        {'quotes': [{'symbol': 'USD', 'crypto_id': 2781, 'total_liquidations_1h': 4615261.252240025,
            'long_liquidations_1h': 3506917.9880817593, 'short_liquidations_1h': 1108343.264158266, 'total_liquidations_4h':
            12888989.407139461, 'long_liquidations_4h': 9462596.325027341, 'short_liquidations_4h': 3426393.0821121223,
            'total_liquidations_24h': 519760825.61196995, 'long_liquidations_24h': 451643104.8996174,
            'short_liquidations_24h': 68117720.71235262, 'last_updated': '2026-07-28T10:36:00.000Z'}]}

    Attributes:
        quotes (list[LiquidationsTotalResultsObjectQuotesItem] | Unset): One entry per requested convert currency. Never
            a bare array at `data`.
    """

    quotes: list[LiquidationsTotalResultsObjectQuotesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quotes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quotes, Unset):
            quotes = []
            for quotes_item_data in self.quotes:
                quotes_item = quotes_item_data.to_dict()
                quotes.append(quotes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quotes is not UNSET:
            field_dict["quotes"] = quotes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.liquidations_total_results_object_quotes_item import LiquidationsTotalResultsObjectQuotesItem

        d = dict(src_dict)
        _quotes = d.pop("quotes", UNSET)
        quotes: list[LiquidationsTotalResultsObjectQuotesItem] | Unset = UNSET
        if _quotes is not UNSET:
            quotes = []
            for quotes_item_data in _quotes:
                quotes_item = LiquidationsTotalResultsObjectQuotesItem.from_dict(quotes_item_data)

                quotes.append(quotes_item)

        liquidations_total_results_object = cls(
            quotes=quotes,
        )

        liquidations_total_results_object.additional_properties = d
        return liquidations_total_results_object

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
