from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AltcoinSeasonIndexLatestResponseObject")


@_attrs_define
class AltcoinSeasonIndexLatestResponseObject:
    """Altcoin Season Index latest snapshot.

    Attributes:
        altcoin_index (int): Altcoin Season Index (0-100). Values above 75 indicate altcoin season; below 25 indicate
            Bitcoin season.
        altcoin_marketcap (float): Altcoin market capitalization (USD).
        snapshot_time (str): Snapshot timestamp (ISO 8601).
        yearly_high (int | Unset): Highest index value in the past year.
        yearly_high_date (str | Unset): Date of yearly high (ISO 8601 date).
        yearly_low (int | Unset): Lowest index value in the past year.
        yearly_low_date (str | Unset): Date of yearly low (ISO 8601 date).
    """

    altcoin_index: int
    altcoin_marketcap: float
    snapshot_time: str
    yearly_high: int | Unset = UNSET
    yearly_high_date: str | Unset = UNSET
    yearly_low: int | Unset = UNSET
    yearly_low_date: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        altcoin_index = self.altcoin_index

        altcoin_marketcap = self.altcoin_marketcap

        snapshot_time = self.snapshot_time

        yearly_high = self.yearly_high

        yearly_high_date = self.yearly_high_date

        yearly_low = self.yearly_low

        yearly_low_date = self.yearly_low_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "altcoin_index": altcoin_index,
                "altcoin_marketcap": altcoin_marketcap,
                "snapshot_time": snapshot_time,
            }
        )
        if yearly_high is not UNSET:
            field_dict["yearly_high"] = yearly_high
        if yearly_high_date is not UNSET:
            field_dict["yearly_high_date"] = yearly_high_date
        if yearly_low is not UNSET:
            field_dict["yearly_low"] = yearly_low
        if yearly_low_date is not UNSET:
            field_dict["yearly_low_date"] = yearly_low_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        altcoin_index = d.pop("altcoin_index")

        altcoin_marketcap = d.pop("altcoin_marketcap")

        snapshot_time = d.pop("snapshot_time")

        yearly_high = d.pop("yearly_high", UNSET)

        yearly_high_date = d.pop("yearly_high_date", UNSET)

        yearly_low = d.pop("yearly_low", UNSET)

        yearly_low_date = d.pop("yearly_low_date", UNSET)

        altcoin_season_index_latest_response_object = cls(
            altcoin_index=altcoin_index,
            altcoin_marketcap=altcoin_marketcap,
            snapshot_time=snapshot_time,
            yearly_high=yearly_high,
            yearly_high_date=yearly_high_date,
            yearly_low=yearly_low,
            yearly_low_date=yearly_low_date,
        )

        altcoin_season_index_latest_response_object.additional_properties = d
        return altcoin_season_index_latest_response_object

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
