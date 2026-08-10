from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.derivatives_market_pairs_list_latest_results_object_market_pairs_item import (
        DerivativesMarketPairsListLatestResultsObjectMarketPairsItem,
    )


T = TypeVar("T", bound="DerivativesMarketPairsListLatestResultsObject")


@_attrs_define
class DerivativesMarketPairsListLatestResultsObject:
    """Results of your query returned as an object.

    Example:
        {'exchange_id': 270, 'exchange_name': 'Binance', 'exchange_slug': 'binance', 'num_market_pairs': 2045,
            'volume_24h': 69306677552.93349, 'market_pairs': [{'market_id': 47150, 'market_pair': 'BTC/USDT', 'category':
            'perpetual', 'fee_type': 'percentage', 'outlier_detected': False, 'exclusions': None, 'market_pair_base':
            {'exchange_symbol': 'BTC', 'symbol': 'BTC', 'crypto_id': 1, 'currency_type': 'cryptocurrency'},
            'market_pair_quote': {'exchange_symbol': 'USDT', 'symbol': 'USDT', 'crypto_id': 825, 'currency_type':
            'cryptocurrency'}, 'exchange_reported_quotes': [{'crypto_id': 2781, 'symbol': 'USD', 'price': 80521.2,
            'volume_24h_base': 184589.83976729, 'volume_24h_quote': 14863395405.87, 'open_interest': 5000000, 'index_price':
            80498.5, 'index_basis': 0.0023, 'funding_rate': 0.0001, 'last_updated': '2026-05-15T06:54:18.743Z',
            'volume_percentage': 21.441131937316662}], 'quotes': [{'crypto_id': 2781, 'symbol': 'USD', 'price':
            80504.01770192, 'volume_24h': 14860136175.4951, 'open_interest': 5000000, 'last_updated':
            '2026-05-15T06:54:18.743Z'}]}]}

    Attributes:
        exchange_id (int | Unset): The CoinMarketCap ID for this exchange. Example: 270.
        exchange_name (str | Unset): The name of this exchange. Example: Binance.
        exchange_slug (str | Unset): The slug for this exchange. Example: binance.
        num_market_pairs (int | Unset): Number of derivative market pairs CoinMarketCap tracks for this exchange.
            Example: 2045.
        volume_24h (float | Unset): Reported 24h trade volume across all derivative market pairs for this exchange in
            USD. Example: 69306677552.93349.
        market_pairs (list[DerivativesMarketPairsListLatestResultsObjectMarketPairsItem] | Unset): Array of derivative
            market pairs for this exchange.
    """

    exchange_id: int | Unset = UNSET
    exchange_name: str | Unset = UNSET
    exchange_slug: str | Unset = UNSET
    num_market_pairs: int | Unset = UNSET
    volume_24h: float | Unset = UNSET
    market_pairs: list[DerivativesMarketPairsListLatestResultsObjectMarketPairsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange_id = self.exchange_id

        exchange_name = self.exchange_name

        exchange_slug = self.exchange_slug

        num_market_pairs = self.num_market_pairs

        volume_24h = self.volume_24h

        market_pairs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.market_pairs, Unset):
            market_pairs = []
            for market_pairs_item_data in self.market_pairs:
                market_pairs_item = market_pairs_item_data.to_dict()
                market_pairs.append(market_pairs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exchange_id is not UNSET:
            field_dict["exchange_id"] = exchange_id
        if exchange_name is not UNSET:
            field_dict["exchange_name"] = exchange_name
        if exchange_slug is not UNSET:
            field_dict["exchange_slug"] = exchange_slug
        if num_market_pairs is not UNSET:
            field_dict["num_market_pairs"] = num_market_pairs
        if volume_24h is not UNSET:
            field_dict["volume_24h"] = volume_24h
        if market_pairs is not UNSET:
            field_dict["market_pairs"] = market_pairs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.derivatives_market_pairs_list_latest_results_object_market_pairs_item import (
            DerivativesMarketPairsListLatestResultsObjectMarketPairsItem,
        )

        d = dict(src_dict)
        exchange_id = d.pop("exchange_id", UNSET)

        exchange_name = d.pop("exchange_name", UNSET)

        exchange_slug = d.pop("exchange_slug", UNSET)

        num_market_pairs = d.pop("num_market_pairs", UNSET)

        volume_24h = d.pop("volume_24h", UNSET)

        _market_pairs = d.pop("market_pairs", UNSET)
        market_pairs: list[DerivativesMarketPairsListLatestResultsObjectMarketPairsItem] | Unset = UNSET
        if _market_pairs is not UNSET:
            market_pairs = []
            for market_pairs_item_data in _market_pairs:
                market_pairs_item = DerivativesMarketPairsListLatestResultsObjectMarketPairsItem.from_dict(
                    market_pairs_item_data
                )

                market_pairs.append(market_pairs_item)

        derivatives_market_pairs_list_latest_results_object = cls(
            exchange_id=exchange_id,
            exchange_name=exchange_name,
            exchange_slug=exchange_slug,
            num_market_pairs=num_market_pairs,
            volume_24h=volume_24h,
            market_pairs=market_pairs,
        )

        derivatives_market_pairs_list_latest_results_object.additional_properties = d
        return derivatives_market_pairs_list_latest_results_object

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
