from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    unit: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    pm: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["platform"] = platform

    params["address"] = address

    params["interval"] = interval

    params["from"] = from_

    params["to"] = to

    params["unit"] = unit

    params["limit"] = limit

    params["pm"] = pm

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/k-line/points",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[list[float]] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = cast(list[float], response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[list[float]]]:
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
    address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    unit: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    pm: str | Unset = UNSET,
) -> Response[list[list[float]]]:
    r"""Get K-line points

     Get K-line price points for a token.

    Response Format: Each point is an array with 3 elements:
    - **[0]** price: Token price
    - **[1]** volume: Trading volume
    - **[2]** timestamp: UNIX timestamp (seconds)

    Example: ``[[1.23, 50000, 1705363200], ...]``

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/k-line/points`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):
        interval (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        unit (str | Unset):
        limit (int | Unset):
        pm (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[list[float]]]
    """

    kwargs = _get_kwargs(
        platform=platform,
        address=address,
        interval=interval,
        from_=from_,
        to=to,
        unit=unit,
        limit=limit,
        pm=pm,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    unit: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    pm: str | Unset = UNSET,
) -> list[list[float]] | None:
    r"""Get K-line points

     Get K-line price points for a token.

    Response Format: Each point is an array with 3 elements:
    - **[0]** price: Token price
    - **[1]** volume: Trading volume
    - **[2]** timestamp: UNIX timestamp (seconds)

    Example: ``[[1.23, 50000, 1705363200], ...]``

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/k-line/points`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):
        interval (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        unit (str | Unset):
        limit (int | Unset):
        pm (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[list[float]]
    """

    return sync_detailed(
        client=client,
        platform=platform,
        address=address,
        interval=interval,
        from_=from_,
        to=to,
        unit=unit,
        limit=limit,
        pm=pm,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    unit: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    pm: str | Unset = UNSET,
) -> Response[list[list[float]]]:
    r"""Get K-line points

     Get K-line price points for a token.

    Response Format: Each point is an array with 3 elements:
    - **[0]** price: Token price
    - **[1]** volume: Trading volume
    - **[2]** timestamp: UNIX timestamp (seconds)

    Example: ``[[1.23, 50000, 1705363200], ...]``

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/k-line/points`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):
        interval (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        unit (str | Unset):
        limit (int | Unset):
        pm (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[list[float]]]
    """

    kwargs = _get_kwargs(
        platform=platform,
        address=address,
        interval=interval,
        from_=from_,
        to=to,
        unit=unit,
        limit=limit,
        pm=pm,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    unit: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    pm: str | Unset = UNSET,
) -> list[list[float]] | None:
    r"""Get K-line points

     Get K-line price points for a token.

    Response Format: Each point is an array with 3 elements:
    - **[0]** price: Token price
    - **[1]** volume: Trading volume
    - **[2]** timestamp: UNIX timestamp (seconds)

    Example: ``[[1.23, 50000, 1705363200], ...]``

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/k-line/points`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):
        interval (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        unit (str | Unset):
        limit (int | Unset):
        pm (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[list[float]]
    """

    return (
        await asyncio_detailed(
            client=client,
            platform=platform,
            address=address,
            interval=interval,
            from_=from_,
            to=to,
            unit=unit,
            limit=limit,
            pm=pm,
        )
    ).parsed
