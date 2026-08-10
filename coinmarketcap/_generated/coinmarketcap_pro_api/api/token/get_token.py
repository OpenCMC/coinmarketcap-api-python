from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.token_detail_dto import TokenDetailDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["platform"] = platform

    params["address"] = address

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/dex/token",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TokenDetailDTO | None:
    if response.status_code == 200:
        response_200 = TokenDetailDTO.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TokenDetailDTO]:
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
) -> Response[TokenDetailDTO]:
    r"""Get token detail

     Get detailed information for a specific token

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/token`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-api-
    reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TokenDetailDTO]
    """

    kwargs = _get_kwargs(
        platform=platform,
        address=address,
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
) -> TokenDetailDTO | None:
    r"""Get token detail

     Get detailed information for a specific token

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/token`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-api-
    reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TokenDetailDTO
    """

    return sync_detailed(
        client=client,
        platform=platform,
        address=address,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
) -> Response[TokenDetailDTO]:
    r"""Get token detail

     Get detailed information for a specific token

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/token`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-api-
    reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TokenDetailDTO]
    """

    kwargs = _get_kwargs(
        platform=platform,
        address=address,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
) -> TokenDetailDTO | None:
    r"""Get token detail

     Get detailed information for a specific token

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/token`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-api-
    reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TokenDetailDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            platform=platform,
            address=address,
        )
    ).parsed
