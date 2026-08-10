from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.leaderboard_filter_dto_boost_type import (
    LeaderboardFilterDTOBoostType,
    check_leaderboard_filter_dto_boost_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.range_filter_dto import RangeFilterDto


T = TypeVar("T", bound="LeaderboardFilterDTO")


@_attrs_define
class LeaderboardFilterDTO:
    """The request parameters for querying the token leaderboard

    Attributes:
        hide_four_meme (bool | Unset): Whether to hide four.meme tokens
        hide_pump_fun (bool | Unset): Whether to hide PumpFun tokens
        hide_moonshot (bool | Unset): Whether to hide Moonshot tokens
        audit_passed (bool | Unset): Only include tokens that passed audit
        social (bool | Unset): Only include tokens with social media presence
        min_age (int | Unset): Minimum token age in minutes
        max_age (int | Unset): Maximum token age in minutes
        min_market_cap (float | Unset): Minimum market cap (USD)
        max_market_cap (float | Unset): Maximum market cap (USD)
        min_liquidity (float | Unset): Minimum liquidity (USD)
        max_liquidity (float | Unset): Maximum liquidity (USD)
        volume (list[RangeFilterDto] | Unset): Volume filter ranges (e.g. 1000~5000)
        txns (list[RangeFilterDto] | Unset): Transaction count filter ranges
        buys (list[RangeFilterDto] | Unset): Buy count filter ranges
        sells (list[RangeFilterDto] | Unset): Sell count filter ranges
        price_change (list[RangeFilterDto] | Unset): Price range filter ranges
        boost_type (LeaderboardFilterDTOBoostType | Unset): Boost filter type
        all_fields_empty (bool | Unset):
    """

    hide_four_meme: bool | Unset = UNSET
    hide_pump_fun: bool | Unset = UNSET
    hide_moonshot: bool | Unset = UNSET
    audit_passed: bool | Unset = UNSET
    social: bool | Unset = UNSET
    min_age: int | Unset = UNSET
    max_age: int | Unset = UNSET
    min_market_cap: float | Unset = UNSET
    max_market_cap: float | Unset = UNSET
    min_liquidity: float | Unset = UNSET
    max_liquidity: float | Unset = UNSET
    volume: list[RangeFilterDto] | Unset = UNSET
    txns: list[RangeFilterDto] | Unset = UNSET
    buys: list[RangeFilterDto] | Unset = UNSET
    sells: list[RangeFilterDto] | Unset = UNSET
    price_change: list[RangeFilterDto] | Unset = UNSET
    boost_type: LeaderboardFilterDTOBoostType | Unset = UNSET
    all_fields_empty: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hide_four_meme = self.hide_four_meme

        hide_pump_fun = self.hide_pump_fun

        hide_moonshot = self.hide_moonshot

        audit_passed = self.audit_passed

        social = self.social

        min_age = self.min_age

        max_age = self.max_age

        min_market_cap = self.min_market_cap

        max_market_cap = self.max_market_cap

        min_liquidity = self.min_liquidity

        max_liquidity = self.max_liquidity

        volume: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.volume, Unset):
            volume = []
            for volume_item_data in self.volume:
                volume_item = volume_item_data.to_dict()
                volume.append(volume_item)

        txns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.txns, Unset):
            txns = []
            for txns_item_data in self.txns:
                txns_item = txns_item_data.to_dict()
                txns.append(txns_item)

        buys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buys, Unset):
            buys = []
            for buys_item_data in self.buys:
                buys_item = buys_item_data.to_dict()
                buys.append(buys_item)

        sells: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sells, Unset):
            sells = []
            for sells_item_data in self.sells:
                sells_item = sells_item_data.to_dict()
                sells.append(sells_item)

        price_change: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.price_change, Unset):
            price_change = []
            for price_change_item_data in self.price_change:
                price_change_item = price_change_item_data.to_dict()
                price_change.append(price_change_item)

        boost_type: str | Unset = UNSET
        if not isinstance(self.boost_type, Unset):
            boost_type = self.boost_type

        all_fields_empty = self.all_fields_empty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hide_four_meme is not UNSET:
            field_dict["hideFourMeme"] = hide_four_meme
        if hide_pump_fun is not UNSET:
            field_dict["hidePumpFun"] = hide_pump_fun
        if hide_moonshot is not UNSET:
            field_dict["hideMoonshot"] = hide_moonshot
        if audit_passed is not UNSET:
            field_dict["auditPassed"] = audit_passed
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
        if volume is not UNSET:
            field_dict["volume"] = volume
        if txns is not UNSET:
            field_dict["txns"] = txns
        if buys is not UNSET:
            field_dict["buys"] = buys
        if sells is not UNSET:
            field_dict["sells"] = sells
        if price_change is not UNSET:
            field_dict["priceChange"] = price_change
        if boost_type is not UNSET:
            field_dict["boostType"] = boost_type
        if all_fields_empty is not UNSET:
            field_dict["allFieldsEmpty"] = all_fields_empty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.range_filter_dto import RangeFilterDto

        d = dict(src_dict)
        hide_four_meme = d.pop("hideFourMeme", UNSET)

        hide_pump_fun = d.pop("hidePumpFun", UNSET)

        hide_moonshot = d.pop("hideMoonshot", UNSET)

        audit_passed = d.pop("auditPassed", UNSET)

        social = d.pop("social", UNSET)

        min_age = d.pop("minAge", UNSET)

        max_age = d.pop("maxAge", UNSET)

        min_market_cap = d.pop("minMarketCap", UNSET)

        max_market_cap = d.pop("maxMarketCap", UNSET)

        min_liquidity = d.pop("minLiquidity", UNSET)

        max_liquidity = d.pop("maxLiquidity", UNSET)

        _volume = d.pop("volume", UNSET)
        volume: list[RangeFilterDto] | Unset = UNSET
        if _volume is not UNSET:
            volume = []
            for volume_item_data in _volume:
                volume_item = RangeFilterDto.from_dict(volume_item_data)

                volume.append(volume_item)

        _txns = d.pop("txns", UNSET)
        txns: list[RangeFilterDto] | Unset = UNSET
        if _txns is not UNSET:
            txns = []
            for txns_item_data in _txns:
                txns_item = RangeFilterDto.from_dict(txns_item_data)

                txns.append(txns_item)

        _buys = d.pop("buys", UNSET)
        buys: list[RangeFilterDto] | Unset = UNSET
        if _buys is not UNSET:
            buys = []
            for buys_item_data in _buys:
                buys_item = RangeFilterDto.from_dict(buys_item_data)

                buys.append(buys_item)

        _sells = d.pop("sells", UNSET)
        sells: list[RangeFilterDto] | Unset = UNSET
        if _sells is not UNSET:
            sells = []
            for sells_item_data in _sells:
                sells_item = RangeFilterDto.from_dict(sells_item_data)

                sells.append(sells_item)

        _price_change = d.pop("priceChange", UNSET)
        price_change: list[RangeFilterDto] | Unset = UNSET
        if _price_change is not UNSET:
            price_change = []
            for price_change_item_data in _price_change:
                price_change_item = RangeFilterDto.from_dict(price_change_item_data)

                price_change.append(price_change_item)

        _boost_type = d.pop("boostType", UNSET)
        boost_type: LeaderboardFilterDTOBoostType | Unset
        if isinstance(_boost_type, Unset):
            boost_type = UNSET
        else:
            boost_type = check_leaderboard_filter_dto_boost_type(_boost_type)

        all_fields_empty = d.pop("allFieldsEmpty", UNSET)

        leaderboard_filter_dto = cls(
            hide_four_meme=hide_four_meme,
            hide_pump_fun=hide_pump_fun,
            hide_moonshot=hide_moonshot,
            audit_passed=audit_passed,
            social=social,
            min_age=min_age,
            max_age=max_age,
            min_market_cap=min_market_cap,
            max_market_cap=max_market_cap,
            min_liquidity=min_liquidity,
            max_liquidity=max_liquidity,
            volume=volume,
            txns=txns,
            buys=buys,
            sells=sells,
            price_change=price_change,
            boost_type=boost_type,
            all_fields_empty=all_fields_empty,
        )

        leaderboard_filter_dto.additional_properties = d
        return leaderboard_filter_dto

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
