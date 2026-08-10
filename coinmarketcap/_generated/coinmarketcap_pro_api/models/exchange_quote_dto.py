from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExchangeQuoteDTO")


@_attrs_define
class ExchangeQuoteDTO:
    """
    Attributes:
        exchange_id (int | Unset): Exchange ID
        num_trade_pairs (int | Unset): Number of trade pairs
        volume_usd (float | Unset): Volume in USD
        original_score (int | Unset): Original score
        score (int | Unset): Score
        time_utc (str | Unset): Time in UTC
    """

    exchange_id: int | Unset = UNSET
    num_trade_pairs: int | Unset = UNSET
    volume_usd: float | Unset = UNSET
    original_score: int | Unset = UNSET
    score: int | Unset = UNSET
    time_utc: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange_id = self.exchange_id

        num_trade_pairs = self.num_trade_pairs

        volume_usd = self.volume_usd

        original_score = self.original_score

        score = self.score

        time_utc = self.time_utc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exchange_id is not UNSET:
            field_dict["exchangeId"] = exchange_id
        if num_trade_pairs is not UNSET:
            field_dict["numTradePairs"] = num_trade_pairs
        if volume_usd is not UNSET:
            field_dict["volumeUsd"] = volume_usd
        if original_score is not UNSET:
            field_dict["originalScore"] = original_score
        if score is not UNSET:
            field_dict["score"] = score
        if time_utc is not UNSET:
            field_dict["time_utc"] = time_utc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exchange_id = d.pop("exchangeId", UNSET)

        num_trade_pairs = d.pop("numTradePairs", UNSET)

        volume_usd = d.pop("volumeUsd", UNSET)

        original_score = d.pop("originalScore", UNSET)

        score = d.pop("score", UNSET)

        time_utc = d.pop("time_utc", UNSET)

        exchange_quote_dto = cls(
            exchange_id=exchange_id,
            num_trade_pairs=num_trade_pairs,
            volume_usd=volume_usd,
            original_score=original_score,
            score=score,
            time_utc=time_utc,
        )

        exchange_quote_dto.additional_properties = d
        return exchange_quote_dto

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
