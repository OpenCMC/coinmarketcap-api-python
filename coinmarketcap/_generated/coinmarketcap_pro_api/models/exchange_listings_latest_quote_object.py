from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExchangeListingsLatestQuoteObject")


@_attrs_define
class ExchangeListingsLatestQuoteObject:
    """A market quote in the currency conversion option.

    Attributes:
        last_updated (str): Timestamp (ISO 8601) of when the conversion currency's current value was referenced for this
            conversion. Example: 2018-06-02T23:59:59.999Z.
        volume_24h (float): Reported 24 hour volume in the specified currency. Example: 768478308.529847.
        volume_24h_adjusted (float): Adjusted 24 hour volume in the specified currency for spot markets excluding
            markets with no fees and transaction mining. Example: 768478308.529847.
        volume_7d (float): 7 day volume in the specified currency. Example: 3666423776.
        volume_30d (float): 30 day volume in the specified currency. Example: 21338299776.
        percent_change_volume_24h (float): 24 hour volume change percentage in the specified currency. Example: 0.03.
        percent_change_volume_7d (float): 7 day volume change percentage in the specified currency. Example: 5.75.
        percent_change_volume_30d (float): 30 day volume change percentage in the specified currency. Example: -19.64.
        effective_liquidity_24h (float | Unset): 24 hour liquidity in the specified currency. Example: -19.64.
        derivative_volume (float | Unset): Reported 24 hour derivative volume in the specified currency. Example:
            768478308.529847.
        open_interest (float | Unset): Reported 24 hour derivative open interest in the specified currency. Example:
            768478308.529847.
        spot_volume_usd (float | Unset): Reported all time spot volume in the specified currency. Example:
            768478308.529847.
    """

    last_updated: str
    volume_24h: float
    volume_24h_adjusted: float
    volume_7d: float
    volume_30d: float
    percent_change_volume_24h: float
    percent_change_volume_7d: float
    percent_change_volume_30d: float
    effective_liquidity_24h: float | Unset = UNSET
    derivative_volume: float | Unset = UNSET
    open_interest: float | Unset = UNSET
    spot_volume_usd: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_updated = self.last_updated

        volume_24h = self.volume_24h

        volume_24h_adjusted = self.volume_24h_adjusted

        volume_7d = self.volume_7d

        volume_30d = self.volume_30d

        percent_change_volume_24h = self.percent_change_volume_24h

        percent_change_volume_7d = self.percent_change_volume_7d

        percent_change_volume_30d = self.percent_change_volume_30d

        effective_liquidity_24h = self.effective_liquidity_24h

        derivative_volume = self.derivative_volume

        open_interest = self.open_interest

        spot_volume_usd = self.spot_volume_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "last_updated": last_updated,
                "volume_24h": volume_24h,
                "volume_24h_adjusted": volume_24h_adjusted,
                "volume_7d": volume_7d,
                "volume_30d": volume_30d,
                "percent_change_volume_24h": percent_change_volume_24h,
                "percent_change_volume_7d": percent_change_volume_7d,
                "percent_change_volume_30d": percent_change_volume_30d,
            }
        )
        if effective_liquidity_24h is not UNSET:
            field_dict["effective_liquidity_24h"] = effective_liquidity_24h
        if derivative_volume is not UNSET:
            field_dict["derivative_volume"] = derivative_volume
        if open_interest is not UNSET:
            field_dict["open_interest"] = open_interest
        if spot_volume_usd is not UNSET:
            field_dict["spot_volume_usd"] = spot_volume_usd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_updated = d.pop("last_updated")

        volume_24h = d.pop("volume_24h")

        volume_24h_adjusted = d.pop("volume_24h_adjusted")

        volume_7d = d.pop("volume_7d")

        volume_30d = d.pop("volume_30d")

        percent_change_volume_24h = d.pop("percent_change_volume_24h")

        percent_change_volume_7d = d.pop("percent_change_volume_7d")

        percent_change_volume_30d = d.pop("percent_change_volume_30d")

        effective_liquidity_24h = d.pop("effective_liquidity_24h", UNSET)

        derivative_volume = d.pop("derivative_volume", UNSET)

        open_interest = d.pop("open_interest", UNSET)

        spot_volume_usd = d.pop("spot_volume_usd", UNSET)

        exchange_listings_latest_quote_object = cls(
            last_updated=last_updated,
            volume_24h=volume_24h,
            volume_24h_adjusted=volume_24h_adjusted,
            volume_7d=volume_7d,
            volume_30d=volume_30d,
            percent_change_volume_24h=percent_change_volume_24h,
            percent_change_volume_7d=percent_change_volume_7d,
            percent_change_volume_30d=percent_change_volume_30d,
            effective_liquidity_24h=effective_liquidity_24h,
            derivative_volume=derivative_volume,
            open_interest=open_interest,
            spot_volume_usd=spot_volume_usd,
        )

        exchange_listings_latest_quote_object.additional_properties = d
        return exchange_listings_latest_quote_object

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
