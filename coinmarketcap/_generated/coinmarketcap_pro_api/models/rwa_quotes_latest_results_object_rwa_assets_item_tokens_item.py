from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RWAQuotesLatestResultsObjectRwaAssetsItemTokensItem")


@_attrs_define
class RWAQuotesLatestResultsObjectRwaAssetsItemTokensItem:
    """
    Attributes:
        crypto_id (int | Unset): CoinMarketCap cryptocurrency ID of the token. Example: 36992.
        symbol (None | str | Unset): Token symbol. Example: NVDAX.
        name (None | str | Unset): Token name. Example: NVIDIA tokenized stock (xStock).
        issuer_id (None | str | Unset): Issuer ID (24-char hex); `null` when the token is not linked to a tracked
            issuer.
        issuer_name (None | str | Unset): Token issuer name (e.g. Backed Finance, Paxos); `null` when unknown.
        price (float | None | Unset): Token price in USD; `null` when unavailable.
        market_cap (float | None | Unset): Token market cap; `null` when unavailable.
        volume_24h (float | None | Unset): Token 24h volume; `null` when unavailable.
    """

    crypto_id: int | Unset = UNSET
    symbol: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    issuer_id: None | str | Unset = UNSET
    issuer_name: None | str | Unset = UNSET
    price: float | None | Unset = UNSET
    market_cap: float | None | Unset = UNSET
    volume_24h: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crypto_id = self.crypto_id

        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        issuer_id: None | str | Unset
        if isinstance(self.issuer_id, Unset):
            issuer_id = UNSET
        else:
            issuer_id = self.issuer_id

        issuer_name: None | str | Unset
        if isinstance(self.issuer_name, Unset):
            issuer_name = UNSET
        else:
            issuer_name = self.issuer_name

        price: float | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        market_cap: float | None | Unset
        if isinstance(self.market_cap, Unset):
            market_cap = UNSET
        else:
            market_cap = self.market_cap

        volume_24h: float | None | Unset
        if isinstance(self.volume_24h, Unset):
            volume_24h = UNSET
        else:
            volume_24h = self.volume_24h

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crypto_id is not UNSET:
            field_dict["crypto_id"] = crypto_id
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if name is not UNSET:
            field_dict["name"] = name
        if issuer_id is not UNSET:
            field_dict["issuer_id"] = issuer_id
        if issuer_name is not UNSET:
            field_dict["issuer_name"] = issuer_name
        if price is not UNSET:
            field_dict["price"] = price
        if market_cap is not UNSET:
            field_dict["market_cap"] = market_cap
        if volume_24h is not UNSET:
            field_dict["volume_24h"] = volume_24h

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        crypto_id = d.pop("crypto_id", UNSET)

        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_issuer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuer_id = _parse_issuer_id(d.pop("issuer_id", UNSET))

        def _parse_issuer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuer_name = _parse_issuer_name(d.pop("issuer_name", UNSET))

        def _parse_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_market_cap(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        market_cap = _parse_market_cap(d.pop("market_cap", UNSET))

        def _parse_volume_24h(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        volume_24h = _parse_volume_24h(d.pop("volume_24h", UNSET))

        rwa_quotes_latest_results_object_rwa_assets_item_tokens_item = cls(
            crypto_id=crypto_id,
            symbol=symbol,
            name=name,
            issuer_id=issuer_id,
            issuer_name=issuer_name,
            price=price,
            market_cap=market_cap,
            volume_24h=volume_24h,
        )

        rwa_quotes_latest_results_object_rwa_assets_item_tokens_item.additional_properties = d
        return rwa_quotes_latest_results_object_rwa_assets_item_tokens_item

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
