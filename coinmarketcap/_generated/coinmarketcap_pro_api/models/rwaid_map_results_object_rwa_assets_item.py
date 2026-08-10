from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rwaid_map_results_object_rwa_assets_item_asset_type import (
    RWAIDMapResultsObjectRwaAssetsItemAssetType,
    check_rwaid_map_results_object_rwa_assets_item_asset_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RWAIDMapResultsObjectRwaAssetsItem")


@_attrs_define
class RWAIDMapResultsObjectRwaAssetsItem:
    """
    Attributes:
        rwa_id (int | Unset): RWA asset ID; the stable identifier to use across the RWA family. Example: 2.
        name (str | Unset): Asset display name. Example: Nvidia Corp.
        symbol (str | Unset): Asset symbol / ticker. Example: NVDA.
        slug (str | Unset): URL-friendly lowercase slug. Example: nvidia.
        asset_type (RWAIDMapResultsObjectRwaAssetsItemAssetType | Unset): Asset type. One of `stock`, `commodity`,
            `currency`, `government_security`, `etf`, `real_estate`. Example: stock.
        rwa_rank (int | Unset): RWA market-cap rank (1 = highest). RWA-specific ranking, distinct from `cmc_rank`.
            Example: 2.
        has_tokens (bool | Unset): `true` if at least one token exists for this asset; `false` if there are no tokenized
            assets. Example: True.
        first_historical_data (datetime.datetime | None | Unset): ISO 8601 timestamp of the earliest historical data
            point available; `null` if none. Example: 2003-09-07T04:00:00.000Z.
        last_historical_data (datetime.datetime | None | Unset): ISO 8601 timestamp of the most recent historical data
            point available; `null` if none. Example: 2026-07-08T10:29:00.000Z.
    """

    rwa_id: int | Unset = UNSET
    name: str | Unset = UNSET
    symbol: str | Unset = UNSET
    slug: str | Unset = UNSET
    asset_type: RWAIDMapResultsObjectRwaAssetsItemAssetType | Unset = UNSET
    rwa_rank: int | Unset = UNSET
    has_tokens: bool | Unset = UNSET
    first_historical_data: datetime.datetime | None | Unset = UNSET
    last_historical_data: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rwa_id = self.rwa_id

        name = self.name

        symbol = self.symbol

        slug = self.slug

        asset_type: str | Unset = UNSET
        if not isinstance(self.asset_type, Unset):
            asset_type = self.asset_type

        rwa_rank = self.rwa_rank

        has_tokens = self.has_tokens

        first_historical_data: None | str | Unset
        if isinstance(self.first_historical_data, Unset):
            first_historical_data = UNSET
        elif isinstance(self.first_historical_data, datetime.datetime):
            first_historical_data = self.first_historical_data.isoformat()
        else:
            first_historical_data = self.first_historical_data

        last_historical_data: None | str | Unset
        if isinstance(self.last_historical_data, Unset):
            last_historical_data = UNSET
        elif isinstance(self.last_historical_data, datetime.datetime):
            last_historical_data = self.last_historical_data.isoformat()
        else:
            last_historical_data = self.last_historical_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rwa_id is not UNSET:
            field_dict["rwa_id"] = rwa_id
        if name is not UNSET:
            field_dict["name"] = name
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if slug is not UNSET:
            field_dict["slug"] = slug
        if asset_type is not UNSET:
            field_dict["asset_type"] = asset_type
        if rwa_rank is not UNSET:
            field_dict["rwa_rank"] = rwa_rank
        if has_tokens is not UNSET:
            field_dict["has_tokens"] = has_tokens
        if first_historical_data is not UNSET:
            field_dict["first_historical_data"] = first_historical_data
        if last_historical_data is not UNSET:
            field_dict["last_historical_data"] = last_historical_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rwa_id = d.pop("rwa_id", UNSET)

        name = d.pop("name", UNSET)

        symbol = d.pop("symbol", UNSET)

        slug = d.pop("slug", UNSET)

        _asset_type = d.pop("asset_type", UNSET)
        asset_type: RWAIDMapResultsObjectRwaAssetsItemAssetType | Unset
        if isinstance(_asset_type, Unset):
            asset_type = UNSET
        else:
            asset_type = check_rwaid_map_results_object_rwa_assets_item_asset_type(_asset_type)

        rwa_rank = d.pop("rwa_rank", UNSET)

        has_tokens = d.pop("has_tokens", UNSET)

        def _parse_first_historical_data(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_historical_data_type_0 = isoparse(data)

                return first_historical_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        first_historical_data = _parse_first_historical_data(d.pop("first_historical_data", UNSET))

        def _parse_last_historical_data(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_historical_data_type_0 = isoparse(data)

                return last_historical_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_historical_data = _parse_last_historical_data(d.pop("last_historical_data", UNSET))

        rwaid_map_results_object_rwa_assets_item = cls(
            rwa_id=rwa_id,
            name=name,
            symbol=symbol,
            slug=slug,
            asset_type=asset_type,
            rwa_rank=rwa_rank,
            has_tokens=has_tokens,
            first_historical_data=first_historical_data,
            last_historical_data=last_historical_data,
        )

        rwaid_map_results_object_rwa_assets_item.additional_properties = d
        return rwaid_map_results_object_rwa_assets_item

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
