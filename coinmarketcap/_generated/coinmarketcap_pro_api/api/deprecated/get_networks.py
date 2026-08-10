from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.network_info_dto import NetworkInfoDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: str | Unset = "1",
    limit: str | Unset = "50",
    sort: str | Unset = "id",
    sort_dir: str | Unset = "desc",
    aux: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["start"] = start

    params["limit"] = limit

    params["sort"] = sort

    params["sort_dir"] = sort_dir

    params["aux"] = aux

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/dex/networks/list",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[NetworkInfoDTO] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = NetworkInfoDTO.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[NetworkInfoDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: str | Unset = "1",
    limit: str | Unset = "50",
    sort: str | Unset = "id",
    sort_dir: str | Unset = "desc",
    aux: str | Unset = UNSET,
) -> Response[list[NetworkInfoDTO]]:
    """CoinMarketCap ID Map

     Returns a list of all networks to unique CoinMarketCap ids.Per our Best Practices we recommend
    utilizing CMC ID instead of network symbols to securely identify networks with our other endpoints
    and in your own application logic. Each network returned includes typical identifiers such as name,
    symbol, and token_address for flexible mapping to id.

    Args:
        start (str | Unset):  Default: '1'.
        limit (str | Unset):  Default: '50'.
        sort (str | Unset):  Default: 'id'.
        sort_dir (str | Unset):  Default: 'desc'.
        aux (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[NetworkInfoDTO]]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
        sort=sort,
        sort_dir=sort_dir,
        aux=aux,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    start: str | Unset = "1",
    limit: str | Unset = "50",
    sort: str | Unset = "id",
    sort_dir: str | Unset = "desc",
    aux: str | Unset = UNSET,
) -> list[NetworkInfoDTO] | None:
    """CoinMarketCap ID Map

     Returns a list of all networks to unique CoinMarketCap ids.Per our Best Practices we recommend
    utilizing CMC ID instead of network symbols to securely identify networks with our other endpoints
    and in your own application logic. Each network returned includes typical identifiers such as name,
    symbol, and token_address for flexible mapping to id.

    Args:
        start (str | Unset):  Default: '1'.
        limit (str | Unset):  Default: '50'.
        sort (str | Unset):  Default: 'id'.
        sort_dir (str | Unset):  Default: 'desc'.
        aux (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[NetworkInfoDTO]
    """

    return sync_detailed(
        client=client,
        start=start,
        limit=limit,
        sort=sort,
        sort_dir=sort_dir,
        aux=aux,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: str | Unset = "1",
    limit: str | Unset = "50",
    sort: str | Unset = "id",
    sort_dir: str | Unset = "desc",
    aux: str | Unset = UNSET,
) -> Response[list[NetworkInfoDTO]]:
    """CoinMarketCap ID Map

     Returns a list of all networks to unique CoinMarketCap ids.Per our Best Practices we recommend
    utilizing CMC ID instead of network symbols to securely identify networks with our other endpoints
    and in your own application logic. Each network returned includes typical identifiers such as name,
    symbol, and token_address for flexible mapping to id.

    Args:
        start (str | Unset):  Default: '1'.
        limit (str | Unset):  Default: '50'.
        sort (str | Unset):  Default: 'id'.
        sort_dir (str | Unset):  Default: 'desc'.
        aux (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[NetworkInfoDTO]]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
        sort=sort,
        sort_dir=sort_dir,
        aux=aux,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start: str | Unset = "1",
    limit: str | Unset = "50",
    sort: str | Unset = "id",
    sort_dir: str | Unset = "desc",
    aux: str | Unset = UNSET,
) -> list[NetworkInfoDTO] | None:
    """CoinMarketCap ID Map

     Returns a list of all networks to unique CoinMarketCap ids.Per our Best Practices we recommend
    utilizing CMC ID instead of network symbols to securely identify networks with our other endpoints
    and in your own application logic. Each network returned includes typical identifiers such as name,
    symbol, and token_address for flexible mapping to id.

    Args:
        start (str | Unset):  Default: '1'.
        limit (str | Unset):  Default: '50'.
        sort (str | Unset):  Default: 'id'.
        sort_dir (str | Unset):  Default: 'desc'.
        aux (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[NetworkInfoDTO]
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            limit=limit,
            sort=sort,
            sort_dir=sort_dir,
            aux=aux,
        )
    ).parsed
