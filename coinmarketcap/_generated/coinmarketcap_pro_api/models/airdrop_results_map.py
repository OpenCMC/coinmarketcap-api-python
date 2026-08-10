from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.airdrop_airdrop_object import AirdropAirdropObject


T = TypeVar("T", bound="AirdropResultsMap")


@_attrs_define
class AirdropResultsMap:
    """Results of your query returned as an object map.

    Example:
        {'1': {'id': '60e59b99c8ca1d58514a2322', 'project_name': 'DeRace Airdrop', 'description': 'For 7 days starting
            from August 15, 2021, CoinMarketCap will host an Airdrop event...', 'status': 'UPCOMING', 'coin': {'id': 10744,
            'name': 'DeRace', 'slug': 'derace', 'symbol': 'DERC'}, 'start_date': '2021-06-01T22:11:00.000Z', 'end_date':
            '2021-07-01T22:11:00.000Z', 'total_prize': 20000000000, 'winner_count': 1000, 'link':
            'https://coinmarketcap.com/currencies/derace/airdrop/'}}

    """

    additional_properties: dict[str, AirdropAirdropObject] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airdrop_airdrop_object import AirdropAirdropObject

        d = dict(src_dict)
        airdrop_results_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = AirdropAirdropObject.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        airdrop_results_map.additional_properties = additional_properties
        return airdrop_results_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> AirdropAirdropObject:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: AirdropAirdropObject) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
