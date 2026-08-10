from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exchanges_info_ur_ls_object import ExchangesInfoURLsObject


T = TypeVar("T", bound="ExchangesInfoExchangeInfoObject")


@_attrs_define
class ExchangesInfoExchangeInfoObject:
    """A results object for each exchange requested. The map key being the id or slug used in the request.

    Attributes:
        id (int): The unique CoinMarketCap ID for this exchange. Example: 1.
        name (str): The name of this exchange. Example: Binance.
        slug (str): The web URL friendly shorthand version of the exchange name. Example: binance.
        logo (str): Link to a CoinMarketCap hosted logo png for this exchange. 64px is default size returned. Replace
            "64x64" in the image path with these alternative sizes: 16, 32, 64, 128, 200 Example:
            https://s2.coinmarketcap.com/static/img/exchanges/64x64/270.png.
        description (str): A CoinMarketCap supplied brief description of this cryptocurrency exchange. This field will
            return null if a description is not available. Example: Launched in Jul-2017, Binance is a centralized exchange
            based in Malta..
        date_launched (str): Timestamp (ISO 8601) of the launch date for this exchange. Example:
            2017-07-14T00:00:00.000Z.
        notice (str): A [Markdown](https://commonmark.org/help/) formatted message outlining a condition that is
            impacting the availability of the exchange's market data or the secure use of the exchange, otherwise null. This
            may include a maintenance event on the exchange's end or CoinMarketCap's end, an alert about reported issues
            with withdrawls from this exchange, or another condition that may be impacting the exchange and it's markets. If
            present, this notice is also displayed in an alert banner at the top of the exchange's page on
            coinmarketcap.com.
        urls (ExchangesInfoURLsObject): An object containing various resource URLs for this exchange.
        weekly_visits (float | Unset): The number of weekly visitors. Example: 1000.
        spot_volume_usd (float | Unset): Reported all time spot volume in the specified currency. Example:
            768478308.529847.
    """

    id: int
    name: str
    slug: str
    logo: str
    description: str
    date_launched: str
    notice: str
    urls: ExchangesInfoURLsObject
    weekly_visits: float | Unset = UNSET
    spot_volume_usd: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        logo = self.logo

        description = self.description

        date_launched = self.date_launched

        notice = self.notice

        urls = self.urls.to_dict()

        weekly_visits = self.weekly_visits

        spot_volume_usd = self.spot_volume_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "logo": logo,
                "description": description,
                "date_launched": date_launched,
                "notice": notice,
                "urls": urls,
            }
        )
        if weekly_visits is not UNSET:
            field_dict["weekly_visits"] = weekly_visits
        if spot_volume_usd is not UNSET:
            field_dict["spot_volume_usd"] = spot_volume_usd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exchanges_info_ur_ls_object import ExchangesInfoURLsObject

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        logo = d.pop("logo")

        description = d.pop("description")

        date_launched = d.pop("date_launched")

        notice = d.pop("notice")

        urls = ExchangesInfoURLsObject.from_dict(d.pop("urls"))

        weekly_visits = d.pop("weekly_visits", UNSET)

        spot_volume_usd = d.pop("spot_volume_usd", UNSET)

        exchanges_info_exchange_info_object = cls(
            id=id,
            name=name,
            slug=slug,
            logo=logo,
            description=description,
            date_launched=date_launched,
            notice=notice,
            urls=urls,
            weekly_visits=weekly_visits,
            spot_volume_usd=spot_volume_usd,
        )

        exchanges_info_exchange_info_object.additional_properties = d
        return exchanges_info_exchange_info_object

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
