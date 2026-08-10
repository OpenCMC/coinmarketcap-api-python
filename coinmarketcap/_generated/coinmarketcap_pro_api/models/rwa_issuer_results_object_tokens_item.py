from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RWAIssuerResultsObjectTokensItem")


@_attrs_define
class RWAIssuerResultsObjectTokensItem:
    """
    Attributes:
        name (str | Unset): Token name (e.g. `SpaceX tokenized stock (Backpack)`). Example: SpaceX tokenized stock
            (Backpack).
        symbol (str | Unset): Token symbol (e.g. `SPCX`). Example: SPCX.
        crypto_id (int | Unset): CoinMarketCap cryptocurrency ID of the token. Example: 40238.
        rwa_id (int | None | Unset): The RWA asset this token represents; `null` if not yet mapped to an RWA asset.
            Example: 9.
    """

    name: str | Unset = UNSET
    symbol: str | Unset = UNSET
    crypto_id: int | Unset = UNSET
    rwa_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        symbol = self.symbol

        crypto_id = self.crypto_id

        rwa_id: int | None | Unset
        if isinstance(self.rwa_id, Unset):
            rwa_id = UNSET
        else:
            rwa_id = self.rwa_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if crypto_id is not UNSET:
            field_dict["crypto_id"] = crypto_id
        if rwa_id is not UNSET:
            field_dict["rwa_id"] = rwa_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        symbol = d.pop("symbol", UNSET)

        crypto_id = d.pop("crypto_id", UNSET)

        def _parse_rwa_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rwa_id = _parse_rwa_id(d.pop("rwa_id", UNSET))

        rwa_issuer_results_object_tokens_item = cls(
            name=name,
            symbol=symbol,
            crypto_id=crypto_id,
            rwa_id=rwa_id,
        )

        rwa_issuer_results_object_tokens_item.additional_properties = d
        return rwa_issuer_results_object_tokens_item

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
