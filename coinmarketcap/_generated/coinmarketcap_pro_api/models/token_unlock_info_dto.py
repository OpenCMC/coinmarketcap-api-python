from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.next_unlocked_detail_dto import NextUnlockedDetailDTO
    from ..models.next_unlocked_dto import NextUnlockedDTO


T = TypeVar("T", bound="TokenUnlockInfoDTO")


@_attrs_define
class TokenUnlockInfoDTO:
    """
    Attributes:
        id (int | Unset): The unique CoinMarketCap ID for this cryptocurrency.
        name (str | Unset): The name of this cryptocurrency.
        symbol (str | Unset): The ticker symbol for this cryptocurrency.
        slug (str | Unset):   The web URL friendly shorthand version of this cryptocurrency name.
        status (str | Unset): Current status of the cryptocurrency. Can be "active" or "inactive".
        last_updated (str | Unset): Timestamp (ISO 8601) of when the next token unlock is.
        approve_time (str | Unset): Timestamp (ISO 8601) of when the token unlock data is reviewed and approved.
        cmc_rank (int | Unset): CoinMarketCap's market cap rank as outlined in our methodology
            (https://coinmarketcap.com/methodology/).
        circulating_supply (float | Unset): The approximate number of coins circulating for this cryptocurrency at the
            end of the requested UTC day.
        max_supply (float | Unset): The expected maximum limit of coins ever to be available for this cryptocurrency.
        total_supply (float | Unset): The approximate total amount of coins in existence right now (minus any coins that
            have been verifiably burned).
        infinite_supply (bool | Unset): The cryptocurrency is known to have an infinite supply.
        self_reported_circulating_supply (float | Unset): The self reported number of coins circulating for this
            cryptocurrency.
        token_locked_amount (float | Unset): The total amount of tokens of this cryptocurrency is locked at the moment.
        token_unlocked_amount (float | Unset): The total amount of tokens of this cryptocurrency that has been unlocked
            at the moment.
        next_unlock (NextUnlockedDTO | Unset): The breakdown of the next token unlock.
        next_unlock_detail (list[NextUnlockedDetailDTO] | Unset): Timestamp (ISO 8601) of when this was last updated.
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    symbol: str | Unset = UNSET
    slug: str | Unset = UNSET
    status: str | Unset = UNSET
    last_updated: str | Unset = UNSET
    approve_time: str | Unset = UNSET
    cmc_rank: int | Unset = UNSET
    circulating_supply: float | Unset = UNSET
    max_supply: float | Unset = UNSET
    total_supply: float | Unset = UNSET
    infinite_supply: bool | Unset = UNSET
    self_reported_circulating_supply: float | Unset = UNSET
    token_locked_amount: float | Unset = UNSET
    token_unlocked_amount: float | Unset = UNSET
    next_unlock: NextUnlockedDTO | Unset = UNSET
    next_unlock_detail: list[NextUnlockedDetailDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        symbol = self.symbol

        slug = self.slug

        status = self.status

        last_updated = self.last_updated

        approve_time = self.approve_time

        cmc_rank = self.cmc_rank

        circulating_supply = self.circulating_supply

        max_supply = self.max_supply

        total_supply = self.total_supply

        infinite_supply = self.infinite_supply

        self_reported_circulating_supply = self.self_reported_circulating_supply

        token_locked_amount = self.token_locked_amount

        token_unlocked_amount = self.token_unlocked_amount

        next_unlock: dict[str, Any] | Unset = UNSET
        if not isinstance(self.next_unlock, Unset):
            next_unlock = self.next_unlock.to_dict()

        next_unlock_detail: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.next_unlock_detail, Unset):
            next_unlock_detail = []
            for next_unlock_detail_item_data in self.next_unlock_detail:
                next_unlock_detail_item = next_unlock_detail_item_data.to_dict()
                next_unlock_detail.append(next_unlock_detail_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if slug is not UNSET:
            field_dict["slug"] = slug
        if status is not UNSET:
            field_dict["status"] = status
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if approve_time is not UNSET:
            field_dict["approveTime"] = approve_time
        if cmc_rank is not UNSET:
            field_dict["cmc_rank"] = cmc_rank
        if circulating_supply is not UNSET:
            field_dict["circulating_supply"] = circulating_supply
        if max_supply is not UNSET:
            field_dict["max_supply"] = max_supply
        if total_supply is not UNSET:
            field_dict["total_supply"] = total_supply
        if infinite_supply is not UNSET:
            field_dict["infinite_supply"] = infinite_supply
        if self_reported_circulating_supply is not UNSET:
            field_dict["self_reported_circulating_supply"] = self_reported_circulating_supply
        if token_locked_amount is not UNSET:
            field_dict["token_locked_amount"] = token_locked_amount
        if token_unlocked_amount is not UNSET:
            field_dict["token_unlocked_amount"] = token_unlocked_amount
        if next_unlock is not UNSET:
            field_dict["next_unlock"] = next_unlock
        if next_unlock_detail is not UNSET:
            field_dict["next_unlock_detail"] = next_unlock_detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.next_unlocked_detail_dto import NextUnlockedDetailDTO
        from ..models.next_unlocked_dto import NextUnlockedDTO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        symbol = d.pop("symbol", UNSET)

        slug = d.pop("slug", UNSET)

        status = d.pop("status", UNSET)

        last_updated = d.pop("lastUpdated", UNSET)

        approve_time = d.pop("approveTime", UNSET)

        cmc_rank = d.pop("cmc_rank", UNSET)

        circulating_supply = d.pop("circulating_supply", UNSET)

        max_supply = d.pop("max_supply", UNSET)

        total_supply = d.pop("total_supply", UNSET)

        infinite_supply = d.pop("infinite_supply", UNSET)

        self_reported_circulating_supply = d.pop("self_reported_circulating_supply", UNSET)

        token_locked_amount = d.pop("token_locked_amount", UNSET)

        token_unlocked_amount = d.pop("token_unlocked_amount", UNSET)

        _next_unlock = d.pop("next_unlock", UNSET)
        next_unlock: NextUnlockedDTO | Unset
        if isinstance(_next_unlock, Unset):
            next_unlock = UNSET
        else:
            next_unlock = NextUnlockedDTO.from_dict(_next_unlock)

        _next_unlock_detail = d.pop("next_unlock_detail", UNSET)
        next_unlock_detail: list[NextUnlockedDetailDTO] | Unset = UNSET
        if _next_unlock_detail is not UNSET:
            next_unlock_detail = []
            for next_unlock_detail_item_data in _next_unlock_detail:
                next_unlock_detail_item = NextUnlockedDetailDTO.from_dict(next_unlock_detail_item_data)

                next_unlock_detail.append(next_unlock_detail_item)

        token_unlock_info_dto = cls(
            id=id,
            name=name,
            symbol=symbol,
            slug=slug,
            status=status,
            last_updated=last_updated,
            approve_time=approve_time,
            cmc_rank=cmc_rank,
            circulating_supply=circulating_supply,
            max_supply=max_supply,
            total_supply=total_supply,
            infinite_supply=infinite_supply,
            self_reported_circulating_supply=self_reported_circulating_supply,
            token_locked_amount=token_locked_amount,
            token_unlocked_amount=token_unlocked_amount,
            next_unlock=next_unlock,
            next_unlock_detail=next_unlock_detail,
        )

        token_unlock_info_dto.additional_properties = d
        return token_unlock_info_dto

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
