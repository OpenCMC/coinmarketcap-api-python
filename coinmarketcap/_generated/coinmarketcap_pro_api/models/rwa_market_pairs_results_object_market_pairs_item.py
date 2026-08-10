from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rwa_market_pairs_results_object_market_pairs_item_category import (
    RWAMarketPairsResultsObjectMarketPairsItemCategory,
    check_rwa_market_pairs_results_object_market_pairs_item_category,
)
from ..models.rwa_market_pairs_results_object_market_pairs_item_fee_type import (
    RWAMarketPairsResultsObjectMarketPairsItemFeeType,
    check_rwa_market_pairs_results_object_market_pairs_item_fee_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rwa_market_pairs_results_object_market_pairs_item_exchange import (
        RWAMarketPairsResultsObjectMarketPairsItemExchange,
    )
    from ..models.rwa_market_pairs_results_object_market_pairs_item_exchange_reported_quotes_item import (
        RWAMarketPairsResultsObjectMarketPairsItemExchangeReportedQuotesItem,
    )
    from ..models.rwa_market_pairs_results_object_market_pairs_item_market_pair_base import (
        RWAMarketPairsResultsObjectMarketPairsItemMarketPairBase,
    )
    from ..models.rwa_market_pairs_results_object_market_pairs_item_market_pair_quote import (
        RWAMarketPairsResultsObjectMarketPairsItemMarketPairQuote,
    )
    from ..models.rwa_market_pairs_results_object_market_pairs_item_quotes_item import (
        RWAMarketPairsResultsObjectMarketPairsItemQuotesItem,
    )


T = TypeVar("T", bound="RWAMarketPairsResultsObjectMarketPairsItem")


@_attrs_define
class RWAMarketPairsResultsObjectMarketPairsItem:
    """
    Attributes:
        exchange (RWAMarketPairsResultsObjectMarketPairsItemExchange | Unset): Exchange listing the pair.
        market_id (int | Unset): CoinMarketCap market (pair) ID. Example: 99001.
        market_pair (str | Unset): Pair label, e.g. `NVDAX/USDT`. Example: NVDAX/USDT.
        category (RWAMarketPairsResultsObjectMarketPairsItemCategory | Unset): Market category. One of `spot`,
            `derivatives`, `otc`, `perpetual`. Example: spot.
        fee_type (RWAMarketPairsResultsObjectMarketPairsItemFeeType | Unset): Fee type. One of `percentage`, `no-fees`,
            `transactional-mining`, `unknown`. Example: percentage.
        market_pair_base (RWAMarketPairsResultsObjectMarketPairsItemMarketPairBase | Unset): Base side of the pair (the
            RWA token).
        market_pair_quote (RWAMarketPairsResultsObjectMarketPairsItemMarketPairQuote | Unset): Quote side of the pair.
        exchange_reported_quotes (list[RWAMarketPairsResultsObjectMarketPairsItemExchangeReportedQuotesItem] | Unset):
            Exchange-reported price/volume.
        quotes (list[RWAMarketPairsResultsObjectMarketPairsItemQuotesItem] | Unset): Converted price/volume; one object
            per `convert`/`convert_id` currency.
    """

    exchange: RWAMarketPairsResultsObjectMarketPairsItemExchange | Unset = UNSET
    market_id: int | Unset = UNSET
    market_pair: str | Unset = UNSET
    category: RWAMarketPairsResultsObjectMarketPairsItemCategory | Unset = UNSET
    fee_type: RWAMarketPairsResultsObjectMarketPairsItemFeeType | Unset = UNSET
    market_pair_base: RWAMarketPairsResultsObjectMarketPairsItemMarketPairBase | Unset = UNSET
    market_pair_quote: RWAMarketPairsResultsObjectMarketPairsItemMarketPairQuote | Unset = UNSET
    exchange_reported_quotes: list[RWAMarketPairsResultsObjectMarketPairsItemExchangeReportedQuotesItem] | Unset = UNSET
    quotes: list[RWAMarketPairsResultsObjectMarketPairsItemQuotesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exchange, Unset):
            exchange = self.exchange.to_dict()

        market_id = self.market_id

        market_pair = self.market_pair

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category

        fee_type: str | Unset = UNSET
        if not isinstance(self.fee_type, Unset):
            fee_type = self.fee_type

        market_pair_base: dict[str, Any] | Unset = UNSET
        if not isinstance(self.market_pair_base, Unset):
            market_pair_base = self.market_pair_base.to_dict()

        market_pair_quote: dict[str, Any] | Unset = UNSET
        if not isinstance(self.market_pair_quote, Unset):
            market_pair_quote = self.market_pair_quote.to_dict()

        exchange_reported_quotes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exchange_reported_quotes, Unset):
            exchange_reported_quotes = []
            for exchange_reported_quotes_item_data in self.exchange_reported_quotes:
                exchange_reported_quotes_item = exchange_reported_quotes_item_data.to_dict()
                exchange_reported_quotes.append(exchange_reported_quotes_item)

        quotes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quotes, Unset):
            quotes = []
            for quotes_item_data in self.quotes:
                quotes_item = quotes_item_data.to_dict()
                quotes.append(quotes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exchange is not UNSET:
            field_dict["exchange"] = exchange
        if market_id is not UNSET:
            field_dict["market_id"] = market_id
        if market_pair is not UNSET:
            field_dict["market_pair"] = market_pair
        if category is not UNSET:
            field_dict["category"] = category
        if fee_type is not UNSET:
            field_dict["fee_type"] = fee_type
        if market_pair_base is not UNSET:
            field_dict["market_pair_base"] = market_pair_base
        if market_pair_quote is not UNSET:
            field_dict["market_pair_quote"] = market_pair_quote
        if exchange_reported_quotes is not UNSET:
            field_dict["exchange_reported_quotes"] = exchange_reported_quotes
        if quotes is not UNSET:
            field_dict["quotes"] = quotes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rwa_market_pairs_results_object_market_pairs_item_exchange import (
            RWAMarketPairsResultsObjectMarketPairsItemExchange,
        )
        from ..models.rwa_market_pairs_results_object_market_pairs_item_exchange_reported_quotes_item import (
            RWAMarketPairsResultsObjectMarketPairsItemExchangeReportedQuotesItem,
        )
        from ..models.rwa_market_pairs_results_object_market_pairs_item_market_pair_base import (
            RWAMarketPairsResultsObjectMarketPairsItemMarketPairBase,
        )
        from ..models.rwa_market_pairs_results_object_market_pairs_item_market_pair_quote import (
            RWAMarketPairsResultsObjectMarketPairsItemMarketPairQuote,
        )
        from ..models.rwa_market_pairs_results_object_market_pairs_item_quotes_item import (
            RWAMarketPairsResultsObjectMarketPairsItemQuotesItem,
        )

        d = dict(src_dict)
        _exchange = d.pop("exchange", UNSET)
        exchange: RWAMarketPairsResultsObjectMarketPairsItemExchange | Unset
        if isinstance(_exchange, Unset):
            exchange = UNSET
        else:
            exchange = RWAMarketPairsResultsObjectMarketPairsItemExchange.from_dict(_exchange)

        market_id = d.pop("market_id", UNSET)

        market_pair = d.pop("market_pair", UNSET)

        _category = d.pop("category", UNSET)
        category: RWAMarketPairsResultsObjectMarketPairsItemCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = check_rwa_market_pairs_results_object_market_pairs_item_category(_category)

        _fee_type = d.pop("fee_type", UNSET)
        fee_type: RWAMarketPairsResultsObjectMarketPairsItemFeeType | Unset
        if isinstance(_fee_type, Unset):
            fee_type = UNSET
        else:
            fee_type = check_rwa_market_pairs_results_object_market_pairs_item_fee_type(_fee_type)

        _market_pair_base = d.pop("market_pair_base", UNSET)
        market_pair_base: RWAMarketPairsResultsObjectMarketPairsItemMarketPairBase | Unset
        if isinstance(_market_pair_base, Unset):
            market_pair_base = UNSET
        else:
            market_pair_base = RWAMarketPairsResultsObjectMarketPairsItemMarketPairBase.from_dict(_market_pair_base)

        _market_pair_quote = d.pop("market_pair_quote", UNSET)
        market_pair_quote: RWAMarketPairsResultsObjectMarketPairsItemMarketPairQuote | Unset
        if isinstance(_market_pair_quote, Unset):
            market_pair_quote = UNSET
        else:
            market_pair_quote = RWAMarketPairsResultsObjectMarketPairsItemMarketPairQuote.from_dict(_market_pair_quote)

        _exchange_reported_quotes = d.pop("exchange_reported_quotes", UNSET)
        exchange_reported_quotes: list[RWAMarketPairsResultsObjectMarketPairsItemExchangeReportedQuotesItem] | Unset = (
            UNSET
        )
        if _exchange_reported_quotes is not UNSET:
            exchange_reported_quotes = []
            for exchange_reported_quotes_item_data in _exchange_reported_quotes:
                exchange_reported_quotes_item = (
                    RWAMarketPairsResultsObjectMarketPairsItemExchangeReportedQuotesItem.from_dict(
                        exchange_reported_quotes_item_data
                    )
                )

                exchange_reported_quotes.append(exchange_reported_quotes_item)

        _quotes = d.pop("quotes", UNSET)
        quotes: list[RWAMarketPairsResultsObjectMarketPairsItemQuotesItem] | Unset = UNSET
        if _quotes is not UNSET:
            quotes = []
            for quotes_item_data in _quotes:
                quotes_item = RWAMarketPairsResultsObjectMarketPairsItemQuotesItem.from_dict(quotes_item_data)

                quotes.append(quotes_item)

        rwa_market_pairs_results_object_market_pairs_item = cls(
            exchange=exchange,
            market_id=market_id,
            market_pair=market_pair,
            category=category,
            fee_type=fee_type,
            market_pair_base=market_pair_base,
            market_pair_quote=market_pair_quote,
            exchange_reported_quotes=exchange_reported_quotes,
            quotes=quotes,
        )

        rwa_market_pairs_results_object_market_pairs_item.additional_properties = d
        return rwa_market_pairs_results_object_market_pairs_item

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
