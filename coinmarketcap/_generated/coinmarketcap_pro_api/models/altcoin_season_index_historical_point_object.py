from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AltcoinSeasonIndexHistoricalPointObject")


@_attrs_define
class AltcoinSeasonIndexHistoricalPointObject:
    """Single Altcoin Season Index sample in a historical series.

    Attributes:
        timestamp (str): Sample time (ISO 8601).
        altcoin_index (int): Altcoin Season Index value (0-100).
        altcoin_marketcap (float | Unset): Altcoin market capitalization at sample time (USD).
    """

    timestamp: str
    altcoin_index: int
    altcoin_marketcap: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        altcoin_index = self.altcoin_index

        altcoin_marketcap = self.altcoin_marketcap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "altcoin_index": altcoin_index,
            }
        )
        if altcoin_marketcap is not UNSET:
            field_dict["altcoin_marketcap"] = altcoin_marketcap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        altcoin_index = d.pop("altcoin_index")

        altcoin_marketcap = d.pop("altcoin_marketcap", UNSET)

        altcoin_season_index_historical_point_object = cls(
            timestamp=timestamp,
            altcoin_index=altcoin_index,
            altcoin_marketcap=altcoin_marketcap,
        )

        altcoin_season_index_historical_point_object.additional_properties = d
        return altcoin_season_index_historical_point_object

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
