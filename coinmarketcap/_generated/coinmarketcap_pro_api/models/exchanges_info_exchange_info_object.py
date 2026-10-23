from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

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
        notice (None | str): A [Markdown](https://commonmark.org/help/) formatted message outlining a condition that is
            impacting the availability of the exchange's market data or the secure use of the exchange, otherwise null. This
            may include a maintenance event on the exchange's end or CoinMarketCap's end, an alert about reported issues
            with withdrawls from this exchange, or another condition that may be impacting the exchange and it's markets. If
            present, this notice is also displayed in an alert banner at the top of the exchange's page on
            coinmarketcap.com.
        urls (ExchangesInfoURLsObject): An object containing various resource URLs for this exchange.
        weekly_visits (float | Unset): The number of weekly visitors. Example: 1000.
        spot_volume_usd (float | Unset): Reported all time spot volume in the specified currency. Example:
            768478308.529847.
        countries (list[str] | Unset): Countries this exchange operates in. `GLOBAL` means no specific country.
        fiats (list[str] | Unset): Fiat currencies accepted by this exchange.
        maker_fee (float | Unset): Maker fee charged by this exchange, as a percentage.
        taker_fee (float | Unset): Taker fee charged by this exchange, as a percentage.
        spot_volume_last_updated (datetime.datetime | Unset): Timestamp (ISO 8601) of the last update to
            `spot_volume_usd`.
        is_redistributable (int | Unset): 1 if this exchange's data can be redistributed, otherwise 0.
        on_ramp_direct_deposit (str | Unset): Comma-separated fiat currencies you can deposit directly (for example by
            bank transfer).
        on_ramp_card_visa_mastercard (str | Unset): Comma-separated fiat currencies you can use to buy crypto with a
            Visa or Mastercard card.
        on_ramp_google_apple_pay (str | Unset): Comma-separated fiat currencies you can use to buy crypto with Google
            Pay or Apple Pay.
        on_ramp_third_party (str | Unset): Comma-separated fiat currencies you can use to buy crypto through third-party
            payment providers.
        on_ramp_p2p (str | Unset): Comma-separated fiat currencies you can use to buy crypto through peer-to-peer
            trading.
        off_ramp_direct_withdrawal (str | Unset): Comma-separated fiat currencies you can withdraw directly (for example
            by bank transfer).
        off_ramp_p2p (str | Unset): Comma-separated fiat currencies you can sell crypto for through peer-to-peer
            trading.
    """

    id: int
    name: str
    slug: str
    logo: str
    description: str
    date_launched: str
    notice: None | str
    urls: ExchangesInfoURLsObject
    weekly_visits: float | Unset = UNSET
    spot_volume_usd: float | Unset = UNSET
    countries: list[str] | Unset = UNSET
    fiats: list[str] | Unset = UNSET
    maker_fee: float | Unset = UNSET
    taker_fee: float | Unset = UNSET
    spot_volume_last_updated: datetime.datetime | Unset = UNSET
    is_redistributable: int | Unset = UNSET
    on_ramp_direct_deposit: str | Unset = UNSET
    on_ramp_card_visa_mastercard: str | Unset = UNSET
    on_ramp_google_apple_pay: str | Unset = UNSET
    on_ramp_third_party: str | Unset = UNSET
    on_ramp_p2p: str | Unset = UNSET
    off_ramp_direct_withdrawal: str | Unset = UNSET
    off_ramp_p2p: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        logo = self.logo

        description = self.description

        date_launched = self.date_launched

        notice: None | str
        notice = self.notice

        urls = self.urls.to_dict()

        weekly_visits = self.weekly_visits

        spot_volume_usd = self.spot_volume_usd

        countries: list[str] | Unset = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        fiats: list[str] | Unset = UNSET
        if not isinstance(self.fiats, Unset):
            fiats = self.fiats

        maker_fee = self.maker_fee

        taker_fee = self.taker_fee

        spot_volume_last_updated: str | Unset = UNSET
        if not isinstance(self.spot_volume_last_updated, Unset):
            spot_volume_last_updated = self.spot_volume_last_updated.isoformat()

        is_redistributable = self.is_redistributable

        on_ramp_direct_deposit = self.on_ramp_direct_deposit

        on_ramp_card_visa_mastercard = self.on_ramp_card_visa_mastercard

        on_ramp_google_apple_pay = self.on_ramp_google_apple_pay

        on_ramp_third_party = self.on_ramp_third_party

        on_ramp_p2p = self.on_ramp_p2p

        off_ramp_direct_withdrawal = self.off_ramp_direct_withdrawal

        off_ramp_p2p = self.off_ramp_p2p

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
        if countries is not UNSET:
            field_dict["countries"] = countries
        if fiats is not UNSET:
            field_dict["fiats"] = fiats
        if maker_fee is not UNSET:
            field_dict["maker_fee"] = maker_fee
        if taker_fee is not UNSET:
            field_dict["taker_fee"] = taker_fee
        if spot_volume_last_updated is not UNSET:
            field_dict["spot_volume_last_updated"] = spot_volume_last_updated
        if is_redistributable is not UNSET:
            field_dict["is_redistributable"] = is_redistributable
        if on_ramp_direct_deposit is not UNSET:
            field_dict["on_ramp_direct_deposit"] = on_ramp_direct_deposit
        if on_ramp_card_visa_mastercard is not UNSET:
            field_dict["on_ramp_card_visa_mastercard"] = on_ramp_card_visa_mastercard
        if on_ramp_google_apple_pay is not UNSET:
            field_dict["on_ramp_google_apple_pay"] = on_ramp_google_apple_pay
        if on_ramp_third_party is not UNSET:
            field_dict["on_ramp_third_party"] = on_ramp_third_party
        if on_ramp_p2p is not UNSET:
            field_dict["on_ramp_p2p"] = on_ramp_p2p
        if off_ramp_direct_withdrawal is not UNSET:
            field_dict["off_ramp_direct_withdrawal"] = off_ramp_direct_withdrawal
        if off_ramp_p2p is not UNSET:
            field_dict["off_ramp_p2p"] = off_ramp_p2p

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

        def _parse_notice(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        notice = _parse_notice(d.pop("notice"))

        urls = ExchangesInfoURLsObject.from_dict(d.pop("urls"))

        weekly_visits = d.pop("weekly_visits", UNSET)

        spot_volume_usd = d.pop("spot_volume_usd", UNSET)

        countries = cast(list[str], d.pop("countries", UNSET))

        fiats = cast(list[str], d.pop("fiats", UNSET))

        maker_fee = d.pop("maker_fee", UNSET)

        taker_fee = d.pop("taker_fee", UNSET)

        _spot_volume_last_updated = d.pop("spot_volume_last_updated", UNSET)
        spot_volume_last_updated: datetime.datetime | Unset
        if isinstance(_spot_volume_last_updated, Unset):
            spot_volume_last_updated = UNSET
        else:
            spot_volume_last_updated = isoparse(_spot_volume_last_updated)

        is_redistributable = d.pop("is_redistributable", UNSET)

        on_ramp_direct_deposit = d.pop("on_ramp_direct_deposit", UNSET)

        on_ramp_card_visa_mastercard = d.pop("on_ramp_card_visa_mastercard", UNSET)

        on_ramp_google_apple_pay = d.pop("on_ramp_google_apple_pay", UNSET)

        on_ramp_third_party = d.pop("on_ramp_third_party", UNSET)

        on_ramp_p2p = d.pop("on_ramp_p2p", UNSET)

        off_ramp_direct_withdrawal = d.pop("off_ramp_direct_withdrawal", UNSET)

        off_ramp_p2p = d.pop("off_ramp_p2p", UNSET)

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
            countries=countries,
            fiats=fiats,
            maker_fee=maker_fee,
            taker_fee=taker_fee,
            spot_volume_last_updated=spot_volume_last_updated,
            is_redistributable=is_redistributable,
            on_ramp_direct_deposit=on_ramp_direct_deposit,
            on_ramp_card_visa_mastercard=on_ramp_card_visa_mastercard,
            on_ramp_google_apple_pay=on_ramp_google_apple_pay,
            on_ramp_third_party=on_ramp_third_party,
            on_ramp_p2p=on_ramp_p2p,
            off_ramp_direct_withdrawal=off_ramp_direct_withdrawal,
            off_ramp_p2p=off_ramp_p2p,
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
