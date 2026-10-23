from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptocurrencyListingsLatestQuoteObject2")


@_attrs_define
class CryptocurrencyListingsLatestQuoteObject2:
    """A market quote in the currency conversion option.

    Attributes:
        price (float): Price in the specified currency for this historical. Example: 7139.82.
        volume_24h (float): Rolling 24 hour adjusted volume in the specified currency. Example: 4885880000.
        market_cap (float): Market cap in the specified currency. Example: 121020662982.
        market_cap_dominance (float): Market cap dominance in the specified currency. Example: 121020662982.
        fully_diluted_market_cap (float): Fully diluted market cap in the specified currency. Example: 121020662982.
        percent_change_1h (float): 1 hour change in the specified currency. Example: 0.03.
        percent_change_24h (float): 24 hour change in the specified currency. Example: 5.75.
        percent_change_7d (float): 7 day change in the specified currency. Example: -19.64.
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
        cex_volume_24h (float | Unset): 24 hour trading volume from centralized exchanges in the requested currency.
        dex_volume_24h (float | Unset): 24 hour trading volume from decentralized exchanges in the requested currency.
        percent_change_30d (float | Unset): 30 day price change as a percentage.
        percent_change_60d (float | Unset): 60 day price change as a percentage.
        percent_change_90d (float | Unset): 90 day price change as a percentage.
        tvl (float | None | Unset): Total value locked in the requested currency. `null` when TVL is not available.
    """

    price: float
    volume_24h: float
    market_cap: float
    market_cap_dominance: float
    fully_diluted_market_cap: float
    percent_change_1h: float
    percent_change_24h: float
    percent_change_7d: float
    last_updated: str
    volume_change_24h: float | Unset = UNSET
    volume_24h_reported: float | Unset = UNSET
    volume_7d: float | Unset = UNSET
    volume_7d_reported: float | Unset = UNSET
    volume_30d: float | Unset = UNSET
    volume_30d_reported: float | Unset = UNSET
    cex_volume_24h: float | Unset = UNSET
    dex_volume_24h: float | Unset = UNSET
    percent_change_30d: float | Unset = UNSET
    percent_change_60d: float | Unset = UNSET
    percent_change_90d: float | Unset = UNSET
    tvl: float | None | Unset = UNSET
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

        last_updated = self.last_updated

        volume_change_24h = self.volume_change_24h

        volume_24h_reported = self.volume_24h_reported

        volume_7d = self.volume_7d

        volume_7d_reported = self.volume_7d_reported

        volume_30d = self.volume_30d

        volume_30d_reported = self.volume_30d_reported

        cex_volume_24h = self.cex_volume_24h

        dex_volume_24h = self.dex_volume_24h

        percent_change_30d = self.percent_change_30d

        percent_change_60d = self.percent_change_60d

        percent_change_90d = self.percent_change_90d

        tvl: float | None | Unset
        if isinstance(self.tvl, Unset):
            tvl = UNSET
        else:
            tvl = self.tvl

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
        if cex_volume_24h is not UNSET:
            field_dict["cex_volume_24h"] = cex_volume_24h
        if dex_volume_24h is not UNSET:
            field_dict["dex_volume_24h"] = dex_volume_24h
        if percent_change_30d is not UNSET:
            field_dict["percent_change_30d"] = percent_change_30d
        if percent_change_60d is not UNSET:
            field_dict["percent_change_60d"] = percent_change_60d
        if percent_change_90d is not UNSET:
            field_dict["percent_change_90d"] = percent_change_90d
        if tvl is not UNSET:
            field_dict["tvl"] = tvl

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

        last_updated = d.pop("last_updated")

        volume_change_24h = d.pop("volume_change_24h", UNSET)

        volume_24h_reported = d.pop("volume_24h_reported", UNSET)

        volume_7d = d.pop("volume_7d", UNSET)

        volume_7d_reported = d.pop("volume_7d_reported", UNSET)

        volume_30d = d.pop("volume_30d", UNSET)

        volume_30d_reported = d.pop("volume_30d_reported", UNSET)

        cex_volume_24h = d.pop("cex_volume_24h", UNSET)

        dex_volume_24h = d.pop("dex_volume_24h", UNSET)

        percent_change_30d = d.pop("percent_change_30d", UNSET)

        percent_change_60d = d.pop("percent_change_60d", UNSET)

        percent_change_90d = d.pop("percent_change_90d", UNSET)

        def _parse_tvl(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tvl = _parse_tvl(d.pop("tvl", UNSET))

        cryptocurrency_listings_latest_quote_object_2 = cls(
            price=price,
            volume_24h=volume_24h,
            market_cap=market_cap,
            market_cap_dominance=market_cap_dominance,
            fully_diluted_market_cap=fully_diluted_market_cap,
            percent_change_1h=percent_change_1h,
            percent_change_24h=percent_change_24h,
            percent_change_7d=percent_change_7d,
            last_updated=last_updated,
            volume_change_24h=volume_change_24h,
            volume_24h_reported=volume_24h_reported,
            volume_7d=volume_7d,
            volume_7d_reported=volume_7d_reported,
            volume_30d=volume_30d,
            volume_30d_reported=volume_30d_reported,
            cex_volume_24h=cex_volume_24h,
            dex_volume_24h=dex_volume_24h,
            percent_change_30d=percent_change_30d,
            percent_change_60d=percent_change_60d,
            percent_change_90d=percent_change_90d,
            tvl=tvl,
        )

        cryptocurrency_listings_latest_quote_object_2.additional_properties = d
        return cryptocurrency_listings_latest_quote_object_2

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
