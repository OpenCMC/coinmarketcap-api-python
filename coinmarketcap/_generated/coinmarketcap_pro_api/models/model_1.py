from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assets import Assets


T = TypeVar("T", bound="Model1")


@_attrs_define
class Model1:
    """
    Attributes:
        cover (str | Unset):
        title (str | Unset):
        subtitle (str | Unset):
        source_name (str | Unset):
        source_url (str | Unset):
        type_ (str | Unset):
        assets (list[Assets] | Unset):
        created_at (str | Unset): Timestamp (ISO 8601) of the time this was created. Example: 2018-06-02T23:59:59.999Z.
        released_at (str | Unset): Timestamp (ISO 8601) of the time this was released. Example:
            2018-06-02T23:59:59.999Z.
    """

    cover: str | Unset = UNSET
    title: str | Unset = UNSET
    subtitle: str | Unset = UNSET
    source_name: str | Unset = UNSET
    source_url: str | Unset = UNSET
    type_: str | Unset = UNSET
    assets: list[Assets] | Unset = UNSET
    created_at: str | Unset = UNSET
    released_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cover = self.cover

        title = self.title

        subtitle = self.subtitle

        source_name = self.source_name

        source_url = self.source_url

        type_ = self.type_

        assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for componentsschemasassets_array_item_data in self.assets:
                componentsschemasassets_array_item = componentsschemasassets_array_item_data.to_dict()
                assets.append(componentsschemasassets_array_item)

        created_at = self.created_at

        released_at = self.released_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cover is not UNSET:
            field_dict["cover"] = cover
        if title is not UNSET:
            field_dict["title"] = title
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if source_name is not UNSET:
            field_dict["source_name"] = source_name
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if assets is not UNSET:
            field_dict["assets"] = assets
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if released_at is not UNSET:
            field_dict["released_at"] = released_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assets import Assets

        d = dict(src_dict)
        cover = d.pop("cover", UNSET)

        title = d.pop("title", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        source_name = d.pop("source_name", UNSET)

        source_url = d.pop("source_url", UNSET)

        type_ = d.pop("type", UNSET)

        _assets = d.pop("assets", UNSET)
        assets: list[Assets] | Unset = UNSET
        if _assets is not UNSET:
            assets = []
            for componentsschemasassets_array_item_data in _assets:
                componentsschemasassets_array_item = Assets.from_dict(componentsschemasassets_array_item_data)

                assets.append(componentsschemasassets_array_item)

        created_at = d.pop("created_at", UNSET)

        released_at = d.pop("released_at", UNSET)

        model_1 = cls(
            cover=cover,
            title=title,
            subtitle=subtitle,
            source_name=source_name,
            source_url=source_url,
            type_=type_,
            assets=assets,
            created_at=created_at,
            released_at=released_at,
        )

        model_1.additional_properties = d
        return model_1

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
