from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crypto_tag import CryptoTag
    from ..models.platform import Platform
    from ..models.quote import Quote


T = TypeVar("T", bound="CryptoQuoteV3DTO")


@_attrs_define
class CryptoQuoteV3DTO:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        symbol (str | Unset):
        slug (str | Unset):
        platform (Platform | Unset):
        quote (list[Quote] | Unset):
        tags (list[CryptoTag] | Unset):
        is_active (int | Unset):
        infinite_supply (bool | Unset):
        is_market_cap_included_in_calc (int | Unset):
        is_fiat (int | Unset):
        circulating_supply (float | Unset): Circulating supply of the cryptocurrency
        total_supply (float | Unset): Total supply of the cryptocurrency
        max_supply (float | Unset): Maximum supply of the cryptocurrency
        date_added (str | Unset):
        num_market_pairs (int | Unset):
        cmc_rank (int | Unset):
        last_updated (str | Unset):
        tvl_ratio (float | Unset): TVL to market cap ratio
        self_reported_circulating_supply (float | Unset): Self-reported circulating supply
        self_reported_market_cap (float | Unset): Self-reported market capitalization
        unlocked_circulating_supply (float | Unset): Unlocked circulating supply
        unlocked_market_cap (float | Unset): Unlocked market capitalization
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    symbol: str | Unset = UNSET
    slug: str | Unset = UNSET
    platform: Platform | Unset = UNSET
    quote: list[Quote] | Unset = UNSET
    tags: list[CryptoTag] | Unset = UNSET
    is_active: int | Unset = UNSET
    infinite_supply: bool | Unset = UNSET
    is_market_cap_included_in_calc: int | Unset = UNSET
    is_fiat: int | Unset = UNSET
    circulating_supply: float | Unset = UNSET
    total_supply: float | Unset = UNSET
    max_supply: float | Unset = UNSET
    date_added: str | Unset = UNSET
    num_market_pairs: int | Unset = UNSET
    cmc_rank: int | Unset = UNSET
    last_updated: str | Unset = UNSET
    tvl_ratio: float | Unset = UNSET
    self_reported_circulating_supply: float | Unset = UNSET
    self_reported_market_cap: float | Unset = UNSET
    unlocked_circulating_supply: float | Unset = UNSET
    unlocked_market_cap: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        symbol = self.symbol

        slug = self.slug

        platform: dict[str, Any] | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.to_dict()

        quote: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quote, Unset):
            quote = []
            for quote_item_data in self.quote:
                quote_item = quote_item_data.to_dict()
                quote.append(quote_item)

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        is_active = self.is_active

        infinite_supply = self.infinite_supply

        is_market_cap_included_in_calc = self.is_market_cap_included_in_calc

        is_fiat = self.is_fiat

        circulating_supply = self.circulating_supply

        total_supply = self.total_supply

        max_supply = self.max_supply

        date_added = self.date_added

        num_market_pairs = self.num_market_pairs

        cmc_rank = self.cmc_rank

        last_updated = self.last_updated

        tvl_ratio = self.tvl_ratio

        self_reported_circulating_supply = self.self_reported_circulating_supply

        self_reported_market_cap = self.self_reported_market_cap

        unlocked_circulating_supply = self.unlocked_circulating_supply

        unlocked_market_cap = self.unlocked_market_cap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if slug is not UNSET:
            field_dict["slug"] = slug
        if platform is not UNSET:
            field_dict["platform"] = platform
        if quote is not UNSET:
            field_dict["quote"] = quote
        if tags is not UNSET:
            field_dict["tags"] = tags
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if infinite_supply is not UNSET:
            field_dict["infinite_supply"] = infinite_supply
        if is_market_cap_included_in_calc is not UNSET:
            field_dict["is_market_cap_included_in_calc"] = is_market_cap_included_in_calc
        if is_fiat is not UNSET:
            field_dict["is_fiat"] = is_fiat
        if circulating_supply is not UNSET:
            field_dict["circulating_supply"] = circulating_supply
        if total_supply is not UNSET:
            field_dict["total_supply"] = total_supply
        if max_supply is not UNSET:
            field_dict["max_supply"] = max_supply
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if num_market_pairs is not UNSET:
            field_dict["num_market_pairs"] = num_market_pairs
        if cmc_rank is not UNSET:
            field_dict["cmc_rank"] = cmc_rank
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if tvl_ratio is not UNSET:
            field_dict["tvl_ratio"] = tvl_ratio
        if self_reported_circulating_supply is not UNSET:
            field_dict["self_reported_circulating_supply"] = self_reported_circulating_supply
        if self_reported_market_cap is not UNSET:
            field_dict["self_reported_market_cap"] = self_reported_market_cap
        if unlocked_circulating_supply is not UNSET:
            field_dict["unlocked_circulating_supply"] = unlocked_circulating_supply
        if unlocked_market_cap is not UNSET:
            field_dict["unlocked_market_cap"] = unlocked_market_cap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crypto_tag import CryptoTag
        from ..models.platform import Platform
        from ..models.quote import Quote

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        symbol = d.pop("symbol", UNSET)

        slug = d.pop("slug", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: Platform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = Platform.from_dict(_platform)

        _quote = d.pop("quote", UNSET)
        quote: list[Quote] | Unset = UNSET
        if _quote is not UNSET:
            quote = []
            for quote_item_data in _quote:
                quote_item = Quote.from_dict(quote_item_data)

                quote.append(quote_item)

        _tags = d.pop("tags", UNSET)
        tags: list[CryptoTag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = CryptoTag.from_dict(tags_item_data)

                tags.append(tags_item)

        is_active = d.pop("is_active", UNSET)

        infinite_supply = d.pop("infinite_supply", UNSET)

        is_market_cap_included_in_calc = d.pop("is_market_cap_included_in_calc", UNSET)

        is_fiat = d.pop("is_fiat", UNSET)

        circulating_supply = d.pop("circulating_supply", UNSET)

        total_supply = d.pop("total_supply", UNSET)

        max_supply = d.pop("max_supply", UNSET)

        date_added = d.pop("date_added", UNSET)

        num_market_pairs = d.pop("num_market_pairs", UNSET)

        cmc_rank = d.pop("cmc_rank", UNSET)

        last_updated = d.pop("last_updated", UNSET)

        tvl_ratio = d.pop("tvl_ratio", UNSET)

        self_reported_circulating_supply = d.pop("self_reported_circulating_supply", UNSET)

        self_reported_market_cap = d.pop("self_reported_market_cap", UNSET)

        unlocked_circulating_supply = d.pop("unlocked_circulating_supply", UNSET)

        unlocked_market_cap = d.pop("unlocked_market_cap", UNSET)

        crypto_quote_v3dto = cls(
            id=id,
            name=name,
            symbol=symbol,
            slug=slug,
            platform=platform,
            quote=quote,
            tags=tags,
            is_active=is_active,
            infinite_supply=infinite_supply,
            is_market_cap_included_in_calc=is_market_cap_included_in_calc,
            is_fiat=is_fiat,
            circulating_supply=circulating_supply,
            total_supply=total_supply,
            max_supply=max_supply,
            date_added=date_added,
            num_market_pairs=num_market_pairs,
            cmc_rank=cmc_rank,
            last_updated=last_updated,
            tvl_ratio=tvl_ratio,
            self_reported_circulating_supply=self_reported_circulating_supply,
            self_reported_market_cap=self_reported_market_cap,
            unlocked_circulating_supply=unlocked_circulating_supply,
            unlocked_market_cap=unlocked_market_cap,
        )

        crypto_quote_v3dto.additional_properties = d
        return crypto_quote_v3dto

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
