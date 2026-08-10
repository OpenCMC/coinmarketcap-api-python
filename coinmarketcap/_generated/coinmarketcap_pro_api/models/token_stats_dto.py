from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenStatsDTO")


@_attrs_define
class TokenStatsDTO:
    """Statistics data for token in specific interval

    Attributes:
        tp (str | Unset): Stat type, e.g., '1h', '24h', '7d' Example: 24h.
        vu (str | Unset): Total volume (string formatted) Example: 123456.789.
        txs (int | Unset): Total number of transactions Example: 1024.
        nb (int | Unset): Number of buy transactions Example: 678.
        ns (int | Unset): Number of sell transactions Example: 346.
        bvu (str | Unset): Buy volume Example: 65432.12.
        svu (str | Unset): Sell volume Example: 58024.67.
        but (int | Unset): Number of unique buyers Example: 431.
        sut (int | Unset): Number of unique sellers Example: 398.
        pc (float | Unset): Price change rate (e.g. 5.23 means +5.23%) Example: 3.51.
        ut (int | Unset): Number of unique traders Example: 789.
    """

    tp: str | Unset = UNSET
    vu: str | Unset = UNSET
    txs: int | Unset = UNSET
    nb: int | Unset = UNSET
    ns: int | Unset = UNSET
    bvu: str | Unset = UNSET
    svu: str | Unset = UNSET
    but: int | Unset = UNSET
    sut: int | Unset = UNSET
    pc: float | Unset = UNSET
    ut: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tp = self.tp

        vu = self.vu

        txs = self.txs

        nb = self.nb

        ns = self.ns

        bvu = self.bvu

        svu = self.svu

        but = self.but

        sut = self.sut

        pc = self.pc

        ut = self.ut

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tp is not UNSET:
            field_dict["tp"] = tp
        if vu is not UNSET:
            field_dict["vu"] = vu
        if txs is not UNSET:
            field_dict["txs"] = txs
        if nb is not UNSET:
            field_dict["nb"] = nb
        if ns is not UNSET:
            field_dict["ns"] = ns
        if bvu is not UNSET:
            field_dict["bvu"] = bvu
        if svu is not UNSET:
            field_dict["svu"] = svu
        if but is not UNSET:
            field_dict["but"] = but
        if sut is not UNSET:
            field_dict["sut"] = sut
        if pc is not UNSET:
            field_dict["pc"] = pc
        if ut is not UNSET:
            field_dict["ut"] = ut

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tp = d.pop("tp", UNSET)

        vu = d.pop("vu", UNSET)

        txs = d.pop("txs", UNSET)

        nb = d.pop("nb", UNSET)

        ns = d.pop("ns", UNSET)

        bvu = d.pop("bvu", UNSET)

        svu = d.pop("svu", UNSET)

        but = d.pop("but", UNSET)

        sut = d.pop("sut", UNSET)

        pc = d.pop("pc", UNSET)

        ut = d.pop("ut", UNSET)

        token_stats_dto = cls(
            tp=tp,
            vu=vu,
            txs=txs,
            nb=nb,
            ns=ns,
            bvu=bvu,
            svu=svu,
            but=but,
            sut=sut,
            pc=pc,
            ut=ut,
        )

        token_stats_dto.additional_properties = d
        return token_stats_dto

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
