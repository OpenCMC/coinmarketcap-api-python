from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalMetricsQuotesLatestQuoteObject")


@_attrs_define
class GlobalMetricsQuotesLatestQuoteObject:
    """A market quote in the currency conversion option.

    Attributes:
        total_market_cap (float): The sum of all individual cryptocurrency market capitalizations in the requested
            currency. Example: 250385096532.124.
        total_volume_24h (float): The sum of rolling 24 hour adjusted volume (as outlined in our methodology) for all
            cryptocurrencies in the requested currency. Example: 119270642406.968.
        total_volume_24h_reported (float): The sum of rolling 24 hour reported volume for all cryptocurrencies in the
            requested currency. Example: 1514905418.39087.
        altcoin_volume_24h (float): The sum of rolling 24 hour adjusted volume (as outlined in our methodology) for all
            cryptocurrencies excluding Bitcoin in the requested currency. Example: 119270642406.968.
        altcoin_volume_24h_reported (float): The sum of rolling 24 hour reported volume for all cryptocurrencies
            excluding Bitcoin in the requested currency. Example: 1514905418.39087.
        altcoin_market_cap (float): The sum of all individual cryptocurrency market capitalizations excluding Bitcoin in
            the requested currency. Example: 250385096532.124.
        last_updated (str): Timestamp (ISO 8601) of when the conversion currency's current value was referenced.
            Example: 2019-05-16T18:47:00.000Z.
        defi_volume_24h (float | Unset): The sum of rolling 24 hour adjusted volume for all DeFi cryptocurrencies in the
            requested currency.
        defi_volume_24h_reported (float | Unset): The sum of rolling 24 hour reported volume for all DeFi
            cryptocurrencies in the requested currency.
        defi_market_cap (float | Unset): The sum of market caps for all DeFi cryptocurrencies in the requested currency.
        defi_24h_percentage_change (float | Unset): Percentage change in 24 hour DeFi volume compared with the previous
            24 hours.
        stablecoin_volume_24h (float | Unset): The sum of rolling 24 hour adjusted volume for all stablecoins in the
            requested currency.
        stablecoin_volume_24h_reported (float | Unset): The sum of rolling 24 hour reported volume for all stablecoins
            in the requested currency.
        stablecoin_market_cap (float | Unset): The sum of market caps for all stablecoins in the requested currency.
        stablecoin_24h_percentage_change (float | Unset): Percentage change in 24 hour stablecoin volume compared with
            the previous 24 hours.
        derivatives_volume_24h (float | Unset): The sum of rolling 24 hour adjusted volume for all derivatives markets
            in the requested currency.
        derivatives_volume_24h_reported (float | Unset): The sum of rolling 24 hour reported volume for all derivatives
            markets in the requested currency.
        derivatives_24h_percentage_change (float | Unset): Percentage change in 24 hour derivatives volume compared with
            the previous 24 hours.
        total_market_cap_yesterday (float | Unset): Total cryptocurrency market cap as of yesterday, in the requested
            currency.
        total_volume_24h_yesterday (float | Unset): Total 24 hour volume as of yesterday, in the requested currency.
        total_market_cap_yesterday_percentage_change (float | Unset): Percentage change in total market cap compared
            with yesterday.
        total_volume_24h_yesterday_percentage_change (float | Unset): Percentage change in total 24 hour volume compared
            with yesterday.
    """

    total_market_cap: float
    total_volume_24h: float
    total_volume_24h_reported: float
    altcoin_volume_24h: float
    altcoin_volume_24h_reported: float
    altcoin_market_cap: float
    last_updated: str
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
    total_market_cap_yesterday: float | Unset = UNSET
    total_volume_24h_yesterday: float | Unset = UNSET
    total_market_cap_yesterday_percentage_change: float | Unset = UNSET
    total_volume_24h_yesterday_percentage_change: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_market_cap = self.total_market_cap

        total_volume_24h = self.total_volume_24h

        total_volume_24h_reported = self.total_volume_24h_reported

        altcoin_volume_24h = self.altcoin_volume_24h

        altcoin_volume_24h_reported = self.altcoin_volume_24h_reported

        altcoin_market_cap = self.altcoin_market_cap

        last_updated = self.last_updated

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

        total_market_cap_yesterday = self.total_market_cap_yesterday

        total_volume_24h_yesterday = self.total_volume_24h_yesterday

        total_market_cap_yesterday_percentage_change = self.total_market_cap_yesterday_percentage_change

        total_volume_24h_yesterday_percentage_change = self.total_volume_24h_yesterday_percentage_change

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_market_cap": total_market_cap,
                "total_volume_24h": total_volume_24h,
                "total_volume_24h_reported": total_volume_24h_reported,
                "altcoin_volume_24h": altcoin_volume_24h,
                "altcoin_volume_24h_reported": altcoin_volume_24h_reported,
                "altcoin_market_cap": altcoin_market_cap,
                "last_updated": last_updated,
            }
        )
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
        if total_market_cap_yesterday is not UNSET:
            field_dict["total_market_cap_yesterday"] = total_market_cap_yesterday
        if total_volume_24h_yesterday is not UNSET:
            field_dict["total_volume_24h_yesterday"] = total_volume_24h_yesterday
        if total_market_cap_yesterday_percentage_change is not UNSET:
            field_dict["total_market_cap_yesterday_percentage_change"] = total_market_cap_yesterday_percentage_change
        if total_volume_24h_yesterday_percentage_change is not UNSET:
            field_dict["total_volume_24h_yesterday_percentage_change"] = total_volume_24h_yesterday_percentage_change

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_market_cap = d.pop("total_market_cap")

        total_volume_24h = d.pop("total_volume_24h")

        total_volume_24h_reported = d.pop("total_volume_24h_reported")

        altcoin_volume_24h = d.pop("altcoin_volume_24h")

        altcoin_volume_24h_reported = d.pop("altcoin_volume_24h_reported")

        altcoin_market_cap = d.pop("altcoin_market_cap")

        last_updated = d.pop("last_updated")

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

        total_market_cap_yesterday = d.pop("total_market_cap_yesterday", UNSET)

        total_volume_24h_yesterday = d.pop("total_volume_24h_yesterday", UNSET)

        total_market_cap_yesterday_percentage_change = d.pop("total_market_cap_yesterday_percentage_change", UNSET)

        total_volume_24h_yesterday_percentage_change = d.pop("total_volume_24h_yesterday_percentage_change", UNSET)

        global_metrics_quotes_latest_quote_object = cls(
            total_market_cap=total_market_cap,
            total_volume_24h=total_volume_24h,
            total_volume_24h_reported=total_volume_24h_reported,
            altcoin_volume_24h=altcoin_volume_24h,
            altcoin_volume_24h_reported=altcoin_volume_24h_reported,
            altcoin_market_cap=altcoin_market_cap,
            last_updated=last_updated,
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
            total_market_cap_yesterday=total_market_cap_yesterday,
            total_volume_24h_yesterday=total_volume_24h_yesterday,
            total_market_cap_yesterday_percentage_change=total_market_cap_yesterday_percentage_change,
            total_volume_24h_yesterday_percentage_change=total_volume_24h_yesterday_percentage_change,
        )

        global_metrics_quotes_latest_quote_object.additional_properties = d
        return global_metrics_quotes_latest_quote_object

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
