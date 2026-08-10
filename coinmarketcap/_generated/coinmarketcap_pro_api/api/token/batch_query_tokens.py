from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dquery_batch_token_request_dto import DqueryBatchTokenRequestDTO
from ...models.token_detail_dto import TokenDetailDTO
from ...types import Response


def _get_kwargs(
    *,
    body: DqueryBatchTokenRequestDTO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/dex/tokens/batch-query",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[TokenDetailDTO] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TokenDetailDTO.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[TokenDetailDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DqueryBatchTokenRequestDTO,
) -> Response[list[TokenDetailDTO]]:
    """Batch query tokens

     Query multiple tokens in one request

    Args:
        body (DqueryBatchTokenRequestDTO): Batch token query request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TokenDetailDTO]]
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
    body: DqueryBatchTokenRequestDTO,
) -> list[TokenDetailDTO] | None:
    """Batch query tokens

     Query multiple tokens in one request

    Args:
        body (DqueryBatchTokenRequestDTO): Batch token query request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TokenDetailDTO]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DqueryBatchTokenRequestDTO,
) -> Response[list[TokenDetailDTO]]:
    """Batch query tokens

     Query multiple tokens in one request

    Args:
        body (DqueryBatchTokenRequestDTO): Batch token query request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TokenDetailDTO]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DqueryBatchTokenRequestDTO,
) -> list[TokenDetailDTO] | None:
    """Batch query tokens

     Query multiple tokens in one request

    Args:
        body (DqueryBatchTokenRequestDTO): Batch token query request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TokenDetailDTO]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
