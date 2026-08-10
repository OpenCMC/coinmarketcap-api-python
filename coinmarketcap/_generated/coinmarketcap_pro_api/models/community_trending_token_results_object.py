from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommunityTrendingTokenResultsObject")


@_attrs_define
class CommunityTrendingTokenResultsObject:
    """
    Attributes:
        id (int): The unique CoinMarketCap ID for this cryptocurrency. Example: 1.
        name (str): The name of this cryptocurrency. Example: Bitcoin.
        symbol (str): The ticker symbol for this cryptocurrency. Example: BTC.
        slug (str): The web URL friendly shorthand version of this cryptocurrency name. Example: bitcoin.
        rank (float | Unset): The community rank of the coin Example: 1.
        cmc_rank (int | Unset): The cryptocurrency's CoinMarketCap rank by market cap. Example: 5.
    """

    id: int
    name: str
    symbol: str
    slug: str
    rank: float | Unset = UNSET
    cmc_rank: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        symbol = self.symbol

        slug = self.slug

        rank = self.rank

        cmc_rank = self.cmc_rank

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "symbol": symbol,
                "slug": slug,
            }
        )
        if rank is not UNSET:
            field_dict["rank"] = rank
        if cmc_rank is not UNSET:
            field_dict["cmc_rank"] = cmc_rank

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        symbol = d.pop("symbol")

        slug = d.pop("slug")

        rank = d.pop("rank", UNSET)

        cmc_rank = d.pop("cmc_rank", UNSET)

        community_trending_token_results_object = cls(
            id=id,
            name=name,
            symbol=symbol,
            slug=slug,
            rank=rank,
            cmc_rank=cmc_rank,
        )

        community_trending_token_results_object.additional_properties = d
        return community_trending_token_results_object

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
