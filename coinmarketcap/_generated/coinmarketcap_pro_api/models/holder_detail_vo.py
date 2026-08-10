from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HolderDetailVO")


@_attrs_define
class HolderDetailVO:
    """
    Attributes:
        block_height (int | Unset):
        first_active_time (int | Unset):
        net_buy_amount (str | Unset):
        realized_pnl_percent (str | Unset):
        spot_position (str | Unset):
        buy_volume (str | Unset):
        sell_volume (str | Unset):
        buy_usd (str | Unset):
        sell_usd (str | Unset):
        buy_count (str | Unset):
        sell_count (str | Unset):
        avg_buy_price_usd (str | Unset):
        avg_sell_price_usd (str | Unset):
        realized_pnl (str | Unset):
        actual_balance (str | Unset):
        price (str | Unset):
        wallet_address (str | Unset):
        token_address (str | Unset):
        platform_id (int | Unset):
        percent (str | Unset):
        balance (str | Unset):
        total_supply (str | Unset):
        token_account (str | Unset):
        logo_url (str | Unset):
        name (str | Unset):
        public_name (str | Unset):
        tags (str | Unset):
        address_explorer_url (str | Unset):
        symbol (str | Unset):
        native_balance (str | Unset):
        funding_source (str | Unset):
        funding_time (int | Unset):
        last_active_time (int | Unset):
        wallet_create_time (int | Unset):
        spot_open_ts (int | Unset):
        spot_clearance_ts (int | Unset):
        token_logo (str | Unset):
        token_symbol (str | Unset):
        platform_crypto_id (int | Unset):
        dexer_platform_name (str | Unset):
        low_liquidity_flag (int | Unset):
        meme_pump_inner_flag (int | Unset):
        black_list_flag (int | Unset):
        stable_coin_flag (int | Unset):
        risk_level_flag (int | Unset):
    """

    block_height: int | Unset = UNSET
    first_active_time: int | Unset = UNSET
    net_buy_amount: str | Unset = UNSET
    realized_pnl_percent: str | Unset = UNSET
    spot_position: str | Unset = UNSET
    buy_volume: str | Unset = UNSET
    sell_volume: str | Unset = UNSET
    buy_usd: str | Unset = UNSET
    sell_usd: str | Unset = UNSET
    buy_count: str | Unset = UNSET
    sell_count: str | Unset = UNSET
    avg_buy_price_usd: str | Unset = UNSET
    avg_sell_price_usd: str | Unset = UNSET
    realized_pnl: str | Unset = UNSET
    actual_balance: str | Unset = UNSET
    price: str | Unset = UNSET
    wallet_address: str | Unset = UNSET
    token_address: str | Unset = UNSET
    platform_id: int | Unset = UNSET
    percent: str | Unset = UNSET
    balance: str | Unset = UNSET
    total_supply: str | Unset = UNSET
    token_account: str | Unset = UNSET
    logo_url: str | Unset = UNSET
    name: str | Unset = UNSET
    public_name: str | Unset = UNSET
    tags: str | Unset = UNSET
    address_explorer_url: str | Unset = UNSET
    symbol: str | Unset = UNSET
    native_balance: str | Unset = UNSET
    funding_source: str | Unset = UNSET
    funding_time: int | Unset = UNSET
    last_active_time: int | Unset = UNSET
    wallet_create_time: int | Unset = UNSET
    spot_open_ts: int | Unset = UNSET
    spot_clearance_ts: int | Unset = UNSET
    token_logo: str | Unset = UNSET
    token_symbol: str | Unset = UNSET
    platform_crypto_id: int | Unset = UNSET
    dexer_platform_name: str | Unset = UNSET
    low_liquidity_flag: int | Unset = UNSET
    meme_pump_inner_flag: int | Unset = UNSET
    black_list_flag: int | Unset = UNSET
    stable_coin_flag: int | Unset = UNSET
    risk_level_flag: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        block_height = self.block_height

        first_active_time = self.first_active_time

        net_buy_amount = self.net_buy_amount

        realized_pnl_percent = self.realized_pnl_percent

        spot_position = self.spot_position

        buy_volume = self.buy_volume

        sell_volume = self.sell_volume

        buy_usd = self.buy_usd

        sell_usd = self.sell_usd

        buy_count = self.buy_count

        sell_count = self.sell_count

        avg_buy_price_usd = self.avg_buy_price_usd

        avg_sell_price_usd = self.avg_sell_price_usd

        realized_pnl = self.realized_pnl

        actual_balance = self.actual_balance

        price = self.price

        wallet_address = self.wallet_address

        token_address = self.token_address

        platform_id = self.platform_id

        percent = self.percent

        balance = self.balance

        total_supply = self.total_supply

        token_account = self.token_account

        logo_url = self.logo_url

        name = self.name

        public_name = self.public_name

        tags = self.tags

        address_explorer_url = self.address_explorer_url

        symbol = self.symbol

        native_balance = self.native_balance

        funding_source = self.funding_source

        funding_time = self.funding_time

        last_active_time = self.last_active_time

        wallet_create_time = self.wallet_create_time

        spot_open_ts = self.spot_open_ts

        spot_clearance_ts = self.spot_clearance_ts

        token_logo = self.token_logo

        token_symbol = self.token_symbol

        platform_crypto_id = self.platform_crypto_id

        dexer_platform_name = self.dexer_platform_name

        low_liquidity_flag = self.low_liquidity_flag

        meme_pump_inner_flag = self.meme_pump_inner_flag

        black_list_flag = self.black_list_flag

        stable_coin_flag = self.stable_coin_flag

        risk_level_flag = self.risk_level_flag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if block_height is not UNSET:
            field_dict["blockHeight"] = block_height
        if first_active_time is not UNSET:
            field_dict["firstActiveTime"] = first_active_time
        if net_buy_amount is not UNSET:
            field_dict["netBuyAmount"] = net_buy_amount
        if realized_pnl_percent is not UNSET:
            field_dict["realizedPnlPercent"] = realized_pnl_percent
        if spot_position is not UNSET:
            field_dict["spotPosition"] = spot_position
        if buy_volume is not UNSET:
            field_dict["buyVolume"] = buy_volume
        if sell_volume is not UNSET:
            field_dict["sellVolume"] = sell_volume
        if buy_usd is not UNSET:
            field_dict["buyUsd"] = buy_usd
        if sell_usd is not UNSET:
            field_dict["sellUsd"] = sell_usd
        if buy_count is not UNSET:
            field_dict["buyCount"] = buy_count
        if sell_count is not UNSET:
            field_dict["sellCount"] = sell_count
        if avg_buy_price_usd is not UNSET:
            field_dict["avgBuyPriceUsd"] = avg_buy_price_usd
        if avg_sell_price_usd is not UNSET:
            field_dict["avgSellPriceUsd"] = avg_sell_price_usd
        if realized_pnl is not UNSET:
            field_dict["realizedPnl"] = realized_pnl
        if actual_balance is not UNSET:
            field_dict["actualBalance"] = actual_balance
        if price is not UNSET:
            field_dict["price"] = price
        if wallet_address is not UNSET:
            field_dict["walletAddress"] = wallet_address
        if token_address is not UNSET:
            field_dict["tokenAddress"] = token_address
        if platform_id is not UNSET:
            field_dict["platformId"] = platform_id
        if percent is not UNSET:
            field_dict["percent"] = percent
        if balance is not UNSET:
            field_dict["balance"] = balance
        if total_supply is not UNSET:
            field_dict["totalSupply"] = total_supply
        if token_account is not UNSET:
            field_dict["tokenAccount"] = token_account
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if name is not UNSET:
            field_dict["name"] = name
        if public_name is not UNSET:
            field_dict["publicName"] = public_name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if address_explorer_url is not UNSET:
            field_dict["addressExplorerUrl"] = address_explorer_url
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if native_balance is not UNSET:
            field_dict["nativeBalance"] = native_balance
        if funding_source is not UNSET:
            field_dict["fundingSource"] = funding_source
        if funding_time is not UNSET:
            field_dict["fundingTime"] = funding_time
        if last_active_time is not UNSET:
            field_dict["lastActiveTime"] = last_active_time
        if wallet_create_time is not UNSET:
            field_dict["walletCreateTime"] = wallet_create_time
        if spot_open_ts is not UNSET:
            field_dict["spotOpenTs"] = spot_open_ts
        if spot_clearance_ts is not UNSET:
            field_dict["spotClearanceTs"] = spot_clearance_ts
        if token_logo is not UNSET:
            field_dict["tokenLogo"] = token_logo
        if token_symbol is not UNSET:
            field_dict["tokenSymbol"] = token_symbol
        if platform_crypto_id is not UNSET:
            field_dict["platformCryptoId"] = platform_crypto_id
        if dexer_platform_name is not UNSET:
            field_dict["dexerPlatformName"] = dexer_platform_name
        if low_liquidity_flag is not UNSET:
            field_dict["lowLiquidityFlag"] = low_liquidity_flag
        if meme_pump_inner_flag is not UNSET:
            field_dict["memePumpInnerFlag"] = meme_pump_inner_flag
        if black_list_flag is not UNSET:
            field_dict["blackListFlag"] = black_list_flag
        if stable_coin_flag is not UNSET:
            field_dict["stableCoinFlag"] = stable_coin_flag
        if risk_level_flag is not UNSET:
            field_dict["riskLevelFlag"] = risk_level_flag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        block_height = d.pop("blockHeight", UNSET)

        first_active_time = d.pop("firstActiveTime", UNSET)

        net_buy_amount = d.pop("netBuyAmount", UNSET)

        realized_pnl_percent = d.pop("realizedPnlPercent", UNSET)

        spot_position = d.pop("spotPosition", UNSET)

        buy_volume = d.pop("buyVolume", UNSET)

        sell_volume = d.pop("sellVolume", UNSET)

        buy_usd = d.pop("buyUsd", UNSET)

        sell_usd = d.pop("sellUsd", UNSET)

        buy_count = d.pop("buyCount", UNSET)

        sell_count = d.pop("sellCount", UNSET)

        avg_buy_price_usd = d.pop("avgBuyPriceUsd", UNSET)

        avg_sell_price_usd = d.pop("avgSellPriceUsd", UNSET)

        realized_pnl = d.pop("realizedPnl", UNSET)

        actual_balance = d.pop("actualBalance", UNSET)

        price = d.pop("price", UNSET)

        wallet_address = d.pop("walletAddress", UNSET)

        token_address = d.pop("tokenAddress", UNSET)

        platform_id = d.pop("platformId", UNSET)

        percent = d.pop("percent", UNSET)

        balance = d.pop("balance", UNSET)

        total_supply = d.pop("totalSupply", UNSET)

        token_account = d.pop("tokenAccount", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        name = d.pop("name", UNSET)

        public_name = d.pop("publicName", UNSET)

        tags = d.pop("tags", UNSET)

        address_explorer_url = d.pop("addressExplorerUrl", UNSET)

        symbol = d.pop("symbol", UNSET)

        native_balance = d.pop("nativeBalance", UNSET)

        funding_source = d.pop("fundingSource", UNSET)

        funding_time = d.pop("fundingTime", UNSET)

        last_active_time = d.pop("lastActiveTime", UNSET)

        wallet_create_time = d.pop("walletCreateTime", UNSET)

        spot_open_ts = d.pop("spotOpenTs", UNSET)

        spot_clearance_ts = d.pop("spotClearanceTs", UNSET)

        token_logo = d.pop("tokenLogo", UNSET)

        token_symbol = d.pop("tokenSymbol", UNSET)

        platform_crypto_id = d.pop("platformCryptoId", UNSET)

        dexer_platform_name = d.pop("dexerPlatformName", UNSET)

        low_liquidity_flag = d.pop("lowLiquidityFlag", UNSET)

        meme_pump_inner_flag = d.pop("memePumpInnerFlag", UNSET)

        black_list_flag = d.pop("blackListFlag", UNSET)

        stable_coin_flag = d.pop("stableCoinFlag", UNSET)

        risk_level_flag = d.pop("riskLevelFlag", UNSET)

        holder_detail_vo = cls(
            block_height=block_height,
            first_active_time=first_active_time,
            net_buy_amount=net_buy_amount,
            realized_pnl_percent=realized_pnl_percent,
            spot_position=spot_position,
            buy_volume=buy_volume,
            sell_volume=sell_volume,
            buy_usd=buy_usd,
            sell_usd=sell_usd,
            buy_count=buy_count,
            sell_count=sell_count,
            avg_buy_price_usd=avg_buy_price_usd,
            avg_sell_price_usd=avg_sell_price_usd,
            realized_pnl=realized_pnl,
            actual_balance=actual_balance,
            price=price,
            wallet_address=wallet_address,
            token_address=token_address,
            platform_id=platform_id,
            percent=percent,
            balance=balance,
            total_supply=total_supply,
            token_account=token_account,
            logo_url=logo_url,
            name=name,
            public_name=public_name,
            tags=tags,
            address_explorer_url=address_explorer_url,
            symbol=symbol,
            native_balance=native_balance,
            funding_source=funding_source,
            funding_time=funding_time,
            last_active_time=last_active_time,
            wallet_create_time=wallet_create_time,
            spot_open_ts=spot_open_ts,
            spot_clearance_ts=spot_clearance_ts,
            token_logo=token_logo,
            token_symbol=token_symbol,
            platform_crypto_id=platform_crypto_id,
            dexer_platform_name=dexer_platform_name,
            low_liquidity_flag=low_liquidity_flag,
            meme_pump_inner_flag=meme_pump_inner_flag,
            black_list_flag=black_list_flag,
            stable_coin_flag=stable_coin_flag,
            risk_level_flag=risk_level_flag,
        )

        holder_detail_vo.additional_properties = d
        return holder_detail_vo

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
