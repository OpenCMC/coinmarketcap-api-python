from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.token_event_dto import TokenEventDTO


T = TypeVar("T", bound="TokenUnlockEventDTO")


@_attrs_define
class TokenUnlockEventDTO:
    """
    Attributes:
        id (int | Unset): The unique CoinMarketCap ID for this cryptocurrency.
        token_event (list[TokenEventDTO] | Unset): The breakdown of the next token unlock.
    """

    id: int | Unset = UNSET
    token_event: list[TokenEventDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        token_event: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.token_event, Unset):
            token_event = []
            for token_event_item_data in self.token_event:
                token_event_item = token_event_item_data.to_dict()
                token_event.append(token_event_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if token_event is not UNSET:
            field_dict["token_event"] = token_event

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_event_dto import TokenEventDTO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _token_event = d.pop("token_event", UNSET)
        token_event: list[TokenEventDTO] | Unset = UNSET
        if _token_event is not UNSET:
            token_event = []
            for token_event_item_data in _token_event:
                token_event_item = TokenEventDTO.from_dict(token_event_item_data)

                token_event.append(token_event_item)

        token_unlock_event_dto = cls(
            id=id,
            token_event=token_event,
        )

        token_unlock_event_dto.additional_properties = d
        return token_unlock_event_dto

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
