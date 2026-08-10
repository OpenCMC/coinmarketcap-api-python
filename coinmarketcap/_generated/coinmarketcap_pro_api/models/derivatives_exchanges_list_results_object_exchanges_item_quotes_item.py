from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DerivativesExchangesListResultsObjectExchangesItemQuotesItem")


@_attrs_define
class DerivativesExchangesListResultsObjectExchangesItemQuotesItem:
    """
    Attributes:
        convert_id (int | Unset): CoinMarketCap ID of the conversion currency. Example: 2781.
        convert_symbol (str | Unset): Symbol of the conversion currency. Example: USD.
        open_interest (float | Unset): Aggregate open interest across this exchange's derivative markets, in the
            conversion currency. Example: 23306624960.78.
        open_interest_usd (float | Unset): Aggregate open interest in USD. Example: 23306624960.78.
        derivative_volume (float | Unset): Aggregate 24h derivative trade volume in the conversion currency. Example:
            62828618628.85901.
        derivative_volume_usd (float | Unset): Aggregate 24h derivative trade volume in USD. Example: 62828618628.85901.
        maker_fees (float | Unset): Maker fee charged by this exchange (percentage). Example: 0.04.
        taker_fees (float | Unset): Taker fee charged by this exchange (percentage). Example: 0.04.
        last_updated (datetime.datetime | Unset): Timestamp (RFC 3339 UTC) of the last update for this quote. Example:
            2026-04-21T10:30:00.000Z.
    """

    convert_id: int | Unset = UNSET
    convert_symbol: str | Unset = UNSET
    open_interest: float | Unset = UNSET
    open_interest_usd: float | Unset = UNSET
    derivative_volume: float | Unset = UNSET
    derivative_volume_usd: float | Unset = UNSET
    maker_fees: float | Unset = UNSET
    taker_fees: float | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        convert_id = self.convert_id

        convert_symbol = self.convert_symbol

        open_interest = self.open_interest

        open_interest_usd = self.open_interest_usd

        derivative_volume = self.derivative_volume

        derivative_volume_usd = self.derivative_volume_usd

        maker_fees = self.maker_fees

        taker_fees = self.taker_fees

        last_updated: str | Unset = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if convert_id is not UNSET:
            field_dict["convert_id"] = convert_id
        if convert_symbol is not UNSET:
            field_dict["convert_symbol"] = convert_symbol
        if open_interest is not UNSET:
            field_dict["open_interest"] = open_interest
        if open_interest_usd is not UNSET:
            field_dict["open_interest_usd"] = open_interest_usd
        if derivative_volume is not UNSET:
            field_dict["derivative_volume"] = derivative_volume
        if derivative_volume_usd is not UNSET:
            field_dict["derivative_volume_usd"] = derivative_volume_usd
        if maker_fees is not UNSET:
            field_dict["maker_fees"] = maker_fees
        if taker_fees is not UNSET:
            field_dict["taker_fees"] = taker_fees
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        convert_id = d.pop("convert_id", UNSET)

        convert_symbol = d.pop("convert_symbol", UNSET)

        open_interest = d.pop("open_interest", UNSET)

        open_interest_usd = d.pop("open_interest_usd", UNSET)

        derivative_volume = d.pop("derivative_volume", UNSET)

        derivative_volume_usd = d.pop("derivative_volume_usd", UNSET)

        maker_fees = d.pop("maker_fees", UNSET)

        taker_fees = d.pop("taker_fees", UNSET)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        derivatives_exchanges_list_results_object_exchanges_item_quotes_item = cls(
            convert_id=convert_id,
            convert_symbol=convert_symbol,
            open_interest=open_interest,
            open_interest_usd=open_interest_usd,
            derivative_volume=derivative_volume,
            derivative_volume_usd=derivative_volume_usd,
            maker_fees=maker_fees,
            taker_fees=taker_fees,
            last_updated=last_updated,
        )

        derivatives_exchanges_list_results_object_exchanges_item_quotes_item.additional_properties = d
        return derivatives_exchanges_list_results_object_exchanges_item_quotes_item

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
