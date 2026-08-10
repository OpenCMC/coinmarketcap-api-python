from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_status_object import APIStatusObject
    from ..models.blockchain_statistics_latest_results_map import BlockchainStatisticsLatestResultsMap


T = TypeVar("T", bound="BlockchainStatisticsLatestResponseModel")


@_attrs_define
class BlockchainStatisticsLatestResponseModel:
    """
    Attributes:
        data (BlockchainStatisticsLatestResultsMap): A map of blockchain objects by ID, symbol, or slug (as used in
            query parameters). Example: {'1': {'id': 1, 'slug': 'bitcoin', 'symbol': 'BTC', 'block_reward_static': 12.5,
            'consensus_mechanism': 'proof-of-work', 'difficulty': '11890594958796', 'hashrate_24h': '85116194130018810000',
            'pending_transactions': 1177, 'reduction_rate': '50%', 'total_blocks': 595165, 'total_transactions':
            '455738994', 'tps_24h': 3.808090277777778, 'first_block_timestamp': '2009-01-09T02:54:25.000Z'}}.
        status (APIStatusObject | Unset): Standardized status object for API calls.
    """

    data: BlockchainStatisticsLatestResultsMap
    status: APIStatusObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_status_object import APIStatusObject
        from ..models.blockchain_statistics_latest_results_map import BlockchainStatisticsLatestResultsMap

        d = dict(src_dict)
        data = BlockchainStatisticsLatestResultsMap.from_dict(d.pop("data"))

        _status = d.pop("status", UNSET)
        status: APIStatusObject | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = APIStatusObject.from_dict(_status)

        blockchain_statistics_latest_response_model = cls(
            data=data,
            status=status,
        )

        blockchain_statistics_latest_response_model.additional_properties = d
        return blockchain_statistics_latest_response_model

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
