from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dex_multiplier_response_model import DexMultiplierResponseModel
from ...models.dex_multiplier_validation_error_object import DexMultiplierValidationErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    platform: str | Unset = UNSET,
    platform_id: int | Unset = UNSET,
    token_address: str | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["platform"] = platform

    params["platform_id"] = platform_id

    params["token_address"] = token_address

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/dex/multiplier",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DexMultiplierResponseModel | DexMultiplierValidationErrorObject | None:
    if response.status_code == 200:
        response_200 = DexMultiplierResponseModel.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DexMultiplierValidationErrorObject.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DexMultiplierResponseModel | DexMultiplierValidationErrorObject]:
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
    platform_id: int | Unset = UNSET,
    token_address: str | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> Response[DexMultiplierResponseModel | DexMultiplierValidationErrorObject]:
    """Get token multiplier

     Returns a paginated list of tokens that has a ERC-8056 UI multiplier.

    You may filter by `platform` or `platform_id` (if both are provided, `platform_id` takes
    precedence). When querying a specific token via `token_address`, you must also provide at least one
    of `platform` or `platform_id`.

    Pagination is controlled by `start` (1-based index) and `limit` (default 100, max 2000).

    **No credit is needed when querying this endpoint.**

    Args:
        platform (str | Unset):  Example: bsc.
        platform_id (int | Unset):  Example: 14.
        token_address (str | Unset):  Example: 0x1234567890abcdef1234567890abcdef12345678.
        start (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 100. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DexMultiplierResponseModel | DexMultiplierValidationErrorObject]
    """

    kwargs = _get_kwargs(
        platform=platform,
        platform_id=platform_id,
        token_address=token_address,
        start=start,
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
    platform_id: int | Unset = UNSET,
    token_address: str | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> DexMultiplierResponseModel | DexMultiplierValidationErrorObject | None:
    """Get token multiplier

     Returns a paginated list of tokens that has a ERC-8056 UI multiplier.

    You may filter by `platform` or `platform_id` (if both are provided, `platform_id` takes
    precedence). When querying a specific token via `token_address`, you must also provide at least one
    of `platform` or `platform_id`.

    Pagination is controlled by `start` (1-based index) and `limit` (default 100, max 2000).

    **No credit is needed when querying this endpoint.**

    Args:
        platform (str | Unset):  Example: bsc.
        platform_id (int | Unset):  Example: 14.
        token_address (str | Unset):  Example: 0x1234567890abcdef1234567890abcdef12345678.
        start (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 100. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DexMultiplierResponseModel | DexMultiplierValidationErrorObject
    """

    return sync_detailed(
        client=client,
        platform=platform,
        platform_id=platform_id,
        token_address=token_address,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    platform_id: int | Unset = UNSET,
    token_address: str | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> Response[DexMultiplierResponseModel | DexMultiplierValidationErrorObject]:
    """Get token multiplier

     Returns a paginated list of tokens that has a ERC-8056 UI multiplier.

    You may filter by `platform` or `platform_id` (if both are provided, `platform_id` takes
    precedence). When querying a specific token via `token_address`, you must also provide at least one
    of `platform` or `platform_id`.

    Pagination is controlled by `start` (1-based index) and `limit` (default 100, max 2000).

    **No credit is needed when querying this endpoint.**

    Args:
        platform (str | Unset):  Example: bsc.
        platform_id (int | Unset):  Example: 14.
        token_address (str | Unset):  Example: 0x1234567890abcdef1234567890abcdef12345678.
        start (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 100. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DexMultiplierResponseModel | DexMultiplierValidationErrorObject]
    """

    kwargs = _get_kwargs(
        platform=platform,
        platform_id=platform_id,
        token_address=token_address,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    platform_id: int | Unset = UNSET,
    token_address: str | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> DexMultiplierResponseModel | DexMultiplierValidationErrorObject | None:
    """Get token multiplier

     Returns a paginated list of tokens that has a ERC-8056 UI multiplier.

    You may filter by `platform` or `platform_id` (if both are provided, `platform_id` takes
    precedence). When querying a specific token via `token_address`, you must also provide at least one
    of `platform` or `platform_id`.

    Pagination is controlled by `start` (1-based index) and `limit` (default 100, max 2000).

    **No credit is needed when querying this endpoint.**

    Args:
        platform (str | Unset):  Example: bsc.
        platform_id (int | Unset):  Example: 14.
        token_address (str | Unset):  Example: 0x1234567890abcdef1234567890abcdef12345678.
        start (int | Unset):  Default: 1. Example: 1.
        limit (int | Unset):  Default: 100. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DexMultiplierResponseModel | DexMultiplierValidationErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            platform=platform,
            platform_id=platform_id,
            token_address=token_address,
            start=start,
            limit=limit,
        )
    ).parsed
