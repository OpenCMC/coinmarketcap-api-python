from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OhlcvBatchRequestDTO")


@_attrs_define
class OhlcvBatchRequestDTO:
    """
    Attributes:
        interval (str | Unset): valid paratmers: 1d/1h, 1d for daily ohlcv data and 1h for houly data.
        crypto_id (int | Unset): crypto id, required.
        scores (list[int] | Unset): scores of the batch, required.
    """

    interval: str | Unset = UNSET
    crypto_id: int | Unset = UNSET
    scores: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interval = self.interval

        crypto_id = self.crypto_id

        scores: list[int] | Unset = UNSET
        if not isinstance(self.scores, Unset):
            scores = self.scores

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interval is not UNSET:
            field_dict["interval"] = interval
        if crypto_id is not UNSET:
            field_dict["cryptoId"] = crypto_id
        if scores is not UNSET:
            field_dict["scores"] = scores

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interval = d.pop("interval", UNSET)

        crypto_id = d.pop("cryptoId", UNSET)

        scores = cast(list[int], d.pop("scores", UNSET))

        ohlcv_batch_request_dto = cls(
            interval=interval,
            crypto_id=crypto_id,
            scores=scores,
        )

        ohlcv_batch_request_dto.additional_properties = d
        return ohlcv_batch_request_dto

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
