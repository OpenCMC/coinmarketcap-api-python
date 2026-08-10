from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dex_transaction_quote_dto import DexTransactionQuoteDTO


T = TypeVar("T", bound="DexTransactionDTO")


@_attrs_define
class DexTransactionDTO:
    """DEX transaction data

    Attributes:
        date (datetime.datetime | Unset): Timestamp (ISO 8601) of specified transaction.
        type_ (str | Unset): Buy or sell trade.
        quote (list[DexTransactionQuoteDTO] | Unset): A map of market quotes in different currency conversions. The
            default map included is USD.
        transaction_hash (str | Unset): Transaction hash of the trade. Only returned if passed in aux.
        blockchain_explorer_link (str | Unset): Link to the transaction on a blockchain explorer if available. Only
            returned if passed in aux.
    """

    date: datetime.datetime | Unset = UNSET
    type_: str | Unset = UNSET
    quote: list[DexTransactionQuoteDTO] | Unset = UNSET
    transaction_hash: str | Unset = UNSET
    blockchain_explorer_link: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        type_ = self.type_

        quote: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quote, Unset):
            quote = []
            for quote_item_data in self.quote:
                quote_item = quote_item_data.to_dict()
                quote.append(quote_item)

        transaction_hash = self.transaction_hash

        blockchain_explorer_link = self.blockchain_explorer_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if type_ is not UNSET:
            field_dict["type"] = type_
        if quote is not UNSET:
            field_dict["quote"] = quote
        if transaction_hash is not UNSET:
            field_dict["transaction_hash"] = transaction_hash
        if blockchain_explorer_link is not UNSET:
            field_dict["blockchain_explorer_link"] = blockchain_explorer_link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dex_transaction_quote_dto import DexTransactionQuoteDTO

        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        type_ = d.pop("type", UNSET)

        _quote = d.pop("quote", UNSET)
        quote: list[DexTransactionQuoteDTO] | Unset = UNSET
        if _quote is not UNSET:
            quote = []
            for quote_item_data in _quote:
                quote_item = DexTransactionQuoteDTO.from_dict(quote_item_data)

                quote.append(quote_item)

        transaction_hash = d.pop("transaction_hash", UNSET)

        blockchain_explorer_link = d.pop("blockchain_explorer_link", UNSET)

        dex_transaction_dto = cls(
            date=date,
            type_=type_,
            quote=quote,
            transaction_hash=transaction_hash,
            blockchain_explorer_link=blockchain_explorer_link,
        )

        dex_transaction_dto.additional_properties = d
        return dex_transaction_dto

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
