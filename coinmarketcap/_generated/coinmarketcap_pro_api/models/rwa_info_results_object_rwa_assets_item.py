from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rwa_info_results_object_rwa_assets_item_asset_type import (
    RWAInfoResultsObjectRwaAssetsItemAssetType,
    check_rwa_info_results_object_rwa_assets_item_asset_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rwa_info_results_object_rwa_assets_item_about import RWAInfoResultsObjectRwaAssetsItemAbout


T = TypeVar("T", bound="RWAInfoResultsObjectRwaAssetsItem")


@_attrs_define
class RWAInfoResultsObjectRwaAssetsItem:
    """
    Attributes:
        name (str | Unset): Asset display name. Example: Nvidia Corp.
        symbol (str | Unset): Asset symbol / ticker. Example: NVDA.
        slug (str | Unset): URL-friendly lowercase slug. Example: nvidia.
        website (None | str | Unset): Company website. `null` for non-equity types (`commodity` / `currency` /
            `government_security` / `real_estate`). Example: https://www.nvidia.com.
        employees (int | None | Unset): Employee count. `null` for non-equity types (unknown is `null`, not `0`).
            Example: 36000.
        founded (None | str | Unset): Founding date (ISO 8601 date). `null` for non-equity types. Example: 1993-04-04.
        industry (None | str | Unset): Industry classification. `null` for non-equity types. Example: Semiconductors &
            Related Devices.
        cik (None | str | Unset): SEC CIK number. `null` for non-equity / non-US assets. Example: 0001045810.
        about (RWAInfoResultsObjectRwaAssetsItemAbout | Unset): About block (descriptive static metadata).
        rwa_id (int | Unset): RWA asset ID; distinct namespace from `crypto_id`. Example: 2.
        asset_type (RWAInfoResultsObjectRwaAssetsItemAssetType | Unset): Asset type. One of `stock`, `commodity`,
            `currency`, `government_security`, `etf`, `real_estate`. Drives nominal-field nullability above. Example: stock.
        rwa_rank (int | Unset): RWA market-cap rank (1 = highest). RWA-specific ranking, distinct from `cmc_rank`.
            Example: 2.
        has_tokens (bool | Unset): `true` if at least one token exists for this asset; `false` if there are no tokenized
            assets. Example: True.
        primary_exchange (None | str | Unset): Primary listing exchange (e.g. `Nasdaq`). `null` for non-equity types.
            Example: Nasdaq.
    """

    name: str | Unset = UNSET
    symbol: str | Unset = UNSET
    slug: str | Unset = UNSET
    website: None | str | Unset = UNSET
    employees: int | None | Unset = UNSET
    founded: None | str | Unset = UNSET
    industry: None | str | Unset = UNSET
    cik: None | str | Unset = UNSET
    about: RWAInfoResultsObjectRwaAssetsItemAbout | Unset = UNSET
    rwa_id: int | Unset = UNSET
    asset_type: RWAInfoResultsObjectRwaAssetsItemAssetType | Unset = UNSET
    rwa_rank: int | Unset = UNSET
    has_tokens: bool | Unset = UNSET
    primary_exchange: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        symbol = self.symbol

        slug = self.slug

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        employees: int | None | Unset
        if isinstance(self.employees, Unset):
            employees = UNSET
        else:
            employees = self.employees

        founded: None | str | Unset
        if isinstance(self.founded, Unset):
            founded = UNSET
        else:
            founded = self.founded

        industry: None | str | Unset
        if isinstance(self.industry, Unset):
            industry = UNSET
        else:
            industry = self.industry

        cik: None | str | Unset
        if isinstance(self.cik, Unset):
            cik = UNSET
        else:
            cik = self.cik

        about: dict[str, Any] | Unset = UNSET
        if not isinstance(self.about, Unset):
            about = self.about.to_dict()

        rwa_id = self.rwa_id

        asset_type: str | Unset = UNSET
        if not isinstance(self.asset_type, Unset):
            asset_type = self.asset_type

        rwa_rank = self.rwa_rank

        has_tokens = self.has_tokens

        primary_exchange: None | str | Unset
        if isinstance(self.primary_exchange, Unset):
            primary_exchange = UNSET
        else:
            primary_exchange = self.primary_exchange

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if slug is not UNSET:
            field_dict["slug"] = slug
        if website is not UNSET:
            field_dict["website"] = website
        if employees is not UNSET:
            field_dict["employees"] = employees
        if founded is not UNSET:
            field_dict["founded"] = founded
        if industry is not UNSET:
            field_dict["industry"] = industry
        if cik is not UNSET:
            field_dict["cik"] = cik
        if about is not UNSET:
            field_dict["about"] = about
        if rwa_id is not UNSET:
            field_dict["rwa_id"] = rwa_id
        if asset_type is not UNSET:
            field_dict["asset_type"] = asset_type
        if rwa_rank is not UNSET:
            field_dict["rwa_rank"] = rwa_rank
        if has_tokens is not UNSET:
            field_dict["has_tokens"] = has_tokens
        if primary_exchange is not UNSET:
            field_dict["primary_exchange"] = primary_exchange

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rwa_info_results_object_rwa_assets_item_about import RWAInfoResultsObjectRwaAssetsItemAbout

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        symbol = d.pop("symbol", UNSET)

        slug = d.pop("slug", UNSET)

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_employees(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        employees = _parse_employees(d.pop("employees", UNSET))

        def _parse_founded(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        founded = _parse_founded(d.pop("founded", UNSET))

        def _parse_industry(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        industry = _parse_industry(d.pop("industry", UNSET))

        def _parse_cik(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cik = _parse_cik(d.pop("cik", UNSET))

        _about = d.pop("about", UNSET)
        about: RWAInfoResultsObjectRwaAssetsItemAbout | Unset
        if isinstance(_about, Unset):
            about = UNSET
        else:
            about = RWAInfoResultsObjectRwaAssetsItemAbout.from_dict(_about)

        rwa_id = d.pop("rwa_id", UNSET)

        _asset_type = d.pop("asset_type", UNSET)
        asset_type: RWAInfoResultsObjectRwaAssetsItemAssetType | Unset
        if isinstance(_asset_type, Unset):
            asset_type = UNSET
        else:
            asset_type = check_rwa_info_results_object_rwa_assets_item_asset_type(_asset_type)

        rwa_rank = d.pop("rwa_rank", UNSET)

        has_tokens = d.pop("has_tokens", UNSET)

        def _parse_primary_exchange(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_exchange = _parse_primary_exchange(d.pop("primary_exchange", UNSET))

        rwa_info_results_object_rwa_assets_item = cls(
            name=name,
            symbol=symbol,
            slug=slug,
            website=website,
            employees=employees,
            founded=founded,
            industry=industry,
            cik=cik,
            about=about,
            rwa_id=rwa_id,
            asset_type=asset_type,
            rwa_rank=rwa_rank,
            has_tokens=has_tokens,
            primary_exchange=primary_exchange,
        )

        rwa_info_results_object_rwa_assets_item.additional_properties = d
        return rwa_info_results_object_rwa_assets_item

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
