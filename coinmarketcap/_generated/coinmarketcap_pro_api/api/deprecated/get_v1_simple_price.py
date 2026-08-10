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
from ...models.simple_price_response_model import SimplePriceResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: str,
    include_market_cap: bool | Unset = False,
    include_volume_24h: bool | Unset = False,
    include_percent_change_24h: bool | Unset = False,
    include_last_updated: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ids"] = ids

    params["include_market_cap"] = include_market_cap

    params["include_volume_24h"] = include_volume_24h

    params["include_percent_change_24h"] = include_percent_change_24h

    params["include_last_updated"] = include_last_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/simple/price",
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
    | SimplePriceResponseModel
    | None
):
    if response.status_code == 200:
        response_200 = SimplePriceResponseModel.from_dict(response.json())

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
    | SimplePriceResponseModel
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
    ids: str,
    include_market_cap: bool | Unset = False,
    include_volume_24h: bool | Unset = False,
    include_percent_change_24h: bool | Unset = False,
    include_last_updated: bool | Unset = False,
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | SimplePriceResponseModel
]:
    r"""Simple Price v1 (deprecated)

     **Deprecated.** Use [/v2/simple/price](/pro-api-reference/cryptocurrency#simple-price) instead - it
    accepts `id` / `slug` / `symbol` lookups (no `/map` round-trip), supports `convert` / `convert_id`,
    and returns the current v3-style response shape. `/v1/simple/price` stays live and unchanged for
    existing integrations.

    Returns current USD spot prices for one or more coins. Optimized for low latency and minimal payload
    size. Optional flags include market cap, 24h volume, 24h percent change, and last updated timestamp.

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
    api/v1/simple/price`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 API call credit per request.

    Args:
        ids (str):
        include_market_cap (bool | Unset):  Default: False.
        include_volume_24h (bool | Unset):  Default: False.
        include_percent_change_24h (bool | Unset):  Default: False.
        include_last_updated (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | SimplePriceResponseModel]
    """

    kwargs = _get_kwargs(
        ids=ids,
        include_market_cap=include_market_cap,
        include_volume_24h=include_volume_24h,
        include_percent_change_24h=include_percent_change_24h,
        include_last_updated=include_last_updated,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    ids: str,
    include_market_cap: bool | Unset = False,
    include_volume_24h: bool | Unset = False,
    include_percent_change_24h: bool | Unset = False,
    include_last_updated: bool | Unset = False,
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | SimplePriceResponseModel
    | None
):
    r"""Simple Price v1 (deprecated)

     **Deprecated.** Use [/v2/simple/price](/pro-api-reference/cryptocurrency#simple-price) instead - it
    accepts `id` / `slug` / `symbol` lookups (no `/map` round-trip), supports `convert` / `convert_id`,
    and returns the current v3-style response shape. `/v1/simple/price` stays live and unchanged for
    existing integrations.

    Returns current USD spot prices for one or more coins. Optimized for low latency and minimal payload
    size. Optional flags include market cap, 24h volume, 24h percent change, and last updated timestamp.

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
    api/v1/simple/price`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 API call credit per request.

    Args:
        ids (str):
        include_market_cap (bool | Unset):  Default: False.
        include_volume_24h (bool | Unset):  Default: False.
        include_percent_change_24h (bool | Unset):  Default: False.
        include_last_updated (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | SimplePriceResponseModel
    """

    return sync_detailed(
        client=client,
        ids=ids,
        include_market_cap=include_market_cap,
        include_volume_24h=include_volume_24h,
        include_percent_change_24h=include_percent_change_24h,
        include_last_updated=include_last_updated,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    ids: str,
    include_market_cap: bool | Unset = False,
    include_volume_24h: bool | Unset = False,
    include_percent_change_24h: bool | Unset = False,
    include_last_updated: bool | Unset = False,
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | SimplePriceResponseModel
]:
    r"""Simple Price v1 (deprecated)

     **Deprecated.** Use [/v2/simple/price](/pro-api-reference/cryptocurrency#simple-price) instead - it
    accepts `id` / `slug` / `symbol` lookups (no `/map` round-trip), supports `convert` / `convert_id`,
    and returns the current v3-style response shape. `/v1/simple/price` stays live and unchanged for
    existing integrations.

    Returns current USD spot prices for one or more coins. Optimized for low latency and minimal payload
    size. Optional flags include market cap, 24h volume, 24h percent change, and last updated timestamp.

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
    api/v1/simple/price`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 API call credit per request.

    Args:
        ids (str):
        include_market_cap (bool | Unset):  Default: False.
        include_volume_24h (bool | Unset):  Default: False.
        include_percent_change_24h (bool | Unset):  Default: False.
        include_last_updated (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | SimplePriceResponseModel]
    """

    kwargs = _get_kwargs(
        ids=ids,
        include_market_cap=include_market_cap,
        include_volume_24h=include_volume_24h,
        include_percent_change_24h=include_percent_change_24h,
        include_last_updated=include_last_updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    ids: str,
    include_market_cap: bool | Unset = False,
    include_volume_24h: bool | Unset = False,
    include_percent_change_24h: bool | Unset = False,
    include_last_updated: bool | Unset = False,
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | SimplePriceResponseModel
    | None
):
    r"""Simple Price v1 (deprecated)

     **Deprecated.** Use [/v2/simple/price](/pro-api-reference/cryptocurrency#simple-price) instead - it
    accepts `id` / `slug` / `symbol` lookups (no `/map` round-trip), supports `convert` / `convert_id`,
    and returns the current v3-style response shape. `/v1/simple/price` stays live and unchanged for
    existing integrations.

    Returns current USD spot prices for one or more coins. Optimized for low latency and minimal payload
    size. Optional flags include market cap, 24h volume, 24h percent change, and last updated timestamp.

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
    api/v1/simple/price`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 API call credit per request.

    Args:
        ids (str):
        include_market_cap (bool | Unset):  Default: False.
        include_volume_24h (bool | Unset):  Default: False.
        include_percent_change_24h (bool | Unset):  Default: False.
        include_last_updated (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | SimplePriceResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            include_market_cap=include_market_cap,
            include_volume_24h=include_volume_24h,
            include_percent_change_24h=include_percent_change_24h,
            include_last_updated=include_last_updated,
        )
    ).parsed
