from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cryptocurrency_market_pairs_latest_market_pair_info_object_category import (
    CryptocurrencyMarketPairsLatestMarketPairInfoObjectCategory,
    check_cryptocurrency_market_pairs_latest_market_pair_info_object_category,
)
from ..models.cryptocurrency_market_pairs_latest_market_pair_info_object_fee_type import (
    CryptocurrencyMarketPairsLatestMarketPairInfoObjectFeeType,
    check_cryptocurrency_market_pairs_latest_market_pair_info_object_fee_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cryptocurrency_market_pairs_latest_exchange_info_object import (
        CryptocurrencyMarketPairsLatestExchangeInfoObject,
    )
    from ..models.cryptocurrency_market_pairs_latest_market_pair_quote_object import (
        CryptocurrencyMarketPairsLatestMarketPairQuoteObject,
    )
    from ..models.cryptocurrency_market_pairs_latest_pair_base_currency_info_object import (
        CryptocurrencyMarketPairsLatestPairBaseCurrencyInfoObject,
    )
    from ..models.cryptocurrency_market_pairs_latest_pair_base_currency_info_object_1 import (
        CryptocurrencyMarketPairsLatestPairBaseCurrencyInfoObject1,
    )


T = TypeVar("T", bound="CryptocurrencyMarketPairsLatestMarketPairInfoObject")


@_attrs_define
class CryptocurrencyMarketPairsLatestMarketPairInfoObject:
    """Market Pair info object.

    Attributes:
        exchange (CryptocurrencyMarketPairsLatestExchangeInfoObject): Exchange details for this market pair.
        quote (CryptocurrencyMarketPairsLatestMarketPairQuoteObject): Market Pair quotes object containing key->quote
            objects for each convert option requested. USD and "exchange_reported" are defaults.
        market_pair_base (CryptocurrencyMarketPairsLatestPairBaseCurrencyInfoObject): Base currency details object for
            this market pair.
        market_pair_quote (CryptocurrencyMarketPairsLatestPairBaseCurrencyInfoObject1): Quote (secondary) currency
            details object for this market pair.
        market_id (int | Unset): The CoinMarketCap ID for this market pair. This ID can reliably be used to identify
            this unique market as the ID never changes. Example: 9933.
        market_pair (str | Unset): The name of this market pair.  Example: "BTC/USD" Example: BTC/USD.
        category (CryptocurrencyMarketPairsLatestMarketPairInfoObjectCategory | Unset): The category of trading this
            market falls under. Spot markets are the most common but options include derivatives and OTC. Example: spot.
        fee_type (CryptocurrencyMarketPairsLatestMarketPairInfoObjectFeeType | Unset): The fee type the exchange
            enforces for this market. Example: percentage.
        market_url (str | Unset): The URL to this market's trading page on the exchange if available. If not available
            the exchange's homepage URL is returned. *This field is only returned if requested through the `aux` request
            parameter.* Example: https://www.binance.com/en/trade/BTC_USDT.
    """

    exchange: CryptocurrencyMarketPairsLatestExchangeInfoObject
    quote: CryptocurrencyMarketPairsLatestMarketPairQuoteObject
    market_pair_base: CryptocurrencyMarketPairsLatestPairBaseCurrencyInfoObject
    market_pair_quote: CryptocurrencyMarketPairsLatestPairBaseCurrencyInfoObject1
    market_id: int | Unset = UNSET
    market_pair: str | Unset = UNSET
    category: CryptocurrencyMarketPairsLatestMarketPairInfoObjectCategory | Unset = UNSET
    fee_type: CryptocurrencyMarketPairsLatestMarketPairInfoObjectFeeType | Unset = UNSET
    market_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange = self.exchange.to_dict()

        quote = self.quote.to_dict()

        market_pair_base = self.market_pair_base.to_dict()

        market_pair_quote = self.market_pair_quote.to_dict()

        market_id = self.market_id

        market_pair = self.market_pair

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category

        fee_type: str | Unset = UNSET
        if not isinstance(self.fee_type, Unset):
            fee_type = self.fee_type

        market_url = self.market_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exchange": exchange,
                "quote": quote,
                "market_pair_base": market_pair_base,
                "market_pair_quote": market_pair_quote,
            }
        )
        if market_id is not UNSET:
            field_dict["market_id"] = market_id
        if market_pair is not UNSET:
            field_dict["market_pair"] = market_pair
        if category is not UNSET:
            field_dict["category"] = category
        if fee_type is not UNSET:
            field_dict["fee_type"] = fee_type
        if market_url is not UNSET:
            field_dict["market_url"] = market_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_market_pairs_latest_exchange_info_object import (
            CryptocurrencyMarketPairsLatestExchangeInfoObject,
        )
        from ..models.cryptocurrency_market_pairs_latest_market_pair_quote_object import (
            CryptocurrencyMarketPairsLatestMarketPairQuoteObject,
        )
        from ..models.cryptocurrency_market_pairs_latest_pair_base_currency_info_object import (
            CryptocurrencyMarketPairsLatestPairBaseCurrencyInfoObject,
        )
        from ..models.cryptocurrency_market_pairs_latest_pair_base_currency_info_object_1 import (
            CryptocurrencyMarketPairsLatestPairBaseCurrencyInfoObject1,
        )

        d = dict(src_dict)
        exchange = CryptocurrencyMarketPairsLatestExchangeInfoObject.from_dict(d.pop("exchange"))

        quote = CryptocurrencyMarketPairsLatestMarketPairQuoteObject.from_dict(d.pop("quote"))

        market_pair_base = CryptocurrencyMarketPairsLatestPairBaseCurrencyInfoObject.from_dict(
            d.pop("market_pair_base")
        )

        market_pair_quote = CryptocurrencyMarketPairsLatestPairBaseCurrencyInfoObject1.from_dict(
            d.pop("market_pair_quote")
        )

        market_id = d.pop("market_id", UNSET)

        market_pair = d.pop("market_pair", UNSET)

        _category = d.pop("category", UNSET)
        category: CryptocurrencyMarketPairsLatestMarketPairInfoObjectCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = check_cryptocurrency_market_pairs_latest_market_pair_info_object_category(_category)

        _fee_type = d.pop("fee_type", UNSET)
        fee_type: CryptocurrencyMarketPairsLatestMarketPairInfoObjectFeeType | Unset
        if isinstance(_fee_type, Unset):
            fee_type = UNSET
        else:
            fee_type = check_cryptocurrency_market_pairs_latest_market_pair_info_object_fee_type(_fee_type)

        market_url = d.pop("market_url", UNSET)

        cryptocurrency_market_pairs_latest_market_pair_info_object = cls(
            exchange=exchange,
            quote=quote,
            market_pair_base=market_pair_base,
            market_pair_quote=market_pair_quote,
            market_id=market_id,
            market_pair=market_pair,
            category=category,
            fee_type=fee_type,
            market_url=market_url,
        )

        cryptocurrency_market_pairs_latest_market_pair_info_object.additional_properties = d
        return cryptocurrency_market_pairs_latest_market_pair_info_object

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
