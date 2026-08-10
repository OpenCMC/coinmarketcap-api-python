from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.rwa_quotes_latest_results_object import RWAQuotesLatestResultsObject


T = TypeVar("T", bound="RWAQuotesLatestResponseModel")


@_attrs_define
class RWAQuotesLatestResponseModel:
    """
    Attributes:
        data (RWAQuotesLatestResultsObject): Results of your query returned as an object. Example: {'rwa_assets':
            [{'name': 'NVIDIA', 'symbol': 'NVDA', 'slug': 'nvidia', 'quotes': [{'symbol': 'USD', 'crypto_id': 2781,
            'average_tokenized_price': 211.04769840665475, 'tokenized_market_cap': 3726091.2870977107,
            'tokenized_volume_24h': 7654132.31153204, 'last_updated': '2026-07-15T10:45:05.000Z'}], 'rwa_id': 2,
            'asset_type': 'stock', 'rwa_rank': 2, 'has_tokens': True, 'average_tokenized_price': 211.04769840665475,
            'tokenized_market_cap': 3726091.2870977107, 'tokenized_volume_24h': 7654132.31153204, 'last_updated':
            '2026-07-15T10:13:26.066Z', 'tokens': [{'symbol': None, 'name': None, 'price': None, 'crypto_id': 37679,
            'issuer_id': None, 'issuer_name': None, 'market_cap': None, 'volume_24h': None}, {'symbol': 'NVDA', 'name':
            'NVIDIA tokenized stock FTX', 'price': None, 'crypto_id': 7913, 'issuer_id': None, 'issuer_name': None,
            'market_cap': None, 'volume_24h': None}, {'symbol': 'DNVDA', 'name': 'Nvidia Tokenized Stock Defichain',
            'price': None, 'crypto_id': 19241, 'issuer_id': None, 'issuer_name': None, 'market_cap': None, 'volume_24h':
            None}, {'symbol': 'NVDA.D', 'name': 'NVIDIA tokenized stock (Dinari)', 'price': None, 'crypto_id': 28616,
            'issuer_id': None, 'issuer_name': None, 'market_cap': None, 'volume_24h': None}, {'symbol': 'NVDAX', 'name':
            'NVIDIA tokenized stock (xStock)', 'price': 211.3282623557711, 'crypto_id': 36992, 'issuer_id':
            '69af7c7fef8bc60199c88622', 'issuer_name': 'Testing1', 'market_cap': 3731044.7, 'volume_24h': 8302814.85222761},
            {'symbol': 'MSTR', 'name': 'Strategy Inc. Tokenized Stock (Robinhood)', 'price': None, 'crypto_id': 40745,
            'issuer_id': None, 'issuer_name': None, 'market_cap': None, 'volume_24h': None}], 'tradfi_markets':
            [{'exchange': {'slug': 'binance', 'name': 'Binance', 'exchange_id': 270}, 'ticker': 'NVDA', 'market_url':
            'https://www.binance.com/en/stocks/EQ_NVDA'}]}, {'name': 'GOLD', 'symbol': 'GOLD', 'slug': 'gold', 'quotes':
            [{'symbol': 'USD', 'crypto_id': 2781, 'average_tokenized_price': 4018.181479970762, 'tokenized_market_cap':
            1884879975.1722481, 'tokenized_volume_24h': 139285845.12748477, 'last_updated': '2026-07-15T10:45:05.000Z'}],
            'rwa_id': 1, 'asset_type': 'commodity', 'rwa_rank': 1, 'has_tokens': True, 'average_tokenized_price':
            4018.181479970762, 'tokenized_market_cap': 1884879975.1722481, 'tokenized_volume_24h': 139285845.12748477,
            'last_updated': '2026-07-15T10:13:26.989Z', 'tokens': [{'symbol': 'DGX', 'name': 'Digix Gold Token', 'price':
            None, 'crypto_id': 2739, 'issuer_id': None, 'issuer_name': None, 'market_cap': 0, 'volume_24h': 0}, {'symbol':
            'PAXG', 'name': 'PAX Gold', 'price': 4024.3699282937187, 'crypto_id': 4705, 'issuer_id': None, 'issuer_name':
            None, 'market_cap': 1806493532.83, 'volume_24h': 134844803.16977933}, {'symbol': 'XAUM', 'name': 'Matrixdock
            Gold', 'price': 4030.1765182593685, 'crypto_id': 34212, 'issuer_id': None, 'issuer_name': None, 'market_cap':
            45234553.51, 'volume_24h': 645710.16264194}, {'symbol': 'GOLDAO', 'name': 'GOLDAO', 'price':
            0.003454950092485161, 'crypto_id': 31296, 'issuer_id': None, 'issuer_name': None, 'market_cap': 2738250.71,
            'volume_24h': 816.29239512}], 'tradfi_markets': []}]}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: RWAQuotesLatestResultsObject
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
        from ..models.rwa_quotes_latest_results_object import RWAQuotesLatestResultsObject

        d = dict(src_dict)
        data = RWAQuotesLatestResultsObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        rwa_quotes_latest_response_model = cls(
            data=data,
            status=status,
        )

        rwa_quotes_latest_response_model.additional_properties = d
        return rwa_quotes_latest_response_model

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
