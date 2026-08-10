from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExchangeBatchRequestDTO")


@_attrs_define
class ExchangeBatchRequestDTO:
    """
    Attributes:
        exchange_id (int | Unset):
        scores (list[int] | Unset):
    """

    exchange_id: int | Unset = UNSET
    scores: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange_id = self.exchange_id

        scores: list[int] | Unset = UNSET
        if not isinstance(self.scores, Unset):
            scores = self.scores

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exchange_id is not UNSET:
            field_dict["exchangeId"] = exchange_id
        if scores is not UNSET:
            field_dict["scores"] = scores

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exchange_id = d.pop("exchangeId", UNSET)

        scores = cast(list[int], d.pop("scores", UNSET))

        exchange_batch_request_dto = cls(
            exchange_id=exchange_id,
            scores=scores,
        )

        exchange_batch_request_dto.additional_properties = d
        return exchange_batch_request_dto

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
