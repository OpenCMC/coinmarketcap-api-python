from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.derivatives_market_pairs_list_latest_results_object_market_pairs_item_category import (
    DerivativesMarketPairsListLatestResultsObjectMarketPairsItemCategory,
    check_derivatives_market_pairs_list_latest_results_object_market_pairs_item_category,
)
from ..models.derivatives_market_pairs_list_latest_results_object_market_pairs_item_fee_type import (
    DerivativesMarketPairsListLatestResultsObjectMarketPairsItemFeeType,
    check_derivatives_market_pairs_list_latest_results_object_market_pairs_item_fee_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.derivatives_market_pairs_list_latest_results_object_market_pairs_item_exchange_reported_quotes_item import (
        DerivativesMarketPairsListLatestResultsObjectMarketPairsItemExchangeReportedQuotesItem,
    )
    from ..models.derivatives_market_pairs_list_latest_results_object_market_pairs_item_market_pair_base import (
        DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBase,
    )
    from ..models.derivatives_market_pairs_list_latest_results_object_market_pairs_item_market_pair_quote import (
        DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuote,
    )
    from ..models.derivatives_market_pairs_list_latest_results_object_market_pairs_item_quotes_item import (
        DerivativesMarketPairsListLatestResultsObjectMarketPairsItemQuotesItem,
    )


T = TypeVar("T", bound="DerivativesMarketPairsListLatestResultsObjectMarketPairsItem")


@_attrs_define
class DerivativesMarketPairsListLatestResultsObjectMarketPairsItem:
    """
    Attributes:
        market_id (int | Unset): The CoinMarketCap ID for this market pair. Example: 47150.
        market_pair (str | Unset): Symbol pair identifier as listed on the exchange. Example: BTC/USDT.
        category (DerivativesMarketPairsListLatestResultsObjectMarketPairsItemCategory | Unset): Derivative category.
            Example: perpetual.
        fee_type (DerivativesMarketPairsListLatestResultsObjectMarketPairsItemFeeType | Unset): Fee type the exchange
            enforces for this market. Example: percentage.
        outlier_detected (bool | Unset): Whether this market pair has been flagged as an outlier.
        exclusions (list[str] | None | Unset): Reasons this market pair is excluded from aggregate calculations, if any.
        market_pair_base (DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBase | Unset): Base
            currency of the market pair.
        market_pair_quote (DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuote | Unset): Quote
            currency of the market pair.
        exchange_reported_quotes
            (list[DerivativesMarketPairsListLatestResultsObjectMarketPairsItemExchangeReportedQuotesItem] | Unset): Quotes
            as reported directly by the exchange, one entry per requested conversion currency.
        quotes (list[DerivativesMarketPairsListLatestResultsObjectMarketPairsItemQuotesItem] | Unset): CoinMarketCap-
            normalized quotes, one entry per requested conversion currency.
    """

    market_id: int | Unset = UNSET
    market_pair: str | Unset = UNSET
    category: DerivativesMarketPairsListLatestResultsObjectMarketPairsItemCategory | Unset = UNSET
    fee_type: DerivativesMarketPairsListLatestResultsObjectMarketPairsItemFeeType | Unset = UNSET
    outlier_detected: bool | Unset = UNSET
    exclusions: list[str] | None | Unset = UNSET
    market_pair_base: DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBase | Unset = UNSET
    market_pair_quote: DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuote | Unset = UNSET
    exchange_reported_quotes: (
        list[DerivativesMarketPairsListLatestResultsObjectMarketPairsItemExchangeReportedQuotesItem] | Unset
    ) = UNSET
    quotes: list[DerivativesMarketPairsListLatestResultsObjectMarketPairsItemQuotesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        market_id = self.market_id

        market_pair = self.market_pair

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category

        fee_type: str | Unset = UNSET
        if not isinstance(self.fee_type, Unset):
            fee_type = self.fee_type

        outlier_detected = self.outlier_detected

        exclusions: list[str] | None | Unset
        if isinstance(self.exclusions, Unset):
            exclusions = UNSET
        elif isinstance(self.exclusions, list):
            exclusions = self.exclusions

        else:
            exclusions = self.exclusions

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
        if market_id is not UNSET:
            field_dict["market_id"] = market_id
        if market_pair is not UNSET:
            field_dict["market_pair"] = market_pair
        if category is not UNSET:
            field_dict["category"] = category
        if fee_type is not UNSET:
            field_dict["fee_type"] = fee_type
        if outlier_detected is not UNSET:
            field_dict["outlier_detected"] = outlier_detected
        if exclusions is not UNSET:
            field_dict["exclusions"] = exclusions
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
        from ..models.derivatives_market_pairs_list_latest_results_object_market_pairs_item_exchange_reported_quotes_item import (
            DerivativesMarketPairsListLatestResultsObjectMarketPairsItemExchangeReportedQuotesItem,
        )
        from ..models.derivatives_market_pairs_list_latest_results_object_market_pairs_item_market_pair_base import (
            DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBase,
        )
        from ..models.derivatives_market_pairs_list_latest_results_object_market_pairs_item_market_pair_quote import (
            DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuote,
        )
        from ..models.derivatives_market_pairs_list_latest_results_object_market_pairs_item_quotes_item import (
            DerivativesMarketPairsListLatestResultsObjectMarketPairsItemQuotesItem,
        )

        d = dict(src_dict)
        market_id = d.pop("market_id", UNSET)

        market_pair = d.pop("market_pair", UNSET)

        _category = d.pop("category", UNSET)
        category: DerivativesMarketPairsListLatestResultsObjectMarketPairsItemCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = check_derivatives_market_pairs_list_latest_results_object_market_pairs_item_category(_category)

        _fee_type = d.pop("fee_type", UNSET)
        fee_type: DerivativesMarketPairsListLatestResultsObjectMarketPairsItemFeeType | Unset
        if isinstance(_fee_type, Unset):
            fee_type = UNSET
        else:
            fee_type = check_derivatives_market_pairs_list_latest_results_object_market_pairs_item_fee_type(_fee_type)

        outlier_detected = d.pop("outlier_detected", UNSET)

        def _parse_exclusions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclusions_type_0 = cast(list[str], data)

                return exclusions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exclusions = _parse_exclusions(d.pop("exclusions", UNSET))

        _market_pair_base = d.pop("market_pair_base", UNSET)
        market_pair_base: DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBase | Unset
        if isinstance(_market_pair_base, Unset):
            market_pair_base = UNSET
        else:
            market_pair_base = DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairBase.from_dict(
                _market_pair_base
            )

        _market_pair_quote = d.pop("market_pair_quote", UNSET)
        market_pair_quote: DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuote | Unset
        if isinstance(_market_pair_quote, Unset):
            market_pair_quote = UNSET
        else:
            market_pair_quote = DerivativesMarketPairsListLatestResultsObjectMarketPairsItemMarketPairQuote.from_dict(
                _market_pair_quote
            )

        _exchange_reported_quotes = d.pop("exchange_reported_quotes", UNSET)
        exchange_reported_quotes: (
            list[DerivativesMarketPairsListLatestResultsObjectMarketPairsItemExchangeReportedQuotesItem] | Unset
        ) = UNSET
        if _exchange_reported_quotes is not UNSET:
            exchange_reported_quotes = []
            for exchange_reported_quotes_item_data in _exchange_reported_quotes:
                exchange_reported_quotes_item = (
                    DerivativesMarketPairsListLatestResultsObjectMarketPairsItemExchangeReportedQuotesItem.from_dict(
                        exchange_reported_quotes_item_data
                    )
                )

                exchange_reported_quotes.append(exchange_reported_quotes_item)

        _quotes = d.pop("quotes", UNSET)
        quotes: list[DerivativesMarketPairsListLatestResultsObjectMarketPairsItemQuotesItem] | Unset = UNSET
        if _quotes is not UNSET:
            quotes = []
            for quotes_item_data in _quotes:
                quotes_item = DerivativesMarketPairsListLatestResultsObjectMarketPairsItemQuotesItem.from_dict(
                    quotes_item_data
                )

                quotes.append(quotes_item)

        derivatives_market_pairs_list_latest_results_object_market_pairs_item = cls(
            market_id=market_id,
            market_pair=market_pair,
            category=category,
            fee_type=fee_type,
            outlier_detected=outlier_detected,
            exclusions=exclusions,
            market_pair_base=market_pair_base,
            market_pair_quote=market_pair_quote,
            exchange_reported_quotes=exchange_reported_quotes,
            quotes=quotes,
        )

        derivatives_market_pairs_list_latest_results_object_market_pairs_item.additional_properties = d
        return derivatives_market_pairs_list_latest_results_object_market_pairs_item

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
