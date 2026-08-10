from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptocurrencyMarketPairsLatestExchangeInfoObject")


@_attrs_define
class CryptocurrencyMarketPairsLatestExchangeInfoObject:
    """Exchange details for this market pair.

    Attributes:
        id (int): The id of the exchange this market pair is under. Example: 1.
        slug (str): The slug of the exchange this market pair is under. Example: binance.
        name (str): The name of the exchange this market pair is under. Example: binance.
        notice (str | Unset): A [Markdown](https://commonmark.org/help/) formatted message outlining a condition that is
            impacting the availability of this exchange's market data or the secure use of the exchange, otherwise null.
            This may include a maintenance event on the exchange's end or CoinMarketCap's end, an alert about reported
            issues with withdrawls from this exchange, or another condition that may be impacting this exchange and it's
            markets. If present, this notice is also displayed in an alert banner at the top of the exchange's page on
            coinmarketcap.com. *This field is only returned if requested through the `aux` request parameter.* Example: The
            BTC/USD market on BitMEX is a derivatives market NOT actually spot trading Bitcoin. As a result, it has been
            excluded from the price and volume averages of Bitcoin..
    """

    id: int
    slug: str
    name: str
    notice: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug = self.slug

        name = self.name

        notice = self.notice

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "name": name,
            }
        )
        if notice is not UNSET:
            field_dict["notice"] = notice

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        slug = d.pop("slug")

        name = d.pop("name")

        notice = d.pop("notice", UNSET)

        cryptocurrency_market_pairs_latest_exchange_info_object = cls(
            id=id,
            slug=slug,
            name=name,
            notice=notice,
        )

        cryptocurrency_market_pairs_latest_exchange_info_object.additional_properties = d
        return cryptocurrency_market_pairs_latest_exchange_info_object

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
