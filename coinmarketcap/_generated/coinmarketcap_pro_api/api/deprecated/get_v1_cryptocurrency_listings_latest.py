from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cryptocurrency_listings_latest_response_model_1 import CryptocurrencyListingsLatestResponseModel1
from ...models.get_v1_cryptocurrency_listings_latest_cryptocurrency_type import (
    GetV1CryptocurrencyListingsLatestCryptocurrencyType,
)
from ...models.get_v1_cryptocurrency_listings_latest_sort import (
    GetV1CryptocurrencyListingsLatestSort,
)
from ...models.get_v1_cryptocurrency_listings_latest_sort_dir import (
    GetV1CryptocurrencyListingsLatestSortDir,
)
from ...models.get_v1_cryptocurrency_listings_latest_tag import (
    GetV1CryptocurrencyListingsLatestTag,
)
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    price_min: float | Unset = UNSET,
    price_max: float | Unset = UNSET,
    market_cap_min: float | Unset = UNSET,
    market_cap_max: float | Unset = UNSET,
    volume_24h_min: float | Unset = UNSET,
    volume_24h_max: float | Unset = UNSET,
    circulating_supply_min: float | Unset = UNSET,
    circulating_supply_max: float | Unset = UNSET,
    percent_change_24h_min: float | Unset = UNSET,
    percent_change_24h_max: float | Unset = UNSET,
    self_reported_circulating_supply_min: float | None | Unset = UNSET,
    self_reported_circulating_supply_max: float | None | Unset = UNSET,
    self_reported_market_cap_min: float | Unset = UNSET,
    self_reported_market_cap_max: float | Unset = UNSET,
    unlocked_market_cap_min: float | Unset = UNSET,
    unlocked_market_cap_max: float | Unset = UNSET,
    unlocked_circulating_supply_min: float | Unset = UNSET,
    unlocked_circulating_supply_max: float | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: GetV1CryptocurrencyListingsLatestSort | Unset = "market_cap",
    sort_dir: GetV1CryptocurrencyListingsLatestSortDir | Unset = UNSET,
    cryptocurrency_type: GetV1CryptocurrencyListingsLatestCryptocurrencyType | Unset = "all",
    tag: GetV1CryptocurrencyListingsLatestTag | Unset = "all",
    aux: str | Unset = "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["start"] = start

    params["limit"] = limit

    params["price_min"] = price_min

    params["price_max"] = price_max

    params["market_cap_min"] = market_cap_min

    params["market_cap_max"] = market_cap_max

    params["volume_24h_min"] = volume_24h_min

    params["volume_24h_max"] = volume_24h_max

    params["circulating_supply_min"] = circulating_supply_min

    params["circulating_supply_max"] = circulating_supply_max

    params["percent_change_24h_min"] = percent_change_24h_min

    params["percent_change_24h_max"] = percent_change_24h_max

    json_self_reported_circulating_supply_min: float | None | Unset
    if isinstance(self_reported_circulating_supply_min, Unset):
        json_self_reported_circulating_supply_min = UNSET
    else:
        json_self_reported_circulating_supply_min = self_reported_circulating_supply_min
    params["self_reported_circulating_supply_min"] = json_self_reported_circulating_supply_min

    json_self_reported_circulating_supply_max: float | None | Unset
    if isinstance(self_reported_circulating_supply_max, Unset):
        json_self_reported_circulating_supply_max = UNSET
    else:
        json_self_reported_circulating_supply_max = self_reported_circulating_supply_max
    params["self_reported_circulating_supply_max"] = json_self_reported_circulating_supply_max

    params["self_reported_market_cap_min"] = self_reported_market_cap_min

    params["self_reported_market_cap_max"] = self_reported_market_cap_max

    params["unlocked_market_cap_min"] = unlocked_market_cap_min

    params["unlocked_market_cap_max"] = unlocked_market_cap_max

    params["unlocked_circulating_supply_min"] = unlocked_circulating_supply_min

    params["unlocked_circulating_supply_max"] = unlocked_circulating_supply_max

    params["convert"] = convert

    params["convert_id"] = convert_id

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_sort_dir: str | Unset = UNSET
    if not isinstance(sort_dir, Unset):
        json_sort_dir = sort_dir

    params["sort_dir"] = json_sort_dir

    json_cryptocurrency_type: str | Unset = UNSET
    if not isinstance(cryptocurrency_type, Unset):
        json_cryptocurrency_type = cryptocurrency_type

    params["cryptocurrency_type"] = json_cryptocurrency_type

    json_tag: str | Unset = UNSET
    if not isinstance(tag, Unset):
        json_tag = tag

    params["tag"] = json_tag

    params["aux"] = aux

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/cryptocurrency/listings/latest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CryptocurrencyListingsLatestResponseModel1
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = CryptocurrencyListingsLatestResponseModel1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = HTTPStatus400ErrorObject.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = HTTPStatus401ErrorObject.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = HTTPStatus403ErrorObject.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = HTTPStatus429ErrorObject.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = HTTPStatus500ErrorObject.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CryptocurrencyListingsLatestResponseModel1
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    price_min: float | Unset = UNSET,
    price_max: float | Unset = UNSET,
    market_cap_min: float | Unset = UNSET,
    market_cap_max: float | Unset = UNSET,
    volume_24h_min: float | Unset = UNSET,
    volume_24h_max: float | Unset = UNSET,
    circulating_supply_min: float | Unset = UNSET,
    circulating_supply_max: float | Unset = UNSET,
    percent_change_24h_min: float | Unset = UNSET,
    percent_change_24h_max: float | Unset = UNSET,
    self_reported_circulating_supply_min: float | None | Unset = UNSET,
    self_reported_circulating_supply_max: float | None | Unset = UNSET,
    self_reported_market_cap_min: float | Unset = UNSET,
    self_reported_market_cap_max: float | Unset = UNSET,
    unlocked_market_cap_min: float | Unset = UNSET,
    unlocked_market_cap_max: float | Unset = UNSET,
    unlocked_circulating_supply_min: float | Unset = UNSET,
    unlocked_circulating_supply_max: float | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: GetV1CryptocurrencyListingsLatestSort | Unset = "market_cap",
    sort_dir: GetV1CryptocurrencyListingsLatestSortDir | Unset = UNSET,
    cryptocurrency_type: GetV1CryptocurrencyListingsLatestCryptocurrencyType | Unset = "all",
    tag: GetV1CryptocurrencyListingsLatestTag | Unset = "all",
    aux: str | Unset = "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply",
) -> Response[
    CryptocurrencyListingsLatestResponseModel1
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Listings Latest v1 (deprecated)

     Returns a paginated list of all active cryptocurrencies with latest market data. The default
    \"market_cap\" sort returns cryptocurrency in order of CoinMarketCap's market cap rank (as outlined
    in [our methodology](https://coinmarketcap.com/methodology/)) but you may configure this call to
    order by another market ranking field. Use the \"convert\" option to return market values in
    multiple fiat and cryptocurrency conversions in the same call.


    You may sort against any of the following:
    **market_cap**: CoinMarketCap's market cap rank as outlined in [our
    methodology](https://coinmarketcap.com/methodology/).
    **market_cap_strict**: A strict market cap sort (latest trade price x circulating supply).
    **name**: The cryptocurrency name.
    **symbol**: The cryptocurrency symbol.
    **date_added**: Date cryptocurrency was added to the system.
    **price**: latest average trade price across markets.
    **circulating_supply**: approximate number of coins currently in circulation.
    **total_supply**: approximate total amount of coins in existence right now (minus any coins that
    have been verifiably burned).
    **max_supply**: our best approximation of the maximum amount of coins that will ever exist in the
    lifetime of the currency.
    **num_market_pairs**: number of market pairs across all exchanges trading each currency.
    **market_cap_by_total_supply_strict**: market cap by total supply.
    **volume_24h**: rolling 24 hour adjusted trading volume.
    **volume_7d**: rolling 24 hour adjusted trading volume.
    **volume_30d**: rolling 24 hour adjusted trading volume.
    **percent_change_1h**: 1 hour trading price percentage change for each currency.
    **percent_change_24h**: 24 hour trading price percentage change for each currency.
    **percent_change_7d**: 7 day trading price percentage change for each currency.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our latest cryptocurrency listing and ranking pages like
    [coinmarketcap.com/all/views/all/](https://coinmarketcap.com/all/views/all/),
    [coinmarketcap.com/tokens/](https://coinmarketcap.com/tokens/), [coinmarketcap.com/gainers-
    losers/](https://coinmarketcap.com/gainers-losers/),
    [coinmarketcap.com/new/](https://coinmarketcap.com/new/).

    ***NOTE:** Use this endpoint if you need a sorted and paginated list of all cryptocurrencies. If you
    want to query for market data on a few specific cryptocurrencies use
    `/v1/cryptocurrency/quotes/latest` which is optimized for that purpose. The response data between
    these endpoints is otherwise the same.*

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        price_min (float | Unset):
        price_max (float | Unset):
        market_cap_min (float | Unset):
        market_cap_max (float | Unset):
        volume_24h_min (float | Unset):
        volume_24h_max (float | Unset):
        circulating_supply_min (float | Unset):
        circulating_supply_max (float | Unset):
        percent_change_24h_min (float | Unset):
        percent_change_24h_max (float | Unset):
        self_reported_circulating_supply_min (float | None | Unset):
        self_reported_circulating_supply_max (float | None | Unset):
        self_reported_market_cap_min (float | Unset):
        self_reported_market_cap_max (float | Unset):
        unlocked_market_cap_min (float | Unset):
        unlocked_market_cap_max (float | Unset):
        unlocked_circulating_supply_min (float | Unset):
        unlocked_circulating_supply_max (float | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        sort (GetV1CryptocurrencyListingsLatestSort | Unset):  Default: 'market_cap'.
        sort_dir (GetV1CryptocurrencyListingsLatestSortDir | Unset):
        cryptocurrency_type (GetV1CryptocurrencyListingsLatestCryptocurrencyType | Unset):
            Default: 'all'.
        tag (GetV1CryptocurrencyListingsLatestTag | Unset):  Default: 'all'.
        aux (str | Unset):  Default: 'num_market_pairs,cmc_rank,date_added,tags,platform,max_suppl
            y,circulating_supply,total_supply'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyListingsLatestResponseModel1 | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
        price_min=price_min,
        price_max=price_max,
        market_cap_min=market_cap_min,
        market_cap_max=market_cap_max,
        volume_24h_min=volume_24h_min,
        volume_24h_max=volume_24h_max,
        circulating_supply_min=circulating_supply_min,
        circulating_supply_max=circulating_supply_max,
        percent_change_24h_min=percent_change_24h_min,
        percent_change_24h_max=percent_change_24h_max,
        self_reported_circulating_supply_min=self_reported_circulating_supply_min,
        self_reported_circulating_supply_max=self_reported_circulating_supply_max,
        self_reported_market_cap_min=self_reported_market_cap_min,
        self_reported_market_cap_max=self_reported_market_cap_max,
        unlocked_market_cap_min=unlocked_market_cap_min,
        unlocked_market_cap_max=unlocked_market_cap_max,
        unlocked_circulating_supply_min=unlocked_circulating_supply_min,
        unlocked_circulating_supply_max=unlocked_circulating_supply_max,
        convert=convert,
        convert_id=convert_id,
        sort=sort,
        sort_dir=sort_dir,
        cryptocurrency_type=cryptocurrency_type,
        tag=tag,
        aux=aux,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    price_min: float | Unset = UNSET,
    price_max: float | Unset = UNSET,
    market_cap_min: float | Unset = UNSET,
    market_cap_max: float | Unset = UNSET,
    volume_24h_min: float | Unset = UNSET,
    volume_24h_max: float | Unset = UNSET,
    circulating_supply_min: float | Unset = UNSET,
    circulating_supply_max: float | Unset = UNSET,
    percent_change_24h_min: float | Unset = UNSET,
    percent_change_24h_max: float | Unset = UNSET,
    self_reported_circulating_supply_min: float | None | Unset = UNSET,
    self_reported_circulating_supply_max: float | None | Unset = UNSET,
    self_reported_market_cap_min: float | Unset = UNSET,
    self_reported_market_cap_max: float | Unset = UNSET,
    unlocked_market_cap_min: float | Unset = UNSET,
    unlocked_market_cap_max: float | Unset = UNSET,
    unlocked_circulating_supply_min: float | Unset = UNSET,
    unlocked_circulating_supply_max: float | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: GetV1CryptocurrencyListingsLatestSort | Unset = "market_cap",
    sort_dir: GetV1CryptocurrencyListingsLatestSortDir | Unset = UNSET,
    cryptocurrency_type: GetV1CryptocurrencyListingsLatestCryptocurrencyType | Unset = "all",
    tag: GetV1CryptocurrencyListingsLatestTag | Unset = "all",
    aux: str | Unset = "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply",
) -> (
    CryptocurrencyListingsLatestResponseModel1
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Listings Latest v1 (deprecated)

     Returns a paginated list of all active cryptocurrencies with latest market data. The default
    \"market_cap\" sort returns cryptocurrency in order of CoinMarketCap's market cap rank (as outlined
    in [our methodology](https://coinmarketcap.com/methodology/)) but you may configure this call to
    order by another market ranking field. Use the \"convert\" option to return market values in
    multiple fiat and cryptocurrency conversions in the same call.


    You may sort against any of the following:
    **market_cap**: CoinMarketCap's market cap rank as outlined in [our
    methodology](https://coinmarketcap.com/methodology/).
    **market_cap_strict**: A strict market cap sort (latest trade price x circulating supply).
    **name**: The cryptocurrency name.
    **symbol**: The cryptocurrency symbol.
    **date_added**: Date cryptocurrency was added to the system.
    **price**: latest average trade price across markets.
    **circulating_supply**: approximate number of coins currently in circulation.
    **total_supply**: approximate total amount of coins in existence right now (minus any coins that
    have been verifiably burned).
    **max_supply**: our best approximation of the maximum amount of coins that will ever exist in the
    lifetime of the currency.
    **num_market_pairs**: number of market pairs across all exchanges trading each currency.
    **market_cap_by_total_supply_strict**: market cap by total supply.
    **volume_24h**: rolling 24 hour adjusted trading volume.
    **volume_7d**: rolling 24 hour adjusted trading volume.
    **volume_30d**: rolling 24 hour adjusted trading volume.
    **percent_change_1h**: 1 hour trading price percentage change for each currency.
    **percent_change_24h**: 24 hour trading price percentage change for each currency.
    **percent_change_7d**: 7 day trading price percentage change for each currency.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our latest cryptocurrency listing and ranking pages like
    [coinmarketcap.com/all/views/all/](https://coinmarketcap.com/all/views/all/),
    [coinmarketcap.com/tokens/](https://coinmarketcap.com/tokens/), [coinmarketcap.com/gainers-
    losers/](https://coinmarketcap.com/gainers-losers/),
    [coinmarketcap.com/new/](https://coinmarketcap.com/new/).

    ***NOTE:** Use this endpoint if you need a sorted and paginated list of all cryptocurrencies. If you
    want to query for market data on a few specific cryptocurrencies use
    `/v1/cryptocurrency/quotes/latest` which is optimized for that purpose. The response data between
    these endpoints is otherwise the same.*

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        price_min (float | Unset):
        price_max (float | Unset):
        market_cap_min (float | Unset):
        market_cap_max (float | Unset):
        volume_24h_min (float | Unset):
        volume_24h_max (float | Unset):
        circulating_supply_min (float | Unset):
        circulating_supply_max (float | Unset):
        percent_change_24h_min (float | Unset):
        percent_change_24h_max (float | Unset):
        self_reported_circulating_supply_min (float | None | Unset):
        self_reported_circulating_supply_max (float | None | Unset):
        self_reported_market_cap_min (float | Unset):
        self_reported_market_cap_max (float | Unset):
        unlocked_market_cap_min (float | Unset):
        unlocked_market_cap_max (float | Unset):
        unlocked_circulating_supply_min (float | Unset):
        unlocked_circulating_supply_max (float | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        sort (GetV1CryptocurrencyListingsLatestSort | Unset):  Default: 'market_cap'.
        sort_dir (GetV1CryptocurrencyListingsLatestSortDir | Unset):
        cryptocurrency_type (GetV1CryptocurrencyListingsLatestCryptocurrencyType | Unset):
            Default: 'all'.
        tag (GetV1CryptocurrencyListingsLatestTag | Unset):  Default: 'all'.
        aux (str | Unset):  Default: 'num_market_pairs,cmc_rank,date_added,tags,platform,max_suppl
            y,circulating_supply,total_supply'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyListingsLatestResponseModel1 | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        start=start,
        limit=limit,
        price_min=price_min,
        price_max=price_max,
        market_cap_min=market_cap_min,
        market_cap_max=market_cap_max,
        volume_24h_min=volume_24h_min,
        volume_24h_max=volume_24h_max,
        circulating_supply_min=circulating_supply_min,
        circulating_supply_max=circulating_supply_max,
        percent_change_24h_min=percent_change_24h_min,
        percent_change_24h_max=percent_change_24h_max,
        self_reported_circulating_supply_min=self_reported_circulating_supply_min,
        self_reported_circulating_supply_max=self_reported_circulating_supply_max,
        self_reported_market_cap_min=self_reported_market_cap_min,
        self_reported_market_cap_max=self_reported_market_cap_max,
        unlocked_market_cap_min=unlocked_market_cap_min,
        unlocked_market_cap_max=unlocked_market_cap_max,
        unlocked_circulating_supply_min=unlocked_circulating_supply_min,
        unlocked_circulating_supply_max=unlocked_circulating_supply_max,
        convert=convert,
        convert_id=convert_id,
        sort=sort,
        sort_dir=sort_dir,
        cryptocurrency_type=cryptocurrency_type,
        tag=tag,
        aux=aux,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    price_min: float | Unset = UNSET,
    price_max: float | Unset = UNSET,
    market_cap_min: float | Unset = UNSET,
    market_cap_max: float | Unset = UNSET,
    volume_24h_min: float | Unset = UNSET,
    volume_24h_max: float | Unset = UNSET,
    circulating_supply_min: float | Unset = UNSET,
    circulating_supply_max: float | Unset = UNSET,
    percent_change_24h_min: float | Unset = UNSET,
    percent_change_24h_max: float | Unset = UNSET,
    self_reported_circulating_supply_min: float | None | Unset = UNSET,
    self_reported_circulating_supply_max: float | None | Unset = UNSET,
    self_reported_market_cap_min: float | Unset = UNSET,
    self_reported_market_cap_max: float | Unset = UNSET,
    unlocked_market_cap_min: float | Unset = UNSET,
    unlocked_market_cap_max: float | Unset = UNSET,
    unlocked_circulating_supply_min: float | Unset = UNSET,
    unlocked_circulating_supply_max: float | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: GetV1CryptocurrencyListingsLatestSort | Unset = "market_cap",
    sort_dir: GetV1CryptocurrencyListingsLatestSortDir | Unset = UNSET,
    cryptocurrency_type: GetV1CryptocurrencyListingsLatestCryptocurrencyType | Unset = "all",
    tag: GetV1CryptocurrencyListingsLatestTag | Unset = "all",
    aux: str | Unset = "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply",
) -> Response[
    CryptocurrencyListingsLatestResponseModel1
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Listings Latest v1 (deprecated)

     Returns a paginated list of all active cryptocurrencies with latest market data. The default
    \"market_cap\" sort returns cryptocurrency in order of CoinMarketCap's market cap rank (as outlined
    in [our methodology](https://coinmarketcap.com/methodology/)) but you may configure this call to
    order by another market ranking field. Use the \"convert\" option to return market values in
    multiple fiat and cryptocurrency conversions in the same call.


    You may sort against any of the following:
    **market_cap**: CoinMarketCap's market cap rank as outlined in [our
    methodology](https://coinmarketcap.com/methodology/).
    **market_cap_strict**: A strict market cap sort (latest trade price x circulating supply).
    **name**: The cryptocurrency name.
    **symbol**: The cryptocurrency symbol.
    **date_added**: Date cryptocurrency was added to the system.
    **price**: latest average trade price across markets.
    **circulating_supply**: approximate number of coins currently in circulation.
    **total_supply**: approximate total amount of coins in existence right now (minus any coins that
    have been verifiably burned).
    **max_supply**: our best approximation of the maximum amount of coins that will ever exist in the
    lifetime of the currency.
    **num_market_pairs**: number of market pairs across all exchanges trading each currency.
    **market_cap_by_total_supply_strict**: market cap by total supply.
    **volume_24h**: rolling 24 hour adjusted trading volume.
    **volume_7d**: rolling 24 hour adjusted trading volume.
    **volume_30d**: rolling 24 hour adjusted trading volume.
    **percent_change_1h**: 1 hour trading price percentage change for each currency.
    **percent_change_24h**: 24 hour trading price percentage change for each currency.
    **percent_change_7d**: 7 day trading price percentage change for each currency.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our latest cryptocurrency listing and ranking pages like
    [coinmarketcap.com/all/views/all/](https://coinmarketcap.com/all/views/all/),
    [coinmarketcap.com/tokens/](https://coinmarketcap.com/tokens/), [coinmarketcap.com/gainers-
    losers/](https://coinmarketcap.com/gainers-losers/),
    [coinmarketcap.com/new/](https://coinmarketcap.com/new/).

    ***NOTE:** Use this endpoint if you need a sorted and paginated list of all cryptocurrencies. If you
    want to query for market data on a few specific cryptocurrencies use
    `/v1/cryptocurrency/quotes/latest` which is optimized for that purpose. The response data between
    these endpoints is otherwise the same.*

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        price_min (float | Unset):
        price_max (float | Unset):
        market_cap_min (float | Unset):
        market_cap_max (float | Unset):
        volume_24h_min (float | Unset):
        volume_24h_max (float | Unset):
        circulating_supply_min (float | Unset):
        circulating_supply_max (float | Unset):
        percent_change_24h_min (float | Unset):
        percent_change_24h_max (float | Unset):
        self_reported_circulating_supply_min (float | None | Unset):
        self_reported_circulating_supply_max (float | None | Unset):
        self_reported_market_cap_min (float | Unset):
        self_reported_market_cap_max (float | Unset):
        unlocked_market_cap_min (float | Unset):
        unlocked_market_cap_max (float | Unset):
        unlocked_circulating_supply_min (float | Unset):
        unlocked_circulating_supply_max (float | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        sort (GetV1CryptocurrencyListingsLatestSort | Unset):  Default: 'market_cap'.
        sort_dir (GetV1CryptocurrencyListingsLatestSortDir | Unset):
        cryptocurrency_type (GetV1CryptocurrencyListingsLatestCryptocurrencyType | Unset):
            Default: 'all'.
        tag (GetV1CryptocurrencyListingsLatestTag | Unset):  Default: 'all'.
        aux (str | Unset):  Default: 'num_market_pairs,cmc_rank,date_added,tags,platform,max_suppl
            y,circulating_supply,total_supply'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyListingsLatestResponseModel1 | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
        price_min=price_min,
        price_max=price_max,
        market_cap_min=market_cap_min,
        market_cap_max=market_cap_max,
        volume_24h_min=volume_24h_min,
        volume_24h_max=volume_24h_max,
        circulating_supply_min=circulating_supply_min,
        circulating_supply_max=circulating_supply_max,
        percent_change_24h_min=percent_change_24h_min,
        percent_change_24h_max=percent_change_24h_max,
        self_reported_circulating_supply_min=self_reported_circulating_supply_min,
        self_reported_circulating_supply_max=self_reported_circulating_supply_max,
        self_reported_market_cap_min=self_reported_market_cap_min,
        self_reported_market_cap_max=self_reported_market_cap_max,
        unlocked_market_cap_min=unlocked_market_cap_min,
        unlocked_market_cap_max=unlocked_market_cap_max,
        unlocked_circulating_supply_min=unlocked_circulating_supply_min,
        unlocked_circulating_supply_max=unlocked_circulating_supply_max,
        convert=convert,
        convert_id=convert_id,
        sort=sort,
        sort_dir=sort_dir,
        cryptocurrency_type=cryptocurrency_type,
        tag=tag,
        aux=aux,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    price_min: float | Unset = UNSET,
    price_max: float | Unset = UNSET,
    market_cap_min: float | Unset = UNSET,
    market_cap_max: float | Unset = UNSET,
    volume_24h_min: float | Unset = UNSET,
    volume_24h_max: float | Unset = UNSET,
    circulating_supply_min: float | Unset = UNSET,
    circulating_supply_max: float | Unset = UNSET,
    percent_change_24h_min: float | Unset = UNSET,
    percent_change_24h_max: float | Unset = UNSET,
    self_reported_circulating_supply_min: float | None | Unset = UNSET,
    self_reported_circulating_supply_max: float | None | Unset = UNSET,
    self_reported_market_cap_min: float | Unset = UNSET,
    self_reported_market_cap_max: float | Unset = UNSET,
    unlocked_market_cap_min: float | Unset = UNSET,
    unlocked_market_cap_max: float | Unset = UNSET,
    unlocked_circulating_supply_min: float | Unset = UNSET,
    unlocked_circulating_supply_max: float | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: GetV1CryptocurrencyListingsLatestSort | Unset = "market_cap",
    sort_dir: GetV1CryptocurrencyListingsLatestSortDir | Unset = UNSET,
    cryptocurrency_type: GetV1CryptocurrencyListingsLatestCryptocurrencyType | Unset = "all",
    tag: GetV1CryptocurrencyListingsLatestTag | Unset = "all",
    aux: str | Unset = "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply",
) -> (
    CryptocurrencyListingsLatestResponseModel1
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Listings Latest v1 (deprecated)

     Returns a paginated list of all active cryptocurrencies with latest market data. The default
    \"market_cap\" sort returns cryptocurrency in order of CoinMarketCap's market cap rank (as outlined
    in [our methodology](https://coinmarketcap.com/methodology/)) but you may configure this call to
    order by another market ranking field. Use the \"convert\" option to return market values in
    multiple fiat and cryptocurrency conversions in the same call.


    You may sort against any of the following:
    **market_cap**: CoinMarketCap's market cap rank as outlined in [our
    methodology](https://coinmarketcap.com/methodology/).
    **market_cap_strict**: A strict market cap sort (latest trade price x circulating supply).
    **name**: The cryptocurrency name.
    **symbol**: The cryptocurrency symbol.
    **date_added**: Date cryptocurrency was added to the system.
    **price**: latest average trade price across markets.
    **circulating_supply**: approximate number of coins currently in circulation.
    **total_supply**: approximate total amount of coins in existence right now (minus any coins that
    have been verifiably burned).
    **max_supply**: our best approximation of the maximum amount of coins that will ever exist in the
    lifetime of the currency.
    **num_market_pairs**: number of market pairs across all exchanges trading each currency.
    **market_cap_by_total_supply_strict**: market cap by total supply.
    **volume_24h**: rolling 24 hour adjusted trading volume.
    **volume_7d**: rolling 24 hour adjusted trading volume.
    **volume_30d**: rolling 24 hour adjusted trading volume.
    **percent_change_1h**: 1 hour trading price percentage change for each currency.
    **percent_change_24h**: 24 hour trading price percentage change for each currency.
    **percent_change_7d**: 7 day trading price percentage change for each currency.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our latest cryptocurrency listing and ranking pages like
    [coinmarketcap.com/all/views/all/](https://coinmarketcap.com/all/views/all/),
    [coinmarketcap.com/tokens/](https://coinmarketcap.com/tokens/), [coinmarketcap.com/gainers-
    losers/](https://coinmarketcap.com/gainers-losers/),
    [coinmarketcap.com/new/](https://coinmarketcap.com/new/).

    ***NOTE:** Use this endpoint if you need a sorted and paginated list of all cryptocurrencies. If you
    want to query for market data on a few specific cryptocurrencies use
    `/v1/cryptocurrency/quotes/latest` which is optimized for that purpose. The response data between
    these endpoints is otherwise the same.*

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        price_min (float | Unset):
        price_max (float | Unset):
        market_cap_min (float | Unset):
        market_cap_max (float | Unset):
        volume_24h_min (float | Unset):
        volume_24h_max (float | Unset):
        circulating_supply_min (float | Unset):
        circulating_supply_max (float | Unset):
        percent_change_24h_min (float | Unset):
        percent_change_24h_max (float | Unset):
        self_reported_circulating_supply_min (float | None | Unset):
        self_reported_circulating_supply_max (float | None | Unset):
        self_reported_market_cap_min (float | Unset):
        self_reported_market_cap_max (float | Unset):
        unlocked_market_cap_min (float | Unset):
        unlocked_market_cap_max (float | Unset):
        unlocked_circulating_supply_min (float | Unset):
        unlocked_circulating_supply_max (float | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        sort (GetV1CryptocurrencyListingsLatestSort | Unset):  Default: 'market_cap'.
        sort_dir (GetV1CryptocurrencyListingsLatestSortDir | Unset):
        cryptocurrency_type (GetV1CryptocurrencyListingsLatestCryptocurrencyType | Unset):
            Default: 'all'.
        tag (GetV1CryptocurrencyListingsLatestTag | Unset):  Default: 'all'.
        aux (str | Unset):  Default: 'num_market_pairs,cmc_rank,date_added,tags,platform,max_suppl
            y,circulating_supply,total_supply'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyListingsLatestResponseModel1 | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            limit=limit,
            price_min=price_min,
            price_max=price_max,
            market_cap_min=market_cap_min,
            market_cap_max=market_cap_max,
            volume_24h_min=volume_24h_min,
            volume_24h_max=volume_24h_max,
            circulating_supply_min=circulating_supply_min,
            circulating_supply_max=circulating_supply_max,
            percent_change_24h_min=percent_change_24h_min,
            percent_change_24h_max=percent_change_24h_max,
            self_reported_circulating_supply_min=self_reported_circulating_supply_min,
            self_reported_circulating_supply_max=self_reported_circulating_supply_max,
            self_reported_market_cap_min=self_reported_market_cap_min,
            self_reported_market_cap_max=self_reported_market_cap_max,
            unlocked_market_cap_min=unlocked_market_cap_min,
            unlocked_market_cap_max=unlocked_market_cap_max,
            unlocked_circulating_supply_min=unlocked_circulating_supply_min,
            unlocked_circulating_supply_max=unlocked_circulating_supply_max,
            convert=convert,
            convert_id=convert_id,
            sort=sort,
            sort_dir=sort_dir,
            cryptocurrency_type=cryptocurrency_type,
            tag=tag,
            aux=aux,
        )
    ).parsed
