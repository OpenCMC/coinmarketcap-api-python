from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crypto_currency_exchange_dto import CryptoCurrencyExchangeDTO
    from ..models.dex_token_signal_dto import DexTokenSignalDTO
    from ..models.token_stats_dto import TokenStatsDTO
    from ..models.token_top_pool_dto import TokenTopPoolDTO


T = TypeVar("T", bound="TokenDetailDTO")


@_attrs_define
class TokenDetailDTO:
    """Detailed token information

    Attributes:
        n (str | Unset): Token name
        sym (str | Unset): Token symbol
        addr (str | Unset): Token address
        plt (str | Unset): Platform name
        pdex (str | Unset): Token platform dexer name (pdex)
        pcid (int | Unset): Token platform crypto ID (pcid)
        pid (int | Unset): Platform ID
        dec (int | Unset): Token decimals
        crt (str | Unset): Token creator address
        own (str | Unset): Token owner address
        rnc (str | Unset): Renounced address
        web (str | Unset): Project website
        tw (str | Unset): Twitter URL
        tg (str | Unset): Telegram URL
        lg (str | Unset): Logo URL
        pub_at (int | Unset): Token publish timestamp
        lch_at (int | Unset): Token launched timestamp
        fdv (str | Unset): Fully Diluted Valuation
        mcap (str | Unset): Market capitalization
        ts (str | Unset): Total token supply
        bs (str | Unset): Burned supply
        cs (str | Unset): Circulating supply
        liq_usd (str | Unset): Liquidity (USD)
        liq (str | Unset): Liquidity (native)
        hld (int | Unset): Holder count
        p (str | Unset): Token price in USD
        ph24h (str | Unset): 24h price high
        pl24h (str | Unset): 24h price low
        pt (int | Unset): Price last updated timestamp
        fpt (int | Unset): Timestamp of the first time this token had a price
        fpct (int | Unset): Timestamp when the first pool for this token was created
        bcr (float | Unset): Bonding curve ratio
        sts (list[TokenStatsDTO] | Unset): Token statistics
        pls (list[TokenTopPoolDTO] | Unset): Top liquidity pools
        turl (str | Unset): DEX trading URL
        nps (int | Unset): Number of top pools
        tsrc (str | Unset): Pool source
        rl (str | Unset): Token risk level
        lf (int | Unset): Listed flag (1 = listed, 0 = unlisted)
        cid (int | Unset): Crypto currency ID
        lmc (str | Unset): Listing market capitalization
        lsmc (str | Unset): Listing self-reported market capitalization
        lsrcs (str | Unset): Listing self-reported circulating supply
        ltcs (str | Unset): Listing circulating supply
        ltda (int | Unset): Listing token date added
        cexs (list[CryptoCurrencyExchangeDTO] | Unset): Centralized exchange listings
        sig (DexTokenSignalDTO | Unset): Token signal
        ecs (int | Unset): Binance exclusive code, 1 - exclusive
        la (int | Unset): show listed alert, 1-show,0-hide
    """

    n: str | Unset = UNSET
    sym: str | Unset = UNSET
    addr: str | Unset = UNSET
    plt: str | Unset = UNSET
    pdex: str | Unset = UNSET
    pcid: int | Unset = UNSET
    pid: int | Unset = UNSET
    dec: int | Unset = UNSET
    crt: str | Unset = UNSET
    own: str | Unset = UNSET
    rnc: str | Unset = UNSET
    web: str | Unset = UNSET
    tw: str | Unset = UNSET
    tg: str | Unset = UNSET
    lg: str | Unset = UNSET
    pub_at: int | Unset = UNSET
    lch_at: int | Unset = UNSET
    fdv: str | Unset = UNSET
    mcap: str | Unset = UNSET
    ts: str | Unset = UNSET
    bs: str | Unset = UNSET
    cs: str | Unset = UNSET
    liq_usd: str | Unset = UNSET
    liq: str | Unset = UNSET
    hld: int | Unset = UNSET
    p: str | Unset = UNSET
    ph24h: str | Unset = UNSET
    pl24h: str | Unset = UNSET
    pt: int | Unset = UNSET
    fpt: int | Unset = UNSET
    fpct: int | Unset = UNSET
    bcr: float | Unset = UNSET
    sts: list[TokenStatsDTO] | Unset = UNSET
    pls: list[TokenTopPoolDTO] | Unset = UNSET
    turl: str | Unset = UNSET
    nps: int | Unset = UNSET
    tsrc: str | Unset = UNSET
    rl: str | Unset = UNSET
    lf: int | Unset = UNSET
    cid: int | Unset = UNSET
    lmc: str | Unset = UNSET
    lsmc: str | Unset = UNSET
    lsrcs: str | Unset = UNSET
    ltcs: str | Unset = UNSET
    ltda: int | Unset = UNSET
    cexs: list[CryptoCurrencyExchangeDTO] | Unset = UNSET
    sig: DexTokenSignalDTO | Unset = UNSET
    ecs: int | Unset = UNSET
    la: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        n = self.n

        sym = self.sym

        addr = self.addr

        plt = self.plt

        pdex = self.pdex

        pcid = self.pcid

        pid = self.pid

        dec = self.dec

        crt = self.crt

        own = self.own

        rnc = self.rnc

        web = self.web

        tw = self.tw

        tg = self.tg

        lg = self.lg

        pub_at = self.pub_at

        lch_at = self.lch_at

        fdv = self.fdv

        mcap = self.mcap

        ts = self.ts

        bs = self.bs

        cs = self.cs

        liq_usd = self.liq_usd

        liq = self.liq

        hld = self.hld

        p = self.p

        ph24h = self.ph24h

        pl24h = self.pl24h

        pt = self.pt

        fpt = self.fpt

        fpct = self.fpct

        bcr = self.bcr

        sts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sts, Unset):
            sts = []
            for sts_item_data in self.sts:
                sts_item = sts_item_data.to_dict()
                sts.append(sts_item)

        pls: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pls, Unset):
            pls = []
            for pls_item_data in self.pls:
                pls_item = pls_item_data.to_dict()
                pls.append(pls_item)

        turl = self.turl

        nps = self.nps

        tsrc = self.tsrc

        rl = self.rl

        lf = self.lf

        cid = self.cid

        lmc = self.lmc

        lsmc = self.lsmc

        lsrcs = self.lsrcs

        ltcs = self.ltcs

        ltda = self.ltda

        cexs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cexs, Unset):
            cexs = []
            for cexs_item_data in self.cexs:
                cexs_item = cexs_item_data.to_dict()
                cexs.append(cexs_item)

        sig: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sig, Unset):
            sig = self.sig.to_dict()

        ecs = self.ecs

        la = self.la

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
        if pdex is not UNSET:
            field_dict["pdex"] = pdex
        if pcid is not UNSET:
            field_dict["pcid"] = pcid
        if pid is not UNSET:
            field_dict["pid"] = pid
        if dec is not UNSET:
            field_dict["dec"] = dec
        if crt is not UNSET:
            field_dict["crt"] = crt
        if own is not UNSET:
            field_dict["own"] = own
        if rnc is not UNSET:
            field_dict["rnc"] = rnc
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
        if ts is not UNSET:
            field_dict["ts"] = ts
        if bs is not UNSET:
            field_dict["bs"] = bs
        if cs is not UNSET:
            field_dict["cs"] = cs
        if liq_usd is not UNSET:
            field_dict["liqUsd"] = liq_usd
        if liq is not UNSET:
            field_dict["liq"] = liq
        if hld is not UNSET:
            field_dict["hld"] = hld
        if p is not UNSET:
            field_dict["p"] = p
        if ph24h is not UNSET:
            field_dict["ph24h"] = ph24h
        if pl24h is not UNSET:
            field_dict["pl24h"] = pl24h
        if pt is not UNSET:
            field_dict["pt"] = pt
        if fpt is not UNSET:
            field_dict["fpt"] = fpt
        if fpct is not UNSET:
            field_dict["fpct"] = fpct
        if bcr is not UNSET:
            field_dict["bcr"] = bcr
        if sts is not UNSET:
            field_dict["sts"] = sts
        if pls is not UNSET:
            field_dict["pls"] = pls
        if turl is not UNSET:
            field_dict["turl"] = turl
        if nps is not UNSET:
            field_dict["nps"] = nps
        if tsrc is not UNSET:
            field_dict["tsrc"] = tsrc
        if rl is not UNSET:
            field_dict["rl"] = rl
        if lf is not UNSET:
            field_dict["lf"] = lf
        if cid is not UNSET:
            field_dict["cid"] = cid
        if lmc is not UNSET:
            field_dict["lmc"] = lmc
        if lsmc is not UNSET:
            field_dict["lsmc"] = lsmc
        if lsrcs is not UNSET:
            field_dict["lsrcs"] = lsrcs
        if ltcs is not UNSET:
            field_dict["ltcs"] = ltcs
        if ltda is not UNSET:
            field_dict["ltda"] = ltda
        if cexs is not UNSET:
            field_dict["cexs"] = cexs
        if sig is not UNSET:
            field_dict["sig"] = sig
        if ecs is not UNSET:
            field_dict["ecs"] = ecs
        if la is not UNSET:
            field_dict["la"] = la

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crypto_currency_exchange_dto import CryptoCurrencyExchangeDTO
        from ..models.dex_token_signal_dto import DexTokenSignalDTO
        from ..models.token_stats_dto import TokenStatsDTO
        from ..models.token_top_pool_dto import TokenTopPoolDTO

        d = dict(src_dict)
        n = d.pop("n", UNSET)

        sym = d.pop("sym", UNSET)

        addr = d.pop("addr", UNSET)

        plt = d.pop("plt", UNSET)

        pdex = d.pop("pdex", UNSET)

        pcid = d.pop("pcid", UNSET)

        pid = d.pop("pid", UNSET)

        dec = d.pop("dec", UNSET)

        crt = d.pop("crt", UNSET)

        own = d.pop("own", UNSET)

        rnc = d.pop("rnc", UNSET)

        web = d.pop("web", UNSET)

        tw = d.pop("tw", UNSET)

        tg = d.pop("tg", UNSET)

        lg = d.pop("lg", UNSET)

        pub_at = d.pop("pubAt", UNSET)

        lch_at = d.pop("lchAt", UNSET)

        fdv = d.pop("fdv", UNSET)

        mcap = d.pop("mcap", UNSET)

        ts = d.pop("ts", UNSET)

        bs = d.pop("bs", UNSET)

        cs = d.pop("cs", UNSET)

        liq_usd = d.pop("liqUsd", UNSET)

        liq = d.pop("liq", UNSET)

        hld = d.pop("hld", UNSET)

        p = d.pop("p", UNSET)

        ph24h = d.pop("ph24h", UNSET)

        pl24h = d.pop("pl24h", UNSET)

        pt = d.pop("pt", UNSET)

        fpt = d.pop("fpt", UNSET)

        fpct = d.pop("fpct", UNSET)

        bcr = d.pop("bcr", UNSET)

        _sts = d.pop("sts", UNSET)
        sts: list[TokenStatsDTO] | Unset = UNSET
        if _sts is not UNSET:
            sts = []
            for sts_item_data in _sts:
                sts_item = TokenStatsDTO.from_dict(sts_item_data)

                sts.append(sts_item)

        _pls = d.pop("pls", UNSET)
        pls: list[TokenTopPoolDTO] | Unset = UNSET
        if _pls is not UNSET:
            pls = []
            for pls_item_data in _pls:
                pls_item = TokenTopPoolDTO.from_dict(pls_item_data)

                pls.append(pls_item)

        turl = d.pop("turl", UNSET)

        nps = d.pop("nps", UNSET)

        tsrc = d.pop("tsrc", UNSET)

        rl = d.pop("rl", UNSET)

        lf = d.pop("lf", UNSET)

        cid = d.pop("cid", UNSET)

        lmc = d.pop("lmc", UNSET)

        lsmc = d.pop("lsmc", UNSET)

        lsrcs = d.pop("lsrcs", UNSET)

        ltcs = d.pop("ltcs", UNSET)

        ltda = d.pop("ltda", UNSET)

        _cexs = d.pop("cexs", UNSET)
        cexs: list[CryptoCurrencyExchangeDTO] | Unset = UNSET
        if _cexs is not UNSET:
            cexs = []
            for cexs_item_data in _cexs:
                cexs_item = CryptoCurrencyExchangeDTO.from_dict(cexs_item_data)

                cexs.append(cexs_item)

        _sig = d.pop("sig", UNSET)
        sig: DexTokenSignalDTO | Unset
        if isinstance(_sig, Unset):
            sig = UNSET
        else:
            sig = DexTokenSignalDTO.from_dict(_sig)

        ecs = d.pop("ecs", UNSET)

        la = d.pop("la", UNSET)

        token_detail_dto = cls(
            n=n,
            sym=sym,
            addr=addr,
            plt=plt,
            pdex=pdex,
            pcid=pcid,
            pid=pid,
            dec=dec,
            crt=crt,
            own=own,
            rnc=rnc,
            web=web,
            tw=tw,
            tg=tg,
            lg=lg,
            pub_at=pub_at,
            lch_at=lch_at,
            fdv=fdv,
            mcap=mcap,
            ts=ts,
            bs=bs,
            cs=cs,
            liq_usd=liq_usd,
            liq=liq,
            hld=hld,
            p=p,
            ph24h=ph24h,
            pl24h=pl24h,
            pt=pt,
            fpt=fpt,
            fpct=fpct,
            bcr=bcr,
            sts=sts,
            pls=pls,
            turl=turl,
            nps=nps,
            tsrc=tsrc,
            rl=rl,
            lf=lf,
            cid=cid,
            lmc=lmc,
            lsmc=lsmc,
            lsrcs=lsrcs,
            ltcs=ltcs,
            ltda=ltda,
            cexs=cexs,
            sig=sig,
            ecs=ecs,
            la=la,
        )

        token_detail_dto.additional_properties = d
        return token_detail_dto

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
