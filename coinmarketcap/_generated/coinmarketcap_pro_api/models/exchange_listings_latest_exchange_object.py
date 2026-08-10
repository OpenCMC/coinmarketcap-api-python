from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exchange_listings_latest_quote_map import ExchangeListingsLatestQuoteMap


T = TypeVar("T", bound="ExchangeListingsLatestExchangeObject")


@_attrs_define
class ExchangeListingsLatestExchangeObject:
    """An exchange object for every exchange that matched list options.

    Attributes:
        id (int): The unique CoinMarketCap ID for this exchange. Example: 1.
        name (str): The name of this exchange. Example: Binance.
        slug (str): The web URL friendly shorthand version of this exchange name. Example: Binance.
        last_updated (str): Timestamp (ISO 8601) of the last time this record was upated. Example:
            2018-06-02T00:00:00.000Z.
        quote (ExchangeListingsLatestQuoteMap): A map of market quotes in different currency conversions. The default
            map included is USD. Example: {'USD': {'volume_24h': 1418940000, 'last_updated': '2018-11-08T22:18:00.000Z',
            'volume_24h_adjusted': 1418940000, 'volume_7d': 3666423776, 'volume_30d': 21338299776,
            'percent_change_volume_24h': -11.62, 'percent_change_volume_7d': 67.21, 'percent_change_volume_30d': 0.0017,
            'effective_liquidity_24h': 629.98}}.
        num_market_pairs (int | Unset): The number of trading pairs actively tracked on this exchange. Example: 500.
        date_launched (str | Unset): Timestamp (ISO 8601) of the date this exchange launched. *This field is only
            returned if requested through the `aux` request parameter.* Example: 2018-06-02T00:00:00.000Z.
        exchange_score (float | Unset): The exchange score. Example: 9.8.
        liquidity_score (float | Unset): The liquidity score. Example: 9.8.
        rank (int | Unset): The exchange rank. Example: 5.
        traffic_score (float | Unset): The traffic score. Example: 1000.
    """

    id: int
    name: str
    slug: str
    last_updated: str
    quote: ExchangeListingsLatestQuoteMap
    num_market_pairs: int | Unset = UNSET
    date_launched: str | Unset = UNSET
    exchange_score: float | Unset = UNSET
    liquidity_score: float | Unset = UNSET
    rank: int | Unset = UNSET
    traffic_score: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        last_updated = self.last_updated

        quote = self.quote.to_dict()

        num_market_pairs = self.num_market_pairs

        date_launched = self.date_launched

        exchange_score = self.exchange_score

        liquidity_score = self.liquidity_score

        rank = self.rank

        traffic_score = self.traffic_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "last_updated": last_updated,
                "quote": quote,
            }
        )
        if num_market_pairs is not UNSET:
            field_dict["num_market_pairs"] = num_market_pairs
        if date_launched is not UNSET:
            field_dict["date_launched"] = date_launched
        if exchange_score is not UNSET:
            field_dict["exchange_score"] = exchange_score
        if liquidity_score is not UNSET:
            field_dict["liquidity_score"] = liquidity_score
        if rank is not UNSET:
            field_dict["rank"] = rank
        if traffic_score is not UNSET:
            field_dict["traffic_score"] = traffic_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exchange_listings_latest_quote_map import ExchangeListingsLatestQuoteMap

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        last_updated = d.pop("last_updated")

        quote = ExchangeListingsLatestQuoteMap.from_dict(d.pop("quote"))

        num_market_pairs = d.pop("num_market_pairs", UNSET)

        date_launched = d.pop("date_launched", UNSET)

        exchange_score = d.pop("exchange_score", UNSET)

        liquidity_score = d.pop("liquidity_score", UNSET)

        rank = d.pop("rank", UNSET)

        traffic_score = d.pop("traffic_score", UNSET)

        exchange_listings_latest_exchange_object = cls(
            id=id,
            name=name,
            slug=slug,
            last_updated=last_updated,
            quote=quote,
            num_market_pairs=num_market_pairs,
            date_launched=date_launched,
            exchange_score=exchange_score,
            liquidity_score=liquidity_score,
            rank=rank,
            traffic_score=traffic_score,
        )

        exchange_listings_latest_exchange_object.additional_properties = d
        return exchange_listings_latest_exchange_object

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
