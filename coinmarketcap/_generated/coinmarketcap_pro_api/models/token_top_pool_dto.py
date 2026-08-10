from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.token import Token


T = TypeVar("T", bound="TokenTopPoolDTO")


@_attrs_define
class TokenTopPoolDTO:
    """Token's top pool information

    Attributes:
        addr (str | Unset): Pool address
        v24 (str | Unset): 24-hour trading volume
        pub_at (int | Unset): Publish timestamp
        t0 (Token | Unset): Basic token info in the pool
        t1 (Token | Unset): Basic token info in the pool
        bidx (int | Unset): Index of the base token in the pool (0 or 1)
        exid (int | Unset): Exchange ID
        exn (str | Unset): Exchange name
        liq_usd (str | Unset): Liquidity in USD
        fa (str | Unset): Factory address
        lr (str | Unset): Locked rate
        br (str | Unset): Burned rate
        top (bool | Unset): Is top pool
        mi (bool | Unset): Is meme inner pool
    """

    addr: str | Unset = UNSET
    v24: str | Unset = UNSET
    pub_at: int | Unset = UNSET
    t0: Token | Unset = UNSET
    t1: Token | Unset = UNSET
    bidx: int | Unset = UNSET
    exid: int | Unset = UNSET
    exn: str | Unset = UNSET
    liq_usd: str | Unset = UNSET
    fa: str | Unset = UNSET
    lr: str | Unset = UNSET
    br: str | Unset = UNSET
    top: bool | Unset = UNSET
    mi: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addr = self.addr

        v24 = self.v24

        pub_at = self.pub_at

        t0: dict[str, Any] | Unset = UNSET
        if not isinstance(self.t0, Unset):
            t0 = self.t0.to_dict()

        t1: dict[str, Any] | Unset = UNSET
        if not isinstance(self.t1, Unset):
            t1 = self.t1.to_dict()

        bidx = self.bidx

        exid = self.exid

        exn = self.exn

        liq_usd = self.liq_usd

        fa = self.fa

        lr = self.lr

        br = self.br

        top = self.top

        mi = self.mi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addr is not UNSET:
            field_dict["addr"] = addr
        if v24 is not UNSET:
            field_dict["v24"] = v24
        if pub_at is not UNSET:
            field_dict["pubAt"] = pub_at
        if t0 is not UNSET:
            field_dict["t0"] = t0
        if t1 is not UNSET:
            field_dict["t1"] = t1
        if bidx is not UNSET:
            field_dict["bidx"] = bidx
        if exid is not UNSET:
            field_dict["exid"] = exid
        if exn is not UNSET:
            field_dict["exn"] = exn
        if liq_usd is not UNSET:
            field_dict["liqUsd"] = liq_usd
        if fa is not UNSET:
            field_dict["fa"] = fa
        if lr is not UNSET:
            field_dict["lr"] = lr
        if br is not UNSET:
            field_dict["br"] = br
        if top is not UNSET:
            field_dict["top"] = top
        if mi is not UNSET:
            field_dict["mi"] = mi

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token import Token

        d = dict(src_dict)
        addr = d.pop("addr", UNSET)

        v24 = d.pop("v24", UNSET)

        pub_at = d.pop("pubAt", UNSET)

        _t0 = d.pop("t0", UNSET)
        t0: Token | Unset
        if isinstance(_t0, Unset):
            t0 = UNSET
        else:
            t0 = Token.from_dict(_t0)

        _t1 = d.pop("t1", UNSET)
        t1: Token | Unset
        if isinstance(_t1, Unset):
            t1 = UNSET
        else:
            t1 = Token.from_dict(_t1)

        bidx = d.pop("bidx", UNSET)

        exid = d.pop("exid", UNSET)

        exn = d.pop("exn", UNSET)

        liq_usd = d.pop("liqUsd", UNSET)

        fa = d.pop("fa", UNSET)

        lr = d.pop("lr", UNSET)

        br = d.pop("br", UNSET)

        top = d.pop("top", UNSET)

        mi = d.pop("mi", UNSET)

        token_top_pool_dto = cls(
            addr=addr,
            v24=v24,
            pub_at=pub_at,
            t0=t0,
            t1=t1,
            bidx=bidx,
            exid=exid,
            exn=exn,
            liq_usd=liq_usd,
            fa=fa,
            lr=lr,
            br=br,
            top=top,
            mi=mi,
        )

        token_top_pool_dto.additional_properties = d
        return token_top_pool_dto

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
