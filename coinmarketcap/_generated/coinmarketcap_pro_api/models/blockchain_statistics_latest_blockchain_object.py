from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BlockchainStatisticsLatestBlockchainObject")


@_attrs_define
class BlockchainStatisticsLatestBlockchainObject:
    """A blockchain object for every blockchain that matched list options.

    Attributes:
        id (int): The unique CoinMarketCap ID for this blockchain's cryptocurrency. Example: 1.
        slug (str): The web URL friendly shorthand version of the cryptocurrency's name. Example: bitcoin.
        symbol (str): The ticker symbol for the cryptocurrency. Example: BTC.
        block_reward_static (float): The reward assigned to the miner of a block excluding fees. Example: 12.5.
        consensus_mechanism (str): The consensus mechanism used by the blockchain, for example, "proof-of-work" or
            "proof-of-stake". Example: proof-of-work.
        difficulty (str): The global block difficulty determining how hard to find a hash on this blockchain. *Note:
            This integer is returned as a string to use with BigInt libraries as it may exceed the max safe integer size for
            many programming languages.* Example: 2264398029247833.
        hashrate_24h (str): The average hashrate over the past 24 hours. *Note: This integer is returned as a string to
            use with BigInt libraries as it may exceed the max safe integer size for many programming languages.* Example:
            169267882822616.
        pending_transactions (int): The number of pending transactions. Example: 5120.
        reduction_rate (str): The rate the block reward is adjusted at a specified interval. Example: 50%.
        total_blocks (int): The total number of blocks. Example: 8385036.
        total_transactions (str): The total number of transactions. *Note: This integer is returned as a string to use
            with BigInt libraries as it may exceed the max safe integer size for many programming languages.* Example:
            523059480.
        tps_24h (float): The average transactions per second over the past 24 hours. Example: 8.463935185185186.
        first_block_timestamp (str): Timestamp (ISO 8601) of the time the first block was mined on this chain. Example:
            2009-01-09T02:54:25.000Z.
    """

    id: int
    slug: str
    symbol: str
    block_reward_static: float
    consensus_mechanism: str
    difficulty: str
    hashrate_24h: str
    pending_transactions: int
    reduction_rate: str
    total_blocks: int
    total_transactions: str
    tps_24h: float
    first_block_timestamp: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug = self.slug

        symbol = self.symbol

        block_reward_static = self.block_reward_static

        consensus_mechanism = self.consensus_mechanism

        difficulty = self.difficulty

        hashrate_24h = self.hashrate_24h

        pending_transactions = self.pending_transactions

        reduction_rate = self.reduction_rate

        total_blocks = self.total_blocks

        total_transactions = self.total_transactions

        tps_24h = self.tps_24h

        first_block_timestamp = self.first_block_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "symbol": symbol,
                "block_reward_static": block_reward_static,
                "consensus_mechanism": consensus_mechanism,
                "difficulty": difficulty,
                "hashrate_24h": hashrate_24h,
                "pending_transactions": pending_transactions,
                "reduction_rate": reduction_rate,
                "total_blocks": total_blocks,
                "total_transactions": total_transactions,
                "tps_24h": tps_24h,
                "first_block_timestamp": first_block_timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        slug = d.pop("slug")

        symbol = d.pop("symbol")

        block_reward_static = d.pop("block_reward_static")

        consensus_mechanism = d.pop("consensus_mechanism")

        difficulty = d.pop("difficulty")

        hashrate_24h = d.pop("hashrate_24h")

        pending_transactions = d.pop("pending_transactions")

        reduction_rate = d.pop("reduction_rate")

        total_blocks = d.pop("total_blocks")

        total_transactions = d.pop("total_transactions")

        tps_24h = d.pop("tps_24h")

        first_block_timestamp = d.pop("first_block_timestamp")

        blockchain_statistics_latest_blockchain_object = cls(
            id=id,
            slug=slug,
            symbol=symbol,
            block_reward_static=block_reward_static,
            consensus_mechanism=consensus_mechanism,
            difficulty=difficulty,
            hashrate_24h=hashrate_24h,
            pending_transactions=pending_transactions,
            reduction_rate=reduction_rate,
            total_blocks=total_blocks,
            total_transactions=total_transactions,
            tps_24h=tps_24h,
            first_block_timestamp=first_block_timestamp,
        )

        blockchain_statistics_latest_blockchain_object.additional_properties = d
        return blockchain_statistics_latest_blockchain_object

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
