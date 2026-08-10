from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tools_price_conversion_quote_object import ToolsPriceConversionQuoteObject


T = TypeVar(
    "T", bound="ToolsPriceConversionQuotesMapPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2Endpoint"
)


@_attrs_define
class ToolsPriceConversionQuotesMapPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2Endpoint:
    """An object map of price conversions."""

    additional_properties: dict[str, ToolsPriceConversionQuoteObject] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tools_price_conversion_quote_object import ToolsPriceConversionQuoteObject

        d = dict(src_dict)
        tools_price_conversion_quotes_map_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ToolsPriceConversionQuoteObject.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        tools_price_conversion_quotes_map_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint.additional_properties = additional_properties
        return tools_price_conversion_quotes_map_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ToolsPriceConversionQuoteObject:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ToolsPriceConversionQuoteObject) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
