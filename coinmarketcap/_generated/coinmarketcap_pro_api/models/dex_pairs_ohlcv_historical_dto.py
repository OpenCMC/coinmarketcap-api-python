from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dex_pairs_ohlcv_historical_quotes import DexPairsOhlcvHistoricalQuotes
    from ..models.security_scan_result import SecurityScanResult


T = TypeVar("T", bound="DexPairsOhlcvHistoricalDTO")


@_attrs_define
class DexPairsOhlcvHistoricalDTO:
    """DEX pairs OHLCV historical data

    Attributes:
        quotes (list[DexPairsOhlcvHistoricalQuotes] | Unset): Collection of historical OHLCV quotes for the DEX pair
        contract_address (str | Unset): The unique contract address for this spot pair.
        name (str | Unset): The name of this spot pair.
        base_asset_id (str | Unset): The id of this base asset in the spot pair.
        base_asset_ucid (str | Unset): The ucid of this base asset in the spot pair.
        base_asset_name (str | Unset): The name of this base asset in the spot pair.
        base_asset_symbol (str | Unset): The symbol of this base asset in the spot pair.
        base_asset_contract_address (str | Unset): The contract addres of this base asset in the spot pair.
        quote_asset_id (str | Unset): The id of this quote asset in the spot pair.
        quote_asset_ucid (str | Unset): The ucid of this quote asset in the spot pair.
        quote_asset_name (str | Unset): The name of this quote asset in the spot pair.
        quote_asset_symbol (str | Unset): The symbol of this quote asset in the spot pair.
        quote_asset_contract_address (str | Unset): The contract addresss of this quote asset in the spot pair.
        dex_id (str | Unset): The id of this dex the spot pair is on.
        dex_slug (str | Unset): The name of this dex the spot pair is on.
        network_id (str | Unset): The id of the network the spot pair is on.
        network_slug (str | Unset): The slug of the network the spot pair is on.
        last_updated (datetime.datetime | Unset): Timestamp (ISO 8601) of the last time this record was updated.
        created_at (datetime.datetime | Unset): Timestamp (ISO 8601) when we started tracking this asset.
        num_transactions_24h (int | Unset): Number of transactions in past 24 hours
        holders (int | Unset): Number of holders of the asset
        field_24h_no_of_buys (int | Unset): Number of asset buys in the past 24 hours
        field_24h_no_of_sells (int | Unset): Number of asset sells in the past 24 hours
        pool_created (datetime.datetime | Unset): When the pool of the asset was created
        buy_tax (float | Unset): Buy tax on the asset
        sell_tax (float | Unset): Sell tax on the asset
        security_scan (list[SecurityScanResult] | Unset): Security scan by Go+.


            All infomation and data relating to contract detection are based on public third party information.
            CoinMarketCap does not confirm or verify the accuracy or timeliness of such information and data.

            CoinMarketCap shall have no responsibility or liability for the accuracy of data, nor have the duty to review,
            confirm, verify or otherwise perform any inquiry or investigation as to the completeness, accuracy, sufficiency,
            integrity, reliability or timeliness of any such information or data provided.

            Only returned if passed in aux.
        pool_base_asset (float | Unset): Base asset in the pool
        pool_quote_asset (float | Unset): Quote asset in the pool
        percent_pooled_base_asset (float | Unset): Percentage of the base asset in the pool
        field_24h_volume_quote_asset (float | Unset): 24 hours volume of the quote asset
        total_supply_quote_asset (float | Unset): Total supply of the quote asset
        total_supply_base_asset (float | Unset): Total supply of the quote asset
        date_launched (datetime.datetime | Unset): Timestamp (ISO 8601) of the launch date for this exchange.
    """

    quotes: list[DexPairsOhlcvHistoricalQuotes] | Unset = UNSET
    contract_address: str | Unset = UNSET
    name: str | Unset = UNSET
    base_asset_id: str | Unset = UNSET
    base_asset_ucid: str | Unset = UNSET
    base_asset_name: str | Unset = UNSET
    base_asset_symbol: str | Unset = UNSET
    base_asset_contract_address: str | Unset = UNSET
    quote_asset_id: str | Unset = UNSET
    quote_asset_ucid: str | Unset = UNSET
    quote_asset_name: str | Unset = UNSET
    quote_asset_symbol: str | Unset = UNSET
    quote_asset_contract_address: str | Unset = UNSET
    dex_id: str | Unset = UNSET
    dex_slug: str | Unset = UNSET
    network_id: str | Unset = UNSET
    network_slug: str | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    num_transactions_24h: int | Unset = UNSET
    holders: int | Unset = UNSET
    field_24h_no_of_buys: int | Unset = UNSET
    field_24h_no_of_sells: int | Unset = UNSET
    pool_created: datetime.datetime | Unset = UNSET
    buy_tax: float | Unset = UNSET
    sell_tax: float | Unset = UNSET
    security_scan: list[SecurityScanResult] | Unset = UNSET
    pool_base_asset: float | Unset = UNSET
    pool_quote_asset: float | Unset = UNSET
    percent_pooled_base_asset: float | Unset = UNSET
    field_24h_volume_quote_asset: float | Unset = UNSET
    total_supply_quote_asset: float | Unset = UNSET
    total_supply_base_asset: float | Unset = UNSET
    date_launched: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quotes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quotes, Unset):
            quotes = []
            for quotes_item_data in self.quotes:
                quotes_item = quotes_item_data.to_dict()
                quotes.append(quotes_item)

        contract_address = self.contract_address

        name = self.name

        base_asset_id = self.base_asset_id

        base_asset_ucid = self.base_asset_ucid

        base_asset_name = self.base_asset_name

        base_asset_symbol = self.base_asset_symbol

        base_asset_contract_address = self.base_asset_contract_address

        quote_asset_id = self.quote_asset_id

        quote_asset_ucid = self.quote_asset_ucid

        quote_asset_name = self.quote_asset_name

        quote_asset_symbol = self.quote_asset_symbol

        quote_asset_contract_address = self.quote_asset_contract_address

        dex_id = self.dex_id

        dex_slug = self.dex_slug

        network_id = self.network_id

        network_slug = self.network_slug

        last_updated: str | Unset = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        num_transactions_24h = self.num_transactions_24h

        holders = self.holders

        field_24h_no_of_buys = self.field_24h_no_of_buys

        field_24h_no_of_sells = self.field_24h_no_of_sells

        pool_created: str | Unset = UNSET
        if not isinstance(self.pool_created, Unset):
            pool_created = self.pool_created.isoformat()

        buy_tax = self.buy_tax

        sell_tax = self.sell_tax

        security_scan: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.security_scan, Unset):
            security_scan = []
            for security_scan_item_data in self.security_scan:
                security_scan_item = security_scan_item_data.to_dict()
                security_scan.append(security_scan_item)

        pool_base_asset = self.pool_base_asset

        pool_quote_asset = self.pool_quote_asset

        percent_pooled_base_asset = self.percent_pooled_base_asset

        field_24h_volume_quote_asset = self.field_24h_volume_quote_asset

        total_supply_quote_asset = self.total_supply_quote_asset

        total_supply_base_asset = self.total_supply_base_asset

        date_launched: str | Unset = UNSET
        if not isinstance(self.date_launched, Unset):
            date_launched = self.date_launched.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quotes is not UNSET:
            field_dict["quotes"] = quotes
        if contract_address is not UNSET:
            field_dict["contract_address"] = contract_address
        if name is not UNSET:
            field_dict["name"] = name
        if base_asset_id is not UNSET:
            field_dict["base_asset_id"] = base_asset_id
        if base_asset_ucid is not UNSET:
            field_dict["base_asset_ucid"] = base_asset_ucid
        if base_asset_name is not UNSET:
            field_dict["base_asset_name"] = base_asset_name
        if base_asset_symbol is not UNSET:
            field_dict["base_asset_symbol"] = base_asset_symbol
        if base_asset_contract_address is not UNSET:
            field_dict["base_asset_contract_address"] = base_asset_contract_address
        if quote_asset_id is not UNSET:
            field_dict["quote_asset_id"] = quote_asset_id
        if quote_asset_ucid is not UNSET:
            field_dict["quote_asset_ucid"] = quote_asset_ucid
        if quote_asset_name is not UNSET:
            field_dict["quote_asset_name"] = quote_asset_name
        if quote_asset_symbol is not UNSET:
            field_dict["quote_asset_symbol"] = quote_asset_symbol
        if quote_asset_contract_address is not UNSET:
            field_dict["quote_asset_contract_address"] = quote_asset_contract_address
        if dex_id is not UNSET:
            field_dict["dex_id"] = dex_id
        if dex_slug is not UNSET:
            field_dict["dex_slug"] = dex_slug
        if network_id is not UNSET:
            field_dict["network_id"] = network_id
        if network_slug is not UNSET:
            field_dict["network_slug"] = network_slug
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if num_transactions_24h is not UNSET:
            field_dict["num_transactions_24h"] = num_transactions_24h
        if holders is not UNSET:
            field_dict["holders"] = holders
        if field_24h_no_of_buys is not UNSET:
            field_dict["24h_no_of_buys"] = field_24h_no_of_buys
        if field_24h_no_of_sells is not UNSET:
            field_dict["24h_no_of_sells"] = field_24h_no_of_sells
        if pool_created is not UNSET:
            field_dict["pool_created"] = pool_created
        if buy_tax is not UNSET:
            field_dict["buy_tax"] = buy_tax
        if sell_tax is not UNSET:
            field_dict["sell_tax"] = sell_tax
        if security_scan is not UNSET:
            field_dict["security_scan"] = security_scan
        if pool_base_asset is not UNSET:
            field_dict["pool_base_asset"] = pool_base_asset
        if pool_quote_asset is not UNSET:
            field_dict["pool_quote_asset"] = pool_quote_asset
        if percent_pooled_base_asset is not UNSET:
            field_dict["percent_pooled_base_asset"] = percent_pooled_base_asset
        if field_24h_volume_quote_asset is not UNSET:
            field_dict["24h_volume_quote_asset"] = field_24h_volume_quote_asset
        if total_supply_quote_asset is not UNSET:
            field_dict["total_supply_quote_asset"] = total_supply_quote_asset
        if total_supply_base_asset is not UNSET:
            field_dict["total_supply_base_asset"] = total_supply_base_asset
        if date_launched is not UNSET:
            field_dict["date_launched"] = date_launched

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dex_pairs_ohlcv_historical_quotes import DexPairsOhlcvHistoricalQuotes
        from ..models.security_scan_result import SecurityScanResult

        d = dict(src_dict)
        _quotes = d.pop("quotes", UNSET)
        quotes: list[DexPairsOhlcvHistoricalQuotes] | Unset = UNSET
        if _quotes is not UNSET:
            quotes = []
            for quotes_item_data in _quotes:
                quotes_item = DexPairsOhlcvHistoricalQuotes.from_dict(quotes_item_data)

                quotes.append(quotes_item)

        contract_address = d.pop("contract_address", UNSET)

        name = d.pop("name", UNSET)

        base_asset_id = d.pop("base_asset_id", UNSET)

        base_asset_ucid = d.pop("base_asset_ucid", UNSET)

        base_asset_name = d.pop("base_asset_name", UNSET)

        base_asset_symbol = d.pop("base_asset_symbol", UNSET)

        base_asset_contract_address = d.pop("base_asset_contract_address", UNSET)

        quote_asset_id = d.pop("quote_asset_id", UNSET)

        quote_asset_ucid = d.pop("quote_asset_ucid", UNSET)

        quote_asset_name = d.pop("quote_asset_name", UNSET)

        quote_asset_symbol = d.pop("quote_asset_symbol", UNSET)

        quote_asset_contract_address = d.pop("quote_asset_contract_address", UNSET)

        dex_id = d.pop("dex_id", UNSET)

        dex_slug = d.pop("dex_slug", UNSET)

        network_id = d.pop("network_id", UNSET)

        network_slug = d.pop("network_slug", UNSET)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        num_transactions_24h = d.pop("num_transactions_24h", UNSET)

        holders = d.pop("holders", UNSET)

        field_24h_no_of_buys = d.pop("24h_no_of_buys", UNSET)

        field_24h_no_of_sells = d.pop("24h_no_of_sells", UNSET)

        _pool_created = d.pop("pool_created", UNSET)
        pool_created: datetime.datetime | Unset
        if isinstance(_pool_created, Unset):
            pool_created = UNSET
        else:
            pool_created = isoparse(_pool_created)

        buy_tax = d.pop("buy_tax", UNSET)

        sell_tax = d.pop("sell_tax", UNSET)

        _security_scan = d.pop("security_scan", UNSET)
        security_scan: list[SecurityScanResult] | Unset = UNSET
        if _security_scan is not UNSET:
            security_scan = []
            for security_scan_item_data in _security_scan:
                security_scan_item = SecurityScanResult.from_dict(security_scan_item_data)

                security_scan.append(security_scan_item)

        pool_base_asset = d.pop("pool_base_asset", UNSET)

        pool_quote_asset = d.pop("pool_quote_asset", UNSET)

        percent_pooled_base_asset = d.pop("percent_pooled_base_asset", UNSET)

        field_24h_volume_quote_asset = d.pop("24h_volume_quote_asset", UNSET)

        total_supply_quote_asset = d.pop("total_supply_quote_asset", UNSET)

        total_supply_base_asset = d.pop("total_supply_base_asset", UNSET)

        _date_launched = d.pop("date_launched", UNSET)
        date_launched: datetime.datetime | Unset
        if isinstance(_date_launched, Unset):
            date_launched = UNSET
        else:
            date_launched = isoparse(_date_launched)

        dex_pairs_ohlcv_historical_dto = cls(
            quotes=quotes,
            contract_address=contract_address,
            name=name,
            base_asset_id=base_asset_id,
            base_asset_ucid=base_asset_ucid,
            base_asset_name=base_asset_name,
            base_asset_symbol=base_asset_symbol,
            base_asset_contract_address=base_asset_contract_address,
            quote_asset_id=quote_asset_id,
            quote_asset_ucid=quote_asset_ucid,
            quote_asset_name=quote_asset_name,
            quote_asset_symbol=quote_asset_symbol,
            quote_asset_contract_address=quote_asset_contract_address,
            dex_id=dex_id,
            dex_slug=dex_slug,
            network_id=network_id,
            network_slug=network_slug,
            last_updated=last_updated,
            created_at=created_at,
            num_transactions_24h=num_transactions_24h,
            holders=holders,
            field_24h_no_of_buys=field_24h_no_of_buys,
            field_24h_no_of_sells=field_24h_no_of_sells,
            pool_created=pool_created,
            buy_tax=buy_tax,
            sell_tax=sell_tax,
            security_scan=security_scan,
            pool_base_asset=pool_base_asset,
            pool_quote_asset=pool_quote_asset,
            percent_pooled_base_asset=percent_pooled_base_asset,
            field_24h_volume_quote_asset=field_24h_volume_quote_asset,
            total_supply_quote_asset=total_supply_quote_asset,
            total_supply_base_asset=total_supply_base_asset,
            date_launched=date_launched,
        )

        dex_pairs_ohlcv_historical_dto.additional_properties = d
        return dex_pairs_ohlcv_historical_dto

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
