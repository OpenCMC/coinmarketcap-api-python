from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...models.rwa_issuers_list_response_model import RWAIssuersListResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    issuer_id: str | Unset = UNSET,
    active: bool | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    skip_invalid: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["issuer_id"] = issuer_id

    params["active"] = active

    params["start"] = start

    params["limit"] = limit

    params["skip_invalid"] = skip_invalid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v5/real-world-assets/issuers/list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAIssuersListResponseModel
    | None
):
    if response.status_code == 200:
        response_200 = RWAIssuersListResponseModel.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = HTTPStatus400ErrorObject.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = HTTPStatus401ErrorObject.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = HTTPStatus403ErrorObject.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = HTTPStatus429ErrorObject.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = HTTPStatus500ErrorObject.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAIssuersListResponseModel
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    issuer_id: str | Unset = UNSET,
    active: bool | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    skip_invalid: str | Unset = UNSET,
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAIssuersListResponseModel
]:
    """Issuers List

     Returns a paginated list of all token issuers CoinMarketCap tracks for RWA assets (e.g. Backed
    Assets, bStocks, Backpack), each with a count of linked tokens but not the tokens themselves. To
    retrieve a single issuer with its linked tokens, use `/v5/real-world-assets/issuers` (Issuer).
    Mirrors the `/v1/cryptocurrency/categories` (list) vs `/v1/cryptocurrency/category` (single) split.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 30 seconds.
    **Plan credit use:** 1 call credit per request, no matter the query size.

    Args:
        issuer_id (str | Unset):  Example: 6a2d54b697c45356b1a634f4.
        active (bool | Unset):
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAIssuersListResponseModel]
    """

    kwargs = _get_kwargs(
        issuer_id=issuer_id,
        active=active,
        start=start,
        limit=limit,
        skip_invalid=skip_invalid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    issuer_id: str | Unset = UNSET,
    active: bool | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    skip_invalid: str | Unset = UNSET,
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAIssuersListResponseModel
    | None
):
    """Issuers List

     Returns a paginated list of all token issuers CoinMarketCap tracks for RWA assets (e.g. Backed
    Assets, bStocks, Backpack), each with a count of linked tokens but not the tokens themselves. To
    retrieve a single issuer with its linked tokens, use `/v5/real-world-assets/issuers` (Issuer).
    Mirrors the `/v1/cryptocurrency/categories` (list) vs `/v1/cryptocurrency/category` (single) split.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 30 seconds.
    **Plan credit use:** 1 call credit per request, no matter the query size.

    Args:
        issuer_id (str | Unset):  Example: 6a2d54b697c45356b1a634f4.
        active (bool | Unset):
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAIssuersListResponseModel
    """

    return sync_detailed(
        client=client,
        issuer_id=issuer_id,
        active=active,
        start=start,
        limit=limit,
        skip_invalid=skip_invalid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    issuer_id: str | Unset = UNSET,
    active: bool | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    skip_invalid: str | Unset = UNSET,
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAIssuersListResponseModel
]:
    """Issuers List

     Returns a paginated list of all token issuers CoinMarketCap tracks for RWA assets (e.g. Backed
    Assets, bStocks, Backpack), each with a count of linked tokens but not the tokens themselves. To
    retrieve a single issuer with its linked tokens, use `/v5/real-world-assets/issuers` (Issuer).
    Mirrors the `/v1/cryptocurrency/categories` (list) vs `/v1/cryptocurrency/category` (single) split.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 30 seconds.
    **Plan credit use:** 1 call credit per request, no matter the query size.

    Args:
        issuer_id (str | Unset):  Example: 6a2d54b697c45356b1a634f4.
        active (bool | Unset):
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAIssuersListResponseModel]
    """

    kwargs = _get_kwargs(
        issuer_id=issuer_id,
        active=active,
        start=start,
        limit=limit,
        skip_invalid=skip_invalid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    issuer_id: str | Unset = UNSET,
    active: bool | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    skip_invalid: str | Unset = UNSET,
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAIssuersListResponseModel
    | None
):
    """Issuers List

     Returns a paginated list of all token issuers CoinMarketCap tracks for RWA assets (e.g. Backed
    Assets, bStocks, Backpack), each with a count of linked tokens but not the tokens themselves. To
    retrieve a single issuer with its linked tokens, use `/v5/real-world-assets/issuers` (Issuer).
    Mirrors the `/v1/cryptocurrency/categories` (list) vs `/v1/cryptocurrency/category` (single) split.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 30 seconds.
    **Plan credit use:** 1 call credit per request, no matter the query size.

    Args:
        issuer_id (str | Unset):  Example: 6a2d54b697c45356b1a634f4.
        active (bool | Unset):
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAIssuersListResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            issuer_id=issuer_id,
            active=active,
            start=start,
            limit=limit,
            skip_invalid=skip_invalid,
        )
    ).parsed
