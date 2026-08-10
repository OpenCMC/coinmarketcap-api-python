from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coin import Coin


T = TypeVar("T", bound="AirdropsAirdropObject")


@_attrs_define
class AirdropsAirdropObject:
    """Airdrop object for each result

    Attributes:
        id (str): The unique ID of the airdrop Example: 60e59b99c8ca1d58514a2322.
        start_date (str): Timestamp (ISO 8601) of when this cryptocurrency was added to CoinMarketCap. Example:
            2013-04-28T00:00:00.000Z.
        end_date (str): Timestamp (ISO 8601) of when this cryptocurrency was added to CoinMarketCap. Example:
            2013-04-28T00:00:00.000Z.
        project_name (str | Unset): The project name Example: DeRace Airdrop.
        description (str | Unset): The description of the airdrop. Example: For 7 days starting from August 15, 2021,
            CoinMarketCap will host an Airdrop event....
        status (str | Unset): The current status of the airdrop. Example: UPCOMING.
        coin (Coin | Unset):
        total_prize (int | Unset):  Example: 10000.
        winner_count (int | Unset):  Example: 55.
        link (str | Unset): A link to the airdrop information. Example:
            https://coinmarketcap.com/currencies/derace/airdrop.
    """

    id: str
    start_date: str
    end_date: str
    project_name: str | Unset = UNSET
    description: str | Unset = UNSET
    status: str | Unset = UNSET
    coin: Coin | Unset = UNSET
    total_prize: int | Unset = UNSET
    winner_count: int | Unset = UNSET
    link: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        start_date = self.start_date

        end_date = self.end_date

        project_name = self.project_name

        description = self.description

        status = self.status

        coin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coin, Unset):
            coin = self.coin.to_dict()

        total_prize = self.total_prize

        winner_count = self.winner_count

        link = self.link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "start_date": start_date,
                "end_date": end_date,
            }
        )
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if coin is not UNSET:
            field_dict["coin"] = coin
        if total_prize is not UNSET:
            field_dict["total_prize"] = total_prize
        if winner_count is not UNSET:
            field_dict["winner_count"] = winner_count
        if link is not UNSET:
            field_dict["link"] = link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coin import Coin

        d = dict(src_dict)
        id = d.pop("id")

        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        project_name = d.pop("project_name", UNSET)

        description = d.pop("description", UNSET)

        status = d.pop("status", UNSET)

        _coin = d.pop("coin", UNSET)
        coin: Coin | Unset
        if isinstance(_coin, Unset):
            coin = UNSET
        else:
            coin = Coin.from_dict(_coin)

        total_prize = d.pop("total_prize", UNSET)

        winner_count = d.pop("winner_count", UNSET)

        link = d.pop("link", UNSET)

        airdrops_airdrop_object = cls(
            id=id,
            start_date=start_date,
            end_date=end_date,
            project_name=project_name,
            description=description,
            status=status,
            coin=coin,
            total_prize=total_prize,
            winner_count=winner_count,
            link=link,
        )

        airdrops_airdrop_object.additional_properties = d
        return airdrops_airdrop_object

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
