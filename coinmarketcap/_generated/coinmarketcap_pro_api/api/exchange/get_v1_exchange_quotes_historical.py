from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exchange_historical_quotes_response_model import ExchangeHistoricalQuotesResponseModel
from ...models.get_v1_exchange_quotes_historical_interval import (
    GetV1ExchangeQuotesHistoricalInterval,
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
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: float | Unset = 10.0,
    interval: GetV1ExchangeQuotesHistoricalInterval | Unset = "5m",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["slug"] = slug

    params["time_start"] = time_start

    params["time_end"] = time_end

    params["count"] = count

    json_interval: str | Unset = UNSET
    if not isinstance(interval, Unset):
        json_interval = interval

    params["interval"] = json_interval

    params["convert"] = convert

    params["convert_id"] = convert_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/exchange/quotes/historical",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ExchangeHistoricalQuotesResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = ExchangeHistoricalQuotesResponseModel.from_dict(response.json())

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
    ExchangeHistoricalQuotesResponseModel
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
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: float | Unset = 10.0,
    interval: GetV1ExchangeQuotesHistoricalInterval | Unset = "5m",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> Response[
    ExchangeHistoricalQuotesResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Quotes Historical

     Returns an interval of historic quotes for any exchange based on time and interval parameters.

    **Technical Notes**
    - A historic quote for every \"interval\" period between your \"time_start\" and \"time_end\" will
    be returned.
    - If a \"time_start\" is not supplied, the \"interval\" will be applied in reverse from
    \"time_end\".
    - If \"time_end\" is not supplied, it defaults to the current time.
    - At each \"interval\" period, the historic quote that is closest in time to the requested time will
    be returned.
    - If no historic quotes are available in a given \"interval\" period up until the next interval
    period, it will be skipped.
    - This endpoint supports requesting multiple exchanges in the same call. Please note the API
    response will be wrapped in an additional object in this case.

    **Interval Options**
    There are 2 types of time interval formats that may be used for \"interval\".

    The first are calendar year and time constants in UTC time:
    **\"hourly\"** - Get the first quote available at the beginning of each calendar hour.
    **\"daily\"** - Get the first quote available at the beginning of each calendar day.
    **\"weekly\"** - Get the first quote available at the beginning of each calendar week.
    **\"monthly\"** - Get the first quote available at the beginning of each calendar month.
    **\"yearly\"** - Get the first quote available at the beginning of each calendar year.

    The second are relative time intervals.
    **\"m\"**: Get the first quote available every \"m\" minutes (60 second intervals). Supported
    minutes are: \"5m\", \"10m\", \"15m\", \"30m\", \"45m\".
    **\"h\"**: Get the first quote available every \"h\" hours (3600 second intervals). Supported hour
    intervals are: \"1h\", \"2h\", \"3h\", \"4h\", \"6h\", \"12h\".
    **\"d\"**: Get the first quote available every \"d\" days (86400 second intervals). Supported day
    intervals are: \"1d\", \"2d\", \"3d\", \"7d\", \"14d\", \"15d\", \"30d\", \"60d\", \"90d\",
    \"365d\".

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - Basic (intraday: 1 month, daily: 1 year)
    - Builder (intraday: 1 month, daily: 3 years)
    - Startup (intraday: 1 month, daily: from 2018)
    - Growth (intraday: 3 months, daily: from 2018)
    - Professional (intraday: 12 months, daily: from 2018)
    - Enterprise (intraday: from 2018, daily: from 2018)

    **Note:** Intraday = `5m-12h` intervals, Daily = `1d-1y` intervals

    **Note:** You may use the /exchange/map endpoint to receive a list of earliest historical dates that
    may be fetched for each exchange as  `first_historical_data`. This timestamp will either be the date
    CoinMarketCap first started tracking the exchange or 2018-04-26T00:45:00.000Z, the earliest date
    this type of historical data is available for.

    **Cache / Update frequency:** Every 5 minutes.
    **Plan credit use:** 1 call credit per 100 historical data points returned (rounded up) and 1 call
    credit per `convert` option beyond the first.
    **CMC equivalent pages:** No equivalent, this data is only available via API outside of our volume
    sparkline charts in
    [coinmarketcap.com/rankings/exchanges/](https://coinmarketcap.com/rankings/exchanges/).

    Args:
        id (str | Unset):
        slug (str | Unset):
        time_start (str | Unset):
        time_end (str | Unset):
        count (float | Unset):  Default: 10.0.
        interval (GetV1ExchangeQuotesHistoricalInterval | Unset):  Default: '5m'.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeHistoricalQuotesResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        time_start=time_start,
        time_end=time_end,
        count=count,
        interval=interval,
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
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: float | Unset = 10.0,
    interval: GetV1ExchangeQuotesHistoricalInterval | Unset = "5m",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> (
    ExchangeHistoricalQuotesResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Quotes Historical

     Returns an interval of historic quotes for any exchange based on time and interval parameters.

    **Technical Notes**
    - A historic quote for every \"interval\" period between your \"time_start\" and \"time_end\" will
    be returned.
    - If a \"time_start\" is not supplied, the \"interval\" will be applied in reverse from
    \"time_end\".
    - If \"time_end\" is not supplied, it defaults to the current time.
    - At each \"interval\" period, the historic quote that is closest in time to the requested time will
    be returned.
    - If no historic quotes are available in a given \"interval\" period up until the next interval
    period, it will be skipped.
    - This endpoint supports requesting multiple exchanges in the same call. Please note the API
    response will be wrapped in an additional object in this case.

    **Interval Options**
    There are 2 types of time interval formats that may be used for \"interval\".

    The first are calendar year and time constants in UTC time:
    **\"hourly\"** - Get the first quote available at the beginning of each calendar hour.
    **\"daily\"** - Get the first quote available at the beginning of each calendar day.
    **\"weekly\"** - Get the first quote available at the beginning of each calendar week.
    **\"monthly\"** - Get the first quote available at the beginning of each calendar month.
    **\"yearly\"** - Get the first quote available at the beginning of each calendar year.

    The second are relative time intervals.
    **\"m\"**: Get the first quote available every \"m\" minutes (60 second intervals). Supported
    minutes are: \"5m\", \"10m\", \"15m\", \"30m\", \"45m\".
    **\"h\"**: Get the first quote available every \"h\" hours (3600 second intervals). Supported hour
    intervals are: \"1h\", \"2h\", \"3h\", \"4h\", \"6h\", \"12h\".
    **\"d\"**: Get the first quote available every \"d\" days (86400 second intervals). Supported day
    intervals are: \"1d\", \"2d\", \"3d\", \"7d\", \"14d\", \"15d\", \"30d\", \"60d\", \"90d\",
    \"365d\".

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - Basic (intraday: 1 month, daily: 1 year)
    - Builder (intraday: 1 month, daily: 3 years)
    - Startup (intraday: 1 month, daily: from 2018)
    - Growth (intraday: 3 months, daily: from 2018)
    - Professional (intraday: 12 months, daily: from 2018)
    - Enterprise (intraday: from 2018, daily: from 2018)

    **Note:** Intraday = `5m-12h` intervals, Daily = `1d-1y` intervals

    **Note:** You may use the /exchange/map endpoint to receive a list of earliest historical dates that
    may be fetched for each exchange as  `first_historical_data`. This timestamp will either be the date
    CoinMarketCap first started tracking the exchange or 2018-04-26T00:45:00.000Z, the earliest date
    this type of historical data is available for.

    **Cache / Update frequency:** Every 5 minutes.
    **Plan credit use:** 1 call credit per 100 historical data points returned (rounded up) and 1 call
    credit per `convert` option beyond the first.
    **CMC equivalent pages:** No equivalent, this data is only available via API outside of our volume
    sparkline charts in
    [coinmarketcap.com/rankings/exchanges/](https://coinmarketcap.com/rankings/exchanges/).

    Args:
        id (str | Unset):
        slug (str | Unset):
        time_start (str | Unset):
        time_end (str | Unset):
        count (float | Unset):  Default: 10.0.
        interval (GetV1ExchangeQuotesHistoricalInterval | Unset):  Default: '5m'.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeHistoricalQuotesResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        id=id,
        slug=slug,
        time_start=time_start,
        time_end=time_end,
        count=count,
        interval=interval,
        convert=convert,
        convert_id=convert_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: float | Unset = 10.0,
    interval: GetV1ExchangeQuotesHistoricalInterval | Unset = "5m",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> Response[
    ExchangeHistoricalQuotesResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Quotes Historical

     Returns an interval of historic quotes for any exchange based on time and interval parameters.

    **Technical Notes**
    - A historic quote for every \"interval\" period between your \"time_start\" and \"time_end\" will
    be returned.
    - If a \"time_start\" is not supplied, the \"interval\" will be applied in reverse from
    \"time_end\".
    - If \"time_end\" is not supplied, it defaults to the current time.
    - At each \"interval\" period, the historic quote that is closest in time to the requested time will
    be returned.
    - If no historic quotes are available in a given \"interval\" period up until the next interval
    period, it will be skipped.
    - This endpoint supports requesting multiple exchanges in the same call. Please note the API
    response will be wrapped in an additional object in this case.

    **Interval Options**
    There are 2 types of time interval formats that may be used for \"interval\".

    The first are calendar year and time constants in UTC time:
    **\"hourly\"** - Get the first quote available at the beginning of each calendar hour.
    **\"daily\"** - Get the first quote available at the beginning of each calendar day.
    **\"weekly\"** - Get the first quote available at the beginning of each calendar week.
    **\"monthly\"** - Get the first quote available at the beginning of each calendar month.
    **\"yearly\"** - Get the first quote available at the beginning of each calendar year.

    The second are relative time intervals.
    **\"m\"**: Get the first quote available every \"m\" minutes (60 second intervals). Supported
    minutes are: \"5m\", \"10m\", \"15m\", \"30m\", \"45m\".
    **\"h\"**: Get the first quote available every \"h\" hours (3600 second intervals). Supported hour
    intervals are: \"1h\", \"2h\", \"3h\", \"4h\", \"6h\", \"12h\".
    **\"d\"**: Get the first quote available every \"d\" days (86400 second intervals). Supported day
    intervals are: \"1d\", \"2d\", \"3d\", \"7d\", \"14d\", \"15d\", \"30d\", \"60d\", \"90d\",
    \"365d\".

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - Basic (intraday: 1 month, daily: 1 year)
    - Builder (intraday: 1 month, daily: 3 years)
    - Startup (intraday: 1 month, daily: from 2018)
    - Growth (intraday: 3 months, daily: from 2018)
    - Professional (intraday: 12 months, daily: from 2018)
    - Enterprise (intraday: from 2018, daily: from 2018)

    **Note:** Intraday = `5m-12h` intervals, Daily = `1d-1y` intervals

    **Note:** You may use the /exchange/map endpoint to receive a list of earliest historical dates that
    may be fetched for each exchange as  `first_historical_data`. This timestamp will either be the date
    CoinMarketCap first started tracking the exchange or 2018-04-26T00:45:00.000Z, the earliest date
    this type of historical data is available for.

    **Cache / Update frequency:** Every 5 minutes.
    **Plan credit use:** 1 call credit per 100 historical data points returned (rounded up) and 1 call
    credit per `convert` option beyond the first.
    **CMC equivalent pages:** No equivalent, this data is only available via API outside of our volume
    sparkline charts in
    [coinmarketcap.com/rankings/exchanges/](https://coinmarketcap.com/rankings/exchanges/).

    Args:
        id (str | Unset):
        slug (str | Unset):
        time_start (str | Unset):
        time_end (str | Unset):
        count (float | Unset):  Default: 10.0.
        interval (GetV1ExchangeQuotesHistoricalInterval | Unset):  Default: '5m'.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeHistoricalQuotesResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        time_start=time_start,
        time_end=time_end,
        count=count,
        interval=interval,
        convert=convert,
        convert_id=convert_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: float | Unset = 10.0,
    interval: GetV1ExchangeQuotesHistoricalInterval | Unset = "5m",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> (
    ExchangeHistoricalQuotesResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Quotes Historical

     Returns an interval of historic quotes for any exchange based on time and interval parameters.

    **Technical Notes**
    - A historic quote for every \"interval\" period between your \"time_start\" and \"time_end\" will
    be returned.
    - If a \"time_start\" is not supplied, the \"interval\" will be applied in reverse from
    \"time_end\".
    - If \"time_end\" is not supplied, it defaults to the current time.
    - At each \"interval\" period, the historic quote that is closest in time to the requested time will
    be returned.
    - If no historic quotes are available in a given \"interval\" period up until the next interval
    period, it will be skipped.
    - This endpoint supports requesting multiple exchanges in the same call. Please note the API
    response will be wrapped in an additional object in this case.

    **Interval Options**
    There are 2 types of time interval formats that may be used for \"interval\".

    The first are calendar year and time constants in UTC time:
    **\"hourly\"** - Get the first quote available at the beginning of each calendar hour.
    **\"daily\"** - Get the first quote available at the beginning of each calendar day.
    **\"weekly\"** - Get the first quote available at the beginning of each calendar week.
    **\"monthly\"** - Get the first quote available at the beginning of each calendar month.
    **\"yearly\"** - Get the first quote available at the beginning of each calendar year.

    The second are relative time intervals.
    **\"m\"**: Get the first quote available every \"m\" minutes (60 second intervals). Supported
    minutes are: \"5m\", \"10m\", \"15m\", \"30m\", \"45m\".
    **\"h\"**: Get the first quote available every \"h\" hours (3600 second intervals). Supported hour
    intervals are: \"1h\", \"2h\", \"3h\", \"4h\", \"6h\", \"12h\".
    **\"d\"**: Get the first quote available every \"d\" days (86400 second intervals). Supported day
    intervals are: \"1d\", \"2d\", \"3d\", \"7d\", \"14d\", \"15d\", \"30d\", \"60d\", \"90d\",
    \"365d\".

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - Basic (intraday: 1 month, daily: 1 year)
    - Builder (intraday: 1 month, daily: 3 years)
    - Startup (intraday: 1 month, daily: from 2018)
    - Growth (intraday: 3 months, daily: from 2018)
    - Professional (intraday: 12 months, daily: from 2018)
    - Enterprise (intraday: from 2018, daily: from 2018)

    **Note:** Intraday = `5m-12h` intervals, Daily = `1d-1y` intervals

    **Note:** You may use the /exchange/map endpoint to receive a list of earliest historical dates that
    may be fetched for each exchange as  `first_historical_data`. This timestamp will either be the date
    CoinMarketCap first started tracking the exchange or 2018-04-26T00:45:00.000Z, the earliest date
    this type of historical data is available for.

    **Cache / Update frequency:** Every 5 minutes.
    **Plan credit use:** 1 call credit per 100 historical data points returned (rounded up) and 1 call
    credit per `convert` option beyond the first.
    **CMC equivalent pages:** No equivalent, this data is only available via API outside of our volume
    sparkline charts in
    [coinmarketcap.com/rankings/exchanges/](https://coinmarketcap.com/rankings/exchanges/).

    Args:
        id (str | Unset):
        slug (str | Unset):
        time_start (str | Unset):
        time_end (str | Unset):
        count (float | Unset):  Default: 10.0.
        interval (GetV1ExchangeQuotesHistoricalInterval | Unset):  Default: '5m'.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeHistoricalQuotesResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            slug=slug,
            time_start=time_start,
            time_end=time_end,
            count=count,
            interval=interval,
            convert=convert,
            convert_id=convert_id,
        )
    ).parsed
