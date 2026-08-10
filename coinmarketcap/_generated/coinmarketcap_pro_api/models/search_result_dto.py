from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchResultDTO")


@_attrs_define
class SearchResultDTO:
    """
    Attributes:
        plt_id (int | Unset):
        plt (str | Unset):
        plti (int | Unset):
        n (str | Unset):
        s (str | Unset):
        addr (str | Unset):
        pt (int | Unset):
        lt (int | Unset):
        w (str | Unset):
        x (str | Unset):
        l (str | Unset):
        pu (str | Unset):
        pc24h (float | Unset):
        dec (int | Unset):
        tsup (str | Unset):
        fpt (int | Unset):
        fpct (int | Unset):
        v24h (float | Unset):
        fdv (float | Unset):
        mc (float | Unset):
        liq (float | Unset):
        ts (int | Unset):
        lf (int | Unset):
        cid (int | Unset):
        bn_cid (str | Unset):
        ut24h (int | Unset):
        ecs (int | Unset): Binance exclusive code, 1 - exclusive
        ssc (float | Unset): Search relevance score
        pin (str | Unset): Comma-separated pinned types based on sort fields: ido,alpha,trending or null
    """

    plt_id: int | Unset = UNSET
    plt: str | Unset = UNSET
    plti: int | Unset = UNSET
    n: str | Unset = UNSET
    s: str | Unset = UNSET
    addr: str | Unset = UNSET
    pt: int | Unset = UNSET
    lt: int | Unset = UNSET
    w: str | Unset = UNSET
    x: str | Unset = UNSET
    l: str | Unset = UNSET
    pu: str | Unset = UNSET
    pc24h: float | Unset = UNSET
    dec: int | Unset = UNSET
    tsup: str | Unset = UNSET
    fpt: int | Unset = UNSET
    fpct: int | Unset = UNSET
    v24h: float | Unset = UNSET
    fdv: float | Unset = UNSET
    mc: float | Unset = UNSET
    liq: float | Unset = UNSET
    ts: int | Unset = UNSET
    lf: int | Unset = UNSET
    cid: int | Unset = UNSET
    bn_cid: str | Unset = UNSET
    ut24h: int | Unset = UNSET
    ecs: int | Unset = UNSET
    ssc: float | Unset = UNSET
    pin: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plt_id = self.plt_id

        plt = self.plt

        plti = self.plti

        n = self.n

        s = self.s

        addr = self.addr

        pt = self.pt

        lt = self.lt

        w = self.w

        x = self.x

        l = self.l

        pu = self.pu

        pc24h = self.pc24h

        dec = self.dec

        tsup = self.tsup

        fpt = self.fpt

        fpct = self.fpct

        v24h = self.v24h

        fdv = self.fdv

        mc = self.mc

        liq = self.liq

        ts = self.ts

        lf = self.lf

        cid = self.cid

        bn_cid = self.bn_cid

        ut24h = self.ut24h

        ecs = self.ecs

        ssc = self.ssc

        pin = self.pin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plt_id is not UNSET:
            field_dict["pltId"] = plt_id
        if plt is not UNSET:
            field_dict["plt"] = plt
        if plti is not UNSET:
            field_dict["plti"] = plti
        if n is not UNSET:
            field_dict["n"] = n
        if s is not UNSET:
            field_dict["s"] = s
        if addr is not UNSET:
            field_dict["addr"] = addr
        if pt is not UNSET:
            field_dict["pt"] = pt
        if lt is not UNSET:
            field_dict["lt"] = lt
        if w is not UNSET:
            field_dict["w"] = w
        if x is not UNSET:
            field_dict["x"] = x
        if l is not UNSET:
            field_dict["l"] = l
        if pu is not UNSET:
            field_dict["pu"] = pu
        if pc24h is not UNSET:
            field_dict["pc24h"] = pc24h
        if dec is not UNSET:
            field_dict["dec"] = dec
        if tsup is not UNSET:
            field_dict["tsup"] = tsup
        if fpt is not UNSET:
            field_dict["fpt"] = fpt
        if fpct is not UNSET:
            field_dict["fpct"] = fpct
        if v24h is not UNSET:
            field_dict["v24h"] = v24h
        if fdv is not UNSET:
            field_dict["fdv"] = fdv
        if mc is not UNSET:
            field_dict["mc"] = mc
        if liq is not UNSET:
            field_dict["liq"] = liq
        if ts is not UNSET:
            field_dict["ts"] = ts
        if lf is not UNSET:
            field_dict["lf"] = lf
        if cid is not UNSET:
            field_dict["cid"] = cid
        if bn_cid is not UNSET:
            field_dict["bnCid"] = bn_cid
        if ut24h is not UNSET:
            field_dict["ut24h"] = ut24h
        if ecs is not UNSET:
            field_dict["ecs"] = ecs
        if ssc is not UNSET:
            field_dict["ssc"] = ssc
        if pin is not UNSET:
            field_dict["pin"] = pin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        plt_id = d.pop("pltId", UNSET)

        plt = d.pop("plt", UNSET)

        plti = d.pop("plti", UNSET)

        n = d.pop("n", UNSET)

        s = d.pop("s", UNSET)

        addr = d.pop("addr", UNSET)

        pt = d.pop("pt", UNSET)

        lt = d.pop("lt", UNSET)

        w = d.pop("w", UNSET)

        x = d.pop("x", UNSET)

        l = d.pop("l", UNSET)

        pu = d.pop("pu", UNSET)

        pc24h = d.pop("pc24h", UNSET)

        dec = d.pop("dec", UNSET)

        tsup = d.pop("tsup", UNSET)

        fpt = d.pop("fpt", UNSET)

        fpct = d.pop("fpct", UNSET)

        v24h = d.pop("v24h", UNSET)

        fdv = d.pop("fdv", UNSET)

        mc = d.pop("mc", UNSET)

        liq = d.pop("liq", UNSET)

        ts = d.pop("ts", UNSET)

        lf = d.pop("lf", UNSET)

        cid = d.pop("cid", UNSET)

        bn_cid = d.pop("bnCid", UNSET)

        ut24h = d.pop("ut24h", UNSET)

        ecs = d.pop("ecs", UNSET)

        ssc = d.pop("ssc", UNSET)

        pin = d.pop("pin", UNSET)

        search_result_dto = cls(
            plt_id=plt_id,
            plt=plt,
            plti=plti,
            n=n,
            s=s,
            addr=addr,
            pt=pt,
            lt=lt,
            w=w,
            x=x,
            l=l,
            pu=pu,
            pc24h=pc24h,
            dec=dec,
            tsup=tsup,
            fpt=fpt,
            fpct=fpct,
            v24h=v24h,
            fdv=fdv,
            mc=mc,
            liq=liq,
            ts=ts,
            lf=lf,
            cid=cid,
            bn_cid=bn_cid,
            ut24h=ut24h,
            ecs=ecs,
            ssc=ssc,
            pin=pin,
        )

        search_result_dto.additional_properties = d
        return search_result_dto

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
