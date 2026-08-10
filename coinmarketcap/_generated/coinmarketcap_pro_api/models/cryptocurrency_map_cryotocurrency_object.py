from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cryptocurrency_map_cryotocurrency_object_status import (
    CryptocurrencyMapCryotocurrencyObjectStatus,
    check_cryptocurrency_map_cryotocurrency_object_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.platform_type_0 import PlatformType0


T = TypeVar("T", bound="CryptocurrencyMapCryotocurrencyObject")


@_attrs_define
class CryptocurrencyMapCryotocurrencyObject:
    """Cryptocurrency object for each result

    Attributes:
        id (int): The unique cryptocurrency ID for this cryptocurrency. Example: 1.
        rank (float): The rank of this cryptocurrency. Example: 1.
        name (str): The name of this cryptocurrency. Example: Bitcoin.
        symbol (str): The ticker symbol for this cryptocurrency, always in all caps. Example: BTC.
        slug (str): The web URL friendly shorthand version of this cryptocurrency name. Example: bitcoin.
        is_active (int | Unset): 1 if this cryptocurrency has at least 1 active market currently being tracked by the
            platform, otherwise 0. A value of 1 is analogous with `listing_status=active`. Example: 1.
        status (CryptocurrencyMapCryotocurrencyObjectStatus | Unset): The listing status of the cryptocurrency. *This
            field is only returned if requested through the `aux` request parameter.* Example: active.
        first_historical_data (str | Unset): Timestamp (ISO 8601) of the date this cryptocurrency was first available on
            the platform. Example: 2013-04-28T18:47:21.000Z.
        last_historical_data (str | Unset): Timestamp (ISO 8601) of the last time this cryptocurrency's market data was
            updated. Example: 2018-06-02T22:51:28.209Z.
        platform (None | PlatformType0 | Unset): Metadata about the parent cryptocurrency platform this cryptocurrency
            belongs to if it is a token, otherwise null.
    """

    id: int
    rank: float
    name: str
    symbol: str
    slug: str
    is_active: int | Unset = UNSET
    status: CryptocurrencyMapCryotocurrencyObjectStatus | Unset = UNSET
    first_historical_data: str | Unset = UNSET
    last_historical_data: str | Unset = UNSET
    platform: None | PlatformType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.platform_type_0 import PlatformType0

        id = self.id

        rank = self.rank

        name = self.name

        symbol = self.symbol

        slug = self.slug

        is_active = self.is_active

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        first_historical_data = self.first_historical_data

        last_historical_data = self.last_historical_data

        platform: dict[str, Any] | None | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        elif isinstance(self.platform, PlatformType0):
            platform = self.platform.to_dict()
        else:
            platform = self.platform

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "rank": rank,
                "name": name,
                "symbol": symbol,
                "slug": slug,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if status is not UNSET:
            field_dict["status"] = status
        if first_historical_data is not UNSET:
            field_dict["first_historical_data"] = first_historical_data
        if last_historical_data is not UNSET:
            field_dict["last_historical_data"] = last_historical_data
        if platform is not UNSET:
            field_dict["platform"] = platform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.platform_type_0 import PlatformType0

        d = dict(src_dict)
        id = d.pop("id")

        rank = d.pop("rank")

        name = d.pop("name")

        symbol = d.pop("symbol")

        slug = d.pop("slug")

        is_active = d.pop("is_active", UNSET)

        _status = d.pop("status", UNSET)
        status: CryptocurrencyMapCryotocurrencyObjectStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_cryptocurrency_map_cryotocurrency_object_status(_status)

        first_historical_data = d.pop("first_historical_data", UNSET)

        last_historical_data = d.pop("last_historical_data", UNSET)

        def _parse_platform(data: object) -> None | PlatformType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasplatform_type_0 = PlatformType0.from_dict(data)

                return componentsschemasplatform_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PlatformType0 | Unset, data)

        platform = _parse_platform(d.pop("platform", UNSET))

        cryptocurrency_map_cryotocurrency_object = cls(
            id=id,
            rank=rank,
            name=name,
            symbol=symbol,
            slug=slug,
            is_active=is_active,
            status=status,
            first_historical_data=first_historical_data,
            last_historical_data=last_historical_data,
            platform=platform,
        )

        cryptocurrency_map_cryotocurrency_object.additional_properties = d
        return cryptocurrency_map_cryotocurrency_object

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
