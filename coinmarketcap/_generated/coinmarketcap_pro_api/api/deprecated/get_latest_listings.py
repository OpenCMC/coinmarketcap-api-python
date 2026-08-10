from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dex_info_dto import DexInfoDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: str | Unset = "1",
    limit: str | Unset = "50",
    sort: str | Unset = "volume_24h",
    sort_dir: str | Unset = "desc",
    type_: str | Unset = "all",
    aux: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["start"] = start

    params["limit"] = limit

    params["sort"] = sort

    params["sort_dir"] = sort_dir

    params["type"] = type_

    params["aux"] = aux

    params["convert_id"] = convert_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/dex/listings/quotes",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[DexInfoDTO] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DexInfoDTO.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[DexInfoDTO]]:
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
    sort: str | Unset = "volume_24h",
    sort_dir: str | Unset = "desc",
    type_: str | Unset = "all",
    aux: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> Response[list[DexInfoDTO]]:
    r"""DEX Listings Latest

     Returns a paginated list of all decentralised cryptocurrency exchanges including
    the latest aggregate market data for each exchange. Use the \"convert\" option to
    return market values in multiple fiat and cryptocurrency conversions in the same call.

    Args:
        start (str | Unset):  Default: '1'.
        limit (str | Unset):  Default: '50'.
        sort (str | Unset):  Default: 'volume_24h'.
        sort_dir (str | Unset):  Default: 'desc'.
        type_ (str | Unset):  Default: 'all'.
        aux (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[DexInfoDTO]]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
        sort=sort,
        sort_dir=sort_dir,
        type_=type_,
        aux=aux,
        convert_id=convert_id,
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
    sort: str | Unset = "volume_24h",
    sort_dir: str | Unset = "desc",
    type_: str | Unset = "all",
    aux: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> list[DexInfoDTO] | None:
    r"""DEX Listings Latest

     Returns a paginated list of all decentralised cryptocurrency exchanges including
    the latest aggregate market data for each exchange. Use the \"convert\" option to
    return market values in multiple fiat and cryptocurrency conversions in the same call.

    Args:
        start (str | Unset):  Default: '1'.
        limit (str | Unset):  Default: '50'.
        sort (str | Unset):  Default: 'volume_24h'.
        sort_dir (str | Unset):  Default: 'desc'.
        type_ (str | Unset):  Default: 'all'.
        aux (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[DexInfoDTO]
    """

    return sync_detailed(
        client=client,
        start=start,
        limit=limit,
        sort=sort,
        sort_dir=sort_dir,
        type_=type_,
        aux=aux,
        convert_id=convert_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: str | Unset = "1",
    limit: str | Unset = "50",
    sort: str | Unset = "volume_24h",
    sort_dir: str | Unset = "desc",
    type_: str | Unset = "all",
    aux: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> Response[list[DexInfoDTO]]:
    r"""DEX Listings Latest

     Returns a paginated list of all decentralised cryptocurrency exchanges including
    the latest aggregate market data for each exchange. Use the \"convert\" option to
    return market values in multiple fiat and cryptocurrency conversions in the same call.

    Args:
        start (str | Unset):  Default: '1'.
        limit (str | Unset):  Default: '50'.
        sort (str | Unset):  Default: 'volume_24h'.
        sort_dir (str | Unset):  Default: 'desc'.
        type_ (str | Unset):  Default: 'all'.
        aux (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[DexInfoDTO]]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
        sort=sort,
        sort_dir=sort_dir,
        type_=type_,
        aux=aux,
        convert_id=convert_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start: str | Unset = "1",
    limit: str | Unset = "50",
    sort: str | Unset = "volume_24h",
    sort_dir: str | Unset = "desc",
    type_: str | Unset = "all",
    aux: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> list[DexInfoDTO] | None:
    r"""DEX Listings Latest

     Returns a paginated list of all decentralised cryptocurrency exchanges including
    the latest aggregate market data for each exchange. Use the \"convert\" option to
    return market values in multiple fiat and cryptocurrency conversions in the same call.

    Args:
        start (str | Unset):  Default: '1'.
        limit (str | Unset):  Default: '50'.
        sort (str | Unset):  Default: 'volume_24h'.
        sort_dir (str | Unset):  Default: 'desc'.
        type_ (str | Unset):  Default: 'all'.
        aux (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[DexInfoDTO]
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            limit=limit,
            sort=sort,
            sort_dir=sort_dir,
            type_=type_,
            aux=aux,
            convert_id=convert_id,
        )
    ).parsed
