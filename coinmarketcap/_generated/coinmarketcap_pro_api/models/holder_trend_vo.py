from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HolderTrendVO")


@_attrs_define
class HolderTrendVO:
    """
    Attributes:
        ts (int | Unset):
        end_ts (int | Unset):
        platform (int | Unset):
        token_address (str | Unset):
        holders (int | Unset):
        holding_ratio_of_top_100 (str | Unset):
        holding_ratio_of_top_50 (str | Unset):
        holding_ratio_of_top_10 (str | Unset):
        total_balance_of_top_100 (str | Unset):
        total_balance_of_top_50 (str | Unset):
        total_balance_of_top_10 (str | Unset):
        bigger_than_10d_holders (int | Unset):
        avg_balance_all_holders (str | Unset):
        avg_balance_of_top_100 (str | Unset):
        avg_position_cost_of_top_100 (str | Unset):
        avg_sell_price_of_top_100 (str | Unset):
        tag_holder (str | Unset):
        avg_balance_usd_all_holders (str | Unset):
        avg_balance_usd_of_top_100 (str | Unset):
        tag_holder_tthm (str | Unset):
        price (str | Unset):
    """

    ts: int | Unset = UNSET
    end_ts: int | Unset = UNSET
    platform: int | Unset = UNSET
    token_address: str | Unset = UNSET
    holders: int | Unset = UNSET
    holding_ratio_of_top_100: str | Unset = UNSET
    holding_ratio_of_top_50: str | Unset = UNSET
    holding_ratio_of_top_10: str | Unset = UNSET
    total_balance_of_top_100: str | Unset = UNSET
    total_balance_of_top_50: str | Unset = UNSET
    total_balance_of_top_10: str | Unset = UNSET
    bigger_than_10d_holders: int | Unset = UNSET
    avg_balance_all_holders: str | Unset = UNSET
    avg_balance_of_top_100: str | Unset = UNSET
    avg_position_cost_of_top_100: str | Unset = UNSET
    avg_sell_price_of_top_100: str | Unset = UNSET
    tag_holder: str | Unset = UNSET
    avg_balance_usd_all_holders: str | Unset = UNSET
    avg_balance_usd_of_top_100: str | Unset = UNSET
    tag_holder_tthm: str | Unset = UNSET
    price: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ts = self.ts

        end_ts = self.end_ts

        platform = self.platform

        token_address = self.token_address

        holders = self.holders

        holding_ratio_of_top_100 = self.holding_ratio_of_top_100

        holding_ratio_of_top_50 = self.holding_ratio_of_top_50

        holding_ratio_of_top_10 = self.holding_ratio_of_top_10

        total_balance_of_top_100 = self.total_balance_of_top_100

        total_balance_of_top_50 = self.total_balance_of_top_50

        total_balance_of_top_10 = self.total_balance_of_top_10

        bigger_than_10d_holders = self.bigger_than_10d_holders

        avg_balance_all_holders = self.avg_balance_all_holders

        avg_balance_of_top_100 = self.avg_balance_of_top_100

        avg_position_cost_of_top_100 = self.avg_position_cost_of_top_100

        avg_sell_price_of_top_100 = self.avg_sell_price_of_top_100

        tag_holder = self.tag_holder

        avg_balance_usd_all_holders = self.avg_balance_usd_all_holders

        avg_balance_usd_of_top_100 = self.avg_balance_usd_of_top_100

        tag_holder_tthm = self.tag_holder_tthm

        price = self.price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ts is not UNSET:
            field_dict["ts"] = ts
        if end_ts is not UNSET:
            field_dict["endTs"] = end_ts
        if platform is not UNSET:
            field_dict["platform"] = platform
        if token_address is not UNSET:
            field_dict["tokenAddress"] = token_address
        if holders is not UNSET:
            field_dict["holders"] = holders
        if holding_ratio_of_top_100 is not UNSET:
            field_dict["holdingRatioOfTop100"] = holding_ratio_of_top_100
        if holding_ratio_of_top_50 is not UNSET:
            field_dict["holdingRatioOfTop50"] = holding_ratio_of_top_50
        if holding_ratio_of_top_10 is not UNSET:
            field_dict["holdingRatioOfTop10"] = holding_ratio_of_top_10
        if total_balance_of_top_100 is not UNSET:
            field_dict["totalBalanceOfTop100"] = total_balance_of_top_100
        if total_balance_of_top_50 is not UNSET:
            field_dict["totalBalanceOfTop50"] = total_balance_of_top_50
        if total_balance_of_top_10 is not UNSET:
            field_dict["totalBalanceOfTop10"] = total_balance_of_top_10
        if bigger_than_10d_holders is not UNSET:
            field_dict["biggerThan10DHolders"] = bigger_than_10d_holders
        if avg_balance_all_holders is not UNSET:
            field_dict["avgBalanceAllHolders"] = avg_balance_all_holders
        if avg_balance_of_top_100 is not UNSET:
            field_dict["avgBalanceOfTop100"] = avg_balance_of_top_100
        if avg_position_cost_of_top_100 is not UNSET:
            field_dict["avgPositionCostOfTop100"] = avg_position_cost_of_top_100
        if avg_sell_price_of_top_100 is not UNSET:
            field_dict["avgSellPriceOfTop100"] = avg_sell_price_of_top_100
        if tag_holder is not UNSET:
            field_dict["tagHolder"] = tag_holder
        if avg_balance_usd_all_holders is not UNSET:
            field_dict["avgBalanceUSDAllHolders"] = avg_balance_usd_all_holders
        if avg_balance_usd_of_top_100 is not UNSET:
            field_dict["avgBalanceUSDOfTop100"] = avg_balance_usd_of_top_100
        if tag_holder_tthm is not UNSET:
            field_dict["tagHolderTTHM"] = tag_holder_tthm
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ts = d.pop("ts", UNSET)

        end_ts = d.pop("endTs", UNSET)

        platform = d.pop("platform", UNSET)

        token_address = d.pop("tokenAddress", UNSET)

        holders = d.pop("holders", UNSET)

        holding_ratio_of_top_100 = d.pop("holdingRatioOfTop100", UNSET)

        holding_ratio_of_top_50 = d.pop("holdingRatioOfTop50", UNSET)

        holding_ratio_of_top_10 = d.pop("holdingRatioOfTop10", UNSET)

        total_balance_of_top_100 = d.pop("totalBalanceOfTop100", UNSET)

        total_balance_of_top_50 = d.pop("totalBalanceOfTop50", UNSET)

        total_balance_of_top_10 = d.pop("totalBalanceOfTop10", UNSET)

        bigger_than_10d_holders = d.pop("biggerThan10DHolders", UNSET)

        avg_balance_all_holders = d.pop("avgBalanceAllHolders", UNSET)

        avg_balance_of_top_100 = d.pop("avgBalanceOfTop100", UNSET)

        avg_position_cost_of_top_100 = d.pop("avgPositionCostOfTop100", UNSET)

        avg_sell_price_of_top_100 = d.pop("avgSellPriceOfTop100", UNSET)

        tag_holder = d.pop("tagHolder", UNSET)

        avg_balance_usd_all_holders = d.pop("avgBalanceUSDAllHolders", UNSET)

        avg_balance_usd_of_top_100 = d.pop("avgBalanceUSDOfTop100", UNSET)

        tag_holder_tthm = d.pop("tagHolderTTHM", UNSET)

        price = d.pop("price", UNSET)

        holder_trend_vo = cls(
            ts=ts,
            end_ts=end_ts,
            platform=platform,
            token_address=token_address,
            holders=holders,
            holding_ratio_of_top_100=holding_ratio_of_top_100,
            holding_ratio_of_top_50=holding_ratio_of_top_50,
            holding_ratio_of_top_10=holding_ratio_of_top_10,
            total_balance_of_top_100=total_balance_of_top_100,
            total_balance_of_top_50=total_balance_of_top_50,
            total_balance_of_top_10=total_balance_of_top_10,
            bigger_than_10d_holders=bigger_than_10d_holders,
            avg_balance_all_holders=avg_balance_all_holders,
            avg_balance_of_top_100=avg_balance_of_top_100,
            avg_position_cost_of_top_100=avg_position_cost_of_top_100,
            avg_sell_price_of_top_100=avg_sell_price_of_top_100,
            tag_holder=tag_holder,
            avg_balance_usd_all_holders=avg_balance_usd_all_holders,
            avg_balance_usd_of_top_100=avg_balance_usd_of_top_100,
            tag_holder_tthm=tag_holder_tthm,
            price=price,
        )

        holder_trend_vo.additional_properties = d
        return holder_trend_vo

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
