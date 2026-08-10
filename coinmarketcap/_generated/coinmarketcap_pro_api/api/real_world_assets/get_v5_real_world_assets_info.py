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
from ...models.rwa_info_response_model import RWAInfoResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    rwa_id: str | Unset = UNSET,
    rwa_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["rwa_id"] = rwa_id

    params["rwa_slug"] = rwa_slug

    params["symbol"] = symbol

    params["skip_invalid"] = skip_invalid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v5/real-world-assets/info",
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
    | RWAInfoResponseModel
    | None
):
    if response.status_code == 200:
        response_200 = RWAInfoResponseModel.from_dict(response.json())

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
    | RWAInfoResponseModel
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
    rwa_id: str | Unset = UNSET,
    rwa_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAInfoResponseModel
]:
    """Metadata

     Returns static metadata for one or more Real-World Asset (RWA) assets: nominal/company fields plus
    an About block (description, logo, website). Mirrors `/v2/cryptocurrency/info`. No market data is
    returned here — use `/v5/real-world-assets/assets/list` for tokenized quotes. At least one of
    `rwa_id`, `rwa_slug`, or `symbol` is required, and only one identifier type may be used per request.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 30 seconds.
    **Plan credit use:** 1 call credit per 250 RWA assets returned (rounded up).

    Args:
        rwa_id (str | Unset):  Example: 1,2.
        rwa_slug (str | Unset):  Example: gold,nvidia.
        symbol (str | Unset):  Example: NVDA,GOLD.
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAInfoResponseModel]
    """

    kwargs = _get_kwargs(
        rwa_id=rwa_id,
        rwa_slug=rwa_slug,
        symbol=symbol,
        skip_invalid=skip_invalid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    rwa_id: str | Unset = UNSET,
    rwa_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAInfoResponseModel
    | None
):
    """Metadata

     Returns static metadata for one or more Real-World Asset (RWA) assets: nominal/company fields plus
    an About block (description, logo, website). Mirrors `/v2/cryptocurrency/info`. No market data is
    returned here — use `/v5/real-world-assets/assets/list` for tokenized quotes. At least one of
    `rwa_id`, `rwa_slug`, or `symbol` is required, and only one identifier type may be used per request.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 30 seconds.
    **Plan credit use:** 1 call credit per 250 RWA assets returned (rounded up).

    Args:
        rwa_id (str | Unset):  Example: 1,2.
        rwa_slug (str | Unset):  Example: gold,nvidia.
        symbol (str | Unset):  Example: NVDA,GOLD.
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAInfoResponseModel
    """

    return sync_detailed(
        client=client,
        rwa_id=rwa_id,
        rwa_slug=rwa_slug,
        symbol=symbol,
        skip_invalid=skip_invalid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    rwa_id: str | Unset = UNSET,
    rwa_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAInfoResponseModel
]:
    """Metadata

     Returns static metadata for one or more Real-World Asset (RWA) assets: nominal/company fields plus
    an About block (description, logo, website). Mirrors `/v2/cryptocurrency/info`. No market data is
    returned here — use `/v5/real-world-assets/assets/list` for tokenized quotes. At least one of
    `rwa_id`, `rwa_slug`, or `symbol` is required, and only one identifier type may be used per request.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 30 seconds.
    **Plan credit use:** 1 call credit per 250 RWA assets returned (rounded up).

    Args:
        rwa_id (str | Unset):  Example: 1,2.
        rwa_slug (str | Unset):  Example: gold,nvidia.
        symbol (str | Unset):  Example: NVDA,GOLD.
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAInfoResponseModel]
    """

    kwargs = _get_kwargs(
        rwa_id=rwa_id,
        rwa_slug=rwa_slug,
        symbol=symbol,
        skip_invalid=skip_invalid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    rwa_id: str | Unset = UNSET,
    rwa_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAInfoResponseModel
    | None
):
    """Metadata

     Returns static metadata for one or more Real-World Asset (RWA) assets: nominal/company fields plus
    an About block (description, logo, website). Mirrors `/v2/cryptocurrency/info`. No market data is
    returned here — use `/v5/real-world-assets/assets/list` for tokenized quotes. At least one of
    `rwa_id`, `rwa_slug`, or `symbol` is required, and only one identifier type may be used per request.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 30 seconds.
    **Plan credit use:** 1 call credit per 250 RWA assets returned (rounded up).

    Args:
        rwa_id (str | Unset):  Example: 1,2.
        rwa_slug (str | Unset):  Example: gold,nvidia.
        symbol (str | Unset):  Example: NVDA,GOLD.
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAInfoResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            rwa_id=rwa_id,
            rwa_slug=rwa_slug,
            symbol=symbol,
            skip_invalid=skip_invalid,
        )
    ).parsed
