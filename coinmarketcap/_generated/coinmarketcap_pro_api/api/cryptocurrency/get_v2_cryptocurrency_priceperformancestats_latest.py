from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cryptocurrency_price_performance_stats_latest_response_model import (
    CryptocurrencyPricePerformanceStatsLatestResponseModel,
)
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    time_period: str | Unset = "all_time",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["slug"] = slug

    params["symbol"] = symbol

    params["time_period"] = time_period

    params["convert"] = convert

    params["convert_id"] = convert_id

    params["skip_invalid"] = skip_invalid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/cryptocurrency/price-performance-stats/latest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CryptocurrencyPricePerformanceStatsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = CryptocurrencyPricePerformanceStatsLatestResponseModel.from_dict(response.json())

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
    CryptocurrencyPricePerformanceStatsLatestResponseModel
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
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    time_period: str | Unset = "all_time",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> Response[
    CryptocurrencyPricePerformanceStatsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """Price Performance Stats

     Returns price performance statistics for one or more cryptocurrencies including launch price ROI and
    all-time high / all-time low. Stats are returned for an `all_time` period by default. UTC
    `yesterday` and a number of *rolling time periods* may be requested using the `time_period`
    parameter. Utilize the `convert` parameter to translate values into multiple fiats or
    cryptocurrencies using historical rates.


    **Please note**: This documentation relates to our updated V2 endpoint, which may be incompatible
    with our V1 versions. Documentation for deprecated endpoints can be found [the deprecated
    section](/pro-api-reference/deprecated).


      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** The statistics module displayed on cryptocurrency pages like
    [Bitcoin](https://coinmarketcap.com/currencies/bitcoin/).

    ***NOTE:** You may also use `/cryptocurrency/ohlcv/historical` for traditional OHLCV data at
    historical daily and hourly intervals. You may also use `/v1/cryptocurrency/ohlcv/latest` for OHLCV
    data for the current UTC day.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        time_period (str | Unset):  Default: 'all_time'.
        convert (str | Unset):
        convert_id (str | Unset):
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyPricePerformanceStatsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        symbol=symbol,
        time_period=time_period,
        convert=convert,
        convert_id=convert_id,
        skip_invalid=skip_invalid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    time_period: str | Unset = "all_time",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> (
    CryptocurrencyPricePerformanceStatsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """Price Performance Stats

     Returns price performance statistics for one or more cryptocurrencies including launch price ROI and
    all-time high / all-time low. Stats are returned for an `all_time` period by default. UTC
    `yesterday` and a number of *rolling time periods* may be requested using the `time_period`
    parameter. Utilize the `convert` parameter to translate values into multiple fiats or
    cryptocurrencies using historical rates.


    **Please note**: This documentation relates to our updated V2 endpoint, which may be incompatible
    with our V1 versions. Documentation for deprecated endpoints can be found [the deprecated
    section](/pro-api-reference/deprecated).


      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** The statistics module displayed on cryptocurrency pages like
    [Bitcoin](https://coinmarketcap.com/currencies/bitcoin/).

    ***NOTE:** You may also use `/cryptocurrency/ohlcv/historical` for traditional OHLCV data at
    historical daily and hourly intervals. You may also use `/v1/cryptocurrency/ohlcv/latest` for OHLCV
    data for the current UTC day.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        time_period (str | Unset):  Default: 'all_time'.
        convert (str | Unset):
        convert_id (str | Unset):
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyPricePerformanceStatsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        id=id,
        slug=slug,
        symbol=symbol,
        time_period=time_period,
        convert=convert,
        convert_id=convert_id,
        skip_invalid=skip_invalid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    time_period: str | Unset = "all_time",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> Response[
    CryptocurrencyPricePerformanceStatsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """Price Performance Stats

     Returns price performance statistics for one or more cryptocurrencies including launch price ROI and
    all-time high / all-time low. Stats are returned for an `all_time` period by default. UTC
    `yesterday` and a number of *rolling time periods* may be requested using the `time_period`
    parameter. Utilize the `convert` parameter to translate values into multiple fiats or
    cryptocurrencies using historical rates.


    **Please note**: This documentation relates to our updated V2 endpoint, which may be incompatible
    with our V1 versions. Documentation for deprecated endpoints can be found [the deprecated
    section](/pro-api-reference/deprecated).


      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** The statistics module displayed on cryptocurrency pages like
    [Bitcoin](https://coinmarketcap.com/currencies/bitcoin/).

    ***NOTE:** You may also use `/cryptocurrency/ohlcv/historical` for traditional OHLCV data at
    historical daily and hourly intervals. You may also use `/v1/cryptocurrency/ohlcv/latest` for OHLCV
    data for the current UTC day.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        time_period (str | Unset):  Default: 'all_time'.
        convert (str | Unset):
        convert_id (str | Unset):
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyPricePerformanceStatsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        symbol=symbol,
        time_period=time_period,
        convert=convert,
        convert_id=convert_id,
        skip_invalid=skip_invalid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    time_period: str | Unset = "all_time",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> (
    CryptocurrencyPricePerformanceStatsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """Price Performance Stats

     Returns price performance statistics for one or more cryptocurrencies including launch price ROI and
    all-time high / all-time low. Stats are returned for an `all_time` period by default. UTC
    `yesterday` and a number of *rolling time periods* may be requested using the `time_period`
    parameter. Utilize the `convert` parameter to translate values into multiple fiats or
    cryptocurrencies using historical rates.


    **Please note**: This documentation relates to our updated V2 endpoint, which may be incompatible
    with our V1 versions. Documentation for deprecated endpoints can be found [the deprecated
    section](/pro-api-reference/deprecated).


      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** The statistics module displayed on cryptocurrency pages like
    [Bitcoin](https://coinmarketcap.com/currencies/bitcoin/).

    ***NOTE:** You may also use `/cryptocurrency/ohlcv/historical` for traditional OHLCV data at
    historical daily and hourly intervals. You may also use `/v1/cryptocurrency/ohlcv/latest` for OHLCV
    data for the current UTC day.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        time_period (str | Unset):  Default: 'all_time'.
        convert (str | Unset):
        convert_id (str | Unset):
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyPricePerformanceStatsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            slug=slug,
            symbol=symbol,
            time_period=time_period,
            convert=convert,
            convert_id=convert_id,
            skip_invalid=skip_invalid,
        )
    ).parsed
