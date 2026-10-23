from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dquery_batch_price_request_dto import DqueryBatchPriceRequestDTO
from ...models.v1dex_token_price_batch_response_model import V1DEXTokenPriceBatchResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: DqueryBatchPriceRequestDTO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/dex/token/price/batch",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> V1DEXTokenPriceBatchResponseModel | None:
    if response.status_code == 200:
        response_200 = V1DEXTokenPriceBatchResponseModel.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V1DEXTokenPriceBatchResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DqueryBatchPriceRequestDTO,
) -> Response[V1DEXTokenPriceBatchResponseModel]:
    """Batch get token prices

     Get prices for multiple tokens in one request

    Args:
        body (DqueryBatchPriceRequestDTO): Batch price query request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V1DEXTokenPriceBatchResponseModel]
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
    body: DqueryBatchPriceRequestDTO,
) -> V1DEXTokenPriceBatchResponseModel | None:
    """Batch get token prices

     Get prices for multiple tokens in one request

    Args:
        body (DqueryBatchPriceRequestDTO): Batch price query request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V1DEXTokenPriceBatchResponseModel
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DqueryBatchPriceRequestDTO,
) -> Response[V1DEXTokenPriceBatchResponseModel]:
    """Batch get token prices

     Get prices for multiple tokens in one request

    Args:
        body (DqueryBatchPriceRequestDTO): Batch price query request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V1DEXTokenPriceBatchResponseModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DqueryBatchPriceRequestDTO,
) -> V1DEXTokenPriceBatchResponseModel | None:
    """Batch get token prices

     Get prices for multiple tokens in one request

    Args:
        body (DqueryBatchPriceRequestDTO): Batch price query request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V1DEXTokenPriceBatchResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
