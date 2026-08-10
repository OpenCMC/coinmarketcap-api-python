from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_response_dto import SearchResponseDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    code: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["platform"] = platform

    params["sort"] = sort

    params["limit"] = limit

    params["code"] = code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/dex/search",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchResponseDTO | None:
    if response.status_code == 200:
        response_200 = SearchResponseDTO.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchResponseDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    code: str | Unset = UNSET,
) -> Response[SearchResponseDTO]:
    r"""Search tokens

     Search for tokens by keyword

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/search`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    Args:
        q (str | Unset):
        platform (str | Unset):
        sort (str | Unset):
        limit (int | Unset):
        code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResponseDTO]
    """

    kwargs = _get_kwargs(
        q=q,
        platform=platform,
        sort=sort,
        limit=limit,
        code=code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    code: str | Unset = UNSET,
) -> SearchResponseDTO | None:
    r"""Search tokens

     Search for tokens by keyword

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/search`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    Args:
        q (str | Unset):
        platform (str | Unset):
        sort (str | Unset):
        limit (int | Unset):
        code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchResponseDTO
    """

    return sync_detailed(
        client=client,
        q=q,
        platform=platform,
        sort=sort,
        limit=limit,
        code=code,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    code: str | Unset = UNSET,
) -> Response[SearchResponseDTO]:
    r"""Search tokens

     Search for tokens by keyword

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/search`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    Args:
        q (str | Unset):
        platform (str | Unset):
        sort (str | Unset):
        limit (int | Unset):
        code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResponseDTO]
    """

    kwargs = _get_kwargs(
        q=q,
        platform=platform,
        sort=sort,
        limit=limit,
        code=code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    platform: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    code: str | Unset = UNSET,
) -> SearchResponseDTO | None:
    r"""Search tokens

     Search for tokens by keyword

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/search`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    Args:
        q (str | Unset):
        platform (str | Unset):
        sort (str | Unset):
        limit (int | Unset):
        code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchResponseDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            platform=platform,
            sort=sort,
            limit=limit,
            code=code,
        )
    ).parsed
