from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemeCoinFilterDTO")


@_attrs_define
class MemeCoinFilterDTO:
    """Filter criteria for meme coins

    Attributes:
        top_holders_less_than (bool | Unset): Whether top holders collectively hold less than a certain threshold
        dev_sold_all (bool | Unset): Whether the developer has sold all of their tokens
        dev_still_holding (bool | Unset): dev still holding
        social (bool | Unset): Whether the token has social media presence
        min_age (int | Unset): Minimum token age in minutes (≥0)
        max_age (int | Unset): Maximum token age in minutes (≥0)
        min_market_cap (float | Unset): Minimum market cap in USD (≥0)
        max_market_cap (float | Unset): Maximum market cap in USD (≥0)
        min_liquidity (float | Unset): Minimum liquidity value in USD (≥0)
        max_liquidity (float | Unset): Maximum liquidity value in USD (≥0)
        min_bonding_curve (float | Unset): Minimum bonding curve value (≥0)
        max_bonding_curve (float | Unset): Maximum bonding curve value (≥0)
        min_dev_holding (float | Unset): Minimum DEX holding amount (≥0)
        max_dev_holding (float | Unset): Maximum DEX holding amount (≥0)
        min_holders (int | Unset): Minimum number of token holders (≥0)
        max_holders (int | Unset): Maximum number of token holders (≥0)
        min_volume (float | Unset): Minimum trading volume (≥0)
        max_volume (float | Unset): Maximum trading volume (≥0)
        min_txns (int | Unset): Minimum 24h transaction count (≥0)
        max_txns (int | Unset): Maximum 24h transaction count (≥0)
        min_buys (int | Unset): Minimum 24h buy transaction count (≥0)
        max_buys (int | Unset): Maximum 24h buy transaction count (≥0)
        min_sells (int | Unset): Minimum 24h sell transaction count (≥0)
        max_sells (int | Unset): Maximum 24h sell transaction count (≥0)
        min_top_10_holding (float | Unset): Minimum Top10Holding (≥0)
        max_top_10_holding (float | Unset): Maximum Top10Holding (≥0)
        min_snipers (float | Unset): Minimum Snipers (≥0)
        max_snipers (float | Unset): Maximum Snipers (≥0)
        min_insiders (float | Unset): Minimum Insiders (≥0)
        max_insiders (float | Unset): Maximum Insiders (≥0)
    """

    top_holders_less_than: bool | Unset = UNSET
    dev_sold_all: bool | Unset = UNSET
    dev_still_holding: bool | Unset = UNSET
    social: bool | Unset = UNSET
    min_age: int | Unset = UNSET
    max_age: int | Unset = UNSET
    min_market_cap: float | Unset = UNSET
    max_market_cap: float | Unset = UNSET
    min_liquidity: float | Unset = UNSET
    max_liquidity: float | Unset = UNSET
    min_bonding_curve: float | Unset = UNSET
    max_bonding_curve: float | Unset = UNSET
    min_dev_holding: float | Unset = UNSET
    max_dev_holding: float | Unset = UNSET
    min_holders: int | Unset = UNSET
    max_holders: int | Unset = UNSET
    min_volume: float | Unset = UNSET
    max_volume: float | Unset = UNSET
    min_txns: int | Unset = UNSET
    max_txns: int | Unset = UNSET
    min_buys: int | Unset = UNSET
    max_buys: int | Unset = UNSET
    min_sells: int | Unset = UNSET
    max_sells: int | Unset = UNSET
    min_top_10_holding: float | Unset = UNSET
    max_top_10_holding: float | Unset = UNSET
    min_snipers: float | Unset = UNSET
    max_snipers: float | Unset = UNSET
    min_insiders: float | Unset = UNSET
    max_insiders: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        top_holders_less_than = self.top_holders_less_than

        dev_sold_all = self.dev_sold_all

        dev_still_holding = self.dev_still_holding

        social = self.social

        min_age = self.min_age

        max_age = self.max_age

        min_market_cap = self.min_market_cap

        max_market_cap = self.max_market_cap

        min_liquidity = self.min_liquidity

        max_liquidity = self.max_liquidity

        min_bonding_curve = self.min_bonding_curve

        max_bonding_curve = self.max_bonding_curve

        min_dev_holding = self.min_dev_holding

        max_dev_holding = self.max_dev_holding

        min_holders = self.min_holders

        max_holders = self.max_holders

        min_volume = self.min_volume

        max_volume = self.max_volume

        min_txns = self.min_txns

        max_txns = self.max_txns

        min_buys = self.min_buys

        max_buys = self.max_buys

        min_sells = self.min_sells

        max_sells = self.max_sells

        min_top_10_holding = self.min_top_10_holding

        max_top_10_holding = self.max_top_10_holding

        min_snipers = self.min_snipers

        max_snipers = self.max_snipers

        min_insiders = self.min_insiders

        max_insiders = self.max_insiders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if top_holders_less_than is not UNSET:
            field_dict["topHoldersLessThan"] = top_holders_less_than
        if dev_sold_all is not UNSET:
            field_dict["devSoldAll"] = dev_sold_all
        if dev_still_holding is not UNSET:
            field_dict["devStillHolding"] = dev_still_holding
        if social is not UNSET:
            field_dict["social"] = social
        if min_age is not UNSET:
            field_dict["minAge"] = min_age
        if max_age is not UNSET:
            field_dict["maxAge"] = max_age
        if min_market_cap is not UNSET:
            field_dict["minMarketCap"] = min_market_cap
        if max_market_cap is not UNSET:
            field_dict["maxMarketCap"] = max_market_cap
        if min_liquidity is not UNSET:
            field_dict["minLiquidity"] = min_liquidity
        if max_liquidity is not UNSET:
            field_dict["maxLiquidity"] = max_liquidity
        if min_bonding_curve is not UNSET:
            field_dict["minBondingCurve"] = min_bonding_curve
        if max_bonding_curve is not UNSET:
            field_dict["maxBondingCurve"] = max_bonding_curve
        if min_dev_holding is not UNSET:
            field_dict["minDevHolding"] = min_dev_holding
        if max_dev_holding is not UNSET:
            field_dict["maxDevHolding"] = max_dev_holding
        if min_holders is not UNSET:
            field_dict["minHolders"] = min_holders
        if max_holders is not UNSET:
            field_dict["maxHolders"] = max_holders
        if min_volume is not UNSET:
            field_dict["minVolume"] = min_volume
        if max_volume is not UNSET:
            field_dict["maxVolume"] = max_volume
        if min_txns is not UNSET:
            field_dict["minTxns"] = min_txns
        if max_txns is not UNSET:
            field_dict["maxTxns"] = max_txns
        if min_buys is not UNSET:
            field_dict["minBuys"] = min_buys
        if max_buys is not UNSET:
            field_dict["maxBuys"] = max_buys
        if min_sells is not UNSET:
            field_dict["minSells"] = min_sells
        if max_sells is not UNSET:
            field_dict["maxSells"] = max_sells
        if min_top_10_holding is not UNSET:
            field_dict["minTop10Holding"] = min_top_10_holding
        if max_top_10_holding is not UNSET:
            field_dict["maxTop10Holding"] = max_top_10_holding
        if min_snipers is not UNSET:
            field_dict["minSnipers"] = min_snipers
        if max_snipers is not UNSET:
            field_dict["maxSnipers"] = max_snipers
        if min_insiders is not UNSET:
            field_dict["minInsiders"] = min_insiders
        if max_insiders is not UNSET:
            field_dict["maxInsiders"] = max_insiders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        top_holders_less_than = d.pop("topHoldersLessThan", UNSET)

        dev_sold_all = d.pop("devSoldAll", UNSET)

        dev_still_holding = d.pop("devStillHolding", UNSET)

        social = d.pop("social", UNSET)

        min_age = d.pop("minAge", UNSET)

        max_age = d.pop("maxAge", UNSET)

        min_market_cap = d.pop("minMarketCap", UNSET)

        max_market_cap = d.pop("maxMarketCap", UNSET)

        min_liquidity = d.pop("minLiquidity", UNSET)

        max_liquidity = d.pop("maxLiquidity", UNSET)

        min_bonding_curve = d.pop("minBondingCurve", UNSET)

        max_bonding_curve = d.pop("maxBondingCurve", UNSET)

        min_dev_holding = d.pop("minDevHolding", UNSET)

        max_dev_holding = d.pop("maxDevHolding", UNSET)

        min_holders = d.pop("minHolders", UNSET)

        max_holders = d.pop("maxHolders", UNSET)

        min_volume = d.pop("minVolume", UNSET)

        max_volume = d.pop("maxVolume", UNSET)

        min_txns = d.pop("minTxns", UNSET)

        max_txns = d.pop("maxTxns", UNSET)

        min_buys = d.pop("minBuys", UNSET)

        max_buys = d.pop("maxBuys", UNSET)

        min_sells = d.pop("minSells", UNSET)

        max_sells = d.pop("maxSells", UNSET)

        min_top_10_holding = d.pop("minTop10Holding", UNSET)

        max_top_10_holding = d.pop("maxTop10Holding", UNSET)

        min_snipers = d.pop("minSnipers", UNSET)

        max_snipers = d.pop("maxSnipers", UNSET)

        min_insiders = d.pop("minInsiders", UNSET)

        max_insiders = d.pop("maxInsiders", UNSET)

        meme_coin_filter_dto = cls(
            top_holders_less_than=top_holders_less_than,
            dev_sold_all=dev_sold_all,
            dev_still_holding=dev_still_holding,
            social=social,
            min_age=min_age,
            max_age=max_age,
            min_market_cap=min_market_cap,
            max_market_cap=max_market_cap,
            min_liquidity=min_liquidity,
            max_liquidity=max_liquidity,
            min_bonding_curve=min_bonding_curve,
            max_bonding_curve=max_bonding_curve,
            min_dev_holding=min_dev_holding,
            max_dev_holding=max_dev_holding,
            min_holders=min_holders,
            max_holders=max_holders,
            min_volume=min_volume,
            max_volume=max_volume,
            min_txns=min_txns,
            max_txns=max_txns,
            min_buys=min_buys,
            max_buys=max_buys,
            min_sells=min_sells,
            max_sells=max_sells,
            min_top_10_holding=min_top_10_holding,
            max_top_10_holding=max_top_10_holding,
            min_snipers=min_snipers,
            max_snipers=max_snipers,
            min_insiders=min_insiders,
            max_insiders=max_insiders,
        )

        meme_coin_filter_dto.additional_properties = d
        return meme_coin_filter_dto

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
