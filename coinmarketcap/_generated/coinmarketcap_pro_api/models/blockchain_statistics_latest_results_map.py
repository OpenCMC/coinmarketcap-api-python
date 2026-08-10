from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.blockchain_statistics_latest_blockchain_object import BlockchainStatisticsLatestBlockchainObject


T = TypeVar("T", bound="BlockchainStatisticsLatestResultsMap")


@_attrs_define
class BlockchainStatisticsLatestResultsMap:
    """A map of blockchain objects by ID, symbol, or slug (as used in query parameters).

    Example:
        {'1': {'id': 1, 'slug': 'bitcoin', 'symbol': 'BTC', 'block_reward_static': 12.5, 'consensus_mechanism': 'proof-
            of-work', 'difficulty': '11890594958796', 'hashrate_24h': '85116194130018810000', 'pending_transactions': 1177,
            'reduction_rate': '50%', 'total_blocks': 595165, 'total_transactions': '455738994', 'tps_24h':
            3.808090277777778, 'first_block_timestamp': '2009-01-09T02:54:25.000Z'}}

    """

    additional_properties: dict[str, BlockchainStatisticsLatestBlockchainObject] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.blockchain_statistics_latest_blockchain_object import BlockchainStatisticsLatestBlockchainObject

        d = dict(src_dict)
        blockchain_statistics_latest_results_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = BlockchainStatisticsLatestBlockchainObject.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        blockchain_statistics_latest_results_map.additional_properties = additional_properties
        return blockchain_statistics_latest_results_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> BlockchainStatisticsLatestBlockchainObject:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: BlockchainStatisticsLatestBlockchainObject) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
