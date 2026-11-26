from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rwa_quotes_historical_results_object_rwa_assets_item_asset_type import (
    RWAQuotesHistoricalResultsObjectRwaAssetsItemAssetType,
    check_rwa_quotes_historical_results_object_rwa_assets_item_asset_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rwa_quotes_historical_results_object_rwa_assets_item_quotes_item import (
        RWAQuotesHistoricalResultsObjectRwaAssetsItemQuotesItem,
    )


T = TypeVar("T", bound="RWAQuotesHistoricalResultsObjectRwaAssetsItem")


@_attrs_define
class RWAQuotesHistoricalResultsObjectRwaAssetsItem:
    """
    Attributes:
        name (str | Unset): Asset display name. Example: NVIDIA.
        symbol (str | Unset): Asset symbol / ticker. Example: NVDA.
        slug (str | Unset): URL-friendly lowercase slug. Example: nvidia.
        quotes (list[RWAQuotesHistoricalResultsObjectRwaAssetsItemQuotesItem] | Unset): The time series: one entry per
            data point per convert currency, oldest first and grouped by currency in the order requested. Empty when the
            asset has no tokens or no data in the window.
        rwa_id (int | Unset): RWA asset ID; the stable identifier to use across the RWA family. Example: 2.
        asset_type (RWAQuotesHistoricalResultsObjectRwaAssetsItemAssetType | Unset): Asset type. One of `stock`,
            `commodity`, `currency`, `government_security`, `etf`, `real_estate`. Example: stock.
        rwa_rank (int | Unset): Current RWA market-cap rank (1 = highest), not the rank at each data point. RWA-specific
            ranking, distinct from `cmc_rank`. Example: 4.
        has_tokens (bool | Unset): `true` if at least one token exists for this asset; `false` if there are no tokenized
            assets, in which case `quotes` is empty. Example: True.
    """

    name: str | Unset = UNSET
    symbol: str | Unset = UNSET
    slug: str | Unset = UNSET
    quotes: list[RWAQuotesHistoricalResultsObjectRwaAssetsItemQuotesItem] | Unset = UNSET
    rwa_id: int | Unset = UNSET
    asset_type: RWAQuotesHistoricalResultsObjectRwaAssetsItemAssetType | Unset = UNSET
    rwa_rank: int | Unset = UNSET
    has_tokens: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        symbol = self.symbol

        slug = self.slug

        quotes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quotes, Unset):
            quotes = []
            for quotes_item_data in self.quotes:
                quotes_item = quotes_item_data.to_dict()
                quotes.append(quotes_item)

        rwa_id = self.rwa_id

        asset_type: str | Unset = UNSET
        if not isinstance(self.asset_type, Unset):
            asset_type = self.asset_type

        rwa_rank = self.rwa_rank

        has_tokens = self.has_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if slug is not UNSET:
            field_dict["slug"] = slug
        if quotes is not UNSET:
            field_dict["quotes"] = quotes
        if rwa_id is not UNSET:
            field_dict["rwa_id"] = rwa_id
        if asset_type is not UNSET:
            field_dict["asset_type"] = asset_type
        if rwa_rank is not UNSET:
            field_dict["rwa_rank"] = rwa_rank
        if has_tokens is not UNSET:
            field_dict["has_tokens"] = has_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rwa_quotes_historical_results_object_rwa_assets_item_quotes_item import (
            RWAQuotesHistoricalResultsObjectRwaAssetsItemQuotesItem,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        symbol = d.pop("symbol", UNSET)

        slug = d.pop("slug", UNSET)

        _quotes = d.pop("quotes", UNSET)
        quotes: list[RWAQuotesHistoricalResultsObjectRwaAssetsItemQuotesItem] | Unset = UNSET
        if _quotes is not UNSET:
            quotes = []
            for quotes_item_data in _quotes:
                quotes_item = RWAQuotesHistoricalResultsObjectRwaAssetsItemQuotesItem.from_dict(quotes_item_data)

                quotes.append(quotes_item)

        rwa_id = d.pop("rwa_id", UNSET)

        _asset_type = d.pop("asset_type", UNSET)
        asset_type: RWAQuotesHistoricalResultsObjectRwaAssetsItemAssetType | Unset
        if isinstance(_asset_type, Unset):
            asset_type = UNSET
        else:
            asset_type = check_rwa_quotes_historical_results_object_rwa_assets_item_asset_type(_asset_type)

        rwa_rank = d.pop("rwa_rank", UNSET)

        has_tokens = d.pop("has_tokens", UNSET)

        rwa_quotes_historical_results_object_rwa_assets_item = cls(
            name=name,
            symbol=symbol,
            slug=slug,
            quotes=quotes,
            rwa_id=rwa_id,
            asset_type=asset_type,
            rwa_rank=rwa_rank,
            has_tokens=has_tokens,
        )

        rwa_quotes_historical_results_object_rwa_assets_item.additional_properties = d
        return rwa_quotes_historical_results_object_rwa_assets_item

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
