from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Token")


@_attrs_define
class Token:
    """Basic token info in the pool

    Attributes:
        addr (str | Unset): Token address
        lg (str | Unset): Token logo URL
        n (str | Unset): Token name
        sym (str | Unset): Token symbol
        liq (str | Unset): Liquidity in native unit
        liq_usd (str | Unset): Liquidity in USD
    """

    addr: str | Unset = UNSET
    lg: str | Unset = UNSET
    n: str | Unset = UNSET
    sym: str | Unset = UNSET
    liq: str | Unset = UNSET
    liq_usd: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addr = self.addr

        lg = self.lg

        n = self.n

        sym = self.sym

        liq = self.liq

        liq_usd = self.liq_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addr is not UNSET:
            field_dict["addr"] = addr
        if lg is not UNSET:
            field_dict["lg"] = lg
        if n is not UNSET:
            field_dict["n"] = n
        if sym is not UNSET:
            field_dict["sym"] = sym
        if liq is not UNSET:
            field_dict["liq"] = liq
        if liq_usd is not UNSET:
            field_dict["liqUsd"] = liq_usd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        addr = d.pop("addr", UNSET)

        lg = d.pop("lg", UNSET)

        n = d.pop("n", UNSET)

        sym = d.pop("sym", UNSET)

        liq = d.pop("liq", UNSET)

        liq_usd = d.pop("liqUsd", UNSET)

        token = cls(
            addr=addr,
            lg=lg,
            n=n,
            sym=sym,
            liq=liq,
            liq_usd=liq_usd,
        )

        token.additional_properties = d
        return token

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
