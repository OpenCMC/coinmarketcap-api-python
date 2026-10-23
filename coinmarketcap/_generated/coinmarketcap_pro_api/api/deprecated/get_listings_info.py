from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.v4dex_listings_info_response_model import V4DEXListingsInfoResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: str | Unset = UNSET,
    aux: str | Unset = "",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["aux"] = aux

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/dex/listings/info",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> V4DEXListingsInfoResponseModel | None:
    if response.status_code == 200:
        response_200 = V4DEXListingsInfoResponseModel.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V4DEXListingsInfoResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    aux: str | Unset = "",
) -> Response[V4DEXListingsInfoResponseModel]:
    """DEX Metadata

     Returns all static metadata for one or more decentralised exchanges. This information includes
    details like launch
    date, logo, official website URL, social links, and market fee documentation URL.

    Args:
        id (str | Unset):
        aux (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V4DEXListingsInfoResponseModel]
    """

    kwargs = _get_kwargs(
        id=id,
        aux=aux,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    aux: str | Unset = "",
) -> V4DEXListingsInfoResponseModel | None:
    """DEX Metadata

     Returns all static metadata for one or more decentralised exchanges. This information includes
    details like launch
    date, logo, official website URL, social links, and market fee documentation URL.

    Args:
        id (str | Unset):
        aux (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V4DEXListingsInfoResponseModel
    """

    return sync_detailed(
        client=client,
        id=id,
        aux=aux,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    aux: str | Unset = "",
) -> Response[V4DEXListingsInfoResponseModel]:
    """DEX Metadata

     Returns all static metadata for one or more decentralised exchanges. This information includes
    details like launch
    date, logo, official website URL, social links, and market fee documentation URL.

    Args:
        id (str | Unset):
        aux (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V4DEXListingsInfoResponseModel]
    """

    kwargs = _get_kwargs(
        id=id,
        aux=aux,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    aux: str | Unset = "",
) -> V4DEXListingsInfoResponseModel | None:
    """DEX Metadata

     Returns all static metadata for one or more decentralised exchanges. This information includes
    details like launch
    date, logo, official website URL, social links, and market fee documentation URL.

    Args:
        id (str | Unset):
        aux (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V4DEXListingsInfoResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            aux=aux,
        )
    ).parsed
