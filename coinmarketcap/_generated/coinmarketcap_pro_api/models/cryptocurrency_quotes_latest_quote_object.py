from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptocurrencyQuotesLatestQuoteObject")


@_attrs_define
class CryptocurrencyQuotesLatestQuoteObject:
    """A market quote in the currency conversion option.

    Attributes:
        price (float): Price in the specified currency. Example: 7139.82.
        volume_24h (float): Rolling 24 hour adjusted volume in the specified currency. Example: 4885880000.
        market_cap (float): Market cap in the specified currency. Example: 121020662982.
        market_cap_dominance (float): Market cap dominance in the specified currency. Example: 121020662982.
        fully_diluted_market_cap (float): Fully diluted market cap in the specified currency. Example: 121020662982.
        percent_change_1h (float): 1 hour change in the specified currency. Example: 0.03.
        percent_change_24h (float): 24 hour change in the specified currency. Example: 5.75.
        percent_change_7d (float): 7 day change in the specified currency. Example: -19.64.
        percent_change_30d (float): 30 day change in the specified currency. Example: -19.64.
        last_updated (str): Timestamp (ISO 8601) of when the conversion currency's current value was referenced.
            Example: 2018-06-02T23:59:59.999Z.
        volume_change_24h (float | Unset): 24 hour change in the specified currencies volume. Example: 5.75.
        volume_24h_reported (float | Unset): Rolling 24 hour reported volume in the specified currency. *This field is
            only returned if requested through the `aux` request parameter.* Example: 4885880000.
        volume_7d (float | Unset): Rolling 7 day adjusted volume in the specified currency. *This field is only returned
            if requested through the `aux` request parameter.* Example: 4885880000.
        volume_7d_reported (float | Unset): Rolling 7 day reported volume in the specified currency. *This field is only
            returned if requested through the `aux` request parameter.* Example: 4885880000.
        volume_30d (float | Unset): Rolling 30 day adjusted volume in the specified currency. *This field is only
            returned if requested through the `aux` request parameter.* Example: 4885880000.
        volume_30d_reported (float | Unset): Rolling 30 day reported volume in the specified currency. *This field is
            only returned if requested through the `aux` request parameter.* Example: 4885880000.
    """

    price: float
    volume_24h: float
    market_cap: float
    market_cap_dominance: float
    fully_diluted_market_cap: float
    percent_change_1h: float
    percent_change_24h: float
    percent_change_7d: float
    percent_change_30d: float
    last_updated: str
    volume_change_24h: float | Unset = UNSET
    volume_24h_reported: float | Unset = UNSET
    volume_7d: float | Unset = UNSET
    volume_7d_reported: float | Unset = UNSET
    volume_30d: float | Unset = UNSET
    volume_30d_reported: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price = self.price

        volume_24h = self.volume_24h

        market_cap = self.market_cap

        market_cap_dominance = self.market_cap_dominance

        fully_diluted_market_cap = self.fully_diluted_market_cap

        percent_change_1h = self.percent_change_1h

        percent_change_24h = self.percent_change_24h

        percent_change_7d = self.percent_change_7d

        percent_change_30d = self.percent_change_30d

        last_updated = self.last_updated

        volume_change_24h = self.volume_change_24h

        volume_24h_reported = self.volume_24h_reported

        volume_7d = self.volume_7d

        volume_7d_reported = self.volume_7d_reported

        volume_30d = self.volume_30d

        volume_30d_reported = self.volume_30d_reported

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "price": price,
                "volume_24h": volume_24h,
                "market_cap": market_cap,
                "market_cap_dominance": market_cap_dominance,
                "fully_diluted_market_cap": fully_diluted_market_cap,
                "percent_change_1h": percent_change_1h,
                "percent_change_24h": percent_change_24h,
                "percent_change_7d": percent_change_7d,
                "percent_change_30d": percent_change_30d,
                "last_updated": last_updated,
            }
        )
        if volume_change_24h is not UNSET:
            field_dict["volume_change_24h"] = volume_change_24h
        if volume_24h_reported is not UNSET:
            field_dict["volume_24h_reported"] = volume_24h_reported
        if volume_7d is not UNSET:
            field_dict["volume_7d"] = volume_7d
        if volume_7d_reported is not UNSET:
            field_dict["volume_7d_reported"] = volume_7d_reported
        if volume_30d is not UNSET:
            field_dict["volume_30d"] = volume_30d
        if volume_30d_reported is not UNSET:
            field_dict["volume_30d_reported"] = volume_30d_reported

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price = d.pop("price")

        volume_24h = d.pop("volume_24h")

        market_cap = d.pop("market_cap")

        market_cap_dominance = d.pop("market_cap_dominance")

        fully_diluted_market_cap = d.pop("fully_diluted_market_cap")

        percent_change_1h = d.pop("percent_change_1h")

        percent_change_24h = d.pop("percent_change_24h")

        percent_change_7d = d.pop("percent_change_7d")

        percent_change_30d = d.pop("percent_change_30d")

        last_updated = d.pop("last_updated")

        volume_change_24h = d.pop("volume_change_24h", UNSET)

        volume_24h_reported = d.pop("volume_24h_reported", UNSET)

        volume_7d = d.pop("volume_7d", UNSET)

        volume_7d_reported = d.pop("volume_7d_reported", UNSET)

        volume_30d = d.pop("volume_30d", UNSET)

        volume_30d_reported = d.pop("volume_30d_reported", UNSET)

        cryptocurrency_quotes_latest_quote_object = cls(
            price=price,
            volume_24h=volume_24h,
            market_cap=market_cap,
            market_cap_dominance=market_cap_dominance,
            fully_diluted_market_cap=fully_diluted_market_cap,
            percent_change_1h=percent_change_1h,
            percent_change_24h=percent_change_24h,
            percent_change_7d=percent_change_7d,
            percent_change_30d=percent_change_30d,
            last_updated=last_updated,
            volume_change_24h=volume_change_24h,
            volume_24h_reported=volume_24h_reported,
            volume_7d=volume_7d,
            volume_7d_reported=volume_7d_reported,
            volume_30d=volume_30d,
            volume_30d_reported=volume_30d_reported,
        )

        cryptocurrency_quotes_latest_quote_object.additional_properties = d
        return cryptocurrency_quotes_latest_quote_object

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
