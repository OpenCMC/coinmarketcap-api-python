from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cryptocurrency_price_performance_stats_latest_period_object_map import (
        CryptocurrencyPricePerformanceStatsLatestPeriodObjectMap,
    )


T = TypeVar("T", bound="CryptocurrencyPricePerformanceStatsLatestCryptocurrencyObject")


@_attrs_define
class CryptocurrencyPricePerformanceStatsLatestCryptocurrencyObject:
    """A cryptocurrency object for each requested.

    Attributes:
        id (int): The unique CoinMarketCap ID for this cryptocurrency. Example: 1.
        name (str): The name of this cryptocurrency. Example: Bitcoin.
        symbol (str): The ticker symbol for this cryptocurrency. Example: BTC.
        slug (str): The web URL friendly shorthand version of this cryptocurrency name. Example: bitcoin.
        last_updated (str): Timestamp (ISO 8601) of the last time this cryptocurrency's market data was updated.
            Example: 2019-08-22T01:51:32.000Z.
        periods (CryptocurrencyPricePerformanceStatsLatestPeriodObjectMap): An object map of time periods by period
            requested.
    """

    id: int
    name: str
    symbol: str
    slug: str
    last_updated: str
    periods: CryptocurrencyPricePerformanceStatsLatestPeriodObjectMap
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        symbol = self.symbol

        slug = self.slug

        last_updated = self.last_updated

        periods = self.periods.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "symbol": symbol,
                "slug": slug,
                "last_updated": last_updated,
                "periods": periods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_price_performance_stats_latest_period_object_map import (
            CryptocurrencyPricePerformanceStatsLatestPeriodObjectMap,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        symbol = d.pop("symbol")

        slug = d.pop("slug")

        last_updated = d.pop("last_updated")

        periods = CryptocurrencyPricePerformanceStatsLatestPeriodObjectMap.from_dict(d.pop("periods"))

        cryptocurrency_price_performance_stats_latest_cryptocurrency_object = cls(
            id=id,
            name=name,
            symbol=symbol,
            slug=slug,
            last_updated=last_updated,
            periods=periods,
        )

        cryptocurrency_price_performance_stats_latest_cryptocurrency_object.additional_properties = d
        return cryptocurrency_price_performance_stats_latest_cryptocurrency_object

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
