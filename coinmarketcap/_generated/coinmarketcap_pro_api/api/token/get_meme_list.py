from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dquery_meme_request_dto import DqueryMemeRequestDTO
from ...models.meme_coin_response_dto import MemeCoinResponseDTO
from ...types import Response


def _get_kwargs(
    *,
    body: DqueryMemeRequestDTO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/dex/meme/list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MemeCoinResponseDTO | None:
    if response.status_code == 200:
        response_200 = MemeCoinResponseDTO.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MemeCoinResponseDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DqueryMemeRequestDTO,
) -> Response[MemeCoinResponseDTO]:
    """Get meme tokens

     Get list of meme tokens

    Args:
        body (DqueryMemeRequestDTO): Meme coin request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemeCoinResponseDTO]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: DqueryMemeRequestDTO,
) -> MemeCoinResponseDTO | None:
    """Get meme tokens

     Get list of meme tokens

    Args:
        body (DqueryMemeRequestDTO): Meme coin request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemeCoinResponseDTO
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DqueryMemeRequestDTO,
) -> Response[MemeCoinResponseDTO]:
    """Get meme tokens

     Get list of meme tokens

    Args:
        body (DqueryMemeRequestDTO): Meme coin request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemeCoinResponseDTO]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DqueryMemeRequestDTO,
) -> MemeCoinResponseDTO | None:
    """Get meme tokens

     Get list of meme tokens

    Args:
        body (DqueryMemeRequestDTO): Meme coin request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemeCoinResponseDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
