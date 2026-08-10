from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.global_metrics_quotes_latest_quote_map import GlobalMetricsQuotesLatestQuoteMap


T = TypeVar("T", bound="GlobalMetricsQuotesLatestResultsObject")


@_attrs_define
class GlobalMetricsQuotesLatestResultsObject:
    """Results object for your API call.

    Attributes:
        active_cryptocurrencies (float): Count of active cryptocurrencies tracked by CoinMarketCap. This includes all
            cryptocurrencies with a `listing_status` of "active" or "listed" as returned from our /cryptocurrency/map call.
            Example: 2941.
        total_cryptocurrencies (float): Count of all cryptocurrencies tracked by CoinMarketCap. This includes "inactive"
            `listing_status` cryptocurrencies. Example: 4637.
        active_market_pairs (float): Count of active market pairs tracked by CoinMarketCap across all exchanges.
            Example: 21209.
        active_exchanges (float): Count of active exchanges tracked by CoinMarketCap. This includes all exchanges with a
            `listing_status` of "active" or "listed" as returned by our /exchange/map call. Example: 445.
        total_exchanges (float): Count of all exchanges tracked by CoinMarketCap. This includes "inactive"
            `listing_status` exchanges. Example: 677.
        last_updated (str): Timestamp of when this record was last updated. Example: 2019-05-16T18:47:00.000Z.
        quote (GlobalMetricsQuotesLatestQuoteMap): A map of market quotes in different currency conversions. The default
            map included is USD. Example: {'USD': {'total_market_cap': 250284668020.67, 'total_volume_24h': 16903498628.86,
            'total_volume_24h_reported': 16903498628.86, 'altcoin_volume_24h': 11883384723.14,
            'altcoin_volume_24h_reported': 11883384723.14, 'altcoin_market_cap': 119597549931.01, 'last_updated':
            '2018-06-02T23:46:14.000Z'}}.
        btc_dominance (float | Unset): Bitcoin's market dominance percentage by market cap. Example: 67.0057.
        eth_dominance (float | Unset): Ethereum's market dominance percentage by market cap. Example: 9.02205.
    """

    active_cryptocurrencies: float
    total_cryptocurrencies: float
    active_market_pairs: float
    active_exchanges: float
    total_exchanges: float
    last_updated: str
    quote: GlobalMetricsQuotesLatestQuoteMap
    btc_dominance: float | Unset = UNSET
    eth_dominance: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_cryptocurrencies = self.active_cryptocurrencies

        total_cryptocurrencies = self.total_cryptocurrencies

        active_market_pairs = self.active_market_pairs

        active_exchanges = self.active_exchanges

        total_exchanges = self.total_exchanges

        last_updated = self.last_updated

        quote = self.quote.to_dict()

        btc_dominance = self.btc_dominance

        eth_dominance = self.eth_dominance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active_cryptocurrencies": active_cryptocurrencies,
                "total_cryptocurrencies": total_cryptocurrencies,
                "active_market_pairs": active_market_pairs,
                "active_exchanges": active_exchanges,
                "total_exchanges": total_exchanges,
                "last_updated": last_updated,
                "quote": quote,
            }
        )
        if btc_dominance is not UNSET:
            field_dict["btc_dominance"] = btc_dominance
        if eth_dominance is not UNSET:
            field_dict["eth_dominance"] = eth_dominance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.global_metrics_quotes_latest_quote_map import GlobalMetricsQuotesLatestQuoteMap

        d = dict(src_dict)
        active_cryptocurrencies = d.pop("active_cryptocurrencies")

        total_cryptocurrencies = d.pop("total_cryptocurrencies")

        active_market_pairs = d.pop("active_market_pairs")

        active_exchanges = d.pop("active_exchanges")

        total_exchanges = d.pop("total_exchanges")

        last_updated = d.pop("last_updated")

        quote = GlobalMetricsQuotesLatestQuoteMap.from_dict(d.pop("quote"))

        btc_dominance = d.pop("btc_dominance", UNSET)

        eth_dominance = d.pop("eth_dominance", UNSET)

        global_metrics_quotes_latest_results_object = cls(
            active_cryptocurrencies=active_cryptocurrencies,
            total_cryptocurrencies=total_cryptocurrencies,
            active_market_pairs=active_market_pairs,
            active_exchanges=active_exchanges,
            total_exchanges=total_exchanges,
            last_updated=last_updated,
            quote=quote,
            btc_dominance=btc_dominance,
            eth_dominance=eth_dominance,
        )

        global_metrics_quotes_latest_results_object.additional_properties = d
        return global_metrics_quotes_latest_results_object

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
