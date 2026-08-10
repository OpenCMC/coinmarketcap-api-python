from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cryptocurrency_quote_map import CryptocurrencyQuoteMap
    from ..models.platform_type_0 import PlatformType0


T = TypeVar("T", bound="CryptocurrencyCryptocurrencyObject")


@_attrs_define
class CryptocurrencyCryptocurrencyObject:
    """A cryptocurrency object for every cryptocurrency that matched list options.

    Attributes:
        id (int): The unique CoinMarketCap ID for this cryptocurrency. Example: 1.
        name (str): The name of this cryptocurrency. Example: Bitcoin.
        symbol (str): The ticker symbol for this cryptocurrency. Example: BTC.
        slug (str): The web URL friendly shorthand version of this cryptocurrency name. Example: bitcoin.
        last_updated (str): Timestamp (ISO 8601) of the last time this cryptocurrency's market data was updated.
            Example: 2018-06-02T22:51:28.209Z.
        quote (CryptocurrencyQuoteMap): A map of market quotes in different currency conversions. The default map
            included is USD. Example: {'USD': {'price': 9283.92, 'volume_24h': 7155680000, 'percent_change_1h': -0.152774,
            'percent_change_24h': 0.518894, 'percent_change_7d': 0.986573, 'market_cap': 158055024432, 'last_updated':
            '2018-08-09T22:53:32.000Z'}}.
        cmc_rank (int | Unset): The cryptocurrency's CoinMarketCap rank by market cap. Example: 5.
        num_market_pairs (int | Unset): The number of active trading pairs available for this cryptocurrency across
            supported exchanges. Example: 500.
        circulating_supply (float | Unset): The approximate number of coins circulating for this cryptocurrency.
            Example: 16950100.
        total_supply (float | Unset): The approximate total amount of coins in existence right now (minus any coins that
            have been verifiably burned). Example: 16950100.
        market_cap_by_total_supply (float | Unset): The market cap by total supply. *This field is only returned if
            requested through the `aux` request parameter.* Example: 158055024432.
        max_supply (float | Unset): The expected maximum limit of coins ever to be available for this cryptocurrency.
            Example: 21000000.
        date_added (str | Unset): Timestamp (ISO 8601) of when this cryptocurrency was added to CoinMarketCap. Example:
            2013-04-28T00:00:00.000Z.
        tags (list[str] | Unset): Array of tags associated with this cryptocurrency. Currently only a mineable tag will
            be returned if the cryptocurrency is mineable. Additional tags will be returned in the future. Example:
            ['mineable'].
        platform (None | PlatformType0 | Unset): Metadata about the parent cryptocurrency platform this cryptocurrency
            belongs to if it is a token, otherwise null.
    """

    id: int
    name: str
    symbol: str
    slug: str
    last_updated: str
    quote: CryptocurrencyQuoteMap
    cmc_rank: int | Unset = UNSET
    num_market_pairs: int | Unset = UNSET
    circulating_supply: float | Unset = UNSET
    total_supply: float | Unset = UNSET
    market_cap_by_total_supply: float | Unset = UNSET
    max_supply: float | Unset = UNSET
    date_added: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    platform: None | PlatformType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.platform_type_0 import PlatformType0

        id = self.id

        name = self.name

        symbol = self.symbol

        slug = self.slug

        last_updated = self.last_updated

        quote = self.quote.to_dict()

        cmc_rank = self.cmc_rank

        num_market_pairs = self.num_market_pairs

        circulating_supply = self.circulating_supply

        total_supply = self.total_supply

        market_cap_by_total_supply = self.market_cap_by_total_supply

        max_supply = self.max_supply

        date_added = self.date_added

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

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
                "name": name,
                "symbol": symbol,
                "slug": slug,
                "last_updated": last_updated,
                "quote": quote,
            }
        )
        if cmc_rank is not UNSET:
            field_dict["cmc_rank"] = cmc_rank
        if num_market_pairs is not UNSET:
            field_dict["num_market_pairs"] = num_market_pairs
        if circulating_supply is not UNSET:
            field_dict["circulating_supply"] = circulating_supply
        if total_supply is not UNSET:
            field_dict["total_supply"] = total_supply
        if market_cap_by_total_supply is not UNSET:
            field_dict["market_cap_by_total_supply"] = market_cap_by_total_supply
        if max_supply is not UNSET:
            field_dict["max_supply"] = max_supply
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if tags is not UNSET:
            field_dict["tags"] = tags
        if platform is not UNSET:
            field_dict["platform"] = platform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_quote_map import CryptocurrencyQuoteMap
        from ..models.platform_type_0 import PlatformType0

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        symbol = d.pop("symbol")

        slug = d.pop("slug")

        last_updated = d.pop("last_updated")

        quote = CryptocurrencyQuoteMap.from_dict(d.pop("quote"))

        cmc_rank = d.pop("cmc_rank", UNSET)

        num_market_pairs = d.pop("num_market_pairs", UNSET)

        circulating_supply = d.pop("circulating_supply", UNSET)

        total_supply = d.pop("total_supply", UNSET)

        market_cap_by_total_supply = d.pop("market_cap_by_total_supply", UNSET)

        max_supply = d.pop("max_supply", UNSET)

        date_added = d.pop("date_added", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

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

        cryptocurrency_cryptocurrency_object = cls(
            id=id,
            name=name,
            symbol=symbol,
            slug=slug,
            last_updated=last_updated,
            quote=quote,
            cmc_rank=cmc_rank,
            num_market_pairs=num_market_pairs,
            circulating_supply=circulating_supply,
            total_supply=total_supply,
            market_cap_by_total_supply=market_cap_by_total_supply,
            max_supply=max_supply,
            date_added=date_added,
            tags=tags,
            platform=platform,
        )

        cryptocurrency_cryptocurrency_object.additional_properties = d
        return cryptocurrency_cryptocurrency_object

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
