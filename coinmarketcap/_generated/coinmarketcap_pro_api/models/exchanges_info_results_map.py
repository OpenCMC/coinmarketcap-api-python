from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exchanges_info_exchange_info_object import ExchangesInfoExchangeInfoObject


T = TypeVar("T", bound="ExchangesInfoResultsMap")


@_attrs_define
class ExchangesInfoResultsMap:
    """Results of your query returned as an object map.

    Example:
        {'1': {'id': 270, 'name': 'Binance', 'slug': 'binance', 'logo':
            'https://s2.coinmarketcap.com/static/img/exchanges/64x64/270.png', 'description': 'Launched in Jul-2017, Binance
            is a centralized exchange based in Malta.', 'date_launched': '2017-07-14T00:00:00.000Z', 'notice': '',
            'countries': [], 'fiats': ['AED', 'USD'], 'tags': None, 'type': '', 'maker_fee': 0.02, 'taker_fee': 0.04,
            'weekly_visits': 5123451, 'spot_volume_usd': 66926283498.60113, 'spot_volume_last_updated':
            '2021-05-06T01:20:15.451Z', 'urls': {'website': ['https://www.binance.com/'], 'twitter':
            ['https://twitter.com/binance'], 'blog': [], 'chat': ['https://t.me/binanceexchange'], 'fee':
            ['https://www.binance.com/fees.html']}}}

    """

    additional_properties: dict[str, ExchangesInfoExchangeInfoObject] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exchanges_info_exchange_info_object import ExchangesInfoExchangeInfoObject

        d = dict(src_dict)
        exchanges_info_results_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ExchangesInfoExchangeInfoObject.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        exchanges_info_results_map.additional_properties = additional_properties
        return exchanges_info_results_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ExchangesInfoExchangeInfoObject:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ExchangesInfoExchangeInfoObject) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
