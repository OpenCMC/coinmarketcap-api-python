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
from ...models.rwa_issuer_response_model import RWAIssuerResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    issuer_id: str,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["issuer_id"] = issuer_id

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v5/real-world-assets/issuers",
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
    | RWAIssuerResponseModel
    | None
):
    if response.status_code == 200:
        response_200 = RWAIssuerResponseModel.from_dict(response.json())

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
    | RWAIssuerResponseModel
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
    issuer_id: str,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAIssuerResponseModel
]:
    """Issuer

     Returns a single issuer with its full list of linked tokens (the cryptos issued by that issuer, each
    tied to an RWA asset). Requires a single `issuer_id`, which you can obtain from `/v5/real-world-
    assets/issuers/list` (Issuers List). Mirrors `/v1/cryptocurrency/category`, which returns one
    category with its nested coins.

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
        issuer_id (str):  Example: 6a2d54b697c45356b1a634f4.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAIssuerResponseModel]
    """

    kwargs = _get_kwargs(
        issuer_id=issuer_id,
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
    issuer_id: str,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAIssuerResponseModel
    | None
):
    """Issuer

     Returns a single issuer with its full list of linked tokens (the cryptos issued by that issuer, each
    tied to an RWA asset). Requires a single `issuer_id`, which you can obtain from `/v5/real-world-
    assets/issuers/list` (Issuers List). Mirrors `/v1/cryptocurrency/category`, which returns one
    category with its nested coins.

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
        issuer_id (str):  Example: 6a2d54b697c45356b1a634f4.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAIssuerResponseModel
    """

    return sync_detailed(
        client=client,
        issuer_id=issuer_id,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    issuer_id: str,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAIssuerResponseModel
]:
    """Issuer

     Returns a single issuer with its full list of linked tokens (the cryptos issued by that issuer, each
    tied to an RWA asset). Requires a single `issuer_id`, which you can obtain from `/v5/real-world-
    assets/issuers/list` (Issuers List). Mirrors `/v1/cryptocurrency/category`, which returns one
    category with its nested coins.

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
        issuer_id (str):  Example: 6a2d54b697c45356b1a634f4.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAIssuerResponseModel]
    """

    kwargs = _get_kwargs(
        issuer_id=issuer_id,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    issuer_id: str,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAIssuerResponseModel
    | None
):
    """Issuer

     Returns a single issuer with its full list of linked tokens (the cryptos issued by that issuer, each
    tied to an RWA asset). Requires a single `issuer_id`, which you can obtain from `/v5/real-world-
    assets/issuers/list` (Issuers List). Mirrors `/v1/cryptocurrency/category`, which returns one
    category with its nested coins.

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
        issuer_id (str):  Example: 6a2d54b697c45356b1a634f4.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAIssuerResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            issuer_id=issuer_id,
            start=start,
            limit=limit,
        )
    ).parsed
