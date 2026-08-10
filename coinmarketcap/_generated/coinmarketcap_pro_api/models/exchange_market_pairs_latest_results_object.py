from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exchange_market_pairs_latest_market_pair_info_object import (
        ExchangeMarketPairsLatestMarketPairInfoObject,
    )


T = TypeVar("T", bound="ExchangeMarketPairsLatestResultsObject")


@_attrs_define
class ExchangeMarketPairsLatestResultsObject:
    """Results of your query returned as an object.

    Example:
        {'id': 270, 'name': 'Binance', 'slug': 'binance', 'num_market_pairs': 473, 'volume_24h': 769291636.239632,
            'market_pairs': [{'market_id': 9933, 'market_pair': 'BTC/USDT', 'category': 'spot', 'fee_type': 'percentage',
            'outlier_detected': 0, 'exclusions': None, 'market_pair_base': {'currency_id': 1, 'currency_symbol': 'BTC',
            'exchange_symbol': 'BTC', 'currency_type': 'cryptocurrency'}, 'market_pair_quote': {'currency_id': 825,
            'currency_symbol': 'USDT', 'exchange_symbol': 'USDT', 'currency_type': 'cryptocurrency'}, 'quote':
            {'exchange_reported': {'price': 7901.83, 'volume_24h_base': 47251.3345550653, 'volume_24h_quote':
            373372012.927251, 'volume_percentage': 19.4346563602467, 'last_updated': '2019-05-24T01:40:10.000Z'}, 'USD':
            {'price': 7933.66233493434, 'volume_24h': 374876133.234903, 'depth_negative_two': 40654.68019906,
            'depth_positive_two': 17352.9964811, 'last_updated': '2019-05-24T01:40:10.000Z'}}}, {'market_id': 36329,
            'market_pair': 'MATIC/BTC', 'category': 'spot', 'fee_type': 'percentage', 'outlier_detected': 0, 'exclusions':
            None, 'market_pair_base': {'currency_id': 3890, 'currency_symbol': 'MATIC', 'exchange_symbol': 'MATIC',
            'currency_type': 'cryptocurrency'}, 'market_pair_quote': {'currency_id': 1, 'currency_symbol': 'BTC',
            'exchange_symbol': 'BTC', 'currency_type': 'cryptocurrency'}, 'quote': {'exchange_reported': {'price': 3.4e-06,
            'volume_24h_base': 8773968381.05, 'volume_24h_quote': 29831.49249557, 'volume_percentage': 19.4346563602467,
            'last_updated': '2019-05-24T01:41:16.000Z'}, 'USD': {'price': 0.0269295015799739, 'volume_24h':
            236278595.380127, 'depth_negative_two': 40654.68019906, 'depth_positive_two': 17352.9964811, 'last_updated':
            '2019-05-24T01:41:16.000Z'}}}]}

    Attributes:
        id (int): The CoinMarketCap ID for this exchange. Example: 1.
        name (str): The name of this exchange. Example: Binance.
        slug (str): The slug for this exchange. Example: binance.
        num_market_pairs (int): The number of market pairs that are open for trading on this exchange. Example: 303.
        volume_24h (float): Reported 24 hour volume in USD. Example: 768478308.529847.
        market_pairs (list[ExchangeMarketPairsLatestMarketPairInfoObject]): Array of all active market pairs for this
            exchange.
    """

    id: int
    name: str
    slug: str
    num_market_pairs: int
    volume_24h: float
    market_pairs: list[ExchangeMarketPairsLatestMarketPairInfoObject]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        num_market_pairs = self.num_market_pairs

        volume_24h = self.volume_24h

        market_pairs = []
        for componentsschemas_exchange_market_pairs_latest_market_pairs_array_item_data in self.market_pairs:
            componentsschemas_exchange_market_pairs_latest_market_pairs_array_item = (
                componentsschemas_exchange_market_pairs_latest_market_pairs_array_item_data.to_dict()
            )
            market_pairs.append(componentsschemas_exchange_market_pairs_latest_market_pairs_array_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "num_market_pairs": num_market_pairs,
                "volume_24h": volume_24h,
                "market_pairs": market_pairs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exchange_market_pairs_latest_market_pair_info_object import (
            ExchangeMarketPairsLatestMarketPairInfoObject,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        num_market_pairs = d.pop("num_market_pairs")

        volume_24h = d.pop("volume_24h")

        market_pairs = []
        _market_pairs = d.pop("market_pairs")
        for componentsschemas_exchange_market_pairs_latest_market_pairs_array_item_data in _market_pairs:
            componentsschemas_exchange_market_pairs_latest_market_pairs_array_item = (
                ExchangeMarketPairsLatestMarketPairInfoObject.from_dict(
                    componentsschemas_exchange_market_pairs_latest_market_pairs_array_item_data
                )
            )

            market_pairs.append(componentsschemas_exchange_market_pairs_latest_market_pairs_array_item)

        exchange_market_pairs_latest_results_object = cls(
            id=id,
            name=name,
            slug=slug,
            num_market_pairs=num_market_pairs,
            volume_24h=volume_24h,
            market_pairs=market_pairs,
        )

        exchange_market_pairs_latest_results_object.additional_properties = d
        return exchange_market_pairs_latest_results_object

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
