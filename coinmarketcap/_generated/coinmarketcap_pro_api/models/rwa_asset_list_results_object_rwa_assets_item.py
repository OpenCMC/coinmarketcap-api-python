from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rwa_asset_list_results_object_rwa_assets_item_asset_type import (
    RWAAssetListResultsObjectRwaAssetsItemAssetType,
    check_rwa_asset_list_results_object_rwa_assets_item_asset_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rwa_asset_list_results_object_rwa_assets_item_quotes_item import (
        RWAAssetListResultsObjectRwaAssetsItemQuotesItem,
    )


T = TypeVar("T", bound="RWAAssetListResultsObjectRwaAssetsItem")


@_attrs_define
class RWAAssetListResultsObjectRwaAssetsItem:
    """
    Attributes:
        rwa_id (int | Unset): RWA asset ID; the stable identifier to use across the RWA family. Example: 2.
        name (str | Unset): Asset display name. Example: NVIDIA.
        symbol (str | Unset): Asset symbol / ticker. Example: NVDA.
        slug (str | Unset): URL-friendly lowercase slug. Example: nvidia.
        asset_type (RWAAssetListResultsObjectRwaAssetsItemAssetType | Unset): Asset type. One of `stock`, `commodity`,
            `currency`, `government_security`, `etf`, `real_estate`. Example: stock.
        rwa_rank (int | Unset): RWA market-cap rank (1 = highest). RWA-specific ranking, distinct from `cmc_rank`.
            Example: 2.
        has_tokens (bool | Unset): `true` if at least one token exists for this asset; `false` if there are no tokenized
            assets. Example: True.
        average_tokenized_price (float | None | Unset): Aggregate price across the underlying tokens.
        tokenized_market_cap (float | None | Unset): Aggregate tokenized market cap.
        tokenized_volume_24h (float | None | Unset): Aggregate 24h tokenized volume.
        last_updated (datetime.datetime | Unset): ISO 8601 timestamp of the market data.
        quotes (list[RWAAssetListResultsObjectRwaAssetsItemQuotesItem] | Unset): Convertible tokenized values; one
            object per `convert`/`convert_id` currency.
    """

    rwa_id: int | Unset = UNSET
    name: str | Unset = UNSET
    symbol: str | Unset = UNSET
    slug: str | Unset = UNSET
    asset_type: RWAAssetListResultsObjectRwaAssetsItemAssetType | Unset = UNSET
    rwa_rank: int | Unset = UNSET
    has_tokens: bool | Unset = UNSET
    average_tokenized_price: float | None | Unset = UNSET
    tokenized_market_cap: float | None | Unset = UNSET
    tokenized_volume_24h: float | None | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    quotes: list[RWAAssetListResultsObjectRwaAssetsItemQuotesItem] | Unset = UNSET
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

        average_tokenized_price: float | None | Unset
        if isinstance(self.average_tokenized_price, Unset):
            average_tokenized_price = UNSET
        else:
            average_tokenized_price = self.average_tokenized_price

        tokenized_market_cap: float | None | Unset
        if isinstance(self.tokenized_market_cap, Unset):
            tokenized_market_cap = UNSET
        else:
            tokenized_market_cap = self.tokenized_market_cap

        tokenized_volume_24h: float | None | Unset
        if isinstance(self.tokenized_volume_24h, Unset):
            tokenized_volume_24h = UNSET
        else:
            tokenized_volume_24h = self.tokenized_volume_24h

        last_updated: str | Unset = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        quotes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quotes, Unset):
            quotes = []
            for quotes_item_data in self.quotes:
                quotes_item = quotes_item_data.to_dict()
                quotes.append(quotes_item)

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
        if average_tokenized_price is not UNSET:
            field_dict["average_tokenized_price"] = average_tokenized_price
        if tokenized_market_cap is not UNSET:
            field_dict["tokenized_market_cap"] = tokenized_market_cap
        if tokenized_volume_24h is not UNSET:
            field_dict["tokenized_volume_24h"] = tokenized_volume_24h
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if quotes is not UNSET:
            field_dict["quotes"] = quotes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rwa_asset_list_results_object_rwa_assets_item_quotes_item import (
            RWAAssetListResultsObjectRwaAssetsItemQuotesItem,
        )

        d = dict(src_dict)
        rwa_id = d.pop("rwa_id", UNSET)

        name = d.pop("name", UNSET)

        symbol = d.pop("symbol", UNSET)

        slug = d.pop("slug", UNSET)

        _asset_type = d.pop("asset_type", UNSET)
        asset_type: RWAAssetListResultsObjectRwaAssetsItemAssetType | Unset
        if isinstance(_asset_type, Unset):
            asset_type = UNSET
        else:
            asset_type = check_rwa_asset_list_results_object_rwa_assets_item_asset_type(_asset_type)

        rwa_rank = d.pop("rwa_rank", UNSET)

        has_tokens = d.pop("has_tokens", UNSET)

        def _parse_average_tokenized_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        average_tokenized_price = _parse_average_tokenized_price(d.pop("average_tokenized_price", UNSET))

        def _parse_tokenized_market_cap(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tokenized_market_cap = _parse_tokenized_market_cap(d.pop("tokenized_market_cap", UNSET))

        def _parse_tokenized_volume_24h(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tokenized_volume_24h = _parse_tokenized_volume_24h(d.pop("tokenized_volume_24h", UNSET))

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _quotes = d.pop("quotes", UNSET)
        quotes: list[RWAAssetListResultsObjectRwaAssetsItemQuotesItem] | Unset = UNSET
        if _quotes is not UNSET:
            quotes = []
            for quotes_item_data in _quotes:
                quotes_item = RWAAssetListResultsObjectRwaAssetsItemQuotesItem.from_dict(quotes_item_data)

                quotes.append(quotes_item)

        rwa_asset_list_results_object_rwa_assets_item = cls(
            rwa_id=rwa_id,
            name=name,
            symbol=symbol,
            slug=slug,
            asset_type=asset_type,
            rwa_rank=rwa_rank,
            has_tokens=has_tokens,
            average_tokenized_price=average_tokenized_price,
            tokenized_market_cap=tokenized_market_cap,
            tokenized_volume_24h=tokenized_volume_24h,
            last_updated=last_updated,
            quotes=quotes,
        )

        rwa_asset_list_results_object_rwa_assets_item.additional_properties = d
        return rwa_asset_list_results_object_rwa_assets_item

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
