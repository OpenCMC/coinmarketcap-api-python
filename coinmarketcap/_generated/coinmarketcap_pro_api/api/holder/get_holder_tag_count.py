from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.holder_tag_count_vo import HolderTagCountVO
from ...types import UNSET, Response


def _get_kwargs(
    *,
    platform: str,
    token_address: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["platform"] = platform

    params["tokenAddress"] = token_address

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/dex/holders/tag_count",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HolderTagCountVO | None:
    if response.status_code == 200:
        response_200 = HolderTagCountVO.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HolderTagCountVO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform: str,
    token_address: str,
) -> Response[HolderTagCountVO]:
    """Get holder tag count

     Get detailed information for holders tag count

    Args:
        platform (str):
        token_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HolderTagCountVO]
    """

    kwargs = _get_kwargs(
        platform=platform,
        token_address=token_address,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    platform: str,
    token_address: str,
) -> HolderTagCountVO | None:
    """Get holder tag count

     Get detailed information for holders tag count

    Args:
        platform (str):
        token_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HolderTagCountVO
    """

    return sync_detailed(
        client=client,
        platform=platform,
        token_address=token_address,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform: str,
    token_address: str,
) -> Response[HolderTagCountVO]:
    """Get holder tag count

     Get detailed information for holders tag count

    Args:
        platform (str):
        token_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HolderTagCountVO]
    """

    kwargs = _get_kwargs(
        platform=platform,
        token_address=token_address,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    platform: str,
    token_address: str,
) -> HolderTagCountVO | None:
    """Get holder tag count

     Get detailed information for holders tag count

    Args:
        platform (str):
        token_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HolderTagCountVO
    """

    return (
        await asyncio_detailed(
            client=client,
            platform=platform,
            token_address=token_address,
        )
    ).parsed
