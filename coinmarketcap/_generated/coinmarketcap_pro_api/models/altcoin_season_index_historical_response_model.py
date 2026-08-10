from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.altcoin_season_index_historical_response_object import AltcoinSeasonIndexHistoricalResponseObject
    from ..models.api_status_object import APIStatusObject


T = TypeVar("T", bound="AltcoinSeasonIndexHistoricalResponseModel")


@_attrs_define
class AltcoinSeasonIndexHistoricalResponseModel:
    """
    Attributes:
        data (AltcoinSeasonIndexHistoricalResponseObject): Altcoin Season Index historical series for a timeframe.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: AltcoinSeasonIndexHistoricalResponseObject
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.altcoin_season_index_historical_response_object import AltcoinSeasonIndexHistoricalResponseObject
        from ..models.api_status_object import APIStatusObject

        d = dict(src_dict)
        data = AltcoinSeasonIndexHistoricalResponseObject.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        altcoin_season_index_historical_response_model = cls(
            data=data,
            status=status,
        )

        altcoin_season_index_historical_response_model.additional_properties = d
        return altcoin_season_index_historical_response_model

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
