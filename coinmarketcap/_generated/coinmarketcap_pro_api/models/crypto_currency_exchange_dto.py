from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptoCurrencyExchangeDTO")


@_attrs_define
class CryptoCurrencyExchangeDTO:
    """Centralized exchange information

    Attributes:
        id (int | Unset): Exchange ID, e.g. 270
        slug (str | Unset): Exchange slug, e.g. binance
        n (str | Unset): Full exchange name, e.g. Binance
        lg (str | Unset): Logo URL, e.g. https://s2.coinmarketcap.com/static/img/exchanges/64x64/270.png
        wst (str | Unset): Exchange website URL
        cat (list[str] | Unset): Exchange categories, e.g. SPOT, DERIVATIVES
    """

    id: int | Unset = UNSET
    slug: str | Unset = UNSET
    n: str | Unset = UNSET
    lg: str | Unset = UNSET
    wst: str | Unset = UNSET
    cat: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug = self.slug

        n = self.n

        lg = self.lg

        wst = self.wst

        cat: list[str] | Unset = UNSET
        if not isinstance(self.cat, Unset):
            cat = self.cat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if n is not UNSET:
            field_dict["n"] = n
        if lg is not UNSET:
            field_dict["lg"] = lg
        if wst is not UNSET:
            field_dict["wst"] = wst
        if cat is not UNSET:
            field_dict["cat"] = cat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        slug = d.pop("slug", UNSET)

        n = d.pop("n", UNSET)

        lg = d.pop("lg", UNSET)

        wst = d.pop("wst", UNSET)

        cat = cast(list[str], d.pop("cat", UNSET))

        crypto_currency_exchange_dto = cls(
            id=id,
            slug=slug,
            n=n,
            lg=lg,
            wst=wst,
            cat=cat,
        )

        crypto_currency_exchange_dto.additional_properties = d
        return crypto_currency_exchange_dto

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
