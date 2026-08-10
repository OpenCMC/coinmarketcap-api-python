from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dex_token_signal_dto import DexTokenSignalDTO
    from ..models.token_stats_dto import TokenStatsDTO


T = TypeVar("T", bound="TokenLeaderboardDTO")


@_attrs_define
class TokenLeaderboardDTO:
    """Token leaderboard response DTO

    Attributes:
        n (str | Unset): Token name (n)
        sym (str | Unset): Token symbol (sym)
        addr (str | Unset): Token address (addr)
        plt (str | Unset): Token platform name (plt)
        pid (int | Unset): Token platform ID (pid)
        pdex (str | Unset): Token platform dexer name (pdex)
        pcid (int | Unset): Token platform crypto ID (pcid)
        web (str | Unset): Token website (web)
        tw (str | Unset): Twitter (tw)
        tg (str | Unset): Telegram (tg)
        lg (str | Unset): Logo URL (lg)
        pub_at (int | Unset): Publish timestamp in ms (pubAt)
        lch_at (int | Unset): Launch timestamp in ms (lchAt)
        fdv (str | Unset): Fully Diluted Valuation (fdv)
        mcap (str | Unset): Market Cap (mcap)
        liq_usd (str | Unset): Liquidity USD (liqUsd)
        liq (str | Unset): Liquidity (liq)
        hld (int | Unset): Holder count (hld)
        p (str | Unset): Price USD (p)
        np (str | Unset): native Price (np)
        pt (int | Unset): Price timestamp (pt)
        v24h (str | Unset): 24h Volume USD (v24h)
        t24h (str | Unset): 24h Transactions (t24h)
        ch24h (str | Unset): 24h Price Change (ch24h)
        thr (str | Unset): Top Holder Rate (thr)
        dhr (str | Unset): Developer Holder Rate (dhr)
        bcr (str | Unset): Bonding Curve Ratio (bcr)
        hcnt (int | Unset): Holder Count (hcnt)
        tsrc (str | Unset): token Source (src) — e.g. four.meme, pump.fun, moonshot
        sts (list[TokenStatsDTO] | Unset): Token statistics (sts)
        rl (str | Unset): Token security status
        ts (str | Unset): total supply (ts)
        bs (str | Unset): burn supply (bs)
        dec (int | Unset): decimals
        sig (DexTokenSignalDTO | Unset): Token signal
        be_score (float | Unset): Meme binance exclusive Score
        be_rank (int | Unset): Meme binance exclusive rank
        plt_a (str | Unset): Token platform acronym name
        ecs (int | Unset): Binance exclusive code, 1 - exclusive
        tags (list[str] | Unset): Token tags
    """

    n: str | Unset = UNSET
    sym: str | Unset = UNSET
    addr: str | Unset = UNSET
    plt: str | Unset = UNSET
    pid: int | Unset = UNSET
    pdex: str | Unset = UNSET
    pcid: int | Unset = UNSET
    web: str | Unset = UNSET
    tw: str | Unset = UNSET
    tg: str | Unset = UNSET
    lg: str | Unset = UNSET
    pub_at: int | Unset = UNSET
    lch_at: int | Unset = UNSET
    fdv: str | Unset = UNSET
    mcap: str | Unset = UNSET
    liq_usd: str | Unset = UNSET
    liq: str | Unset = UNSET
    hld: int | Unset = UNSET
    p: str | Unset = UNSET
    np: str | Unset = UNSET
    pt: int | Unset = UNSET
    v24h: str | Unset = UNSET
    t24h: str | Unset = UNSET
    ch24h: str | Unset = UNSET
    thr: str | Unset = UNSET
    dhr: str | Unset = UNSET
    bcr: str | Unset = UNSET
    hcnt: int | Unset = UNSET
    tsrc: str | Unset = UNSET
    sts: list[TokenStatsDTO] | Unset = UNSET
    rl: str | Unset = UNSET
    ts: str | Unset = UNSET
    bs: str | Unset = UNSET
    dec: int | Unset = UNSET
    sig: DexTokenSignalDTO | Unset = UNSET
    be_score: float | Unset = UNSET
    be_rank: int | Unset = UNSET
    plt_a: str | Unset = UNSET
    ecs: int | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        n = self.n

        sym = self.sym

        addr = self.addr

        plt = self.plt

        pid = self.pid

        pdex = self.pdex

        pcid = self.pcid

        web = self.web

        tw = self.tw

        tg = self.tg

        lg = self.lg

        pub_at = self.pub_at

        lch_at = self.lch_at

        fdv = self.fdv

        mcap = self.mcap

        liq_usd = self.liq_usd

        liq = self.liq

        hld = self.hld

        p = self.p

        np = self.np

        pt = self.pt

        v24h = self.v24h

        t24h = self.t24h

        ch24h = self.ch24h

        thr = self.thr

        dhr = self.dhr

        bcr = self.bcr

        hcnt = self.hcnt

        tsrc = self.tsrc

        sts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sts, Unset):
            sts = []
            for sts_item_data in self.sts:
                sts_item = sts_item_data.to_dict()
                sts.append(sts_item)

        rl = self.rl

        ts = self.ts

        bs = self.bs

        dec = self.dec

        sig: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sig, Unset):
            sig = self.sig.to_dict()

        be_score = self.be_score

        be_rank = self.be_rank

        plt_a = self.plt_a

        ecs = self.ecs

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if n is not UNSET:
            field_dict["n"] = n
        if sym is not UNSET:
            field_dict["sym"] = sym
        if addr is not UNSET:
            field_dict["addr"] = addr
        if plt is not UNSET:
            field_dict["plt"] = plt
        if pid is not UNSET:
            field_dict["pid"] = pid
        if pdex is not UNSET:
            field_dict["pdex"] = pdex
        if pcid is not UNSET:
            field_dict["pcid"] = pcid
        if web is not UNSET:
            field_dict["web"] = web
        if tw is not UNSET:
            field_dict["tw"] = tw
        if tg is not UNSET:
            field_dict["tg"] = tg
        if lg is not UNSET:
            field_dict["lg"] = lg
        if pub_at is not UNSET:
            field_dict["pubAt"] = pub_at
        if lch_at is not UNSET:
            field_dict["lchAt"] = lch_at
        if fdv is not UNSET:
            field_dict["fdv"] = fdv
        if mcap is not UNSET:
            field_dict["mcap"] = mcap
        if liq_usd is not UNSET:
            field_dict["liqUsd"] = liq_usd
        if liq is not UNSET:
            field_dict["liq"] = liq
        if hld is not UNSET:
            field_dict["hld"] = hld
        if p is not UNSET:
            field_dict["p"] = p
        if np is not UNSET:
            field_dict["np"] = np
        if pt is not UNSET:
            field_dict["pt"] = pt
        if v24h is not UNSET:
            field_dict["v24h"] = v24h
        if t24h is not UNSET:
            field_dict["t24h"] = t24h
        if ch24h is not UNSET:
            field_dict["ch24h"] = ch24h
        if thr is not UNSET:
            field_dict["thr"] = thr
        if dhr is not UNSET:
            field_dict["dhr"] = dhr
        if bcr is not UNSET:
            field_dict["bcr"] = bcr
        if hcnt is not UNSET:
            field_dict["hcnt"] = hcnt
        if tsrc is not UNSET:
            field_dict["tsrc"] = tsrc
        if sts is not UNSET:
            field_dict["sts"] = sts
        if rl is not UNSET:
            field_dict["rl"] = rl
        if ts is not UNSET:
            field_dict["ts"] = ts
        if bs is not UNSET:
            field_dict["bs"] = bs
        if dec is not UNSET:
            field_dict["dec"] = dec
        if sig is not UNSET:
            field_dict["sig"] = sig
        if be_score is not UNSET:
            field_dict["beScore"] = be_score
        if be_rank is not UNSET:
            field_dict["beRank"] = be_rank
        if plt_a is not UNSET:
            field_dict["pltA"] = plt_a
        if ecs is not UNSET:
            field_dict["ecs"] = ecs
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dex_token_signal_dto import DexTokenSignalDTO
        from ..models.token_stats_dto import TokenStatsDTO

        d = dict(src_dict)
        n = d.pop("n", UNSET)

        sym = d.pop("sym", UNSET)

        addr = d.pop("addr", UNSET)

        plt = d.pop("plt", UNSET)

        pid = d.pop("pid", UNSET)

        pdex = d.pop("pdex", UNSET)

        pcid = d.pop("pcid", UNSET)

        web = d.pop("web", UNSET)

        tw = d.pop("tw", UNSET)

        tg = d.pop("tg", UNSET)

        lg = d.pop("lg", UNSET)

        pub_at = d.pop("pubAt", UNSET)

        lch_at = d.pop("lchAt", UNSET)

        fdv = d.pop("fdv", UNSET)

        mcap = d.pop("mcap", UNSET)

        liq_usd = d.pop("liqUsd", UNSET)

        liq = d.pop("liq", UNSET)

        hld = d.pop("hld", UNSET)

        p = d.pop("p", UNSET)

        np = d.pop("np", UNSET)

        pt = d.pop("pt", UNSET)

        v24h = d.pop("v24h", UNSET)

        t24h = d.pop("t24h", UNSET)

        ch24h = d.pop("ch24h", UNSET)

        thr = d.pop("thr", UNSET)

        dhr = d.pop("dhr", UNSET)

        bcr = d.pop("bcr", UNSET)

        hcnt = d.pop("hcnt", UNSET)

        tsrc = d.pop("tsrc", UNSET)

        _sts = d.pop("sts", UNSET)
        sts: list[TokenStatsDTO] | Unset = UNSET
        if _sts is not UNSET:
            sts = []
            for sts_item_data in _sts:
                sts_item = TokenStatsDTO.from_dict(sts_item_data)

                sts.append(sts_item)

        rl = d.pop("rl", UNSET)

        ts = d.pop("ts", UNSET)

        bs = d.pop("bs", UNSET)

        dec = d.pop("dec", UNSET)

        _sig = d.pop("sig", UNSET)
        sig: DexTokenSignalDTO | Unset
        if isinstance(_sig, Unset):
            sig = UNSET
        else:
            sig = DexTokenSignalDTO.from_dict(_sig)

        be_score = d.pop("beScore", UNSET)

        be_rank = d.pop("beRank", UNSET)

        plt_a = d.pop("pltA", UNSET)

        ecs = d.pop("ecs", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        token_leaderboard_dto = cls(
            n=n,
            sym=sym,
            addr=addr,
            plt=plt,
            pid=pid,
            pdex=pdex,
            pcid=pcid,
            web=web,
            tw=tw,
            tg=tg,
            lg=lg,
            pub_at=pub_at,
            lch_at=lch_at,
            fdv=fdv,
            mcap=mcap,
            liq_usd=liq_usd,
            liq=liq,
            hld=hld,
            p=p,
            np=np,
            pt=pt,
            v24h=v24h,
            t24h=t24h,
            ch24h=ch24h,
            thr=thr,
            dhr=dhr,
            bcr=bcr,
            hcnt=hcnt,
            tsrc=tsrc,
            sts=sts,
            rl=rl,
            ts=ts,
            bs=bs,
            dec=dec,
            sig=sig,
            be_score=be_score,
            be_rank=be_rank,
            plt_a=plt_a,
            ecs=ecs,
            tags=tags,
        )

        token_leaderboard_dto.additional_properties = d
        return token_leaderboard_dto

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
