from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.exchanges_info_results_map import ExchangesInfoResultsMap


T = TypeVar("T", bound="ExchangesInfoResponseModel")


@_attrs_define
class ExchangesInfoResponseModel:
    """
    Attributes:
        data (ExchangesInfoResultsMap): Results of your query returned as an object map. Example: {'1': {'id': 270,
            'name': 'Binance', 'slug': 'binance', 'logo': 'https://s2.coinmarketcap.com/static/img/exchanges/64x64/270.png',
            'description': 'Launched in Jul-2017, Binance is a centralized exchange based in Malta.', 'date_launched':
            '2017-07-14T00:00:00.000Z', 'notice': '', 'countries': [], 'fiats': ['AED', 'USD'], 'tags': None, 'type': '',
            'maker_fee': 0.02, 'taker_fee': 0.04, 'weekly_visits': 5123451, 'spot_volume_usd': 66926283498.60113,
            'spot_volume_last_updated': '2021-05-06T01:20:15.451Z', 'urls': {'website': ['https://www.binance.com/'],
            'twitter': ['https://twitter.com/binance'], 'blog': [], 'chat': ['https://t.me/binanceexchange'], 'fee':
            ['https://www.binance.com/fees.html']}}}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: ExchangesInfoResultsMap
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
        from ..models.exchanges_info_results_map import ExchangesInfoResultsMap

        d = dict(src_dict)
        data = ExchangesInfoResultsMap.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        exchanges_info_response_model = cls(
            data=data,
            status=status,
        )

        exchanges_info_response_model.additional_properties = d
        return exchanges_info_response_model

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
