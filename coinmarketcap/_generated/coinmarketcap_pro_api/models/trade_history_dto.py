from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tag_dto import TagDTO


T = TypeVar("T", bound="TradeHistoryDTO")


@_attrs_define
class TradeHistoryDTO:
    """Swap transaction data

    Attributes:
        ts (int | Unset): Transaction time (timestamp)
        tp (str | Unset): Transaction type (buy/sell)
        t0a (str | Unset): Base token address
        t1a (str | Unset): Quote token address
        t0s (str | Unset): Base token symbol
        t1s (str | Unset): Quote token symbol
        eid (int | Unset): exchange id
        en (str | Unset): exchange name
        f (str | Unset): factory address
        a0 (float | Unset): Base token amount
        a1 (float | Unset): Quote token amount
        t0pu (float | Unset): Price in USD
        t1pu (float | Unset): Price in USD
        q (float | Unset): Price in quote
        v (float | Unset): Total transaction value in USD
        qi (int | Unset): quoteIndex
        ma (str | Unset): Maker address
        ex (bool | Unset): exclude
        txtp (int | Unset): exclude
        tx (str | Unset): Transaction hash
        h (int | Unset): height
        tx_id (int | Unset): txId
        lgid (int | Unset): Log ID
        t0t (bool | Unset): t0top
        t1t (bool | Unset): t1top
        tags (list[TagDTO] | Unset): holder tags
        tc (int | Unset): transaction count
        kn (str | Unset): kol name
        kpn (str | Unset): kol public name
        klu (str | Unset): kol logo url
        t0pt (str | Unset): Token0 position type (open/close/add/reduce)
        t1pt (str | Unset): Token1 position type (open/close/add/reduce)
    """

    ts: int | Unset = UNSET
    tp: str | Unset = UNSET
    t0a: str | Unset = UNSET
    t1a: str | Unset = UNSET
    t0s: str | Unset = UNSET
    t1s: str | Unset = UNSET
    eid: int | Unset = UNSET
    en: str | Unset = UNSET
    f: str | Unset = UNSET
    a0: float | Unset = UNSET
    a1: float | Unset = UNSET
    t0pu: float | Unset = UNSET
    t1pu: float | Unset = UNSET
    q: float | Unset = UNSET
    v: float | Unset = UNSET
    qi: int | Unset = UNSET
    ma: str | Unset = UNSET
    ex: bool | Unset = UNSET
    txtp: int | Unset = UNSET
    tx: str | Unset = UNSET
    h: int | Unset = UNSET
    tx_id: int | Unset = UNSET
    lgid: int | Unset = UNSET
    t0t: bool | Unset = UNSET
    t1t: bool | Unset = UNSET
    tags: list[TagDTO] | Unset = UNSET
    tc: int | Unset = UNSET
    kn: str | Unset = UNSET
    kpn: str | Unset = UNSET
    klu: str | Unset = UNSET
    t0pt: str | Unset = UNSET
    t1pt: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ts = self.ts

        tp = self.tp

        t0a = self.t0a

        t1a = self.t1a

        t0s = self.t0s

        t1s = self.t1s

        eid = self.eid

        en = self.en

        f = self.f

        a0 = self.a0

        a1 = self.a1

        t0pu = self.t0pu

        t1pu = self.t1pu

        q = self.q

        v = self.v

        qi = self.qi

        ma = self.ma

        ex = self.ex

        txtp = self.txtp

        tx = self.tx

        h = self.h

        tx_id = self.tx_id

        lgid = self.lgid

        t0t = self.t0t

        t1t = self.t1t

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        tc = self.tc

        kn = self.kn

        kpn = self.kpn

        klu = self.klu

        t0pt = self.t0pt

        t1pt = self.t1pt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ts is not UNSET:
            field_dict["ts"] = ts
        if tp is not UNSET:
            field_dict["tp"] = tp
        if t0a is not UNSET:
            field_dict["t0a"] = t0a
        if t1a is not UNSET:
            field_dict["t1a"] = t1a
        if t0s is not UNSET:
            field_dict["t0s"] = t0s
        if t1s is not UNSET:
            field_dict["t1s"] = t1s
        if eid is not UNSET:
            field_dict["eid"] = eid
        if en is not UNSET:
            field_dict["en"] = en
        if f is not UNSET:
            field_dict["f"] = f
        if a0 is not UNSET:
            field_dict["a0"] = a0
        if a1 is not UNSET:
            field_dict["a1"] = a1
        if t0pu is not UNSET:
            field_dict["t0pu"] = t0pu
        if t1pu is not UNSET:
            field_dict["t1pu"] = t1pu
        if q is not UNSET:
            field_dict["q"] = q
        if v is not UNSET:
            field_dict["v"] = v
        if qi is not UNSET:
            field_dict["qi"] = qi
        if ma is not UNSET:
            field_dict["ma"] = ma
        if ex is not UNSET:
            field_dict["ex"] = ex
        if txtp is not UNSET:
            field_dict["txtp"] = txtp
        if tx is not UNSET:
            field_dict["tx"] = tx
        if h is not UNSET:
            field_dict["h"] = h
        if tx_id is not UNSET:
            field_dict["txId"] = tx_id
        if lgid is not UNSET:
            field_dict["lgid"] = lgid
        if t0t is not UNSET:
            field_dict["t0t"] = t0t
        if t1t is not UNSET:
            field_dict["t1t"] = t1t
        if tags is not UNSET:
            field_dict["tags"] = tags
        if tc is not UNSET:
            field_dict["tc"] = tc
        if kn is not UNSET:
            field_dict["kn"] = kn
        if kpn is not UNSET:
            field_dict["kpn"] = kpn
        if klu is not UNSET:
            field_dict["klu"] = klu
        if t0pt is not UNSET:
            field_dict["t0pt"] = t0pt
        if t1pt is not UNSET:
            field_dict["t1pt"] = t1pt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tag_dto import TagDTO

        d = dict(src_dict)
        ts = d.pop("ts", UNSET)

        tp = d.pop("tp", UNSET)

        t0a = d.pop("t0a", UNSET)

        t1a = d.pop("t1a", UNSET)

        t0s = d.pop("t0s", UNSET)

        t1s = d.pop("t1s", UNSET)

        eid = d.pop("eid", UNSET)

        en = d.pop("en", UNSET)

        f = d.pop("f", UNSET)

        a0 = d.pop("a0", UNSET)

        a1 = d.pop("a1", UNSET)

        t0pu = d.pop("t0pu", UNSET)

        t1pu = d.pop("t1pu", UNSET)

        q = d.pop("q", UNSET)

        v = d.pop("v", UNSET)

        qi = d.pop("qi", UNSET)

        ma = d.pop("ma", UNSET)

        ex = d.pop("ex", UNSET)

        txtp = d.pop("txtp", UNSET)

        tx = d.pop("tx", UNSET)

        h = d.pop("h", UNSET)

        tx_id = d.pop("txId", UNSET)

        lgid = d.pop("lgid", UNSET)

        t0t = d.pop("t0t", UNSET)

        t1t = d.pop("t1t", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[TagDTO] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = TagDTO.from_dict(tags_item_data)

                tags.append(tags_item)

        tc = d.pop("tc", UNSET)

        kn = d.pop("kn", UNSET)

        kpn = d.pop("kpn", UNSET)

        klu = d.pop("klu", UNSET)

        t0pt = d.pop("t0pt", UNSET)

        t1pt = d.pop("t1pt", UNSET)

        trade_history_dto = cls(
            ts=ts,
            tp=tp,
            t0a=t0a,
            t1a=t1a,
            t0s=t0s,
            t1s=t1s,
            eid=eid,
            en=en,
            f=f,
            a0=a0,
            a1=a1,
            t0pu=t0pu,
            t1pu=t1pu,
            q=q,
            v=v,
            qi=qi,
            ma=ma,
            ex=ex,
            txtp=txtp,
            tx=tx,
            h=h,
            tx_id=tx_id,
            lgid=lgid,
            t0t=t0t,
            t1t=t1t,
            tags=tags,
            tc=tc,
            kn=kn,
            kpn=kpn,
            klu=klu,
            t0pt=t0pt,
            t1pt=t1pt,
        )

        trade_history_dto.additional_properties = d
        return trade_history_dto

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
