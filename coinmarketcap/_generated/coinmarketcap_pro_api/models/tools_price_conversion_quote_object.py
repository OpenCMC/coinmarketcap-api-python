from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ToolsPriceConversionQuoteObject")


@_attrs_define
class ToolsPriceConversionQuoteObject:
    """A quote object for each conversion requested. The map key being the id/symbol used in the request.

    Attributes:
        price (float): Converted price in terms of the quoted currency and historic time (if supplied). Example:
            1235000.
        last_updated (str): Timestamp (ISO 8601) of when the destination currency's market value was recorded. Example:
            2018-06-02T00:00:00.000Z.
    """

    price: float
    last_updated: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price = self.price

        last_updated = self.last_updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "price": price,
                "last_updated": last_updated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price = d.pop("price")

        last_updated = d.pop("last_updated")

        tools_price_conversion_quote_object = cls(
            price=price,
            last_updated=last_updated,
        )

        tools_price_conversion_quote_object.additional_properties = d
        return tools_price_conversion_quote_object

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
