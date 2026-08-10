from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalMetricsQuoteDTO")


@_attrs_define
class GlobalMetricsQuoteDTO:
    """
    Attributes:
        score (int | Unset): Score value for sorting or ranking
        id (int | Unset): Unique identifier
        market_cap_by_available_supply_usd (float | Unset): Total market capitalization by available supply in USD
        market_cap_by_total_supply_usd (float | Unset): Total market capitalization by total supply in USD
        volume_usd (float | Unset): 24-hour trading volume in USD
        volume_usd_reported (float | Unset): Reported 24-hour trading volume in USD
        alt_coin_market_cap_by_available_supply_usd (float | Unset): Altcoin market capitalization by available supply
            in USD
        alt_coin_volume_usd (float | Unset): Altcoin 24-hour trading volume in USD
        alt_coin_volume_usd_reported (float | Unset): Reported altcoin 24-hour trading volume in USD
        bitcoin_percentage_of_market_cap (float | Unset): Bitcoin percentage of total market cap
        eth_percentage_of_market_cap (float | Unset): Ethereum percentage of total market cap
        active_cryptocurrencies (int | Unset): Number of active cryptocurrencies
        active_exchanges (int | Unset): Number of active exchanges
        active_market_pairs (int | Unset): Number of active market pairs
        defi_volume_24_h (float | Unset): DeFi 24-hour trading volume
        defi_volume_24_h_reported (float | Unset): Reported DeFi 24-hour trading volume
        defi_market_cap (float | Unset): DeFi market capitalization
        stable_coin_volume_24_h (float | Unset): Stablecoin 24-hour trading volume
        stable_coin_volume_24_h_reported (float | Unset): Reported stablecoin 24-hour trading volume
        stable_coin_market_cap (float | Unset): Stablecoin market capitalization
        derivatives_volume_24_h (float | Unset): Derivatives 24-hour trading volume
        derivatives_volume_24_h_reported (float | Unset): Reported derivatives 24-hour trading volume
        total_cryptocurrencies (int | Unset): Total number of cryptocurrencies
        total_exchanges (int | Unset): Total number of exchanges
    """

    score: int | Unset = UNSET
    id: int | Unset = UNSET
    market_cap_by_available_supply_usd: float | Unset = UNSET
    market_cap_by_total_supply_usd: float | Unset = UNSET
    volume_usd: float | Unset = UNSET
    volume_usd_reported: float | Unset = UNSET
    alt_coin_market_cap_by_available_supply_usd: float | Unset = UNSET
    alt_coin_volume_usd: float | Unset = UNSET
    alt_coin_volume_usd_reported: float | Unset = UNSET
    bitcoin_percentage_of_market_cap: float | Unset = UNSET
    eth_percentage_of_market_cap: float | Unset = UNSET
    active_cryptocurrencies: int | Unset = UNSET
    active_exchanges: int | Unset = UNSET
    active_market_pairs: int | Unset = UNSET
    defi_volume_24_h: float | Unset = UNSET
    defi_volume_24_h_reported: float | Unset = UNSET
    defi_market_cap: float | Unset = UNSET
    stable_coin_volume_24_h: float | Unset = UNSET
    stable_coin_volume_24_h_reported: float | Unset = UNSET
    stable_coin_market_cap: float | Unset = UNSET
    derivatives_volume_24_h: float | Unset = UNSET
    derivatives_volume_24_h_reported: float | Unset = UNSET
    total_cryptocurrencies: int | Unset = UNSET
    total_exchanges: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        score = self.score

        id = self.id

        market_cap_by_available_supply_usd = self.market_cap_by_available_supply_usd

        market_cap_by_total_supply_usd = self.market_cap_by_total_supply_usd

        volume_usd = self.volume_usd

        volume_usd_reported = self.volume_usd_reported

        alt_coin_market_cap_by_available_supply_usd = self.alt_coin_market_cap_by_available_supply_usd

        alt_coin_volume_usd = self.alt_coin_volume_usd

        alt_coin_volume_usd_reported = self.alt_coin_volume_usd_reported

        bitcoin_percentage_of_market_cap = self.bitcoin_percentage_of_market_cap

        eth_percentage_of_market_cap = self.eth_percentage_of_market_cap

        active_cryptocurrencies = self.active_cryptocurrencies

        active_exchanges = self.active_exchanges

        active_market_pairs = self.active_market_pairs

        defi_volume_24_h = self.defi_volume_24_h

        defi_volume_24_h_reported = self.defi_volume_24_h_reported

        defi_market_cap = self.defi_market_cap

        stable_coin_volume_24_h = self.stable_coin_volume_24_h

        stable_coin_volume_24_h_reported = self.stable_coin_volume_24_h_reported

        stable_coin_market_cap = self.stable_coin_market_cap

        derivatives_volume_24_h = self.derivatives_volume_24_h

        derivatives_volume_24_h_reported = self.derivatives_volume_24_h_reported

        total_cryptocurrencies = self.total_cryptocurrencies

        total_exchanges = self.total_exchanges

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if score is not UNSET:
            field_dict["score"] = score
        if id is not UNSET:
            field_dict["id"] = id
        if market_cap_by_available_supply_usd is not UNSET:
            field_dict["marketCapByAvailableSupplyUsd"] = market_cap_by_available_supply_usd
        if market_cap_by_total_supply_usd is not UNSET:
            field_dict["marketCapByTotalSupplyUsd"] = market_cap_by_total_supply_usd
        if volume_usd is not UNSET:
            field_dict["volumeUsd"] = volume_usd
        if volume_usd_reported is not UNSET:
            field_dict["volumeUsdReported"] = volume_usd_reported
        if alt_coin_market_cap_by_available_supply_usd is not UNSET:
            field_dict["altCoinMarketCapByAvailableSupplyUsd"] = alt_coin_market_cap_by_available_supply_usd
        if alt_coin_volume_usd is not UNSET:
            field_dict["altCoinVolumeUsd"] = alt_coin_volume_usd
        if alt_coin_volume_usd_reported is not UNSET:
            field_dict["altCoinVolumeUsdReported"] = alt_coin_volume_usd_reported
        if bitcoin_percentage_of_market_cap is not UNSET:
            field_dict["bitcoinPercentageOfMarketCap"] = bitcoin_percentage_of_market_cap
        if eth_percentage_of_market_cap is not UNSET:
            field_dict["ethPercentageOfMarketCap"] = eth_percentage_of_market_cap
        if active_cryptocurrencies is not UNSET:
            field_dict["activeCryptocurrencies"] = active_cryptocurrencies
        if active_exchanges is not UNSET:
            field_dict["activeExchanges"] = active_exchanges
        if active_market_pairs is not UNSET:
            field_dict["activeMarketPairs"] = active_market_pairs
        if defi_volume_24_h is not UNSET:
            field_dict["defiVolume24h"] = defi_volume_24_h
        if defi_volume_24_h_reported is not UNSET:
            field_dict["defiVolume24hReported"] = defi_volume_24_h_reported
        if defi_market_cap is not UNSET:
            field_dict["defiMarketCap"] = defi_market_cap
        if stable_coin_volume_24_h is not UNSET:
            field_dict["stableCoinVolume24h"] = stable_coin_volume_24_h
        if stable_coin_volume_24_h_reported is not UNSET:
            field_dict["stableCoinVolume24hReported"] = stable_coin_volume_24_h_reported
        if stable_coin_market_cap is not UNSET:
            field_dict["stableCoinMarketCap"] = stable_coin_market_cap
        if derivatives_volume_24_h is not UNSET:
            field_dict["derivativesVolume24h"] = derivatives_volume_24_h
        if derivatives_volume_24_h_reported is not UNSET:
            field_dict["derivativesVolume24hReported"] = derivatives_volume_24_h_reported
        if total_cryptocurrencies is not UNSET:
            field_dict["totalCryptocurrencies"] = total_cryptocurrencies
        if total_exchanges is not UNSET:
            field_dict["totalExchanges"] = total_exchanges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        score = d.pop("score", UNSET)

        id = d.pop("id", UNSET)

        market_cap_by_available_supply_usd = d.pop("marketCapByAvailableSupplyUsd", UNSET)

        market_cap_by_total_supply_usd = d.pop("marketCapByTotalSupplyUsd", UNSET)

        volume_usd = d.pop("volumeUsd", UNSET)

        volume_usd_reported = d.pop("volumeUsdReported", UNSET)

        alt_coin_market_cap_by_available_supply_usd = d.pop("altCoinMarketCapByAvailableSupplyUsd", UNSET)

        alt_coin_volume_usd = d.pop("altCoinVolumeUsd", UNSET)

        alt_coin_volume_usd_reported = d.pop("altCoinVolumeUsdReported", UNSET)

        bitcoin_percentage_of_market_cap = d.pop("bitcoinPercentageOfMarketCap", UNSET)

        eth_percentage_of_market_cap = d.pop("ethPercentageOfMarketCap", UNSET)

        active_cryptocurrencies = d.pop("activeCryptocurrencies", UNSET)

        active_exchanges = d.pop("activeExchanges", UNSET)

        active_market_pairs = d.pop("activeMarketPairs", UNSET)

        defi_volume_24_h = d.pop("defiVolume24h", UNSET)

        defi_volume_24_h_reported = d.pop("defiVolume24hReported", UNSET)

        defi_market_cap = d.pop("defiMarketCap", UNSET)

        stable_coin_volume_24_h = d.pop("stableCoinVolume24h", UNSET)

        stable_coin_volume_24_h_reported = d.pop("stableCoinVolume24hReported", UNSET)

        stable_coin_market_cap = d.pop("stableCoinMarketCap", UNSET)

        derivatives_volume_24_h = d.pop("derivativesVolume24h", UNSET)

        derivatives_volume_24_h_reported = d.pop("derivativesVolume24hReported", UNSET)

        total_cryptocurrencies = d.pop("totalCryptocurrencies", UNSET)

        total_exchanges = d.pop("totalExchanges", UNSET)

        global_metrics_quote_dto = cls(
            score=score,
            id=id,
            market_cap_by_available_supply_usd=market_cap_by_available_supply_usd,
            market_cap_by_total_supply_usd=market_cap_by_total_supply_usd,
            volume_usd=volume_usd,
            volume_usd_reported=volume_usd_reported,
            alt_coin_market_cap_by_available_supply_usd=alt_coin_market_cap_by_available_supply_usd,
            alt_coin_volume_usd=alt_coin_volume_usd,
            alt_coin_volume_usd_reported=alt_coin_volume_usd_reported,
            bitcoin_percentage_of_market_cap=bitcoin_percentage_of_market_cap,
            eth_percentage_of_market_cap=eth_percentage_of_market_cap,
            active_cryptocurrencies=active_cryptocurrencies,
            active_exchanges=active_exchanges,
            active_market_pairs=active_market_pairs,
            defi_volume_24_h=defi_volume_24_h,
            defi_volume_24_h_reported=defi_volume_24_h_reported,
            defi_market_cap=defi_market_cap,
            stable_coin_volume_24_h=stable_coin_volume_24_h,
            stable_coin_volume_24_h_reported=stable_coin_volume_24_h_reported,
            stable_coin_market_cap=stable_coin_market_cap,
            derivatives_volume_24_h=derivatives_volume_24_h,
            derivatives_volume_24_h_reported=derivatives_volume_24_h_reported,
            total_cryptocurrencies=total_cryptocurrencies,
            total_exchanges=total_exchanges,
        )

        global_metrics_quote_dto.additional_properties = d
        return global_metrics_quote_dto

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
