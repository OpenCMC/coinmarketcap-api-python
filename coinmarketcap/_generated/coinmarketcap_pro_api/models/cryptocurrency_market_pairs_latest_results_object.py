from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cryptocurrency_market_pairs_latest_market_pair_info_object import (
        CryptocurrencyMarketPairsLatestMarketPairInfoObject,
    )


T = TypeVar("T", bound="CryptocurrencyMarketPairsLatestResultsObject")


@_attrs_define
class CryptocurrencyMarketPairsLatestResultsObject:
    """Results of your query returned as an object.

    Example:
        {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'num_market_pairs': 7526, 'market_pairs': [{'exchange': {'id':
            157, 'name': 'BitMEX', 'slug': 'bitmex'}, 'market_id': 4902, 'market_pair': 'BTC/USD', 'category':
            'derivatives', 'fee_type': 'no-fees', 'market_pair_base': {'currency_id': 1, 'currency_symbol': 'BTC',
            'exchange_symbol': 'XBT', 'currency_type': 'cryptocurrency'}, 'market_pair_quote': {'currency_id': 2781,
            'currency_symbol': 'USD', 'exchange_symbol': 'USD', 'currency_type': 'fiat'}, 'quote': {'exchange_reported':
            {'price': 7839, 'volume_24h_base': 434215.85308502, 'volume_24h_quote': 3403818072.33347, 'last_updated':
            '2019-05-24T02:39:00.000Z'}, 'USD': {'price': 7839, 'volume_24h': 3403818072.33347, 'last_updated':
            '2019-05-24T02:39:00.000Z'}}}, {'exchange': {'id': 108, 'name': 'Negocie Coins', 'slug': 'negocie-coins'},
            'market_id': 3377, 'market_pair': 'BTC/BRL', 'category': 'spot', 'fee_type': 'percentage', 'market_pair_base':
            {'currency_id': 1, 'currency_symbol': 'BTC', 'exchange_symbol': 'BTC', 'currency_type': 'cryptocurrency'},
            'market_pair_quote': {'currency_id': 2783, 'currency_symbol': 'BRL', 'exchange_symbol': 'BRL', 'currency_type':
            'fiat'}, 'quote': {'exchange_reported': {'price': 33002.11, 'volume_24h_base': 336699.03559957,
            'volume_24h_quote': 11111778609.7509, 'last_updated': '2019-05-24T02:39:00.000Z'}, 'USD': {'price':
            8165.02539531659, 'volume_24h': 2749156176.2491, 'last_updated': '2019-05-24T02:39:00.000Z'}}}]}

    Attributes:
        id (int): The CoinMarketCap ID for this cryptocurrency. Example: 1.
        name (str): The name of this cryptocurrency. Example: Bitcoin.
        symbol (str): The symbol for this cryptocurrency. Example: BTC.
        market_pairs (list[CryptocurrencyMarketPairsLatestMarketPairInfoObject]): Array of all market pairs for this
            cryptocurrency.
        num_market_pairs (int | Unset): The number of active market pairs listed for this cryptocurrency. This number is
            filtered down to only matching markets if a `matched` parameter is used. Example: 303.
    """

    id: int
    name: str
    symbol: str
    market_pairs: list[CryptocurrencyMarketPairsLatestMarketPairInfoObject]
    num_market_pairs: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        symbol = self.symbol

        market_pairs = []
        for componentsschemas_cryptocurrency_market_pairs_latest_market_pairs_array_item_data in self.market_pairs:
            componentsschemas_cryptocurrency_market_pairs_latest_market_pairs_array_item = (
                componentsschemas_cryptocurrency_market_pairs_latest_market_pairs_array_item_data.to_dict()
            )
            market_pairs.append(componentsschemas_cryptocurrency_market_pairs_latest_market_pairs_array_item)

        num_market_pairs = self.num_market_pairs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "symbol": symbol,
                "market_pairs": market_pairs,
            }
        )
        if num_market_pairs is not UNSET:
            field_dict["num_market_pairs"] = num_market_pairs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_market_pairs_latest_market_pair_info_object import (
            CryptocurrencyMarketPairsLatestMarketPairInfoObject,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        symbol = d.pop("symbol")

        market_pairs = []
        _market_pairs = d.pop("market_pairs")
        for componentsschemas_cryptocurrency_market_pairs_latest_market_pairs_array_item_data in _market_pairs:
            componentsschemas_cryptocurrency_market_pairs_latest_market_pairs_array_item = (
                CryptocurrencyMarketPairsLatestMarketPairInfoObject.from_dict(
                    componentsschemas_cryptocurrency_market_pairs_latest_market_pairs_array_item_data
                )
            )

            market_pairs.append(componentsschemas_cryptocurrency_market_pairs_latest_market_pairs_array_item)

        num_market_pairs = d.pop("num_market_pairs", UNSET)

        cryptocurrency_market_pairs_latest_results_object = cls(
            id=id,
            name=name,
            symbol=symbol,
            market_pairs=market_pairs,
            num_market_pairs=num_market_pairs,
        )

        cryptocurrency_market_pairs_latest_results_object.additional_properties = d
        return cryptocurrency_market_pairs_latest_results_object

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
