from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.global_metrics_quotes_historic_quote_currency_map import GlobalMetricsQuotesHistoricQuoteCurrencyMap


T = TypeVar("T", bound="GlobalMetricsQuotesHistoricIntervalQuoteObject")


@_attrs_define
class GlobalMetricsQuotesHistoricIntervalQuoteObject:
    """An object containing details for the current interval quote.

    Attributes:
        timestamp (str): Timestamp (ISO 8601) of when this historical quote was recorded. Example:
            2018-06-02T00:00:00.000Z.
        btc_dominance (float): Percent of BTC market dominance by marketcap at this interval.
        eth_dominance (float): Percent of ETH market dominance by marketcap at this interval.
        active_cryptocurrencies (float): Number of active cryptocurrencies tracked by CoinMarketCap at the given point
            in time. This includes all cryptocurrencies with a `listing_status` of "active" or "untracked" as returned from
            our /cryptocurrency/map call. *Note: This field is only available after 2019-05-10 and will return `null` prior
            to that time.* Example: 500.
        active_exchanges (float): Number of active exchanges tracked by CoinMarketCap at the given point in time. This
            includes all exchanges with a `listing_status` of "active" or "untracked" as returned by our /exchange/map call.
            *Note: This field is only available after 2019-06-18 and will return `null` prior to that time.* Example: 200.
        active_market_pairs (float): Number of active market pairs tracked by CoinMarketCap across all exchanges at the
            given point in time. *Note: This field is only available after 2019-05-10 and will return `null` prior to that
            time.* Example: 1000.
        quote (GlobalMetricsQuotesHistoricQuoteCurrencyMap): An object containing market data for this interval by
            currency option. The default currency mapped is USD.
        search_interval (str | Unset): The interval timestamp for the search period that this historical quote was
            located against. *This field is only returned if requested through the `aux` request parameter.* Example:
            2018-06-02T00:00:00.000Z.
    """

    timestamp: str
    btc_dominance: float
    eth_dominance: float
    active_cryptocurrencies: float
    active_exchanges: float
    active_market_pairs: float
    quote: GlobalMetricsQuotesHistoricQuoteCurrencyMap
    search_interval: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        btc_dominance = self.btc_dominance

        eth_dominance = self.eth_dominance

        active_cryptocurrencies = self.active_cryptocurrencies

        active_exchanges = self.active_exchanges

        active_market_pairs = self.active_market_pairs

        quote = self.quote.to_dict()

        search_interval = self.search_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "btc_dominance": btc_dominance,
                "eth_dominance": eth_dominance,
                "active_cryptocurrencies": active_cryptocurrencies,
                "active_exchanges": active_exchanges,
                "active_market_pairs": active_market_pairs,
                "quote": quote,
            }
        )
        if search_interval is not UNSET:
            field_dict["search_interval"] = search_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.global_metrics_quotes_historic_quote_currency_map import (
            GlobalMetricsQuotesHistoricQuoteCurrencyMap,
        )

        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        btc_dominance = d.pop("btc_dominance")

        eth_dominance = d.pop("eth_dominance")

        active_cryptocurrencies = d.pop("active_cryptocurrencies")

        active_exchanges = d.pop("active_exchanges")

        active_market_pairs = d.pop("active_market_pairs")

        quote = GlobalMetricsQuotesHistoricQuoteCurrencyMap.from_dict(d.pop("quote"))

        search_interval = d.pop("search_interval", UNSET)

        global_metrics_quotes_historic_interval_quote_object = cls(
            timestamp=timestamp,
            btc_dominance=btc_dominance,
            eth_dominance=eth_dominance,
            active_cryptocurrencies=active_cryptocurrencies,
            active_exchanges=active_exchanges,
            active_market_pairs=active_market_pairs,
            quote=quote,
            search_interval=search_interval,
        )

        global_metrics_quotes_historic_interval_quote_object.additional_properties = d
        return global_metrics_quotes_historic_interval_quote_object

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
