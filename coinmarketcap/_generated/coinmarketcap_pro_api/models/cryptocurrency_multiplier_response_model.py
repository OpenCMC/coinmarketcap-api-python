from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.cryptocurrency_multiplier_data_object import CryptocurrencyMultiplierDataObject


T = TypeVar("T", bound="CryptocurrencyMultiplierResponseModel")


@_attrs_define
class CryptocurrencyMultiplierResponseModel:
    """
    Attributes:
        data (CryptocurrencyMultiplierDataObject): Paginated multiplier results.
        status (APIStatusObject): Standardized status object for API calls.
    """

    data: CryptocurrencyMultiplierDataObject
    status: APIStatusObject
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_status_object import APIStatusObject
        from ..models.cryptocurrency_multiplier_data_object import CryptocurrencyMultiplierDataObject

        d = dict(src_dict)
        data = CryptocurrencyMultiplierDataObject.from_dict(d.pop("data"))

        status = APIStatusObject.from_dict(d.pop("status"))

        cryptocurrency_multiplier_response_model = cls(
            data=data,
            status=status,
        )

        cryptocurrency_multiplier_response_model.additional_properties = d
        return cryptocurrency_multiplier_response_model

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
