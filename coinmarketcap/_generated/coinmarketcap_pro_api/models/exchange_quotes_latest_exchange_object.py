from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exchange_quotes_latest_quote_map import ExchangeQuotesLatestQuoteMap


T = TypeVar("T", bound="ExchangeQuotesLatestExchangeObject")


@_attrs_define
class ExchangeQuotesLatestExchangeObject:
    """An exchange object for each requested.

    Attributes:
        id (int): The CoinMarketCap exchange ID. Example: 1.
        name (str): The exchange name. Example: Binance.
        slug (str): The exchange slug. Example: binance.
        num_market_pairs (int): The number of active trading pairs available for this exchange. Example: 500.
        last_updated (str): Timestamp (ISO 8601) of the last time this exchange's market data was updated. Example:
            2018-06-02T00:00:00.000Z.
        quote (ExchangeQuotesLatestQuoteMap): A map of market quotes in different currency conversions. The default map
            included is USD.
        exchange_score (float | Unset): The exchange score. Example: 9.8.
        liquidity_score (float | Unset): The liquidity score. Example: 9.8.
        rank (int | Unset): The exchange rank. Example: 5.
        traffic_score (float | Unset): The traffic score. Example: 1000.
    """

    id: int
    name: str
    slug: str
    num_market_pairs: int
    last_updated: str
    quote: ExchangeQuotesLatestQuoteMap
    exchange_score: float | Unset = UNSET
    liquidity_score: float | Unset = UNSET
    rank: int | Unset = UNSET
    traffic_score: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        num_market_pairs = self.num_market_pairs

        last_updated = self.last_updated

        quote = self.quote.to_dict()

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
                "num_market_pairs": num_market_pairs,
                "last_updated": last_updated,
                "quote": quote,
            }
        )
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
        from ..models.exchange_quotes_latest_quote_map import ExchangeQuotesLatestQuoteMap

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        num_market_pairs = d.pop("num_market_pairs")

        last_updated = d.pop("last_updated")

        quote = ExchangeQuotesLatestQuoteMap.from_dict(d.pop("quote"))

        exchange_score = d.pop("exchange_score", UNSET)

        liquidity_score = d.pop("liquidity_score", UNSET)

        rank = d.pop("rank", UNSET)

        traffic_score = d.pop("traffic_score", UNSET)

        exchange_quotes_latest_exchange_object = cls(
            id=id,
            name=name,
            slug=slug,
            num_market_pairs=num_market_pairs,
            last_updated=last_updated,
            quote=quote,
            exchange_score=exchange_score,
            liquidity_score=liquidity_score,
            rank=rank,
            traffic_score=traffic_score,
        )

        exchange_quotes_latest_exchange_object.additional_properties = d
        return exchange_quotes_latest_exchange_object

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
