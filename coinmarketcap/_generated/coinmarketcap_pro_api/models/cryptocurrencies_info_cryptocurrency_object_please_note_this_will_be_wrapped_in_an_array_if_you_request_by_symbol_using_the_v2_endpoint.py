from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cryptocurrencies_info_cryptocurrency_object_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint_category import (
    CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2EndpointCategory,
    check_cryptocurrencies_info_cryptocurrency_object_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint_category,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cryptocurrencies_info_ur_ls_object import CryptocurrenciesInfoURLsObject
    from ..models.platform_type_0 import PlatformType0


T = TypeVar(
    "T",
    bound="CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2Endpoint",
)


@_attrs_define
class CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2Endpoint:
    """A results object for each cryptocurrency requested. The map key being the id/symbol used in the request.

    Attributes:
        id (int): The unique CoinMarketCap ID for this cryptocurrency. Example: 1.
        name (str): The name of this cryptocurrency. Example: Bitcoin.
        symbol (str): The ticker symbol for this cryptocurrency. Example: BTC.
        category (CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingT
            heV2EndpointCategory): The category for this cryptocurrency. Example: coin.
        slug (str): The web URL friendly shorthand version of this cryptocurrency name. Example: bitcoin.
        logo (str): Link to a CoinMarketCap hosted logo png for this cryptocurrency. 64px is default size returned.
            Replace "64x64" in the image path with these alternative sizes: 16, 32, 64, 128, 200 Example:
            https://s2.coinmarketcap.com/static/img/coins/64x64/1.png.
        description (str): A CoinMarketCap supplied brief description of this cryptocurrency. This field will return
            null if a description is not available. Example: Bitcoin (BTC) is a consensus network that enables a new payment
            system and a completely digital currency. Powered by its users, it is a peer to peer payment network that
            requires no central authority to operate..
        date_added (str): Timestamp (ISO 8601) of when this cryptocurrency was added to CoinMarketCap. Example:
            2013-04-28T00:00:00.000Z.
        date_launched (str): Timestamp (ISO 8601) of when this cryptocurrency was launched. Example:
            2013-04-28T00:00:00.000Z.
        tags (list[str]): Tags associated with this cryptocurrency. Example: ['mineable'].
        platform (None | PlatformType0): Metadata about the parent cryptocurrency platform this cryptocurrency belongs
            to if it is a token, otherwise null.
        urls (CryptocurrenciesInfoURLsObject): An object containing various resource URLs for this cryptocurrency.
        notice (str | Unset): A [Markdown](https://commonmark.org/help/) formatted notice that may highlight a
            significant event or condition that is impacting the cryptocurrency or how it is displayed, otherwise null. A
            notice may highlight a recent or upcoming mainnet swap, symbol change, exploit event, or known issue with a
            particular exchange or market, for example. If present, this notice is also displayed in an alert banner at the
            top of the cryptocurrency's page on coinmarketcap.com.
        self_reported_circulating_supply (float | None | Unset): The self reported number of coins circulating for this
            cryptocurrency. Example: 16950100.
        self_reported_market_cap (float | None | Unset): The self reported market cap for this cryptocurrency. Example:
            16950100.
        self_reported_tags (list[str] | Unset): Array of self reported tags associated with this cryptocurrency.
            Example: ['Store Of Value', 'Play To Earn'].
        infinite_supply (bool | Unset): The cryptocurrency is known to have an infinite supply.
    """

    id: int
    name: str
    symbol: str
    category: CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2EndpointCategory
    slug: str
    logo: str
    description: str
    date_added: str
    date_launched: str
    tags: list[str]
    platform: None | PlatformType0
    urls: CryptocurrenciesInfoURLsObject
    notice: str | Unset = UNSET
    self_reported_circulating_supply: float | None | Unset = UNSET
    self_reported_market_cap: float | None | Unset = UNSET
    self_reported_tags: list[str] | Unset = UNSET
    infinite_supply: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.platform_type_0 import PlatformType0

        id = self.id

        name = self.name

        symbol = self.symbol

        category: str = self.category

        slug = self.slug

        logo = self.logo

        description = self.description

        date_added = self.date_added

        date_launched = self.date_launched

        tags = self.tags

        platform: dict[str, Any] | None
        if isinstance(self.platform, PlatformType0):
            platform = self.platform.to_dict()
        else:
            platform = self.platform

        urls = self.urls.to_dict()

        notice = self.notice

        self_reported_circulating_supply: float | None | Unset
        if isinstance(self.self_reported_circulating_supply, Unset):
            self_reported_circulating_supply = UNSET
        else:
            self_reported_circulating_supply = self.self_reported_circulating_supply

        self_reported_market_cap: float | None | Unset
        if isinstance(self.self_reported_market_cap, Unset):
            self_reported_market_cap = UNSET
        else:
            self_reported_market_cap = self.self_reported_market_cap

        self_reported_tags: list[str] | Unset = UNSET
        if not isinstance(self.self_reported_tags, Unset):
            self_reported_tags = self.self_reported_tags

        infinite_supply = self.infinite_supply

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "symbol": symbol,
                "category": category,
                "slug": slug,
                "logo": logo,
                "description": description,
                "date_added": date_added,
                "date_launched": date_launched,
                "tags": tags,
                "platform": platform,
                "urls": urls,
            }
        )
        if notice is not UNSET:
            field_dict["notice"] = notice
        if self_reported_circulating_supply is not UNSET:
            field_dict["self_reported_circulating_supply"] = self_reported_circulating_supply
        if self_reported_market_cap is not UNSET:
            field_dict["self_reported_market_cap"] = self_reported_market_cap
        if self_reported_tags is not UNSET:
            field_dict["self_reported_tags"] = self_reported_tags
        if infinite_supply is not UNSET:
            field_dict["infinite_supply"] = infinite_supply

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrencies_info_ur_ls_object import CryptocurrenciesInfoURLsObject
        from ..models.platform_type_0 import PlatformType0

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        symbol = d.pop("symbol")

        category = check_cryptocurrencies_info_cryptocurrency_object_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint_category(
            d.pop("category")
        )

        slug = d.pop("slug")

        logo = d.pop("logo")

        description = d.pop("description")

        date_added = d.pop("date_added")

        date_launched = d.pop("date_launched")

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

        urls = CryptocurrenciesInfoURLsObject.from_dict(d.pop("urls"))

        notice = d.pop("notice", UNSET)

        def _parse_self_reported_circulating_supply(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        self_reported_circulating_supply = _parse_self_reported_circulating_supply(
            d.pop("self_reported_circulating_supply", UNSET)
        )

        def _parse_self_reported_market_cap(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        self_reported_market_cap = _parse_self_reported_market_cap(d.pop("self_reported_market_cap", UNSET))

        self_reported_tags = cast(list[str], d.pop("self_reported_tags", UNSET))

        infinite_supply = d.pop("infinite_supply", UNSET)

        cryptocurrencies_info_cryptocurrency_object_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint = cls(
            id=id,
            name=name,
            symbol=symbol,
            category=category,
            slug=slug,
            logo=logo,
            description=description,
            date_added=date_added,
            date_launched=date_launched,
            tags=tags,
            platform=platform,
            urls=urls,
            notice=notice,
            self_reported_circulating_supply=self_reported_circulating_supply,
            self_reported_market_cap=self_reported_market_cap,
            self_reported_tags=self_reported_tags,
            infinite_supply=infinite_supply,
        )

        cryptocurrencies_info_cryptocurrency_object_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint.additional_properties = d
        return cryptocurrencies_info_cryptocurrency_object_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint

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
