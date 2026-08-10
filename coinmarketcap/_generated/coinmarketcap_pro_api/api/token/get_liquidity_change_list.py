from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.liquidity_change_list_response_dto import LiquidityChangeListResponseDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
    type_: int | Unset = UNSET,
    maker: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_type: str | Unset = UNSET,
    start_time: int | Unset = UNSET,
    end_time: int | Unset = UNSET,
    min_volume: float | Unset = UNSET,
    max_volume: float | Unset = UNSET,
    last_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["platform"] = platform

    params["address"] = address

    params["type"] = type_

    params["maker"] = maker

    params["sortBy"] = sort_by

    params["sortType"] = sort_type

    params["startTime"] = start_time

    params["endTime"] = end_time

    params["minVolume"] = min_volume

    params["maxVolume"] = max_volume

    params["lastId"] = last_id

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/dex/liquidity-change/list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LiquidityChangeListResponseDTO | None:
    if response.status_code == 200:
        response_200 = LiquidityChangeListResponseDTO.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LiquidityChangeListResponseDTO]:
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
    type_: int | Unset = UNSET,
    maker: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_type: str | Unset = UNSET,
    start_time: int | Unset = UNSET,
    end_time: int | Unset = UNSET,
    min_volume: float | Unset = UNSET,
    max_volume: float | Unset = UNSET,
    last_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[LiquidityChangeListResponseDTO]:
    r"""Get liquidity change list

     Get liquidity change history for a token

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/liquidity-change/list`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):
        type_ (int | Unset):
        maker (str | Unset):
        sort_by (str | Unset):
        sort_type (str | Unset):
        start_time (int | Unset):
        end_time (int | Unset):
        min_volume (float | Unset):
        max_volume (float | Unset):
        last_id (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiquidityChangeListResponseDTO]
    """

    kwargs = _get_kwargs(
        platform=platform,
        address=address,
        type_=type_,
        maker=maker,
        sort_by=sort_by,
        sort_type=sort_type,
        start_time=start_time,
        end_time=end_time,
        min_volume=min_volume,
        max_volume=max_volume,
        last_id=last_id,
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
    address: str | Unset = UNSET,
    type_: int | Unset = UNSET,
    maker: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_type: str | Unset = UNSET,
    start_time: int | Unset = UNSET,
    end_time: int | Unset = UNSET,
    min_volume: float | Unset = UNSET,
    max_volume: float | Unset = UNSET,
    last_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> LiquidityChangeListResponseDTO | None:
    r"""Get liquidity change list

     Get liquidity change history for a token

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/liquidity-change/list`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):
        type_ (int | Unset):
        maker (str | Unset):
        sort_by (str | Unset):
        sort_type (str | Unset):
        start_time (int | Unset):
        end_time (int | Unset):
        min_volume (float | Unset):
        max_volume (float | Unset):
        last_id (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiquidityChangeListResponseDTO
    """

    return sync_detailed(
        client=client,
        platform=platform,
        address=address,
        type_=type_,
        maker=maker,
        sort_by=sort_by,
        sort_type=sort_type,
        start_time=start_time,
        end_time=end_time,
        min_volume=min_volume,
        max_volume=max_volume,
        last_id=last_id,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
    type_: int | Unset = UNSET,
    maker: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_type: str | Unset = UNSET,
    start_time: int | Unset = UNSET,
    end_time: int | Unset = UNSET,
    min_volume: float | Unset = UNSET,
    max_volume: float | Unset = UNSET,
    last_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[LiquidityChangeListResponseDTO]:
    r"""Get liquidity change list

     Get liquidity change history for a token

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/liquidity-change/list`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):
        type_ (int | Unset):
        maker (str | Unset):
        sort_by (str | Unset):
        sort_type (str | Unset):
        start_time (int | Unset):
        end_time (int | Unset):
        min_volume (float | Unset):
        max_volume (float | Unset):
        last_id (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LiquidityChangeListResponseDTO]
    """

    kwargs = _get_kwargs(
        platform=platform,
        address=address,
        type_=type_,
        maker=maker,
        sort_by=sort_by,
        sort_type=sort_type,
        start_time=start_time,
        end_time=end_time,
        min_volume=min_volume,
        max_volume=max_volume,
        last_id=last_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
    type_: int | Unset = UNSET,
    maker: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_type: str | Unset = UNSET,
    start_time: int | Unset = UNSET,
    end_time: int | Unset = UNSET,
    min_volume: float | Unset = UNSET,
    max_volume: float | Unset = UNSET,
    last_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> LiquidityChangeListResponseDTO | None:
    r"""Get liquidity change list

     Get liquidity change history for a token

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/dex/liquidity-change/list`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):
        type_ (int | Unset):
        maker (str | Unset):
        sort_by (str | Unset):
        sort_type (str | Unset):
        start_time (int | Unset):
        end_time (int | Unset):
        min_volume (float | Unset):
        max_volume (float | Unset):
        last_id (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LiquidityChangeListResponseDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            platform=platform,
            address=address,
            type_=type_,
            maker=maker,
            sort_by=sort_by,
            sort_type=sort_type,
            start_time=start_time,
            end_time=end_time,
            min_volume=min_volume,
            max_volume=max_volume,
            last_id=last_id,
            limit=limit,
        )
    ).parsed
