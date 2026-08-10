from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v3_cryptocurrency_listings_latest_response_200 import GetV3CryptocurrencyListingsLatestResponse200
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: str | Unset = "1",
    limit: str | Unset = "100",
    price_min: str | Unset = UNSET,
    price_max: str | Unset = UNSET,
    market_cap_min: str | Unset = UNSET,
    market_cap_max: str | Unset = UNSET,
    volume_24h_min: str | Unset = UNSET,
    volume_24h_max: str | Unset = UNSET,
    circulating_supply_min: str | Unset = UNSET,
    circulating_supply_max: str | Unset = UNSET,
    percent_change_24h_min: str | Unset = UNSET,
    percent_change_24h_max: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: str | Unset = "market_cap",
    sort_dir: str | Unset = "desc",
    cryptocurrency_type: str | Unset = "all",
    tag: str | Unset = "all",
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

    params["convert"] = convert

    params["convert_id"] = convert_id

    params["sort"] = sort

    params["sort_dir"] = sort_dir

    params["cryptocurrency_type"] = cryptocurrency_type

    params["tag"] = tag

    params["aux"] = aux

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/cryptocurrency/listings/latest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetV3CryptocurrencyListingsLatestResponse200
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = GetV3CryptocurrencyListingsLatestResponse200.from_dict(response.json())

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
    GetV3CryptocurrencyListingsLatestResponse200
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
    start: str | Unset = "1",
    limit: str | Unset = "100",
    price_min: str | Unset = UNSET,
    price_max: str | Unset = UNSET,
    market_cap_min: str | Unset = UNSET,
    market_cap_max: str | Unset = UNSET,
    volume_24h_min: str | Unset = UNSET,
    volume_24h_max: str | Unset = UNSET,
    circulating_supply_min: str | Unset = UNSET,
    circulating_supply_max: str | Unset = UNSET,
    percent_change_24h_min: str | Unset = UNSET,
    percent_change_24h_max: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: str | Unset = "market_cap",
    sort_dir: str | Unset = "desc",
    cryptocurrency_type: str | Unset = "all",
    tag: str | Unset = "all",
    aux: str | Unset = "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply",
) -> Response[
    GetV3CryptocurrencyListingsLatestResponse200
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Listings Latest

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

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v3/cryptocurrency/listings/latest`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per \`convert\` option beyond the first.
    **CMC equivalent pages:** Our latest cryptocurrency listing and ranking pages like
    [coinmarketcap.com/all/views/all/](https://coinmarketcap.com/all/views/all/),
    [coinmarketcap.com/tokens/](https://coinmarketcap.com/tokens/), [coinmarketcap.com/gainers-
    losers/](https://coinmarketcap.com/gainers-losers/),
    [coinmarketcap.com/new/](https://coinmarketcap.com/new/).

    ***NOTE:** Use this endpoint if you need a sorted and paginated list of all cryptocurrencies. If you
    want to query for market data on a few specific cryptocurrencies use
    `/v3/cryptocurrency/quotes/latest` which is optimized for that purpose. The response data between
    these endpoints is otherwise the same.*

    Args:
        start (str | Unset):  Default: '1'.
        limit (str | Unset):  Default: '100'.
        price_min (str | Unset):
        price_max (str | Unset):
        market_cap_min (str | Unset):
        market_cap_max (str | Unset):
        volume_24h_min (str | Unset):
        volume_24h_max (str | Unset):
        circulating_supply_min (str | Unset):
        circulating_supply_max (str | Unset):
        percent_change_24h_min (str | Unset):
        percent_change_24h_max (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        sort (str | Unset):  Default: 'market_cap'.
        sort_dir (str | Unset):  Default: 'desc'.
        cryptocurrency_type (str | Unset):  Default: 'all'.
        tag (str | Unset):  Default: 'all'.
        aux (str | Unset):  Default: 'num_market_pairs,cmc_rank,date_added,tags,platform,max_suppl
            y,circulating_supply,total_supply'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV3CryptocurrencyListingsLatestResponse200 | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
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
    start: str | Unset = "1",
    limit: str | Unset = "100",
    price_min: str | Unset = UNSET,
    price_max: str | Unset = UNSET,
    market_cap_min: str | Unset = UNSET,
    market_cap_max: str | Unset = UNSET,
    volume_24h_min: str | Unset = UNSET,
    volume_24h_max: str | Unset = UNSET,
    circulating_supply_min: str | Unset = UNSET,
    circulating_supply_max: str | Unset = UNSET,
    percent_change_24h_min: str | Unset = UNSET,
    percent_change_24h_max: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: str | Unset = "market_cap",
    sort_dir: str | Unset = "desc",
    cryptocurrency_type: str | Unset = "all",
    tag: str | Unset = "all",
    aux: str | Unset = "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply",
) -> (
    GetV3CryptocurrencyListingsLatestResponse200
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Listings Latest

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

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v3/cryptocurrency/listings/latest`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per \`convert\` option beyond the first.
    **CMC equivalent pages:** Our latest cryptocurrency listing and ranking pages like
    [coinmarketcap.com/all/views/all/](https://coinmarketcap.com/all/views/all/),
    [coinmarketcap.com/tokens/](https://coinmarketcap.com/tokens/), [coinmarketcap.com/gainers-
    losers/](https://coinmarketcap.com/gainers-losers/),
    [coinmarketcap.com/new/](https://coinmarketcap.com/new/).

    ***NOTE:** Use this endpoint if you need a sorted and paginated list of all cryptocurrencies. If you
    want to query for market data on a few specific cryptocurrencies use
    `/v3/cryptocurrency/quotes/latest` which is optimized for that purpose. The response data between
    these endpoints is otherwise the same.*

    Args:
        start (str | Unset):  Default: '1'.
        limit (str | Unset):  Default: '100'.
        price_min (str | Unset):
        price_max (str | Unset):
        market_cap_min (str | Unset):
        market_cap_max (str | Unset):
        volume_24h_min (str | Unset):
        volume_24h_max (str | Unset):
        circulating_supply_min (str | Unset):
        circulating_supply_max (str | Unset):
        percent_change_24h_min (str | Unset):
        percent_change_24h_max (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        sort (str | Unset):  Default: 'market_cap'.
        sort_dir (str | Unset):  Default: 'desc'.
        cryptocurrency_type (str | Unset):  Default: 'all'.
        tag (str | Unset):  Default: 'all'.
        aux (str | Unset):  Default: 'num_market_pairs,cmc_rank,date_added,tags,platform,max_suppl
            y,circulating_supply,total_supply'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV3CryptocurrencyListingsLatestResponse200 | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
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
    start: str | Unset = "1",
    limit: str | Unset = "100",
    price_min: str | Unset = UNSET,
    price_max: str | Unset = UNSET,
    market_cap_min: str | Unset = UNSET,
    market_cap_max: str | Unset = UNSET,
    volume_24h_min: str | Unset = UNSET,
    volume_24h_max: str | Unset = UNSET,
    circulating_supply_min: str | Unset = UNSET,
    circulating_supply_max: str | Unset = UNSET,
    percent_change_24h_min: str | Unset = UNSET,
    percent_change_24h_max: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: str | Unset = "market_cap",
    sort_dir: str | Unset = "desc",
    cryptocurrency_type: str | Unset = "all",
    tag: str | Unset = "all",
    aux: str | Unset = "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply",
) -> Response[
    GetV3CryptocurrencyListingsLatestResponse200
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Listings Latest

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

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v3/cryptocurrency/listings/latest`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per \`convert\` option beyond the first.
    **CMC equivalent pages:** Our latest cryptocurrency listing and ranking pages like
    [coinmarketcap.com/all/views/all/](https://coinmarketcap.com/all/views/all/),
    [coinmarketcap.com/tokens/](https://coinmarketcap.com/tokens/), [coinmarketcap.com/gainers-
    losers/](https://coinmarketcap.com/gainers-losers/),
    [coinmarketcap.com/new/](https://coinmarketcap.com/new/).

    ***NOTE:** Use this endpoint if you need a sorted and paginated list of all cryptocurrencies. If you
    want to query for market data on a few specific cryptocurrencies use
    `/v3/cryptocurrency/quotes/latest` which is optimized for that purpose. The response data between
    these endpoints is otherwise the same.*

    Args:
        start (str | Unset):  Default: '1'.
        limit (str | Unset):  Default: '100'.
        price_min (str | Unset):
        price_max (str | Unset):
        market_cap_min (str | Unset):
        market_cap_max (str | Unset):
        volume_24h_min (str | Unset):
        volume_24h_max (str | Unset):
        circulating_supply_min (str | Unset):
        circulating_supply_max (str | Unset):
        percent_change_24h_min (str | Unset):
        percent_change_24h_max (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        sort (str | Unset):  Default: 'market_cap'.
        sort_dir (str | Unset):  Default: 'desc'.
        cryptocurrency_type (str | Unset):  Default: 'all'.
        tag (str | Unset):  Default: 'all'.
        aux (str | Unset):  Default: 'num_market_pairs,cmc_rank,date_added,tags,platform,max_suppl
            y,circulating_supply,total_supply'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV3CryptocurrencyListingsLatestResponse200 | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
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
    start: str | Unset = "1",
    limit: str | Unset = "100",
    price_min: str | Unset = UNSET,
    price_max: str | Unset = UNSET,
    market_cap_min: str | Unset = UNSET,
    market_cap_max: str | Unset = UNSET,
    volume_24h_min: str | Unset = UNSET,
    volume_24h_max: str | Unset = UNSET,
    circulating_supply_min: str | Unset = UNSET,
    circulating_supply_max: str | Unset = UNSET,
    percent_change_24h_min: str | Unset = UNSET,
    percent_change_24h_max: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: str | Unset = "market_cap",
    sort_dir: str | Unset = "desc",
    cryptocurrency_type: str | Unset = "all",
    tag: str | Unset = "all",
    aux: str | Unset = "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply",
) -> (
    GetV3CryptocurrencyListingsLatestResponse200
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Listings Latest

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

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v3/cryptocurrency/listings/latest`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per \`convert\` option beyond the first.
    **CMC equivalent pages:** Our latest cryptocurrency listing and ranking pages like
    [coinmarketcap.com/all/views/all/](https://coinmarketcap.com/all/views/all/),
    [coinmarketcap.com/tokens/](https://coinmarketcap.com/tokens/), [coinmarketcap.com/gainers-
    losers/](https://coinmarketcap.com/gainers-losers/),
    [coinmarketcap.com/new/](https://coinmarketcap.com/new/).

    ***NOTE:** Use this endpoint if you need a sorted and paginated list of all cryptocurrencies. If you
    want to query for market data on a few specific cryptocurrencies use
    `/v3/cryptocurrency/quotes/latest` which is optimized for that purpose. The response data between
    these endpoints is otherwise the same.*

    Args:
        start (str | Unset):  Default: '1'.
        limit (str | Unset):  Default: '100'.
        price_min (str | Unset):
        price_max (str | Unset):
        market_cap_min (str | Unset):
        market_cap_max (str | Unset):
        volume_24h_min (str | Unset):
        volume_24h_max (str | Unset):
        circulating_supply_min (str | Unset):
        circulating_supply_max (str | Unset):
        percent_change_24h_min (str | Unset):
        percent_change_24h_max (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        sort (str | Unset):  Default: 'market_cap'.
        sort_dir (str | Unset):  Default: 'desc'.
        cryptocurrency_type (str | Unset):  Default: 'all'.
        tag (str | Unset):  Default: 'all'.
        aux (str | Unset):  Default: 'num_market_pairs,cmc_rank,date_added,tags,platform,max_suppl
            y,circulating_supply,total_supply'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV3CryptocurrencyListingsLatestResponse200 | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
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
            convert=convert,
            convert_id=convert_id,
            sort=sort,
            sort_dir=sort_dir,
            cryptocurrency_type=cryptocurrency_type,
            tag=tag,
            aux=aux,
        )
    ).parsed
