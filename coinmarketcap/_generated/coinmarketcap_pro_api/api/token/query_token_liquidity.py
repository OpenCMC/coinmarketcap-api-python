from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.token_liquidity_snapshot_dto import TokenLiquiditySnapshotDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    to: int | Unset = UNSET,
    need_latest: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["platform"] = platform

    params["address"] = address

    params["interval"] = interval

    params["limit"] = limit

    params["to"] = to

    params["needLatest"] = need_latest

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/dex/token-liquidity/query",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[TokenLiquiditySnapshotDTO] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TokenLiquiditySnapshotDTO.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[TokenLiquiditySnapshotDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    to: int | Unset = UNSET,
    need_latest: bool | Unset = UNSET,
) -> Response[list[TokenLiquiditySnapshotDTO]]:
    r"""Query token liquidity

     Get liquidity information for a specific token

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/token-liquidity/query`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):
        interval (str | Unset):
        limit (int | Unset):
        to (int | Unset):
        need_latest (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TokenLiquiditySnapshotDTO]]
    """

    kwargs = _get_kwargs(
        platform=platform,
        address=address,
        interval=interval,
        limit=limit,
        to=to,
        need_latest=need_latest,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    to: int | Unset = UNSET,
    need_latest: bool | Unset = UNSET,
) -> list[TokenLiquiditySnapshotDTO] | None:
    r"""Query token liquidity

     Get liquidity information for a specific token

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/token-liquidity/query`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):
        interval (str | Unset):
        limit (int | Unset):
        to (int | Unset):
        need_latest (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TokenLiquiditySnapshotDTO]
    """

    return sync_detailed(
        client=client,
        platform=platform,
        address=address,
        interval=interval,
        limit=limit,
        to=to,
        need_latest=need_latest,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    to: int | Unset = UNSET,
    need_latest: bool | Unset = UNSET,
) -> Response[list[TokenLiquiditySnapshotDTO]]:
    r"""Query token liquidity

     Get liquidity information for a specific token

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/token-liquidity/query`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):
        interval (str | Unset):
        limit (int | Unset):
        to (int | Unset):
        need_latest (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TokenLiquiditySnapshotDTO]]
    """

    kwargs = _get_kwargs(
        platform=platform,
        address=address,
        interval=interval,
        limit=limit,
        to=to,
        need_latest=need_latest,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    to: int | Unset = UNSET,
    need_latest: bool | Unset = UNSET,
) -> list[TokenLiquiditySnapshotDTO] | None:
    r"""Query token liquidity

     Get liquidity information for a specific token

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/token-liquidity/query`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):
        interval (str | Unset):
        limit (int | Unset):
        to (int | Unset):
        need_latest (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TokenLiquiditySnapshotDTO]
    """

    return (
        await asyncio_detailed(
            client=client,
            platform=platform,
            address=address,
            interval=interval,
            limit=limit,
            to=to,
            need_latest=need_latest,
        )
    ).parsed
