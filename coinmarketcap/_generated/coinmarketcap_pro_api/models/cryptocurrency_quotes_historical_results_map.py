from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cryptocurrency_quotes_historical_result_object import CryptocurrencyQuotesHistoricalResultObject


T = TypeVar("T", bound="CryptocurrencyQuotesHistoricalResultsMap")


@_attrs_define
class CryptocurrencyQuotesHistoricalResultsMap:
    """One entry per identifier you sent, keyed by cryptocurrency ID or symbol.

    Example:
        {'1': {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'is_active': 1, 'is_fiat': 0, 'quotes': [{'timestamp':
            '2018-06-22T00:00:00.000Z', 'quote': {'USD': {'price': 6242.48, 'volume_24h': 4894120000, 'market_cap':
            107057808682, 'timestamp': '2018-06-22T00:04:16.000Z'}}}]}}

    """

    additional_properties: dict[
        str, CryptocurrencyQuotesHistoricalResultObject | list[CryptocurrencyQuotesHistoricalResultObject]
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cryptocurrency_quotes_historical_result_object import CryptocurrencyQuotesHistoricalResultObject

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, CryptocurrencyQuotesHistoricalResultObject):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = []
                for additional_property_symbol_matches_v_2_and_v_3_symbol_requests_item_data in prop:
                    additional_property_symbol_matches_v_2_and_v_3_symbol_requests_item = (
                        additional_property_symbol_matches_v_2_and_v_3_symbol_requests_item_data.to_dict()
                    )
                    field_dict[prop_name].append(additional_property_symbol_matches_v_2_and_v_3_symbol_requests_item)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_quotes_historical_result_object import CryptocurrencyQuotesHistoricalResultObject

        d = dict(src_dict)
        cryptocurrency_quotes_historical_results_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> CryptocurrencyQuotesHistoricalResultObject | list[CryptocurrencyQuotesHistoricalResultObject]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = CryptocurrencyQuotesHistoricalResultObject.from_dict(data)

                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, list):
                    raise TypeError()
                additional_property_symbol_matches_v_2_and_v_3_symbol_requests = []
                _additional_property_symbol_matches_v_2_and_v_3_symbol_requests = data
                for (
                    additional_property_symbol_matches_v_2_and_v_3_symbol_requests_item_data
                ) in _additional_property_symbol_matches_v_2_and_v_3_symbol_requests:
                    additional_property_symbol_matches_v_2_and_v_3_symbol_requests_item = (
                        CryptocurrencyQuotesHistoricalResultObject.from_dict(
                            additional_property_symbol_matches_v_2_and_v_3_symbol_requests_item_data
                        )
                    )

                    additional_property_symbol_matches_v_2_and_v_3_symbol_requests.append(
                        additional_property_symbol_matches_v_2_and_v_3_symbol_requests_item
                    )

                return additional_property_symbol_matches_v_2_and_v_3_symbol_requests

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        cryptocurrency_quotes_historical_results_map.additional_properties = additional_properties
        return cryptocurrency_quotes_historical_results_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> CryptocurrencyQuotesHistoricalResultObject | list[CryptocurrencyQuotesHistoricalResultObject]:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: CryptocurrencyQuotesHistoricalResultObject | list[CryptocurrencyQuotesHistoricalResultObject],
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
