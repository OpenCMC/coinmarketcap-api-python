from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenPriceDTO")


@_attrs_define
class TokenPriceDTO:
    """Token price information

    Attributes:
        pid (int | Unset): Platform ID
        pdex (str | Unset): Platform dexer name
        pcid (int | Unset): Platform crypto ID
        a (str | Unset): Token address
        n (str | Unset): Token name
        sym (str | Unset): Token symbol
        lg (str | Unset): Logo URL
        p (float | Unset): Current price (USD)
        pc1h (float | Unset): Price change in last 1 hour (percentage)
        pc24h (float | Unset): Price change in last 24 hours (percentage)
        pc7d (float | Unset): Price change in last 7 days (percentage)
        v24h (float | Unset): 24-hour trading volume (USD)
        l (float | Unset): Liquidity (USD)
        ts (int | Unset): Timestamp of price data
        mc (float | Unset): Market cap
    """

    pid: int | Unset = UNSET
    pdex: str | Unset = UNSET
    pcid: int | Unset = UNSET
    a: str | Unset = UNSET
    n: str | Unset = UNSET
    sym: str | Unset = UNSET
    lg: str | Unset = UNSET
    p: float | Unset = UNSET
    pc1h: float | Unset = UNSET
    pc24h: float | Unset = UNSET
    pc7d: float | Unset = UNSET
    v24h: float | Unset = UNSET
    l: float | Unset = UNSET
    ts: int | Unset = UNSET
    mc: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pid = self.pid

        pdex = self.pdex

        pcid = self.pcid

        a = self.a

        n = self.n

        sym = self.sym

        lg = self.lg

        p = self.p

        pc1h = self.pc1h

        pc24h = self.pc24h

        pc7d = self.pc7d

        v24h = self.v24h

        l = self.l

        ts = self.ts

        mc = self.mc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pid is not UNSET:
            field_dict["pid"] = pid
        if pdex is not UNSET:
            field_dict["pdex"] = pdex
        if pcid is not UNSET:
            field_dict["pcid"] = pcid
        if a is not UNSET:
            field_dict["a"] = a
        if n is not UNSET:
            field_dict["n"] = n
        if sym is not UNSET:
            field_dict["sym"] = sym
        if lg is not UNSET:
            field_dict["lg"] = lg
        if p is not UNSET:
            field_dict["p"] = p
        if pc1h is not UNSET:
            field_dict["pc1h"] = pc1h
        if pc24h is not UNSET:
            field_dict["pc24h"] = pc24h
        if pc7d is not UNSET:
            field_dict["pc7d"] = pc7d
        if v24h is not UNSET:
            field_dict["v24h"] = v24h
        if l is not UNSET:
            field_dict["l"] = l
        if ts is not UNSET:
            field_dict["ts"] = ts
        if mc is not UNSET:
            field_dict["mc"] = mc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pid = d.pop("pid", UNSET)

        pdex = d.pop("pdex", UNSET)

        pcid = d.pop("pcid", UNSET)

        a = d.pop("a", UNSET)

        n = d.pop("n", UNSET)

        sym = d.pop("sym", UNSET)

        lg = d.pop("lg", UNSET)

        p = d.pop("p", UNSET)

        pc1h = d.pop("pc1h", UNSET)

        pc24h = d.pop("pc24h", UNSET)

        pc7d = d.pop("pc7d", UNSET)

        v24h = d.pop("v24h", UNSET)

        l = d.pop("l", UNSET)

        ts = d.pop("ts", UNSET)

        mc = d.pop("mc", UNSET)

        token_price_dto = cls(
            pid=pid,
            pdex=pdex,
            pcid=pcid,
            a=a,
            n=n,
            sym=sym,
            lg=lg,
            p=p,
            pc1h=pc1h,
            pc24h=pc24h,
            pc7d=pc7d,
            v24h=v24h,
            l=l,
            ts=ts,
            mc=mc,
        )

        token_price_dto.additional_properties = d
        return token_price_dto

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
