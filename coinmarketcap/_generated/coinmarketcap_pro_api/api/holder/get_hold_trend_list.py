from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.holder_trend_vo import HolderTrendVO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    platform: str | Unset = UNSET,
    token_address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["platform"] = platform

    params["tokenAddress"] = token_address

    params["interval"] = interval

    params["from"] = from_

    params["to"] = to

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/dex/holders/trend/list",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[HolderTrendVO] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = HolderTrendVO.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[HolderTrendVO]]:
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
    token_address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[list[HolderTrendVO]]:
    """Get holder trend list

     Get detailed information for holders trend list

    Args:
        platform (str | Unset):
        token_address (str | Unset):
        interval (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[HolderTrendVO]]
    """

    kwargs = _get_kwargs(
        platform=platform,
        token_address=token_address,
        interval=interval,
        from_=from_,
        to=to,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    token_address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> list[HolderTrendVO] | None:
    """Get holder trend list

     Get detailed information for holders trend list

    Args:
        platform (str | Unset):
        token_address (str | Unset):
        interval (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[HolderTrendVO]
    """

    return sync_detailed(
        client=client,
        platform=platform,
        token_address=token_address,
        interval=interval,
        from_=from_,
        to=to,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    token_address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[list[HolderTrendVO]]:
    """Get holder trend list

     Get detailed information for holders trend list

    Args:
        platform (str | Unset):
        token_address (str | Unset):
        interval (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[HolderTrendVO]]
    """

    kwargs = _get_kwargs(
        platform=platform,
        token_address=token_address,
        interval=interval,
        from_=from_,
        to=to,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    token_address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> list[HolderTrendVO] | None:
    """Get holder trend list

     Get detailed information for holders trend list

    Args:
        platform (str | Unset):
        token_address (str | Unset):
        interval (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[HolderTrendVO]
    """

    return (
        await asyncio_detailed(
            client=client,
            platform=platform,
            token_address=token_address,
            interval=interval,
            from_=from_,
            to=to,
            limit=limit,
        )
    ).parsed
