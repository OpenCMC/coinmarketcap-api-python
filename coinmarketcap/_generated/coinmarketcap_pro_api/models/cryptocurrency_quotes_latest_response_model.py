from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.cryptocurrency_quotes_latest_cryptocurrency_results_map import (
        CryptocurrencyQuotesLatestCryptocurrencyResultsMap,
    )


T = TypeVar("T", bound="CryptocurrencyQuotesLatestResponseModel")


@_attrs_define
class CryptocurrencyQuotesLatestResponseModel:
    """
    Attributes:
        data (CryptocurrencyQuotesLatestCryptocurrencyResultsMap): A map of cryptocurrency objects by ID, symbol, or
            slug (as used in query parameters). Example: {'1': {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug':
            'bitcoin', 'is_active': 1, 'is_fiat': 0, 'circulating_supply': 17199862, 'total_supply': 17199862, 'max_supply':
            21000000, 'date_added': '2013-04-28T00:00:00.000Z', 'num_market_pairs': 331, 'cmc_rank': 1, 'last_updated':
            '2018-08-09T21:56:28.000Z', 'tags': ['mineable'], 'platform': None, 'self_reported_circulating_supply': None,
            'self_reported_market_cap': None, 'minted_market_cap': 1802955697670.94, 'quote': {'USD': {'price':
            6602.60701122, 'volume_24h': 4314444687.5194, 'volume_change_24h': -0.152774, 'percent_change_1h': 0.988615,
            'percent_change_24h': 4.37185, 'percent_change_7d': -12.1352, 'percent_change_30d': -12.1352, 'market_cap':
            852164659250.2758, 'market_cap_dominance': 51, 'fully_diluted_market_cap': 952835089431.14, 'last_updated':
            '2018-08-09T21:56:28.000Z'}}}}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: CryptocurrencyQuotesLatestCryptocurrencyResultsMap
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
        from ..models.cryptocurrency_quotes_latest_cryptocurrency_results_map import (
            CryptocurrencyQuotesLatestCryptocurrencyResultsMap,
        )

        d = dict(src_dict)
        data = CryptocurrencyQuotesLatestCryptocurrencyResultsMap.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        cryptocurrency_quotes_latest_response_model = cls(
            data=data,
            status=status,
        )

        cryptocurrency_quotes_latest_response_model.additional_properties = d
        return cryptocurrency_quotes_latest_response_model

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
