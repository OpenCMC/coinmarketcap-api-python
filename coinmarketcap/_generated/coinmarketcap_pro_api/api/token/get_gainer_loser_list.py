from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dquery_market_request_dto import DqueryMarketRequestDTO
from ...models.gainer_leader_board_response_dto import GainerLeaderBoardResponseDTO
from ...types import Response


def _get_kwargs(
    *,
    body: DqueryMarketRequestDTO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/dex/gainer-loser/list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GainerLeaderBoardResponseDTO | None:
    if response.status_code == 200:
        response_200 = GainerLeaderBoardResponseDTO.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GainerLeaderBoardResponseDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DqueryMarketRequestDTO,
) -> Response[GainerLeaderBoardResponseDTO]:
    """Get top gainers and losers

     Get list of top gainer and loser tokens

    Args:
        body (DqueryMarketRequestDTO): Market list request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GainerLeaderBoardResponseDTO]
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
    body: DqueryMarketRequestDTO,
) -> GainerLeaderBoardResponseDTO | None:
    """Get top gainers and losers

     Get list of top gainer and loser tokens

    Args:
        body (DqueryMarketRequestDTO): Market list request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GainerLeaderBoardResponseDTO
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DqueryMarketRequestDTO,
) -> Response[GainerLeaderBoardResponseDTO]:
    """Get top gainers and losers

     Get list of top gainer and loser tokens

    Args:
        body (DqueryMarketRequestDTO): Market list request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GainerLeaderBoardResponseDTO]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DqueryMarketRequestDTO,
) -> GainerLeaderBoardResponseDTO | None:
    """Get top gainers and losers

     Get list of top gainer and loser tokens

    Args:
        body (DqueryMarketRequestDTO): Market list request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GainerLeaderBoardResponseDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
