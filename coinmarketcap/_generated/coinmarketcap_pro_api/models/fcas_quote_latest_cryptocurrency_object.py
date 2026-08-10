from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FCASQuoteLatestCryptocurrencyObject")


@_attrs_define
class FCASQuoteLatestCryptocurrencyObject:
    """A cryptocurrency object for each requested.

    Attributes:
        id (int): The unique CoinMarketCap ID for this cryptocurrency. Example: 1.
        name (str): The name of this cryptocurrency. Example: Bitcoin.
        symbol (str): The ticker symbol for this cryptocurrency. Example: BTC.
        slug (str): The web URL friendly shorthand version of this cryptocurrency name. Example: bitcoin.
        score (int | Unset): The cryptocurrency's current FCAS score out of 1000 Example: 1000.
        grade (str | Unset): The cryptocurrency's current FCAS letter grade Example: A.
        percent_change_24h (float | Unset): 24 hour % FCAS score change Example: 0.03.
        point_change_24h (float | Unset): 24 hour FCAS point change Example: 5.
        last_updated (str | Unset): Timestamp (ISO 8601) of the last time this cryptocurrency's FCAS value was updated.
            Example: 2018-06-02T23:59:59.999Z.
    """

    id: int
    name: str
    symbol: str
    slug: str
    score: int | Unset = UNSET
    grade: str | Unset = UNSET
    percent_change_24h: float | Unset = UNSET
    point_change_24h: float | Unset = UNSET
    last_updated: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        symbol = self.symbol

        slug = self.slug

        score = self.score

        grade = self.grade

        percent_change_24h = self.percent_change_24h

        point_change_24h = self.point_change_24h

        last_updated = self.last_updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "symbol": symbol,
                "slug": slug,
            }
        )
        if score is not UNSET:
            field_dict["score"] = score
        if grade is not UNSET:
            field_dict["grade"] = grade
        if percent_change_24h is not UNSET:
            field_dict["percent_change_24h"] = percent_change_24h
        if point_change_24h is not UNSET:
            field_dict["point_change_24h"] = point_change_24h
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        symbol = d.pop("symbol")

        slug = d.pop("slug")

        score = d.pop("score", UNSET)

        grade = d.pop("grade", UNSET)

        percent_change_24h = d.pop("percent_change_24h", UNSET)

        point_change_24h = d.pop("point_change_24h", UNSET)

        last_updated = d.pop("last_updated", UNSET)

        fcas_quote_latest_cryptocurrency_object = cls(
            id=id,
            name=name,
            symbol=symbol,
            slug=slug,
            score=score,
            grade=grade,
            percent_change_24h=percent_change_24h,
            point_change_24h=point_change_24h,
            last_updated=last_updated,
        )

        fcas_quote_latest_cryptocurrency_object.additional_properties = d
        return fcas_quote_latest_cryptocurrency_object

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
