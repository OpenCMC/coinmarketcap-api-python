from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dex_multiplier_validation_status_object import DexMultiplierValidationStatusObject


T = TypeVar("T", bound="DexMultiplierValidationErrorObject")


@_attrs_define
class DexMultiplierValidationErrorObject:
    """Bad Request (validation error).

    Attributes:
        status (DexMultiplierValidationStatusObject): Validation error status object for DEX multiplier.
    """

    status: DexMultiplierValidationStatusObject
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dex_multiplier_validation_status_object import DexMultiplierValidationStatusObject

        d = dict(src_dict)
        status = DexMultiplierValidationStatusObject.from_dict(d.pop("status"))

        dex_multiplier_validation_error_object = cls(
            status=status,
        )

        dex_multiplier_validation_error_object.additional_properties = d
        return dex_multiplier_validation_error_object

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
