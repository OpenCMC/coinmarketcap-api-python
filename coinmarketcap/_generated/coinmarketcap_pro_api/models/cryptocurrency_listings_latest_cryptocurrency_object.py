from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cryptocurrency_listings_latest_quote_map import CryptocurrencyListingsLatestQuoteMap
    from ..models.platform_type_0 import PlatformType0


T = TypeVar("T", bound="CryptocurrencyListingsLatestCryptocurrencyObject")


@_attrs_define
class CryptocurrencyListingsLatestCryptocurrencyObject:
    """A cryptocurrency object for every cryptocurrency that matched list options.

    Attributes:
        id (int): The unique CoinMarketCap ID for this cryptocurrency. Example: 1.
        name (str): The name of this cryptocurrency. Example: Bitcoin.
        symbol (str): The ticker symbol for this cryptocurrency. Example: BTC.
        slug (str): The web URL friendly shorthand version of this cryptocurrency name. Example: bitcoin.
        cmc_rank (int): The cryptocurrency's historic CoinMarketCap rank at the end of the requested UTC day. Example:
            5.
        circulating_supply (float): The approximate number of coins circulating for this cryptocurrency at the end of
            the requested UTC day. Example: 16950100.
        total_supply (float): The approximate total amount of coins in existence right now (minus any coins that have
            been verifiably burned) at the end of the requested UTC day. Example: 16950100.
        max_supply (float): The expected maximum limit of coins ever to be available for this cryptocurrency. Example:
            21000000.
        last_updated (str): Timestamp (ISO 8601) of when this cryptocurrency's market data was referenced for this UTC
            date snapshot. This is always the last update available during the UTC date requested. Example:
            2018-06-02T22:51:28.209Z.
        date_added (str): Timestamp (ISO 8601) of when this cryptocurrency was added to CoinMarketCap. Example:
            2013-04-28T00:00:00.000Z.
        tags (list[str]): Array of tags associated with this cryptocurrency. Currently only a mineable tag will be
            returned if the cryptocurrency is mineable. Additional tags will be returned in the future. Example:
            ['mineable'].
        platform (None | PlatformType0): Metadata about the parent cryptocurrency platform this cryptocurrency belongs
            to if it is a token, otherwise null.
        quote (CryptocurrencyListingsLatestQuoteMap): A map of market quotes in different currency conversions. The
            default map included is USD. Example: {'USD': {'price': 9283.92, 'volume_24h': 7155680000, 'percent_change_1h':
            -0.152774, 'percent_change_24h': 0.518894, 'percent_change_7d': 0.986573, 'market_cap': 158055024432,
            'last_updated': '2018-08-09T22:53:32.000Z'}}.
        num_market_pairs (int | Unset): The number of active trading pairs available for this cryptocurrency across
            supported exchanges. Example: 500.
    """

    id: int
    name: str
    symbol: str
    slug: str
    cmc_rank: int
    circulating_supply: float
    total_supply: float
    max_supply: float
    last_updated: str
    date_added: str
    tags: list[str]
    platform: None | PlatformType0
    quote: CryptocurrencyListingsLatestQuoteMap
    num_market_pairs: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.platform_type_0 import PlatformType0

        id = self.id

        name = self.name

        symbol = self.symbol

        slug = self.slug

        cmc_rank = self.cmc_rank

        circulating_supply = self.circulating_supply

        total_supply = self.total_supply

        max_supply = self.max_supply

        last_updated = self.last_updated

        date_added = self.date_added

        tags = self.tags

        platform: dict[str, Any] | None
        if isinstance(self.platform, PlatformType0):
            platform = self.platform.to_dict()
        else:
            platform = self.platform

        quote = self.quote.to_dict()

        num_market_pairs = self.num_market_pairs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "symbol": symbol,
                "slug": slug,
                "cmc_rank": cmc_rank,
                "circulating_supply": circulating_supply,
                "total_supply": total_supply,
                "max_supply": max_supply,
                "last_updated": last_updated,
                "date_added": date_added,
                "tags": tags,
                "platform": platform,
                "quote": quote,
            }
        )
        if num_market_pairs is not UNSET:
            field_dict["num_market_pairs"] = num_market_pairs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_listings_latest_quote_map import CryptocurrencyListingsLatestQuoteMap
        from ..models.platform_type_0 import PlatformType0

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        symbol = d.pop("symbol")

        slug = d.pop("slug")

        cmc_rank = d.pop("cmc_rank")

        circulating_supply = d.pop("circulating_supply")

        total_supply = d.pop("total_supply")

        max_supply = d.pop("max_supply")

        last_updated = d.pop("last_updated")

        date_added = d.pop("date_added")

        tags = cast(list[str], d.pop("tags"))

        def _parse_platform(data: object) -> None | PlatformType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasplatform_type_0 = PlatformType0.from_dict(data)

                return componentsschemasplatform_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PlatformType0, data)

        platform = _parse_platform(d.pop("platform"))

        quote = CryptocurrencyListingsLatestQuoteMap.from_dict(d.pop("quote"))

        num_market_pairs = d.pop("num_market_pairs", UNSET)

        cryptocurrency_listings_latest_cryptocurrency_object = cls(
            id=id,
            name=name,
            symbol=symbol,
            slug=slug,
            cmc_rank=cmc_rank,
            circulating_supply=circulating_supply,
            total_supply=total_supply,
            max_supply=max_supply,
            last_updated=last_updated,
            date_added=date_added,
            tags=tags,
            platform=platform,
            quote=quote,
            num_market_pairs=num_market_pairs,
        )

        cryptocurrency_listings_latest_cryptocurrency_object.additional_properties = d
        return cryptocurrency_listings_latest_cryptocurrency_object

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
