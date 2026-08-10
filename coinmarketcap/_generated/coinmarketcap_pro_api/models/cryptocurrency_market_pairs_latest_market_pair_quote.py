from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptocurrencyMarketPairsLatestMarketPairQuote")


@_attrs_define
class CryptocurrencyMarketPairsLatestMarketPairQuote:
    """One or more market quotes where $key is the conversion currency requested, ex. USD

    Attributes:
        price (float): The lastest exchange reported price for this market pair converted into the requested convert
            currency. Example: 8000.23.
        volume_24h (float): The latest exchange reported 24 hour rolling volume in quote units for this market pair
            converted into the requested convert currency. Example: 1600000.
        last_updated (str): Timestamp (ISO 8601) of when the conversion currency's current value was referenced for this
            conversion. Example: 2018-06-02T23:59:59.999Z.
        price_quote (float | Unset): The latest exchange reported price in base units converted into the requested
            convert currency. *This field is only returned if requested through the `aux` request parameter.* Example:
            8000.23.
    """

    price: float
    volume_24h: float
    last_updated: str
    price_quote: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price = self.price

        volume_24h = self.volume_24h

        last_updated = self.last_updated

        price_quote = self.price_quote

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "price": price,
                "volume_24h": volume_24h,
                "last_updated": last_updated,
            }
        )
        if price_quote is not UNSET:
            field_dict["price_quote"] = price_quote

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price = d.pop("price")

        volume_24h = d.pop("volume_24h")

        last_updated = d.pop("last_updated")

        price_quote = d.pop("price_quote", UNSET)

        cryptocurrency_market_pairs_latest_market_pair_quote = cls(
            price=price,
            volume_24h=volume_24h,
            last_updated=last_updated,
            price_quote=price_quote,
        )

        cryptocurrency_market_pairs_latest_market_pair_quote.additional_properties = d
        return cryptocurrency_market_pairs_latest_market_pair_quote

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
