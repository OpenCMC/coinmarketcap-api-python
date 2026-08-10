from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response_of_index_historical_response_dto import ApiResponseOfIndexHistoricalResponseDTO
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: str | Unset = UNSET,
    interval: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["time_start"] = time_start

    params["time_end"] = time_end

    params["count"] = count

    params["interval"] = interval

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/index/cmc100-historical",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ApiResponseOfIndexHistoricalResponseDTO
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = ApiResponseOfIndexHistoricalResponseDTO.from_dict(response.json())

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
    ApiResponseOfIndexHistoricalResponseDTO
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
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
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: str | Unset = UNSET,
    interval: str | Unset = UNSET,
) -> Response[
    ApiResponseOfIndexHistoricalResponseDTO
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""CoinMarketCap 100 Index Historical

     Returns an interval of historic CoinMarketCap 100 Index values based on the interval parameter.



     **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
     - Basic
     - Startup
     - Builder
     - Growth
     - Professional
     - Enterprise

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v3/index/cmc100-historical`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 5 minutes.
    **Plan credit use:** 1 API call credit per request no matter query size.
    **CMC equivalent pages:** Our CoinMarketCap 100 Index on https://coinmarketcap.com/charts/cmc100/.

    Args:
        time_start (str | Unset):
        time_end (str | Unset):
        count (str | Unset):
        interval (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiResponseOfIndexHistoricalResponseDTO | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        time_start=time_start,
        time_end=time_end,
        count=count,
        interval=interval,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: str | Unset = UNSET,
    interval: str | Unset = UNSET,
) -> (
    ApiResponseOfIndexHistoricalResponseDTO
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""CoinMarketCap 100 Index Historical

     Returns an interval of historic CoinMarketCap 100 Index values based on the interval parameter.



     **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
     - Basic
     - Startup
     - Builder
     - Growth
     - Professional
     - Enterprise

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v3/index/cmc100-historical`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 5 minutes.
    **Plan credit use:** 1 API call credit per request no matter query size.
    **CMC equivalent pages:** Our CoinMarketCap 100 Index on https://coinmarketcap.com/charts/cmc100/.

    Args:
        time_start (str | Unset):
        time_end (str | Unset):
        count (str | Unset):
        interval (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiResponseOfIndexHistoricalResponseDTO | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        time_start=time_start,
        time_end=time_end,
        count=count,
        interval=interval,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: str | Unset = UNSET,
    interval: str | Unset = UNSET,
) -> Response[
    ApiResponseOfIndexHistoricalResponseDTO
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""CoinMarketCap 100 Index Historical

     Returns an interval of historic CoinMarketCap 100 Index values based on the interval parameter.



     **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
     - Basic
     - Startup
     - Builder
     - Growth
     - Professional
     - Enterprise

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v3/index/cmc100-historical`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 5 minutes.
    **Plan credit use:** 1 API call credit per request no matter query size.
    **CMC equivalent pages:** Our CoinMarketCap 100 Index on https://coinmarketcap.com/charts/cmc100/.

    Args:
        time_start (str | Unset):
        time_end (str | Unset):
        count (str | Unset):
        interval (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiResponseOfIndexHistoricalResponseDTO | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        time_start=time_start,
        time_end=time_end,
        count=count,
        interval=interval,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: str | Unset = UNSET,
    interval: str | Unset = UNSET,
) -> (
    ApiResponseOfIndexHistoricalResponseDTO
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""CoinMarketCap 100 Index Historical

     Returns an interval of historic CoinMarketCap 100 Index values based on the interval parameter.



     **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
     - Basic
     - Startup
     - Builder
     - Growth
     - Professional
     - Enterprise

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v3/index/cmc100-historical`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 5 minutes.
    **Plan credit use:** 1 API call credit per request no matter query size.
    **CMC equivalent pages:** Our CoinMarketCap 100 Index on https://coinmarketcap.com/charts/cmc100/.

    Args:
        time_start (str | Unset):
        time_end (str | Unset):
        count (str | Unset):
        interval (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiResponseOfIndexHistoricalResponseDTO | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            time_start=time_start,
            time_end=time_end,
            count=count,
            interval=interval,
        )
    ).parsed
