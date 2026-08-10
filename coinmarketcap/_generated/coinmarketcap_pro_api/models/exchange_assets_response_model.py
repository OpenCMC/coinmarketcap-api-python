from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.exchange_assets_wallets_response_model import ExchangeAssetsWalletsResponseModel


T = TypeVar("T", bound="ExchangeAssetsResponseModel")


@_attrs_define
class ExchangeAssetsResponseModel:
    """
    Example:
        {'status': {'timestamp': '2022-11-24T08:23:22.028Z', 'error_code': 0, 'error_message': None, 'elapsed': 1828,
            'credit_count': 0, 'notice': None}, 'data': [{'wallet_address': '0x5a52e96bacdabb82fd05763e25335261b270efcb',
            'balance': 45000000, 'platform': {'crypto_id': 1027, 'symbol': 'ETH', 'name': 'Ethereum'}, 'currency':
            {'crypto_id': 5117, 'price_usd': 0.10241799413549, 'symbol': 'OGN', 'name': 'Origin Protocol'}},
            {'wallet_address': '0xf977814e90da44bfa03b6295a0616a897441acec', 'balance': 400000000, 'platform': {'crypto_id':
            1027, 'symbol': 'ETH', 'name': 'Ethereum'}, 'currency': {'crypto_id': 5824, 'price_usd': 0.00251174724338,
            'symbol': 'SLP', 'name': 'Smooth Love Potion'}}, {'wallet_address':
            '0x5a52e96bacdabb82fd05763e25335261b270efcb', 'balance': 5588175, 'platform': {'crypto_id': 1027, 'symbol':
            'ETH', 'name': 'Ethereum'}, 'currency': {'crypto_id': 3928, 'price_usd': 0.04813245442357, 'symbol': 'IDEX',
            'name': 'IDEX'}}, {'wallet_address': '0x5a52e96bacdabb82fd05763e25335261b270efcb', 'balance': 125000,
            'platform': {'crypto_id': 1027, 'symbol': 'ETH', 'name': 'Ethereum'}, 'currency': {'crypto_id': 1552,
            'price_usd': 20.46545919550142, 'symbol': 'MLN', 'name': 'Enzyme'}}, {'wallet_address':
            '0x21a31ee1afc51d94c2efccaa2092ad1028285549', 'balance': 27241191.98, 'platform': {'crypto_id': 1027, 'symbol':
            'ETH', 'name': 'Ethereum'}, 'currency': {'crypto_id': 14806, 'price_usd': 0.02390427295165, 'symbol': 'PEOPLE',
            'name': 'ConstitutionDAO'}}]}

    Attributes:
        data (list[ExchangeAssetsWalletsResponseModel] | Unset):
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: list[ExchangeAssetsWalletsResponseModel] | Unset = UNSET
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for componentsschemasdata_item_data in self.data:
                componentsschemasdata_item = componentsschemasdata_item_data.to_dict()
                data.append(componentsschemasdata_item)

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_status_object import APIStatusObject
        from ..models.exchange_assets_wallets_response_model import ExchangeAssetsWalletsResponseModel

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[ExchangeAssetsWalletsResponseModel] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for componentsschemasdata_item_data in _data:
                componentsschemasdata_item = ExchangeAssetsWalletsResponseModel.from_dict(
                    componentsschemasdata_item_data
                )

                data.append(componentsschemasdata_item)

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        exchange_assets_response_model = cls(
            data=data,
            status=status,
        )

        exchange_assets_response_model.additional_properties = d
        return exchange_assets_response_model

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
