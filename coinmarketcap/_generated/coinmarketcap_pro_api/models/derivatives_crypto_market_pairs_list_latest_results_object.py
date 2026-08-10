from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.derivatives_crypto_market_pairs_list_latest_results_object_market_pairs_item import (
        DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItem,
    )


T = TypeVar("T", bound="DerivativesCryptoMarketPairsListLatestResultsObject")


@_attrs_define
class DerivativesCryptoMarketPairsListLatestResultsObject:
    """Results of your query returned as an object.

    Example:
        {'crypto_id': 1, 'crypto_name': 'Bitcoin', 'symbol': 'BTC', 'num_market_pairs': 5, 'market_pairs':
            [{'market_id': 79477, 'market_pair': 'BTC/USDT', 'category': 'perpetual', 'fee_type': 'percentage',
            'outlier_detected': False, 'exclusions': None, 'exchange': {'exchange_id': 270, 'exchange_name': 'Binance',
            'exchange_slug': 'binance'}, 'market_pair_base': {'crypto_id': 1, 'symbol': 'BTC', 'exchange_symbol': 'BTC',
            'currency_type': 'cryptocurrency'}, 'market_pair_quote': {'crypto_id': 825, 'symbol': 'USDT', 'exchange_symbol':
            'USDT', 'currency_type': 'cryptocurrency'}, 'exchange_reported_quotes': [{'crypto_id': 2781, 'symbol': 'USD',
            'price': 80496.6, 'volume_24h_base': 686357.90331837, 'volume_24h_quote': 55249477600.25728, 'open_interest':
            5000000, 'index_price': 80498.5, 'index_basis': 0.0023, 'funding_rate': 0.0001, 'last_updated':
            '2026-05-15T06:36:15.586Z'}], 'quotes': [{'crypto_id': 2781, 'symbol': 'USD', 'price': 80470.69372308,
            'volume_24h': 55231696622.35106, 'open_interest': 5000000, 'last_updated': '2026-05-15T06:36:15.586Z'}]}]}

    Attributes:
        crypto_id (int | Unset): The CoinMarketCap ID for this cryptocurrency. Example: 1.
        crypto_name (str | Unset): The name of this cryptocurrency. Example: Bitcoin.
        symbol (str | Unset): The symbol of this cryptocurrency. Example: BTC.
        num_market_pairs (int | Unset): Number of derivative market pairs CoinMarketCap tracks for this cryptocurrency
            across all exchanges. Example: 5.
        market_pairs (list[DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItem] | Unset): Array of
            derivative market pairs for this cryptocurrency, across exchanges.
    """

    crypto_id: int | Unset = UNSET
    crypto_name: str | Unset = UNSET
    symbol: str | Unset = UNSET
    num_market_pairs: int | Unset = UNSET
    market_pairs: list[DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crypto_id = self.crypto_id

        crypto_name = self.crypto_name

        symbol = self.symbol

        num_market_pairs = self.num_market_pairs

        market_pairs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.market_pairs, Unset):
            market_pairs = []
            for market_pairs_item_data in self.market_pairs:
                market_pairs_item = market_pairs_item_data.to_dict()
                market_pairs.append(market_pairs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crypto_id is not UNSET:
            field_dict["crypto_id"] = crypto_id
        if crypto_name is not UNSET:
            field_dict["crypto_name"] = crypto_name
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if num_market_pairs is not UNSET:
            field_dict["num_market_pairs"] = num_market_pairs
        if market_pairs is not UNSET:
            field_dict["market_pairs"] = market_pairs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.derivatives_crypto_market_pairs_list_latest_results_object_market_pairs_item import (
            DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItem,
        )

        d = dict(src_dict)
        crypto_id = d.pop("crypto_id", UNSET)

        crypto_name = d.pop("crypto_name", UNSET)

        symbol = d.pop("symbol", UNSET)

        num_market_pairs = d.pop("num_market_pairs", UNSET)

        _market_pairs = d.pop("market_pairs", UNSET)
        market_pairs: list[DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItem] | Unset = UNSET
        if _market_pairs is not UNSET:
            market_pairs = []
            for market_pairs_item_data in _market_pairs:
                market_pairs_item = DerivativesCryptoMarketPairsListLatestResultsObjectMarketPairsItem.from_dict(
                    market_pairs_item_data
                )

                market_pairs.append(market_pairs_item)

        derivatives_crypto_market_pairs_list_latest_results_object = cls(
            crypto_id=crypto_id,
            crypto_name=crypto_name,
            symbol=symbol,
            num_market_pairs=num_market_pairs,
            market_pairs=market_pairs,
        )

        derivatives_crypto_market_pairs_list_latest_results_object.additional_properties = d
        return derivatives_crypto_market_pairs_list_latest_results_object

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
