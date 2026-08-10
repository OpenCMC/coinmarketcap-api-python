from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemeCoinResultDTO")


@_attrs_define
class MemeCoinResultDTO:
    """List of meme coins that have graduated

    Attributes:
        plt (int | Unset): Token platform ID
        cid (str | Unset): chain platform id
        pr (int | Unset): Platform crypto id
        pn (str | Unset): Platform name
        it (str | Unset): Item link
        addr (str | Unset): Token address
        n (str | Unset): Name of the token
        sym (str | Unset): Symbol of the token
        lg (str | Unset): URL to the token's logo image
        tw (str | Unset): Twitter URL
        web (str | Unset): Official website URL
        tg (str | Unset): Telegram URL
        pt (int | Unset): Token protocol type: 1001=Pump.fun, 1002=Moonshot, 2001=Four.meme
        pub_at (int | Unset): Timestamp when the token was published, in milliseconds since epoch
        dec (int | Unset): Number of decimals
        tp (str | Unset): Total supply of the token
        bc (float | Unset): Bonding curve progress percentage (0~1)
        mcap (float | Unset): Market capitalization in USD
        liq (float | Unset): Liquidity value in USD
        vu (float | Unset): Trading volume in USD over the last 24 hours
        np (float | Unset): Native price of the token (in native currency, e.g., SOL)
        p (float | Unset): Price of the token in USD
        txs (int | Unset): Total number of transactions associated with this token
        nb (int | Unset): Number of buy transactions in the last 24 hours
        ns (int | Unset): Number of sell transactions in the last 24 hours
        htp (float | Unset): Percentage of tokens held by top 10 wallets
        hdp (float | Unset): Percentage of tokens held by developer wallets
        hsp (float | Unset): Percentage of tokens held by sniper wallets
        hip (float | Unset): Percentage of tokens held by insider wallets
        dsp (float | Unset): Percentage of tokens sold by DEX developers
        dmc (int | Unset): Number of times the token has migrated from a DEX
        ms (int | Unset): Migration status
        mt (int | Unset): Timestamp when the token was migrated, in milliseconds since epoch
        md (str | Unset): Name of the DEX where the token was migrated to
        h (int | Unset): Total number of unique token holders
        ecs (int | Unset): Binance exclusive code, 1 - exclusive
    """

    plt: int | Unset = UNSET
    cid: str | Unset = UNSET
    pr: int | Unset = UNSET
    pn: str | Unset = UNSET
    it: str | Unset = UNSET
    addr: str | Unset = UNSET
    n: str | Unset = UNSET
    sym: str | Unset = UNSET
    lg: str | Unset = UNSET
    tw: str | Unset = UNSET
    web: str | Unset = UNSET
    tg: str | Unset = UNSET
    pt: int | Unset = UNSET
    pub_at: int | Unset = UNSET
    dec: int | Unset = UNSET
    tp: str | Unset = UNSET
    bc: float | Unset = UNSET
    mcap: float | Unset = UNSET
    liq: float | Unset = UNSET
    vu: float | Unset = UNSET
    np: float | Unset = UNSET
    p: float | Unset = UNSET
    txs: int | Unset = UNSET
    nb: int | Unset = UNSET
    ns: int | Unset = UNSET
    htp: float | Unset = UNSET
    hdp: float | Unset = UNSET
    hsp: float | Unset = UNSET
    hip: float | Unset = UNSET
    dsp: float | Unset = UNSET
    dmc: int | Unset = UNSET
    ms: int | Unset = UNSET
    mt: int | Unset = UNSET
    md: str | Unset = UNSET
    h: int | Unset = UNSET
    ecs: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plt = self.plt

        cid = self.cid

        pr = self.pr

        pn = self.pn

        it = self.it

        addr = self.addr

        n = self.n

        sym = self.sym

        lg = self.lg

        tw = self.tw

        web = self.web

        tg = self.tg

        pt = self.pt

        pub_at = self.pub_at

        dec = self.dec

        tp = self.tp

        bc = self.bc

        mcap = self.mcap

        liq = self.liq

        vu = self.vu

        np = self.np

        p = self.p

        txs = self.txs

        nb = self.nb

        ns = self.ns

        htp = self.htp

        hdp = self.hdp

        hsp = self.hsp

        hip = self.hip

        dsp = self.dsp

        dmc = self.dmc

        ms = self.ms

        mt = self.mt

        md = self.md

        h = self.h

        ecs = self.ecs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plt is not UNSET:
            field_dict["plt"] = plt
        if cid is not UNSET:
            field_dict["cid"] = cid
        if pr is not UNSET:
            field_dict["pr"] = pr
        if pn is not UNSET:
            field_dict["pn"] = pn
        if it is not UNSET:
            field_dict["it"] = it
        if addr is not UNSET:
            field_dict["addr"] = addr
        if n is not UNSET:
            field_dict["n"] = n
        if sym is not UNSET:
            field_dict["sym"] = sym
        if lg is not UNSET:
            field_dict["lg"] = lg
        if tw is not UNSET:
            field_dict["tw"] = tw
        if web is not UNSET:
            field_dict["web"] = web
        if tg is not UNSET:
            field_dict["tg"] = tg
        if pt is not UNSET:
            field_dict["pt"] = pt
        if pub_at is not UNSET:
            field_dict["pubAt"] = pub_at
        if dec is not UNSET:
            field_dict["dec"] = dec
        if tp is not UNSET:
            field_dict["tp"] = tp
        if bc is not UNSET:
            field_dict["bc"] = bc
        if mcap is not UNSET:
            field_dict["mcap"] = mcap
        if liq is not UNSET:
            field_dict["liq"] = liq
        if vu is not UNSET:
            field_dict["vu"] = vu
        if np is not UNSET:
            field_dict["np"] = np
        if p is not UNSET:
            field_dict["p"] = p
        if txs is not UNSET:
            field_dict["txs"] = txs
        if nb is not UNSET:
            field_dict["nb"] = nb
        if ns is not UNSET:
            field_dict["ns"] = ns
        if htp is not UNSET:
            field_dict["htp"] = htp
        if hdp is not UNSET:
            field_dict["hdp"] = hdp
        if hsp is not UNSET:
            field_dict["hsp"] = hsp
        if hip is not UNSET:
            field_dict["hip"] = hip
        if dsp is not UNSET:
            field_dict["dsp"] = dsp
        if dmc is not UNSET:
            field_dict["dmc"] = dmc
        if ms is not UNSET:
            field_dict["ms"] = ms
        if mt is not UNSET:
            field_dict["mt"] = mt
        if md is not UNSET:
            field_dict["md"] = md
        if h is not UNSET:
            field_dict["h"] = h
        if ecs is not UNSET:
            field_dict["ecs"] = ecs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        plt = d.pop("plt", UNSET)

        cid = d.pop("cid", UNSET)

        pr = d.pop("pr", UNSET)

        pn = d.pop("pn", UNSET)

        it = d.pop("it", UNSET)

        addr = d.pop("addr", UNSET)

        n = d.pop("n", UNSET)

        sym = d.pop("sym", UNSET)

        lg = d.pop("lg", UNSET)

        tw = d.pop("tw", UNSET)

        web = d.pop("web", UNSET)

        tg = d.pop("tg", UNSET)

        pt = d.pop("pt", UNSET)

        pub_at = d.pop("pubAt", UNSET)

        dec = d.pop("dec", UNSET)

        tp = d.pop("tp", UNSET)

        bc = d.pop("bc", UNSET)

        mcap = d.pop("mcap", UNSET)

        liq = d.pop("liq", UNSET)

        vu = d.pop("vu", UNSET)

        np = d.pop("np", UNSET)

        p = d.pop("p", UNSET)

        txs = d.pop("txs", UNSET)

        nb = d.pop("nb", UNSET)

        ns = d.pop("ns", UNSET)

        htp = d.pop("htp", UNSET)

        hdp = d.pop("hdp", UNSET)

        hsp = d.pop("hsp", UNSET)

        hip = d.pop("hip", UNSET)

        dsp = d.pop("dsp", UNSET)

        dmc = d.pop("dmc", UNSET)

        ms = d.pop("ms", UNSET)

        mt = d.pop("mt", UNSET)

        md = d.pop("md", UNSET)

        h = d.pop("h", UNSET)

        ecs = d.pop("ecs", UNSET)

        meme_coin_result_dto = cls(
            plt=plt,
            cid=cid,
            pr=pr,
            pn=pn,
            it=it,
            addr=addr,
            n=n,
            sym=sym,
            lg=lg,
            tw=tw,
            web=web,
            tg=tg,
            pt=pt,
            pub_at=pub_at,
            dec=dec,
            tp=tp,
            bc=bc,
            mcap=mcap,
            liq=liq,
            vu=vu,
            np=np,
            p=p,
            txs=txs,
            nb=nb,
            ns=ns,
            htp=htp,
            hdp=hdp,
            hsp=hsp,
            hip=hip,
            dsp=dsp,
            dmc=dmc,
            ms=ms,
            mt=mt,
            md=md,
            h=h,
            ecs=ecs,
        )

        meme_coin_result_dto.additional_properties = d
        return meme_coin_result_dto

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
