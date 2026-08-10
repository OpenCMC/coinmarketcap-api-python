from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rwa_quotes_latest_results_object_rwa_assets_item_tradfi_markets_item_exchange import (
        RWAQuotesLatestResultsObjectRwaAssetsItemTradfiMarketsItemExchange,
    )


T = TypeVar("T", bound="RWAQuotesLatestResultsObjectRwaAssetsItemTradfiMarketsItem")


@_attrs_define
class RWAQuotesLatestResultsObjectRwaAssetsItemTradfiMarketsItem:
    """
    Attributes:
        exchange (RWAQuotesLatestResultsObjectRwaAssetsItemTradfiMarketsItemExchange | Unset): Exchange listing the
            market.
        ticker (str | Unset): The ticker as listed on that exchange. Example: NVDA.
        market_url (str | Unset): Direct link to the market/trading page on the exchange. Example:
            https://www.binance.com/en/stocks/EQ_NVDA.
    """

    exchange: RWAQuotesLatestResultsObjectRwaAssetsItemTradfiMarketsItemExchange | Unset = UNSET
    ticker: str | Unset = UNSET
    market_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exchange, Unset):
            exchange = self.exchange.to_dict()

        ticker = self.ticker

        market_url = self.market_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exchange is not UNSET:
            field_dict["exchange"] = exchange
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if market_url is not UNSET:
            field_dict["market_url"] = market_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rwa_quotes_latest_results_object_rwa_assets_item_tradfi_markets_item_exchange import (
            RWAQuotesLatestResultsObjectRwaAssetsItemTradfiMarketsItemExchange,
        )

        d = dict(src_dict)
        _exchange = d.pop("exchange", UNSET)
        exchange: RWAQuotesLatestResultsObjectRwaAssetsItemTradfiMarketsItemExchange | Unset
        if isinstance(_exchange, Unset):
            exchange = UNSET
        else:
            exchange = RWAQuotesLatestResultsObjectRwaAssetsItemTradfiMarketsItemExchange.from_dict(_exchange)

        ticker = d.pop("ticker", UNSET)

        market_url = d.pop("market_url", UNSET)

        rwa_quotes_latest_results_object_rwa_assets_item_tradfi_markets_item = cls(
            exchange=exchange,
            ticker=ticker,
            market_url=market_url,
        )

        rwa_quotes_latest_results_object_rwa_assets_item_tradfi_markets_item.additional_properties = d
        return rwa_quotes_latest_results_object_rwa_assets_item_tradfi_markets_item

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
