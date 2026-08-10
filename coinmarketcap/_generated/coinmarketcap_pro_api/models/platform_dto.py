from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlatformDTO")


@_attrs_define
class PlatformDTO:
    """Data Transfer Object representing a supported blockchain platform

    Attributes:
        id (int | Unset): Unique platform ID Example: 14.
        n (str | Unset): Platform name Example: Ethereum.
        i (str | Unset): Icon URL for the platform Example: https://cdn.example.com/icons/eth.png.
        uf (str | Unset): URL format for block explorer (contract/token) Example:
            https://etherscan.io/token/{tokenAddress}.
        dn (str | Unset): Number of supported DEXs on this platform Example: 12.
        txuf (str | Unset): URL format for viewing transactions Example: https://etherscan.io/tx/{txHash}.
        v (bool | Unset): Whether the platform is visible in the UI Example: True.
        p (bool | Unset): Whether the platform is pinned (e.g., prioritized display)
        addr_url (str | Unset): URL format for address explorer Example: https://etherscan.io/address/{address}.
        ch_id (int | Unset): Internal chain ID Example: 1.
        puf (str | Unset): URL format for pool explorer Example: https://dexscan.io/pool/{poolAddress}.
        wc_id (int | Unset): Wrapped native token ID (e.g., WETH) Example: 2001.
        hl (int | Unset): Whether the platform is highlighted Example: 1.
        ho (int | Unset): Display order for highlighted platforms Example: 3.
        plt_a (str | Unset): platform acronym Example: ETH.
        cid (int | Unset):
    """

    id: int | Unset = UNSET
    n: str | Unset = UNSET
    i: str | Unset = UNSET
    uf: str | Unset = UNSET
    dn: str | Unset = UNSET
    txuf: str | Unset = UNSET
    v: bool | Unset = UNSET
    p: bool | Unset = UNSET
    addr_url: str | Unset = UNSET
    ch_id: int | Unset = UNSET
    puf: str | Unset = UNSET
    wc_id: int | Unset = UNSET
    hl: int | Unset = UNSET
    ho: int | Unset = UNSET
    plt_a: str | Unset = UNSET
    cid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        n = self.n

        i = self.i

        uf = self.uf

        dn = self.dn

        txuf = self.txuf

        v = self.v

        p = self.p

        addr_url = self.addr_url

        ch_id = self.ch_id

        puf = self.puf

        wc_id = self.wc_id

        hl = self.hl

        ho = self.ho

        plt_a = self.plt_a

        cid = self.cid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if n is not UNSET:
            field_dict["n"] = n
        if i is not UNSET:
            field_dict["i"] = i
        if uf is not UNSET:
            field_dict["uf"] = uf
        if dn is not UNSET:
            field_dict["dn"] = dn
        if txuf is not UNSET:
            field_dict["txuf"] = txuf
        if v is not UNSET:
            field_dict["v"] = v
        if p is not UNSET:
            field_dict["p"] = p
        if addr_url is not UNSET:
            field_dict["addrUrl"] = addr_url
        if ch_id is not UNSET:
            field_dict["chId"] = ch_id
        if puf is not UNSET:
            field_dict["puf"] = puf
        if wc_id is not UNSET:
            field_dict["wcId"] = wc_id
        if hl is not UNSET:
            field_dict["hl"] = hl
        if ho is not UNSET:
            field_dict["ho"] = ho
        if plt_a is not UNSET:
            field_dict["pltA"] = plt_a
        if cid is not UNSET:
            field_dict["cid"] = cid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        n = d.pop("n", UNSET)

        i = d.pop("i", UNSET)

        uf = d.pop("uf", UNSET)

        dn = d.pop("dn", UNSET)

        txuf = d.pop("txuf", UNSET)

        v = d.pop("v", UNSET)

        p = d.pop("p", UNSET)

        addr_url = d.pop("addrUrl", UNSET)

        ch_id = d.pop("chId", UNSET)

        puf = d.pop("puf", UNSET)

        wc_id = d.pop("wcId", UNSET)

        hl = d.pop("hl", UNSET)

        ho = d.pop("ho", UNSET)

        plt_a = d.pop("pltA", UNSET)

        cid = d.pop("cid", UNSET)

        platform_dto = cls(
            id=id,
            n=n,
            i=i,
            uf=uf,
            dn=dn,
            txuf=txuf,
            v=v,
            p=p,
            addr_url=addr_url,
            ch_id=ch_id,
            puf=puf,
            wc_id=wc_id,
            hl=hl,
            ho=ho,
            plt_a=plt_a,
            cid=cid,
        )

        platform_dto.additional_properties = d
        return platform_dto

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
