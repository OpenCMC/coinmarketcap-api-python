from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cryptocurrency_trending_most_visited_response_model import CryptocurrencyTrendingMostVisitedResponseModel
from ...models.get_v1_cryptocurrency_trending_mostvisited_time_period import (
    GetV1CryptocurrencyTrendingMostvisitedTimePeriod,
)
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    time_period: GetV1CryptocurrencyTrendingMostvisitedTimePeriod | Unset = "24h",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["start"] = start

    params["limit"] = limit

    json_time_period: str | Unset = UNSET
    if not isinstance(time_period, Unset):
        json_time_period = time_period

    params["time_period"] = json_time_period

    params["convert"] = convert

    params["convert_id"] = convert_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/cryptocurrency/trending/most-visited",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CryptocurrencyTrendingMostVisitedResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = CryptocurrencyTrendingMostVisitedResponseModel.from_dict(response.json())

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
    CryptocurrencyTrendingMostVisitedResponseModel
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
    start: int | Unset = 1,
    limit: int | Unset = 100,
    time_period: GetV1CryptocurrencyTrendingMostvisitedTimePeriod | Unset = "24h",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> Response[
    CryptocurrencyTrendingMostVisitedResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """Trending Most Visited

     Returns a paginated list of all trending cryptocurrency market data, determined and sorted by
    traffic to coin detail pages.



      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 24 hours.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** The CoinMarketCap “Most Visited” trending list. [coinmarketcap.com/most-
    viewed-pages/](https://coinmarketcap.com/most-viewed-pages/).

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        time_period (GetV1CryptocurrencyTrendingMostvisitedTimePeriod | Unset):  Default: '24h'.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyTrendingMostVisitedResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
        time_period=time_period,
        convert=convert,
        convert_id=convert_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    time_period: GetV1CryptocurrencyTrendingMostvisitedTimePeriod | Unset = "24h",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> (
    CryptocurrencyTrendingMostVisitedResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """Trending Most Visited

     Returns a paginated list of all trending cryptocurrency market data, determined and sorted by
    traffic to coin detail pages.



      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 24 hours.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** The CoinMarketCap “Most Visited” trending list. [coinmarketcap.com/most-
    viewed-pages/](https://coinmarketcap.com/most-viewed-pages/).

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        time_period (GetV1CryptocurrencyTrendingMostvisitedTimePeriod | Unset):  Default: '24h'.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyTrendingMostVisitedResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        start=start,
        limit=limit,
        time_period=time_period,
        convert=convert,
        convert_id=convert_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    time_period: GetV1CryptocurrencyTrendingMostvisitedTimePeriod | Unset = "24h",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> Response[
    CryptocurrencyTrendingMostVisitedResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """Trending Most Visited

     Returns a paginated list of all trending cryptocurrency market data, determined and sorted by
    traffic to coin detail pages.



      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 24 hours.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** The CoinMarketCap “Most Visited” trending list. [coinmarketcap.com/most-
    viewed-pages/](https://coinmarketcap.com/most-viewed-pages/).

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        time_period (GetV1CryptocurrencyTrendingMostvisitedTimePeriod | Unset):  Default: '24h'.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyTrendingMostVisitedResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
        time_period=time_period,
        convert=convert,
        convert_id=convert_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    time_period: GetV1CryptocurrencyTrendingMostvisitedTimePeriod | Unset = "24h",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> (
    CryptocurrencyTrendingMostVisitedResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """Trending Most Visited

     Returns a paginated list of all trending cryptocurrency market data, determined and sorted by
    traffic to coin detail pages.



      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 24 hours.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** The CoinMarketCap “Most Visited” trending list. [coinmarketcap.com/most-
    viewed-pages/](https://coinmarketcap.com/most-viewed-pages/).

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        time_period (GetV1CryptocurrencyTrendingMostvisitedTimePeriod | Unset):  Default: '24h'.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyTrendingMostVisitedResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            limit=limit,
            time_period=time_period,
            convert=convert,
            convert_id=convert_id,
        )
    ).parsed
