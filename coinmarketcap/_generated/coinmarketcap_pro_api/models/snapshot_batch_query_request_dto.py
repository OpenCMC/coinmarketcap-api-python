from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnapshotBatchQueryRequestDTO")


@_attrs_define
class SnapshotBatchQueryRequestDTO:
    """fetch batch snapshot data points request body

    Attributes:
        target_date (str | Unset): The date of the snapshot data was created (2022-04-29 as an example). required.
        crypto_ids (list[int] | Unset): The crypto ids of the snapshot data will be retrieved.
    """

    target_date: str | Unset = UNSET
    crypto_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_date = self.target_date

        crypto_ids: list[int] | Unset = UNSET
        if not isinstance(self.crypto_ids, Unset):
            crypto_ids = self.crypto_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_date is not UNSET:
            field_dict["targetDate"] = target_date
        if crypto_ids is not UNSET:
            field_dict["cryptoIds"] = crypto_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_date = d.pop("targetDate", UNSET)

        crypto_ids = cast(list[int], d.pop("cryptoIds", UNSET))

        snapshot_batch_query_request_dto = cls(
            target_date=target_date,
            crypto_ids=crypto_ids,
        )

        snapshot_batch_query_request_dto.additional_properties = d
        return snapshot_batch_query_request_dto

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
