from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DexMultiplierValidationStatusObject")


@_attrs_define
class DexMultiplierValidationStatusObject:
    """Validation error status object for DEX multiplier.

    Attributes:
        error_code (int): Application error code. Example: 4001.
        category (str): Error category. Example: VALIDATION.
        error_message (str): Error message. Example: Invalid parameter..
        error_detail (str): Detailed error information. Example: start should be an integer >= 1..
    """

    error_code: int
    category: str
    error_message: str
    error_detail: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_code = self.error_code

        category = self.category

        error_message = self.error_message

        error_detail = self.error_detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error_code": error_code,
                "category": category,
                "error_message": error_message,
                "error_detail": error_detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error_code = d.pop("error_code")

        category = d.pop("category")

        error_message = d.pop("error_message")

        error_detail = d.pop("error_detail")

        dex_multiplier_validation_status_object = cls(
            error_code=error_code,
            category=category,
            error_message=error_message,
            error_detail=error_detail,
        )

        dex_multiplier_validation_status_object.additional_properties = d
        return dex_multiplier_validation_status_object

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
