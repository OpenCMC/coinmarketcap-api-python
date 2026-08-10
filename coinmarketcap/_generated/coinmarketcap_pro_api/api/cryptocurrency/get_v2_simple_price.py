from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...models.v2_simple_price_response_model import V2SimplePriceResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    convert: str | Unset = "USD",
    convert_id: str | Unset = UNSET,
    include_market_cap: bool | Unset = False,
    include_24h_volume: bool | Unset = False,
    include_24h_change: bool | Unset = False,
    include_last_updated: bool | Unset = False,
    include_all: bool | Unset = False,
    precision: int | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["slug"] = slug

    params["symbol"] = symbol

    params["convert"] = convert

    params["convert_id"] = convert_id

    params["include_market_cap"] = include_market_cap

    params["include_24h_volume"] = include_24h_volume

    params["include_24h_change"] = include_24h_change

    params["include_last_updated"] = include_last_updated

    params["include_all"] = include_all

    params["precision"] = precision

    params["skip_invalid"] = skip_invalid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/simple/price",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | V2SimplePriceResponseModel
    | None
):
    if response.status_code == 200:
        response_200 = V2SimplePriceResponseModel.from_dict(response.json())

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
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | V2SimplePriceResponseModel
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
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    convert: str | Unset = "USD",
    convert_id: str | Unset = UNSET,
    include_market_cap: bool | Unset = False,
    include_24h_volume: bool | Unset = False,
    include_24h_change: bool | Unset = False,
    include_last_updated: bool | Unset = False,
    include_all: bool | Unset = False,
    precision: int | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | V2SimplePriceResponseModel
]:
    r"""Simple Price

     Returns a lightweight latest price for one or more cryptocurrencies, with optional inline market
    cap, 24h volume, 24h change, and freshness timestamp. It is a slimmed-down alternative to
    [/v3/cryptocurrency/quotes/latest](/pro-api-reference/cryptocurrency#quotes-latest), optimized for
    the single most common question - \"what is X worth right now\" - without returning the full `quote`
    object.

    You can look assets up by `id`, `slug`, or `symbol`, and at least one of those is required. The
    endpoint deliberately does not return supply, rank, market pairs, or descriptive metadata; for any
    of those, use [/v3/cryptocurrency/quotes/latest](/pro-api-reference/cryptocurrency#quotes-latest) or
    [/v2/cryptocurrency/info](/pro-api-reference/cryptocurrency#metadata) instead.

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
    api/v2/simple/price`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 250 cryptocurrencies returned (rounded up), plus 1 credit per
    `convert` / `convert_id` option beyond the first. The `include_*` flags do not add credits.

    Args:
        id (str | Unset):  Example: 1,1027.
        slug (str | Unset):  Example: bitcoin,ethereum.
        symbol (str | Unset):  Example: BTC,ETH.
        convert (str | Unset):  Default: 'USD'. Example: USD.
        convert_id (str | Unset):  Example: 2781.
        include_market_cap (bool | Unset):  Default: False.
        include_24h_volume (bool | Unset):  Default: False.
        include_24h_change (bool | Unset):  Default: False.
        include_last_updated (bool | Unset):  Default: False.
        include_all (bool | Unset):  Default: False.
        precision (int | Unset):
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | V2SimplePriceResponseModel]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        symbol=symbol,
        convert=convert,
        convert_id=convert_id,
        include_market_cap=include_market_cap,
        include_24h_volume=include_24h_volume,
        include_24h_change=include_24h_change,
        include_last_updated=include_last_updated,
        include_all=include_all,
        precision=precision,
        skip_invalid=skip_invalid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    convert: str | Unset = "USD",
    convert_id: str | Unset = UNSET,
    include_market_cap: bool | Unset = False,
    include_24h_volume: bool | Unset = False,
    include_24h_change: bool | Unset = False,
    include_last_updated: bool | Unset = False,
    include_all: bool | Unset = False,
    precision: int | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | V2SimplePriceResponseModel
    | None
):
    r"""Simple Price

     Returns a lightweight latest price for one or more cryptocurrencies, with optional inline market
    cap, 24h volume, 24h change, and freshness timestamp. It is a slimmed-down alternative to
    [/v3/cryptocurrency/quotes/latest](/pro-api-reference/cryptocurrency#quotes-latest), optimized for
    the single most common question - \"what is X worth right now\" - without returning the full `quote`
    object.

    You can look assets up by `id`, `slug`, or `symbol`, and at least one of those is required. The
    endpoint deliberately does not return supply, rank, market pairs, or descriptive metadata; for any
    of those, use [/v3/cryptocurrency/quotes/latest](/pro-api-reference/cryptocurrency#quotes-latest) or
    [/v2/cryptocurrency/info](/pro-api-reference/cryptocurrency#metadata) instead.

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
    api/v2/simple/price`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 250 cryptocurrencies returned (rounded up), plus 1 credit per
    `convert` / `convert_id` option beyond the first. The `include_*` flags do not add credits.

    Args:
        id (str | Unset):  Example: 1,1027.
        slug (str | Unset):  Example: bitcoin,ethereum.
        symbol (str | Unset):  Example: BTC,ETH.
        convert (str | Unset):  Default: 'USD'. Example: USD.
        convert_id (str | Unset):  Example: 2781.
        include_market_cap (bool | Unset):  Default: False.
        include_24h_volume (bool | Unset):  Default: False.
        include_24h_change (bool | Unset):  Default: False.
        include_last_updated (bool | Unset):  Default: False.
        include_all (bool | Unset):  Default: False.
        precision (int | Unset):
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | V2SimplePriceResponseModel
    """

    return sync_detailed(
        client=client,
        id=id,
        slug=slug,
        symbol=symbol,
        convert=convert,
        convert_id=convert_id,
        include_market_cap=include_market_cap,
        include_24h_volume=include_24h_volume,
        include_24h_change=include_24h_change,
        include_last_updated=include_last_updated,
        include_all=include_all,
        precision=precision,
        skip_invalid=skip_invalid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    convert: str | Unset = "USD",
    convert_id: str | Unset = UNSET,
    include_market_cap: bool | Unset = False,
    include_24h_volume: bool | Unset = False,
    include_24h_change: bool | Unset = False,
    include_last_updated: bool | Unset = False,
    include_all: bool | Unset = False,
    precision: int | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | V2SimplePriceResponseModel
]:
    r"""Simple Price

     Returns a lightweight latest price for one or more cryptocurrencies, with optional inline market
    cap, 24h volume, 24h change, and freshness timestamp. It is a slimmed-down alternative to
    [/v3/cryptocurrency/quotes/latest](/pro-api-reference/cryptocurrency#quotes-latest), optimized for
    the single most common question - \"what is X worth right now\" - without returning the full `quote`
    object.

    You can look assets up by `id`, `slug`, or `symbol`, and at least one of those is required. The
    endpoint deliberately does not return supply, rank, market pairs, or descriptive metadata; for any
    of those, use [/v3/cryptocurrency/quotes/latest](/pro-api-reference/cryptocurrency#quotes-latest) or
    [/v2/cryptocurrency/info](/pro-api-reference/cryptocurrency#metadata) instead.

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
    api/v2/simple/price`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 250 cryptocurrencies returned (rounded up), plus 1 credit per
    `convert` / `convert_id` option beyond the first. The `include_*` flags do not add credits.

    Args:
        id (str | Unset):  Example: 1,1027.
        slug (str | Unset):  Example: bitcoin,ethereum.
        symbol (str | Unset):  Example: BTC,ETH.
        convert (str | Unset):  Default: 'USD'. Example: USD.
        convert_id (str | Unset):  Example: 2781.
        include_market_cap (bool | Unset):  Default: False.
        include_24h_volume (bool | Unset):  Default: False.
        include_24h_change (bool | Unset):  Default: False.
        include_last_updated (bool | Unset):  Default: False.
        include_all (bool | Unset):  Default: False.
        precision (int | Unset):
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | V2SimplePriceResponseModel]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        symbol=symbol,
        convert=convert,
        convert_id=convert_id,
        include_market_cap=include_market_cap,
        include_24h_volume=include_24h_volume,
        include_24h_change=include_24h_change,
        include_last_updated=include_last_updated,
        include_all=include_all,
        precision=precision,
        skip_invalid=skip_invalid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    convert: str | Unset = "USD",
    convert_id: str | Unset = UNSET,
    include_market_cap: bool | Unset = False,
    include_24h_volume: bool | Unset = False,
    include_24h_change: bool | Unset = False,
    include_last_updated: bool | Unset = False,
    include_all: bool | Unset = False,
    precision: int | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | V2SimplePriceResponseModel
    | None
):
    r"""Simple Price

     Returns a lightweight latest price for one or more cryptocurrencies, with optional inline market
    cap, 24h volume, 24h change, and freshness timestamp. It is a slimmed-down alternative to
    [/v3/cryptocurrency/quotes/latest](/pro-api-reference/cryptocurrency#quotes-latest), optimized for
    the single most common question - \"what is X worth right now\" - without returning the full `quote`
    object.

    You can look assets up by `id`, `slug`, or `symbol`, and at least one of those is required. The
    endpoint deliberately does not return supply, rank, market pairs, or descriptive metadata; for any
    of those, use [/v3/cryptocurrency/quotes/latest](/pro-api-reference/cryptocurrency#quotes-latest) or
    [/v2/cryptocurrency/info](/pro-api-reference/cryptocurrency#metadata) instead.

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
    api/v2/simple/price`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 250 cryptocurrencies returned (rounded up), plus 1 credit per
    `convert` / `convert_id` option beyond the first. The `include_*` flags do not add credits.

    Args:
        id (str | Unset):  Example: 1,1027.
        slug (str | Unset):  Example: bitcoin,ethereum.
        symbol (str | Unset):  Example: BTC,ETH.
        convert (str | Unset):  Default: 'USD'. Example: USD.
        convert_id (str | Unset):  Example: 2781.
        include_market_cap (bool | Unset):  Default: False.
        include_24h_volume (bool | Unset):  Default: False.
        include_24h_change (bool | Unset):  Default: False.
        include_last_updated (bool | Unset):  Default: False.
        include_all (bool | Unset):  Default: False.
        precision (int | Unset):
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | V2SimplePriceResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            slug=slug,
            symbol=symbol,
            convert=convert,
            convert_id=convert_id,
            include_market_cap=include_market_cap,
            include_24h_volume=include_24h_volume,
            include_24h_change=include_24h_change,
            include_last_updated=include_last_updated,
            include_all=include_all,
            precision=precision,
            skip_invalid=skip_invalid,
        )
    ).parsed
