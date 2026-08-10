from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_4 import Model4


T = TypeVar("T", bound="ContentTopPostsResults")


@_attrs_define
class ContentTopPostsResults:
    """Cntent objects.

    Attributes:
        list_ (list[Model4] | Unset):
        last_score (str | Unset):
    """

    list_: list[Model4] | Unset = UNSET
    last_score: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.list_, Unset):
            list_ = []
            for componentsschemaslist_item_data in self.list_:
                componentsschemaslist_item = componentsschemaslist_item_data.to_dict()
                list_.append(componentsschemaslist_item)

        last_score = self.last_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if list_ is not UNSET:
            field_dict["list"] = list_
        if last_score is not UNSET:
            field_dict["last_score"] = last_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_4 import Model4

        d = dict(src_dict)
        _list_ = d.pop("list", UNSET)
        list_: list[Model4] | Unset = UNSET
        if _list_ is not UNSET:
            list_ = []
            for componentsschemaslist_item_data in _list_:
                componentsschemaslist_item = Model4.from_dict(componentsschemaslist_item_data)

                list_.append(componentsschemaslist_item)

        last_score = d.pop("last_score", UNSET)

        content_top_posts_results = cls(
            list_=list_,
            last_score=last_score,
        )

        content_top_posts_results.additional_properties = d
        return content_top_posts_results

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
