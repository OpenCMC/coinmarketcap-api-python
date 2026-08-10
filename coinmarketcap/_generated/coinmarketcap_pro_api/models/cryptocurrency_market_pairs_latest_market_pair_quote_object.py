from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cryptocurrency_market_pairs_latest_market_pair_exchange_reported_quote import (
        CryptocurrencyMarketPairsLatestMarketPairExchangeReportedQuote,
    )
    from ..models.cryptocurrency_market_pairs_latest_market_pair_quote import (
        CryptocurrencyMarketPairsLatestMarketPairQuote,
    )


T = TypeVar("T", bound="CryptocurrencyMarketPairsLatestMarketPairQuoteObject")


@_attrs_define
class CryptocurrencyMarketPairsLatestMarketPairQuoteObject:
    """Market Pair quotes object containing key->quote objects for each convert option requested. USD and
    "exchange_reported" are defaults.

        Attributes:
            exchange_reported (CryptocurrencyMarketPairsLatestMarketPairExchangeReportedQuote): A default exchange reported
                quote containing raw exchange reported values.
    """

    exchange_reported: CryptocurrencyMarketPairsLatestMarketPairExchangeReportedQuote
    additional_properties: dict[str, CryptocurrencyMarketPairsLatestMarketPairQuote] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        exchange_reported = self.exchange_reported.to_dict()

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update(
            {
                "exchange_reported": exchange_reported,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cryptocurrency_market_pairs_latest_market_pair_exchange_reported_quote import (
            CryptocurrencyMarketPairsLatestMarketPairExchangeReportedQuote,
        )
        from ..models.cryptocurrency_market_pairs_latest_market_pair_quote import (
            CryptocurrencyMarketPairsLatestMarketPairQuote,
        )

        d = dict(src_dict)
        exchange_reported = CryptocurrencyMarketPairsLatestMarketPairExchangeReportedQuote.from_dict(
            d.pop("exchange_reported")
        )

        cryptocurrency_market_pairs_latest_market_pair_quote_object = cls(
            exchange_reported=exchange_reported,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CryptocurrencyMarketPairsLatestMarketPairQuote.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        cryptocurrency_market_pairs_latest_market_pair_quote_object.additional_properties = additional_properties
        return cryptocurrency_market_pairs_latest_market_pair_quote_object

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> CryptocurrencyMarketPairsLatestMarketPairQuote:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: CryptocurrencyMarketPairsLatestMarketPairQuote) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
