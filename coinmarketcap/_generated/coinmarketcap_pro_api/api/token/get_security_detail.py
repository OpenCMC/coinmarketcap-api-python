from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.token_security_response_dto import TokenSecurityResponseDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    platform_name: str | Unset = UNSET,
    address: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["platformName"] = platform_name

    params["address"] = address

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/dex/security/detail",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[TokenSecurityResponseDTO] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TokenSecurityResponseDTO.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[TokenSecurityResponseDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform_name: str | Unset = UNSET,
    address: str | Unset = UNSET,
) -> Response[list[TokenSecurityResponseDTO]]:
    r"""Get security detail

     Get security audit information for a token

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/security/detail`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        platform_name (str | Unset):
        address (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TokenSecurityResponseDTO]]
    """

    kwargs = _get_kwargs(
        platform_name=platform_name,
        address=address,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    platform_name: str | Unset = UNSET,
    address: str | Unset = UNSET,
) -> list[TokenSecurityResponseDTO] | None:
    r"""Get security detail

     Get security audit information for a token

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/security/detail`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        platform_name (str | Unset):
        address (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TokenSecurityResponseDTO]
    """

    return sync_detailed(
        client=client,
        platform_name=platform_name,
        address=address,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform_name: str | Unset = UNSET,
    address: str | Unset = UNSET,
) -> Response[list[TokenSecurityResponseDTO]]:
    r"""Get security detail

     Get security audit information for a token

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/security/detail`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        platform_name (str | Unset):
        address (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TokenSecurityResponseDTO]]
    """

    kwargs = _get_kwargs(
        platform_name=platform_name,
        address=address,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    platform_name: str | Unset = UNSET,
    address: str | Unset = UNSET,
) -> list[TokenSecurityResponseDTO] | None:
    r"""Get security detail

     Get security audit information for a token

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/security/detail`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        platform_name (str | Unset):
        address (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TokenSecurityResponseDTO]
    """

    return (
        await asyncio_detailed(
            client=client,
            platform_name=platform_name,
            address=address,
        )
    ).parsed
