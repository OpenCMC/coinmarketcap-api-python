from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.global_metrics_quotes_latest_quote_map import GlobalMetricsQuotesLatestQuoteMap
    from ..models.global_metrics_quotes_latest_results_object_tracked_yearly_number import (
        GlobalMetricsQuotesLatestResultsObjectTrackedYearlyNumber,
    )


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
        eth_dominance_yesterday (float | Unset): Ethereum's market dominance percentage by market cap as of yesterday.
        btc_dominance_yesterday (float | Unset): Bitcoin's market dominance percentage by market cap as of yesterday.
        eth_dominance_24h_percentage_change (float | Unset): Change in Ethereum's market dominance since yesterday, in
            percentage points.
        btc_dominance_24h_percentage_change (float | Unset): Change in Bitcoin's market dominance since yesterday, in
            percentage points.
        defi_volume_24h (float | Unset): The sum of rolling 24 hour adjusted volume for all DeFi cryptocurrencies in
            USD.
        defi_volume_24h_reported (float | Unset): The sum of rolling 24 hour reported volume for all DeFi
            cryptocurrencies in USD.
        defi_market_cap (float | Unset): The sum of market caps for all DeFi cryptocurrencies in USD.
        defi_24h_percentage_change (float | Unset): Percentage change in 24 hour DeFi volume compared with the previous
            24 hours.
        stablecoin_volume_24h (float | Unset): The sum of rolling 24 hour adjusted volume for all stablecoins in USD.
        stablecoin_volume_24h_reported (float | Unset): The sum of rolling 24 hour reported volume for all stablecoins
            in USD.
        stablecoin_market_cap (float | Unset): The sum of market caps for all stablecoins in USD.
        stablecoin_24h_percentage_change (float | Unset): Percentage change in 24 hour stablecoin volume compared with
            the previous 24 hours.
        derivatives_volume_24h (float | Unset): The sum of rolling 24 hour adjusted volume for all derivatives markets
            in USD.
        derivatives_volume_24h_reported (float | Unset): The sum of rolling 24 hour reported volume for all derivatives
            markets in USD.
        derivatives_24h_percentage_change (float | Unset): Percentage change in 24 hour derivatives volume compared with
            the previous 24 hours.
        total_crypto_dex_currencies (int | Unset): Total number of DEX tokens tracked by CoinMarketCap.
        today_incremental_crypto_number (int | Unset): Number of new cryptocurrencies and DEX tokens tracked so far
            today (UTC).
        past_24h_incremental_crypto_number (int | Unset): Number of new cryptocurrencies and DEX tokens tracked in the
            past 24 hours.
        past_7d_incremental_crypto_number (int | Unset): Number of new cryptocurrencies and DEX tokens tracked in the
            past 7 days.
        past_30d_incremental_crypto_number (int | Unset): Number of new cryptocurrencies and DEX tokens tracked in the
            past 30 days.
        tracked_yearly_number (GlobalMetricsQuotesLatestResultsObjectTrackedYearlyNumber | Unset): The highest and
            lowest number of new cryptocurrencies and DEX tokens tracked in a single day over the past year.
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
    eth_dominance_yesterday: float | Unset = UNSET
    btc_dominance_yesterday: float | Unset = UNSET
    eth_dominance_24h_percentage_change: float | Unset = UNSET
    btc_dominance_24h_percentage_change: float | Unset = UNSET
    defi_volume_24h: float | Unset = UNSET
    defi_volume_24h_reported: float | Unset = UNSET
    defi_market_cap: float | Unset = UNSET
    defi_24h_percentage_change: float | Unset = UNSET
    stablecoin_volume_24h: float | Unset = UNSET
    stablecoin_volume_24h_reported: float | Unset = UNSET
    stablecoin_market_cap: float | Unset = UNSET
    stablecoin_24h_percentage_change: float | Unset = UNSET
    derivatives_volume_24h: float | Unset = UNSET
    derivatives_volume_24h_reported: float | Unset = UNSET
    derivatives_24h_percentage_change: float | Unset = UNSET
    total_crypto_dex_currencies: int | Unset = UNSET
    today_incremental_crypto_number: int | Unset = UNSET
    past_24h_incremental_crypto_number: int | Unset = UNSET
    past_7d_incremental_crypto_number: int | Unset = UNSET
    past_30d_incremental_crypto_number: int | Unset = UNSET
    tracked_yearly_number: GlobalMetricsQuotesLatestResultsObjectTrackedYearlyNumber | Unset = UNSET
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

        eth_dominance_yesterday = self.eth_dominance_yesterday

        btc_dominance_yesterday = self.btc_dominance_yesterday

        eth_dominance_24h_percentage_change = self.eth_dominance_24h_percentage_change

        btc_dominance_24h_percentage_change = self.btc_dominance_24h_percentage_change

        defi_volume_24h = self.defi_volume_24h

        defi_volume_24h_reported = self.defi_volume_24h_reported

        defi_market_cap = self.defi_market_cap

        defi_24h_percentage_change = self.defi_24h_percentage_change

        stablecoin_volume_24h = self.stablecoin_volume_24h

        stablecoin_volume_24h_reported = self.stablecoin_volume_24h_reported

        stablecoin_market_cap = self.stablecoin_market_cap

        stablecoin_24h_percentage_change = self.stablecoin_24h_percentage_change

        derivatives_volume_24h = self.derivatives_volume_24h

        derivatives_volume_24h_reported = self.derivatives_volume_24h_reported

        derivatives_24h_percentage_change = self.derivatives_24h_percentage_change

        total_crypto_dex_currencies = self.total_crypto_dex_currencies

        today_incremental_crypto_number = self.today_incremental_crypto_number

        past_24h_incremental_crypto_number = self.past_24h_incremental_crypto_number

        past_7d_incremental_crypto_number = self.past_7d_incremental_crypto_number

        past_30d_incremental_crypto_number = self.past_30d_incremental_crypto_number

        tracked_yearly_number: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tracked_yearly_number, Unset):
            tracked_yearly_number = self.tracked_yearly_number.to_dict()

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
        if eth_dominance_yesterday is not UNSET:
            field_dict["eth_dominance_yesterday"] = eth_dominance_yesterday
        if btc_dominance_yesterday is not UNSET:
            field_dict["btc_dominance_yesterday"] = btc_dominance_yesterday
        if eth_dominance_24h_percentage_change is not UNSET:
            field_dict["eth_dominance_24h_percentage_change"] = eth_dominance_24h_percentage_change
        if btc_dominance_24h_percentage_change is not UNSET:
            field_dict["btc_dominance_24h_percentage_change"] = btc_dominance_24h_percentage_change
        if defi_volume_24h is not UNSET:
            field_dict["defi_volume_24h"] = defi_volume_24h
        if defi_volume_24h_reported is not UNSET:
            field_dict["defi_volume_24h_reported"] = defi_volume_24h_reported
        if defi_market_cap is not UNSET:
            field_dict["defi_market_cap"] = defi_market_cap
        if defi_24h_percentage_change is not UNSET:
            field_dict["defi_24h_percentage_change"] = defi_24h_percentage_change
        if stablecoin_volume_24h is not UNSET:
            field_dict["stablecoin_volume_24h"] = stablecoin_volume_24h
        if stablecoin_volume_24h_reported is not UNSET:
            field_dict["stablecoin_volume_24h_reported"] = stablecoin_volume_24h_reported
        if stablecoin_market_cap is not UNSET:
            field_dict["stablecoin_market_cap"] = stablecoin_market_cap
        if stablecoin_24h_percentage_change is not UNSET:
            field_dict["stablecoin_24h_percentage_change"] = stablecoin_24h_percentage_change
        if derivatives_volume_24h is not UNSET:
            field_dict["derivatives_volume_24h"] = derivatives_volume_24h
        if derivatives_volume_24h_reported is not UNSET:
            field_dict["derivatives_volume_24h_reported"] = derivatives_volume_24h_reported
        if derivatives_24h_percentage_change is not UNSET:
            field_dict["derivatives_24h_percentage_change"] = derivatives_24h_percentage_change
        if total_crypto_dex_currencies is not UNSET:
            field_dict["total_crypto_dex_currencies"] = total_crypto_dex_currencies
        if today_incremental_crypto_number is not UNSET:
            field_dict["today_incremental_crypto_number"] = today_incremental_crypto_number
        if past_24h_incremental_crypto_number is not UNSET:
            field_dict["past_24h_incremental_crypto_number"] = past_24h_incremental_crypto_number
        if past_7d_incremental_crypto_number is not UNSET:
            field_dict["past_7d_incremental_crypto_number"] = past_7d_incremental_crypto_number
        if past_30d_incremental_crypto_number is not UNSET:
            field_dict["past_30d_incremental_crypto_number"] = past_30d_incremental_crypto_number
        if tracked_yearly_number is not UNSET:
            field_dict["tracked_yearly_number"] = tracked_yearly_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.global_metrics_quotes_latest_quote_map import GlobalMetricsQuotesLatestQuoteMap
        from ..models.global_metrics_quotes_latest_results_object_tracked_yearly_number import (
            GlobalMetricsQuotesLatestResultsObjectTrackedYearlyNumber,
        )

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

        eth_dominance_yesterday = d.pop("eth_dominance_yesterday", UNSET)

        btc_dominance_yesterday = d.pop("btc_dominance_yesterday", UNSET)

        eth_dominance_24h_percentage_change = d.pop("eth_dominance_24h_percentage_change", UNSET)

        btc_dominance_24h_percentage_change = d.pop("btc_dominance_24h_percentage_change", UNSET)

        defi_volume_24h = d.pop("defi_volume_24h", UNSET)

        defi_volume_24h_reported = d.pop("defi_volume_24h_reported", UNSET)

        defi_market_cap = d.pop("defi_market_cap", UNSET)

        defi_24h_percentage_change = d.pop("defi_24h_percentage_change", UNSET)

        stablecoin_volume_24h = d.pop("stablecoin_volume_24h", UNSET)

        stablecoin_volume_24h_reported = d.pop("stablecoin_volume_24h_reported", UNSET)

        stablecoin_market_cap = d.pop("stablecoin_market_cap", UNSET)

        stablecoin_24h_percentage_change = d.pop("stablecoin_24h_percentage_change", UNSET)

        derivatives_volume_24h = d.pop("derivatives_volume_24h", UNSET)

        derivatives_volume_24h_reported = d.pop("derivatives_volume_24h_reported", UNSET)

        derivatives_24h_percentage_change = d.pop("derivatives_24h_percentage_change", UNSET)

        total_crypto_dex_currencies = d.pop("total_crypto_dex_currencies", UNSET)

        today_incremental_crypto_number = d.pop("today_incremental_crypto_number", UNSET)

        past_24h_incremental_crypto_number = d.pop("past_24h_incremental_crypto_number", UNSET)

        past_7d_incremental_crypto_number = d.pop("past_7d_incremental_crypto_number", UNSET)

        past_30d_incremental_crypto_number = d.pop("past_30d_incremental_crypto_number", UNSET)

        _tracked_yearly_number = d.pop("tracked_yearly_number", UNSET)
        tracked_yearly_number: GlobalMetricsQuotesLatestResultsObjectTrackedYearlyNumber | Unset
        if isinstance(_tracked_yearly_number, Unset):
            tracked_yearly_number = UNSET
        else:
            tracked_yearly_number = GlobalMetricsQuotesLatestResultsObjectTrackedYearlyNumber.from_dict(
                _tracked_yearly_number
            )

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
            eth_dominance_yesterday=eth_dominance_yesterday,
            btc_dominance_yesterday=btc_dominance_yesterday,
            eth_dominance_24h_percentage_change=eth_dominance_24h_percentage_change,
            btc_dominance_24h_percentage_change=btc_dominance_24h_percentage_change,
            defi_volume_24h=defi_volume_24h,
            defi_volume_24h_reported=defi_volume_24h_reported,
            defi_market_cap=defi_market_cap,
            defi_24h_percentage_change=defi_24h_percentage_change,
            stablecoin_volume_24h=stablecoin_volume_24h,
            stablecoin_volume_24h_reported=stablecoin_volume_24h_reported,
            stablecoin_market_cap=stablecoin_market_cap,
            stablecoin_24h_percentage_change=stablecoin_24h_percentage_change,
            derivatives_volume_24h=derivatives_volume_24h,
            derivatives_volume_24h_reported=derivatives_volume_24h_reported,
            derivatives_24h_percentage_change=derivatives_24h_percentage_change,
            total_crypto_dex_currencies=total_crypto_dex_currencies,
            today_incremental_crypto_number=today_incremental_crypto_number,
            past_24h_incremental_crypto_number=past_24h_incremental_crypto_number,
            past_7d_incremental_crypto_number=past_7d_incremental_crypto_number,
            past_30d_incremental_crypto_number=past_30d_incremental_crypto_number,
            tracked_yearly_number=tracked_yearly_number,
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
