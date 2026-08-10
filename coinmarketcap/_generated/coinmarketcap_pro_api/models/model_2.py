from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.owner import Owner


T = TypeVar("T", bound="Model2")


@_attrs_define
class Model2:
    """
    Attributes:
        owner (Owner):
        post_id (str | Unset):
        text_content (str | Unset):
        photos (list[str] | Unset):
        comment_count (str | Unset):
        like_count (str | Unset):
        post_time (str | Unset):
        language_code (str | Unset):
        comments_url (str | Unset): Returns comments of the current post/comment
    """

    owner: Owner
    post_id: str | Unset = UNSET
    text_content: str | Unset = UNSET
    photos: list[str] | Unset = UNSET
    comment_count: str | Unset = UNSET
    like_count: str | Unset = UNSET
    post_time: str | Unset = UNSET
    language_code: str | Unset = UNSET
    comments_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner = self.owner.to_dict()

        post_id = self.post_id

        text_content = self.text_content

        photos: list[str] | Unset = UNSET
        if not isinstance(self.photos, Unset):
            photos = self.photos

        comment_count = self.comment_count

        like_count = self.like_count

        post_time = self.post_time

        language_code = self.language_code

        comments_url = self.comments_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner": owner,
            }
        )
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
        if text_content is not UNSET:
            field_dict["text_content"] = text_content
        if photos is not UNSET:
            field_dict["photos"] = photos
        if comment_count is not UNSET:
            field_dict["comment_count"] = comment_count
        if like_count is not UNSET:
            field_dict["like_count"] = like_count
        if post_time is not UNSET:
            field_dict["post_time"] = post_time
        if language_code is not UNSET:
            field_dict["language_code"] = language_code
        if comments_url is not UNSET:
            field_dict["comments_url"] = comments_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.owner import Owner

        d = dict(src_dict)
        owner = Owner.from_dict(d.pop("owner"))

        post_id = d.pop("post_id", UNSET)

        text_content = d.pop("text_content", UNSET)

        photos = cast(list[str], d.pop("photos", UNSET))

        comment_count = d.pop("comment_count", UNSET)

        like_count = d.pop("like_count", UNSET)

        post_time = d.pop("post_time", UNSET)

        language_code = d.pop("language_code", UNSET)

        comments_url = d.pop("comments_url", UNSET)

        model_2 = cls(
            owner=owner,
            post_id=post_id,
            text_content=text_content,
            photos=photos,
            comment_count=comment_count,
            like_count=like_count,
            post_time=post_time,
            language_code=language_code,
            comments_url=comments_url,
        )

        model_2.additional_properties = d
        return model_2

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
