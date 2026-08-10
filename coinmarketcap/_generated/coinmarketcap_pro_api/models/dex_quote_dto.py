from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DexQuoteDTO")


@_attrs_define
class DexQuoteDTO:
    """A map of market quotes in different currency conversions. The default map included is USD.

    Attributes:
        price (float | Unset): Price in the specified currency for this spot pair.
        liquidity (float | Unset): Total liquidity available currently in the specified currency. This field will return
            null if not available.
        convert_id (str | Unset): id of specified currency.
        price_by_quote_asset (float | Unset): Price of the base asset in quote asset for this spot pair.
        last_updated (datetime.datetime | Unset): Timestamp (ISO 8601) of when the conversion currency's current value
            was referenced for this conversion.
        volume_24h (float | Unset): Reported 24 hour volume in the specified spot pair in the specified currency.
        percent_change_price_1h (float | Unset): 1 hour price change percentage in the specified spot pair in the
            specified currency.
        percent_change_price_24h (float | Unset): 24 hour price change percentage in the specified spot pair in the
            specified currency.
        fully_diluted_value (float | Unset): Fully Diluted Value = (Total Supply - Burned Supply) * Price. Returned in
            the specified currency.
        field_24h_buy_volume (float | Unset): 24 hours buy volume of the asset
        field_24h_sell_volume (float | Unset): 24 hours sell volume of the asset
    """

    price: float | Unset = UNSET
    liquidity: float | Unset = UNSET
    convert_id: str | Unset = UNSET
    price_by_quote_asset: float | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    volume_24h: float | Unset = UNSET
    percent_change_price_1h: float | Unset = UNSET
    percent_change_price_24h: float | Unset = UNSET
    fully_diluted_value: float | Unset = UNSET
    field_24h_buy_volume: float | Unset = UNSET
    field_24h_sell_volume: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price = self.price

        liquidity = self.liquidity

        convert_id = self.convert_id

        price_by_quote_asset = self.price_by_quote_asset

        last_updated: str | Unset = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        volume_24h = self.volume_24h

        percent_change_price_1h = self.percent_change_price_1h

        percent_change_price_24h = self.percent_change_price_24h

        fully_diluted_value = self.fully_diluted_value

        field_24h_buy_volume = self.field_24h_buy_volume

        field_24h_sell_volume = self.field_24h_sell_volume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price is not UNSET:
            field_dict["price"] = price
        if liquidity is not UNSET:
            field_dict["liquidity"] = liquidity
        if convert_id is not UNSET:
            field_dict["convert_id"] = convert_id
        if price_by_quote_asset is not UNSET:
            field_dict["price_by_quote_asset"] = price_by_quote_asset
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if volume_24h is not UNSET:
            field_dict["volume_24h"] = volume_24h
        if percent_change_price_1h is not UNSET:
            field_dict["percent_change_price_1h"] = percent_change_price_1h
        if percent_change_price_24h is not UNSET:
            field_dict["percent_change_price_24h"] = percent_change_price_24h
        if fully_diluted_value is not UNSET:
            field_dict["fully_diluted_value"] = fully_diluted_value
        if field_24h_buy_volume is not UNSET:
            field_dict["24h_buy_volume"] = field_24h_buy_volume
        if field_24h_sell_volume is not UNSET:
            field_dict["24h_sell_volume"] = field_24h_sell_volume

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price = d.pop("price", UNSET)

        liquidity = d.pop("liquidity", UNSET)

        convert_id = d.pop("convert_id", UNSET)

        price_by_quote_asset = d.pop("price_by_quote_asset", UNSET)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        volume_24h = d.pop("volume_24h", UNSET)

        percent_change_price_1h = d.pop("percent_change_price_1h", UNSET)

        percent_change_price_24h = d.pop("percent_change_price_24h", UNSET)

        fully_diluted_value = d.pop("fully_diluted_value", UNSET)

        field_24h_buy_volume = d.pop("24h_buy_volume", UNSET)

        field_24h_sell_volume = d.pop("24h_sell_volume", UNSET)

        dex_quote_dto = cls(
            price=price,
            liquidity=liquidity,
            convert_id=convert_id,
            price_by_quote_asset=price_by_quote_asset,
            last_updated=last_updated,
            volume_24h=volume_24h,
            percent_change_price_1h=percent_change_price_1h,
            percent_change_price_24h=percent_change_price_24h,
            fully_diluted_value=fully_diluted_value,
            field_24h_buy_volume=field_24h_buy_volume,
            field_24h_sell_volume=field_24h_sell_volume,
        )

        dex_quote_dto.additional_properties = d
        return dex_quote_dto

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
