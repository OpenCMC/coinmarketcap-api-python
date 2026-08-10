from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DexTransactionQuoteDTO")


@_attrs_define
class DexTransactionQuoteDTO:
    """DEX transaction quote data

    Attributes:
        price (float | Unset): Price of the base asset in the specified currency.
        total (float | Unset): Total value of trade in the specified currency.
        convert_id (str | Unset): id of specified currency.
        price_by_quote_asset (float | Unset): Price of the base asset in quote asset.
        amount_base_asset (float | Unset): Amount of base asset traded.
        amount_quote_asset (float | Unset): Amount of quote asset traded.
    """

    price: float | Unset = UNSET
    total: float | Unset = UNSET
    convert_id: str | Unset = UNSET
    price_by_quote_asset: float | Unset = UNSET
    amount_base_asset: float | Unset = UNSET
    amount_quote_asset: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price = self.price

        total = self.total

        convert_id = self.convert_id

        price_by_quote_asset = self.price_by_quote_asset

        amount_base_asset = self.amount_base_asset

        amount_quote_asset = self.amount_quote_asset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price is not UNSET:
            field_dict["price"] = price
        if total is not UNSET:
            field_dict["total"] = total
        if convert_id is not UNSET:
            field_dict["convert_id"] = convert_id
        if price_by_quote_asset is not UNSET:
            field_dict["price_by_quote_asset"] = price_by_quote_asset
        if amount_base_asset is not UNSET:
            field_dict["amount_base_asset"] = amount_base_asset
        if amount_quote_asset is not UNSET:
            field_dict["amount_quote_asset"] = amount_quote_asset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price = d.pop("price", UNSET)

        total = d.pop("total", UNSET)

        convert_id = d.pop("convert_id", UNSET)

        price_by_quote_asset = d.pop("price_by_quote_asset", UNSET)

        amount_base_asset = d.pop("amount_base_asset", UNSET)

        amount_quote_asset = d.pop("amount_quote_asset", UNSET)

        dex_transaction_quote_dto = cls(
            price=price,
            total=total,
            convert_id=convert_id,
            price_by_quote_asset=price_by_quote_asset,
            amount_base_asset=amount_base_asset,
            amount_quote_asset=amount_quote_asset,
        )

        dex_transaction_quote_dto.additional_properties = d
        return dex_transaction_quote_dto

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
