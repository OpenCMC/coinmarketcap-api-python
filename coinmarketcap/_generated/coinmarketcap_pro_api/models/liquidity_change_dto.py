from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LiquidityChangeDTO")


@_attrs_define
class LiquidityChangeDTO:
    """List of liquidity change transactions

    Attributes:
        ts (int | Unset):
        tp (str | Unset):
        eid (int | Unset): exchange id
        en (str | Unset): exchange name
        f (str | Unset): factory address
        t0a (str | Unset): Base token address
        t1a (str | Unset): Quote token address
        t0s (str | Unset):
        t1s (str | Unset):
        a0 (float | Unset):
        a1 (float | Unset):
        tu (float | Unset):
        m (str | Unset):
        txn (str | Unset):
        h (int | Unset):
        tx_id (int | Unset):
        lgid (int | Unset):
    """

    ts: int | Unset = UNSET
    tp: str | Unset = UNSET
    eid: int | Unset = UNSET
    en: str | Unset = UNSET
    f: str | Unset = UNSET
    t0a: str | Unset = UNSET
    t1a: str | Unset = UNSET
    t0s: str | Unset = UNSET
    t1s: str | Unset = UNSET
    a0: float | Unset = UNSET
    a1: float | Unset = UNSET
    tu: float | Unset = UNSET
    m: str | Unset = UNSET
    txn: str | Unset = UNSET
    h: int | Unset = UNSET
    tx_id: int | Unset = UNSET
    lgid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ts = self.ts

        tp = self.tp

        eid = self.eid

        en = self.en

        f = self.f

        t0a = self.t0a

        t1a = self.t1a

        t0s = self.t0s

        t1s = self.t1s

        a0 = self.a0

        a1 = self.a1

        tu = self.tu

        m = self.m

        txn = self.txn

        h = self.h

        tx_id = self.tx_id

        lgid = self.lgid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ts is not UNSET:
            field_dict["ts"] = ts
        if tp is not UNSET:
            field_dict["tp"] = tp
        if eid is not UNSET:
            field_dict["eid"] = eid
        if en is not UNSET:
            field_dict["en"] = en
        if f is not UNSET:
            field_dict["f"] = f
        if t0a is not UNSET:
            field_dict["t0a"] = t0a
        if t1a is not UNSET:
            field_dict["t1a"] = t1a
        if t0s is not UNSET:
            field_dict["t0s"] = t0s
        if t1s is not UNSET:
            field_dict["t1s"] = t1s
        if a0 is not UNSET:
            field_dict["a0"] = a0
        if a1 is not UNSET:
            field_dict["a1"] = a1
        if tu is not UNSET:
            field_dict["tu"] = tu
        if m is not UNSET:
            field_dict["m"] = m
        if txn is not UNSET:
            field_dict["txn"] = txn
        if h is not UNSET:
            field_dict["h"] = h
        if tx_id is not UNSET:
            field_dict["txId"] = tx_id
        if lgid is not UNSET:
            field_dict["lgid"] = lgid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ts = d.pop("ts", UNSET)

        tp = d.pop("tp", UNSET)

        eid = d.pop("eid", UNSET)

        en = d.pop("en", UNSET)

        f = d.pop("f", UNSET)

        t0a = d.pop("t0a", UNSET)

        t1a = d.pop("t1a", UNSET)

        t0s = d.pop("t0s", UNSET)

        t1s = d.pop("t1s", UNSET)

        a0 = d.pop("a0", UNSET)

        a1 = d.pop("a1", UNSET)

        tu = d.pop("tu", UNSET)

        m = d.pop("m", UNSET)

        txn = d.pop("txn", UNSET)

        h = d.pop("h", UNSET)

        tx_id = d.pop("txId", UNSET)

        lgid = d.pop("lgid", UNSET)

        liquidity_change_dto = cls(
            ts=ts,
            tp=tp,
            eid=eid,
            en=en,
            f=f,
            t0a=t0a,
            t1a=t1a,
            t0s=t0s,
            t1s=t1s,
            a0=a0,
            a1=a1,
            tu=tu,
            m=m,
            txn=txn,
            h=h,
            tx_id=tx_id,
            lgid=lgid,
        )

        liquidity_change_dto.additional_properties = d
        return liquidity_change_dto

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
