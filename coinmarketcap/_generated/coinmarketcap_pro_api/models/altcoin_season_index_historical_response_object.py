from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.altcoin_season_index_historical_point_object import AltcoinSeasonIndexHistoricalPointObject


T = TypeVar("T", bound="AltcoinSeasonIndexHistoricalResponseObject")


@_attrs_define
class AltcoinSeasonIndexHistoricalResponseObject:
    """Altcoin Season Index historical series for a timeframe.

    Attributes:
        timeframe (str): Requested timeframe (7d, 30d, or 90d).
        points (list[AltcoinSeasonIndexHistoricalPointObject]): Historical points sorted by timestamp (oldest first).
    """

    timeframe: str
    points: list[AltcoinSeasonIndexHistoricalPointObject]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timeframe = self.timeframe

        points = []
        for points_item_data in self.points:
            points_item = points_item_data.to_dict()
            points.append(points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timeframe": timeframe,
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.altcoin_season_index_historical_point_object import AltcoinSeasonIndexHistoricalPointObject

        d = dict(src_dict)
        timeframe = d.pop("timeframe")

        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = AltcoinSeasonIndexHistoricalPointObject.from_dict(points_item_data)

            points.append(points_item)

        altcoin_season_index_historical_response_object = cls(
            timeframe=timeframe,
            points=points,
        )

        altcoin_season_index_historical_response_object.additional_properties = d
        return altcoin_season_index_historical_response_object

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
