from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.exchange_market_pairs_latest_market_pair_info_object_category import (
    ExchangeMarketPairsLatestMarketPairInfoObjectCategory,
    check_exchange_market_pairs_latest_market_pair_info_object_category,
)
from ..models.exchange_market_pairs_latest_market_pair_info_object_fee_type import (
    ExchangeMarketPairsLatestMarketPairInfoObjectFeeType,
    check_exchange_market_pairs_latest_market_pair_info_object_fee_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exchange_market_pairs_latest_market_pair_quote_object import (
        ExchangeMarketPairsLatestMarketPairQuoteObject,
    )
    from ..models.exchange_market_pairs_latest_pair_base_currency_info_object import (
        ExchangeMarketPairsLatestPairBaseCurrencyInfoObject,
    )
    from ..models.exchange_market_pairs_latest_pair_base_currency_info_object_1 import (
        ExchangeMarketPairsLatestPairBaseCurrencyInfoObject1,
    )


T = TypeVar("T", bound="ExchangeMarketPairsLatestMarketPairInfoObject")


@_attrs_define
class ExchangeMarketPairsLatestMarketPairInfoObject:
    """Market Pair info object.

    Attributes:
        market_id (int): The CoinMarketCap ID for this market pair. This ID can reliably be used to identify this unique
            market as the ID never changes. Example: 9933.
        market_pair (str): The name of this market pair. Example: "BTC/USD" Example: BTC/USD.
        category (ExchangeMarketPairsLatestMarketPairInfoObjectCategory): The category of trading this market falls
            under. Spot markets are the most common but options include derivatives and OTC. Example: spot.
        quote (ExchangeMarketPairsLatestMarketPairQuoteObject): Market Pair quotes object containing key->quote objects
            for each convert option requested. USD and "exchange_reported" are defaults.
        market_pair_base (ExchangeMarketPairsLatestPairBaseCurrencyInfoObject): Base currency details object for this
            market pair.
        market_pair_quote (ExchangeMarketPairsLatestPairBaseCurrencyInfoObject1): Quote (secondary) currency details
            object for this market pair
        fee_type (ExchangeMarketPairsLatestMarketPairInfoObjectFeeType | Unset): The fee type the exchange enforces for
            this market. Example: percentage.
        market_url (str | Unset): The URL to this market's trading page on the exchange if available. If not available
            the exchange's homepage URL is returned. *This field is only returned if requested through the `aux` request
            parameter.* Example: https://www.binance.com/en/trade/BTC_USDT.
    """

    market_id: int
    market_pair: str
    category: ExchangeMarketPairsLatestMarketPairInfoObjectCategory
    quote: ExchangeMarketPairsLatestMarketPairQuoteObject
    market_pair_base: ExchangeMarketPairsLatestPairBaseCurrencyInfoObject
    market_pair_quote: ExchangeMarketPairsLatestPairBaseCurrencyInfoObject1
    fee_type: ExchangeMarketPairsLatestMarketPairInfoObjectFeeType | Unset = UNSET
    market_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        market_id = self.market_id

        market_pair = self.market_pair

        category: str = self.category

        quote = self.quote.to_dict()

        market_pair_base = self.market_pair_base.to_dict()

        market_pair_quote = self.market_pair_quote.to_dict()

        fee_type: str | Unset = UNSET
        if not isinstance(self.fee_type, Unset):
            fee_type = self.fee_type

        market_url = self.market_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "market_id": market_id,
                "market_pair": market_pair,
                "category": category,
                "quote": quote,
                "market_pair_base": market_pair_base,
                "market_pair_quote": market_pair_quote,
            }
        )
        if fee_type is not UNSET:
            field_dict["fee_type"] = fee_type
        if market_url is not UNSET:
            field_dict["market_url"] = market_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exchange_market_pairs_latest_market_pair_quote_object import (
            ExchangeMarketPairsLatestMarketPairQuoteObject,
        )
        from ..models.exchange_market_pairs_latest_pair_base_currency_info_object import (
            ExchangeMarketPairsLatestPairBaseCurrencyInfoObject,
        )
        from ..models.exchange_market_pairs_latest_pair_base_currency_info_object_1 import (
            ExchangeMarketPairsLatestPairBaseCurrencyInfoObject1,
        )

        d = dict(src_dict)
        market_id = d.pop("market_id")

        market_pair = d.pop("market_pair")

        category = check_exchange_market_pairs_latest_market_pair_info_object_category(d.pop("category"))

        quote = ExchangeMarketPairsLatestMarketPairQuoteObject.from_dict(d.pop("quote"))

        market_pair_base = ExchangeMarketPairsLatestPairBaseCurrencyInfoObject.from_dict(d.pop("market_pair_base"))

        market_pair_quote = ExchangeMarketPairsLatestPairBaseCurrencyInfoObject1.from_dict(d.pop("market_pair_quote"))

        _fee_type = d.pop("fee_type", UNSET)
        fee_type: ExchangeMarketPairsLatestMarketPairInfoObjectFeeType | Unset
        if isinstance(_fee_type, Unset):
            fee_type = UNSET
        else:
            fee_type = check_exchange_market_pairs_latest_market_pair_info_object_fee_type(_fee_type)

        market_url = d.pop("market_url", UNSET)

        exchange_market_pairs_latest_market_pair_info_object = cls(
            market_id=market_id,
            market_pair=market_pair,
            category=category,
            quote=quote,
            market_pair_base=market_pair_base,
            market_pair_quote=market_pair_quote,
            fee_type=fee_type,
            market_url=market_url,
        )

        exchange_market_pairs_latest_market_pair_info_object.additional_properties = d
        return exchange_market_pairs_latest_market_pair_info_object

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
