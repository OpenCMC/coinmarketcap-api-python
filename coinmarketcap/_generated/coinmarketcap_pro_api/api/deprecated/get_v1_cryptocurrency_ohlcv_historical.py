from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cryptocurrency_ohlcv_historical_response_model import CryptocurrencyOHLCVHistoricalResponseModel
from ...models.get_v1_cryptocurrency_ohlcv_historical_interval import (
    GetV1CryptocurrencyOhlcvHistoricalInterval,
)
from ...models.get_v1_cryptocurrency_ohlcv_historical_time_period import (
    GetV1CryptocurrencyOhlcvHistoricalTimePeriod,
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
    time_period: GetV1CryptocurrencyOhlcvHistoricalTimePeriod | Unset = "daily",
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: float | Unset = 10.0,
    interval: GetV1CryptocurrencyOhlcvHistoricalInterval | Unset = "daily",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["slug"] = slug

    params["symbol"] = symbol

    json_time_period: str | Unset = UNSET
    if not isinstance(time_period, Unset):
        json_time_period = time_period

    params["time_period"] = json_time_period

    params["time_start"] = time_start

    params["time_end"] = time_end

    params["count"] = count

    json_interval: str | Unset = UNSET
    if not isinstance(interval, Unset):
        json_interval = interval

    params["interval"] = json_interval

    params["convert"] = convert

    params["convert_id"] = convert_id

    params["skip_invalid"] = skip_invalid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/cryptocurrency/ohlcv/historical",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CryptocurrencyOHLCVHistoricalResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = CryptocurrencyOHLCVHistoricalResponseModel.from_dict(response.json())

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
    CryptocurrencyOHLCVHistoricalResponseModel
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
    time_period: GetV1CryptocurrencyOhlcvHistoricalTimePeriod | Unset = "daily",
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: float | Unset = 10.0,
    interval: GetV1CryptocurrencyOhlcvHistoricalInterval | Unset = "daily",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> Response[
    CryptocurrencyOHLCVHistoricalResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""OHLCV Historical v1 (deprecated)

     Returns historical OHLCV (Open, High, Low, Close, Volume) data along with market cap for any
    cryptocurrency using time interval parameters. Currently daily and hourly OHLCV periods are
    supported. Volume is not currently supported for hourly OHLCV intervals before 2020-09-22.


    **Technical Notes**
    - Only the date portion of the timestamp is used for daily OHLCV so it's recommended to send an ISO
    date format like \"2018-09-19\" without time for this \"time_period\".
    - One OHLCV quote will be returned for every \"time_period\" between your \"time_start\" (exclusive)
    and \"time_end\" (inclusive).
    - If a \"time_start\" is not supplied, the \"time_period\" will be calculated in reverse from
    \"time_end\" using the \"count\" parameter which defaults to 10 results.
    - If \"time_end\" is not supplied, it defaults to the current time.
    - If you don't need every \"time_period\" between your dates you may adjust the frequency that
    \"time_period\" is sampled using the \"interval\" parameter. For example with \"time_period\" set to
    \"daily\" you may set \"interval\" to \"2d\" to get the daily OHLCV for every other day. You could
    set \"interval\" to \"monthly\" to get the first daily OHLCV for each month, or set it to \"yearly\"
    to get the daily OHLCV value against the same date every year.

    **Implementation Tips**
    - If querying for a specific OHLCV date your \"time_start\" should specify a timestamp of 1 interval
    prior as \"time_start\" is an exclusive time parameter (as opposed to \"time_end\" which is
    inclusive to the search). This means that when you pass a \"time_start\" results will be returned
    for the *next* complete \"time_period\". For example, if you are querying for a daily OHLCV
    datapoint for 2018-11-30 your \"time_start\" should be \"2018-11-29\".
    - If only specifying a \"count\" parameter to return latest OHLCV periods, your \"count\" should be
    1 number higher than the number of results you expect to receive. \"Count\" defines the number of
    \"time_period\" intervals queried, *not* the number of results to return, and this includes the
    currently active time period which is incomplete when working backwards from current time. For
    example, if you want the last daily OHLCV value available simply pass \"count=2\" to skip the
    incomplete active time period.
    - This endpoint supports requesting multiple cryptocurrencies in the same call. Please note the API
    response will be wrapped in an additional object in this case.

    **Interval Options**

    There are 2 types of time interval formats that may be used for \"time_period\" and \"interval\"
    parameters. For \"time_period\" these return aggregate OHLCV data from the beginning to end of each
    interval period. Apply these time intervals to \"interval\" to adjust how frequently \"time_period\"
    is sampled.

    The first are calendar year and time constants in UTC time:
    **\"hourly\"** - Hour intervals in UTC.
    **\"daily\"** - Calendar day intervals for each UTC day.
    **\"weekly\"** - Calendar week intervals for each calendar week.
    **\"monthly\"** - Calendar month intervals for each calendar month.
    **\"yearly\"** - Calendar year intervals for each calendar year.

    The second are relative time intervals.
    **\"h\"**: Get the first quote available every \"h\" hours (3600 second intervals). Supported hour
    intervals are: \"1h\", \"2h\", \"3h\", \"4h\", \"6h\", \"12h\".
    **\"d\"**: Time periods that repeat every \"d\" days (86400 second intervals). Supported day
    intervals are: \"1d\", \"2d\", \"3d\", \"7d\", \"14d\", \"15d\", \"30d\", \"60d\", \"90d\",
    \"365d\".

    Please note that \"time_period\" currently supports the \"daily\" and \"hourly\" options.
    \"interval\" supports all interval options.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - ~~Basic~~
    - ~~Builder~~
    - Startup (1 month)
    - Growth (3 months)
    - Professional (12 months)
    - Enterprise (Up to 6 years)

    **Cache / Update frequency:** Latest Daily OHLCV record is available ~5 to ~10 minutes after each
    midnight UTC. The latest hourly OHLCV record is available 5 minutes after each UTC hour.
    **Plan credit use:** 1 call credit per 100 OHLCV data points returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our historical cryptocurrency data pages like
    [coinmarketcap.com/currencies/bitcoin/historical-
    data/](https://coinmarketcap.com/currencies/bitcoin/historical-data/).

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        time_period (GetV1CryptocurrencyOhlcvHistoricalTimePeriod | Unset):  Default: 'daily'.
        time_start (str | Unset):
        time_end (str | Unset):
        count (float | Unset):  Default: 10.0.
        interval (GetV1CryptocurrencyOhlcvHistoricalInterval | Unset):  Default: 'daily'.
        convert (str | Unset):
        convert_id (str | Unset):
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyOHLCVHistoricalResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        symbol=symbol,
        time_period=time_period,
        time_start=time_start,
        time_end=time_end,
        count=count,
        interval=interval,
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
    time_period: GetV1CryptocurrencyOhlcvHistoricalTimePeriod | Unset = "daily",
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: float | Unset = 10.0,
    interval: GetV1CryptocurrencyOhlcvHistoricalInterval | Unset = "daily",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> (
    CryptocurrencyOHLCVHistoricalResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""OHLCV Historical v1 (deprecated)

     Returns historical OHLCV (Open, High, Low, Close, Volume) data along with market cap for any
    cryptocurrency using time interval parameters. Currently daily and hourly OHLCV periods are
    supported. Volume is not currently supported for hourly OHLCV intervals before 2020-09-22.


    **Technical Notes**
    - Only the date portion of the timestamp is used for daily OHLCV so it's recommended to send an ISO
    date format like \"2018-09-19\" without time for this \"time_period\".
    - One OHLCV quote will be returned for every \"time_period\" between your \"time_start\" (exclusive)
    and \"time_end\" (inclusive).
    - If a \"time_start\" is not supplied, the \"time_period\" will be calculated in reverse from
    \"time_end\" using the \"count\" parameter which defaults to 10 results.
    - If \"time_end\" is not supplied, it defaults to the current time.
    - If you don't need every \"time_period\" between your dates you may adjust the frequency that
    \"time_period\" is sampled using the \"interval\" parameter. For example with \"time_period\" set to
    \"daily\" you may set \"interval\" to \"2d\" to get the daily OHLCV for every other day. You could
    set \"interval\" to \"monthly\" to get the first daily OHLCV for each month, or set it to \"yearly\"
    to get the daily OHLCV value against the same date every year.

    **Implementation Tips**
    - If querying for a specific OHLCV date your \"time_start\" should specify a timestamp of 1 interval
    prior as \"time_start\" is an exclusive time parameter (as opposed to \"time_end\" which is
    inclusive to the search). This means that when you pass a \"time_start\" results will be returned
    for the *next* complete \"time_period\". For example, if you are querying for a daily OHLCV
    datapoint for 2018-11-30 your \"time_start\" should be \"2018-11-29\".
    - If only specifying a \"count\" parameter to return latest OHLCV periods, your \"count\" should be
    1 number higher than the number of results you expect to receive. \"Count\" defines the number of
    \"time_period\" intervals queried, *not* the number of results to return, and this includes the
    currently active time period which is incomplete when working backwards from current time. For
    example, if you want the last daily OHLCV value available simply pass \"count=2\" to skip the
    incomplete active time period.
    - This endpoint supports requesting multiple cryptocurrencies in the same call. Please note the API
    response will be wrapped in an additional object in this case.

    **Interval Options**

    There are 2 types of time interval formats that may be used for \"time_period\" and \"interval\"
    parameters. For \"time_period\" these return aggregate OHLCV data from the beginning to end of each
    interval period. Apply these time intervals to \"interval\" to adjust how frequently \"time_period\"
    is sampled.

    The first are calendar year and time constants in UTC time:
    **\"hourly\"** - Hour intervals in UTC.
    **\"daily\"** - Calendar day intervals for each UTC day.
    **\"weekly\"** - Calendar week intervals for each calendar week.
    **\"monthly\"** - Calendar month intervals for each calendar month.
    **\"yearly\"** - Calendar year intervals for each calendar year.

    The second are relative time intervals.
    **\"h\"**: Get the first quote available every \"h\" hours (3600 second intervals). Supported hour
    intervals are: \"1h\", \"2h\", \"3h\", \"4h\", \"6h\", \"12h\".
    **\"d\"**: Time periods that repeat every \"d\" days (86400 second intervals). Supported day
    intervals are: \"1d\", \"2d\", \"3d\", \"7d\", \"14d\", \"15d\", \"30d\", \"60d\", \"90d\",
    \"365d\".

    Please note that \"time_period\" currently supports the \"daily\" and \"hourly\" options.
    \"interval\" supports all interval options.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - ~~Basic~~
    - ~~Builder~~
    - Startup (1 month)
    - Growth (3 months)
    - Professional (12 months)
    - Enterprise (Up to 6 years)

    **Cache / Update frequency:** Latest Daily OHLCV record is available ~5 to ~10 minutes after each
    midnight UTC. The latest hourly OHLCV record is available 5 minutes after each UTC hour.
    **Plan credit use:** 1 call credit per 100 OHLCV data points returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our historical cryptocurrency data pages like
    [coinmarketcap.com/currencies/bitcoin/historical-
    data/](https://coinmarketcap.com/currencies/bitcoin/historical-data/).

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        time_period (GetV1CryptocurrencyOhlcvHistoricalTimePeriod | Unset):  Default: 'daily'.
        time_start (str | Unset):
        time_end (str | Unset):
        count (float | Unset):  Default: 10.0.
        interval (GetV1CryptocurrencyOhlcvHistoricalInterval | Unset):  Default: 'daily'.
        convert (str | Unset):
        convert_id (str | Unset):
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyOHLCVHistoricalResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        id=id,
        slug=slug,
        symbol=symbol,
        time_period=time_period,
        time_start=time_start,
        time_end=time_end,
        count=count,
        interval=interval,
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
    time_period: GetV1CryptocurrencyOhlcvHistoricalTimePeriod | Unset = "daily",
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: float | Unset = 10.0,
    interval: GetV1CryptocurrencyOhlcvHistoricalInterval | Unset = "daily",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> Response[
    CryptocurrencyOHLCVHistoricalResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""OHLCV Historical v1 (deprecated)

     Returns historical OHLCV (Open, High, Low, Close, Volume) data along with market cap for any
    cryptocurrency using time interval parameters. Currently daily and hourly OHLCV periods are
    supported. Volume is not currently supported for hourly OHLCV intervals before 2020-09-22.


    **Technical Notes**
    - Only the date portion of the timestamp is used for daily OHLCV so it's recommended to send an ISO
    date format like \"2018-09-19\" without time for this \"time_period\".
    - One OHLCV quote will be returned for every \"time_period\" between your \"time_start\" (exclusive)
    and \"time_end\" (inclusive).
    - If a \"time_start\" is not supplied, the \"time_period\" will be calculated in reverse from
    \"time_end\" using the \"count\" parameter which defaults to 10 results.
    - If \"time_end\" is not supplied, it defaults to the current time.
    - If you don't need every \"time_period\" between your dates you may adjust the frequency that
    \"time_period\" is sampled using the \"interval\" parameter. For example with \"time_period\" set to
    \"daily\" you may set \"interval\" to \"2d\" to get the daily OHLCV for every other day. You could
    set \"interval\" to \"monthly\" to get the first daily OHLCV for each month, or set it to \"yearly\"
    to get the daily OHLCV value against the same date every year.

    **Implementation Tips**
    - If querying for a specific OHLCV date your \"time_start\" should specify a timestamp of 1 interval
    prior as \"time_start\" is an exclusive time parameter (as opposed to \"time_end\" which is
    inclusive to the search). This means that when you pass a \"time_start\" results will be returned
    for the *next* complete \"time_period\". For example, if you are querying for a daily OHLCV
    datapoint for 2018-11-30 your \"time_start\" should be \"2018-11-29\".
    - If only specifying a \"count\" parameter to return latest OHLCV periods, your \"count\" should be
    1 number higher than the number of results you expect to receive. \"Count\" defines the number of
    \"time_period\" intervals queried, *not* the number of results to return, and this includes the
    currently active time period which is incomplete when working backwards from current time. For
    example, if you want the last daily OHLCV value available simply pass \"count=2\" to skip the
    incomplete active time period.
    - This endpoint supports requesting multiple cryptocurrencies in the same call. Please note the API
    response will be wrapped in an additional object in this case.

    **Interval Options**

    There are 2 types of time interval formats that may be used for \"time_period\" and \"interval\"
    parameters. For \"time_period\" these return aggregate OHLCV data from the beginning to end of each
    interval period. Apply these time intervals to \"interval\" to adjust how frequently \"time_period\"
    is sampled.

    The first are calendar year and time constants in UTC time:
    **\"hourly\"** - Hour intervals in UTC.
    **\"daily\"** - Calendar day intervals for each UTC day.
    **\"weekly\"** - Calendar week intervals for each calendar week.
    **\"monthly\"** - Calendar month intervals for each calendar month.
    **\"yearly\"** - Calendar year intervals for each calendar year.

    The second are relative time intervals.
    **\"h\"**: Get the first quote available every \"h\" hours (3600 second intervals). Supported hour
    intervals are: \"1h\", \"2h\", \"3h\", \"4h\", \"6h\", \"12h\".
    **\"d\"**: Time periods that repeat every \"d\" days (86400 second intervals). Supported day
    intervals are: \"1d\", \"2d\", \"3d\", \"7d\", \"14d\", \"15d\", \"30d\", \"60d\", \"90d\",
    \"365d\".

    Please note that \"time_period\" currently supports the \"daily\" and \"hourly\" options.
    \"interval\" supports all interval options.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - ~~Basic~~
    - ~~Builder~~
    - Startup (1 month)
    - Growth (3 months)
    - Professional (12 months)
    - Enterprise (Up to 6 years)

    **Cache / Update frequency:** Latest Daily OHLCV record is available ~5 to ~10 minutes after each
    midnight UTC. The latest hourly OHLCV record is available 5 minutes after each UTC hour.
    **Plan credit use:** 1 call credit per 100 OHLCV data points returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our historical cryptocurrency data pages like
    [coinmarketcap.com/currencies/bitcoin/historical-
    data/](https://coinmarketcap.com/currencies/bitcoin/historical-data/).

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        time_period (GetV1CryptocurrencyOhlcvHistoricalTimePeriod | Unset):  Default: 'daily'.
        time_start (str | Unset):
        time_end (str | Unset):
        count (float | Unset):  Default: 10.0.
        interval (GetV1CryptocurrencyOhlcvHistoricalInterval | Unset):  Default: 'daily'.
        convert (str | Unset):
        convert_id (str | Unset):
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyOHLCVHistoricalResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        symbol=symbol,
        time_period=time_period,
        time_start=time_start,
        time_end=time_end,
        count=count,
        interval=interval,
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
    time_period: GetV1CryptocurrencyOhlcvHistoricalTimePeriod | Unset = "daily",
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: float | Unset = 10.0,
    interval: GetV1CryptocurrencyOhlcvHistoricalInterval | Unset = "daily",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> (
    CryptocurrencyOHLCVHistoricalResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""OHLCV Historical v1 (deprecated)

     Returns historical OHLCV (Open, High, Low, Close, Volume) data along with market cap for any
    cryptocurrency using time interval parameters. Currently daily and hourly OHLCV periods are
    supported. Volume is not currently supported for hourly OHLCV intervals before 2020-09-22.


    **Technical Notes**
    - Only the date portion of the timestamp is used for daily OHLCV so it's recommended to send an ISO
    date format like \"2018-09-19\" without time for this \"time_period\".
    - One OHLCV quote will be returned for every \"time_period\" between your \"time_start\" (exclusive)
    and \"time_end\" (inclusive).
    - If a \"time_start\" is not supplied, the \"time_period\" will be calculated in reverse from
    \"time_end\" using the \"count\" parameter which defaults to 10 results.
    - If \"time_end\" is not supplied, it defaults to the current time.
    - If you don't need every \"time_period\" between your dates you may adjust the frequency that
    \"time_period\" is sampled using the \"interval\" parameter. For example with \"time_period\" set to
    \"daily\" you may set \"interval\" to \"2d\" to get the daily OHLCV for every other day. You could
    set \"interval\" to \"monthly\" to get the first daily OHLCV for each month, or set it to \"yearly\"
    to get the daily OHLCV value against the same date every year.

    **Implementation Tips**
    - If querying for a specific OHLCV date your \"time_start\" should specify a timestamp of 1 interval
    prior as \"time_start\" is an exclusive time parameter (as opposed to \"time_end\" which is
    inclusive to the search). This means that when you pass a \"time_start\" results will be returned
    for the *next* complete \"time_period\". For example, if you are querying for a daily OHLCV
    datapoint for 2018-11-30 your \"time_start\" should be \"2018-11-29\".
    - If only specifying a \"count\" parameter to return latest OHLCV periods, your \"count\" should be
    1 number higher than the number of results you expect to receive. \"Count\" defines the number of
    \"time_period\" intervals queried, *not* the number of results to return, and this includes the
    currently active time period which is incomplete when working backwards from current time. For
    example, if you want the last daily OHLCV value available simply pass \"count=2\" to skip the
    incomplete active time period.
    - This endpoint supports requesting multiple cryptocurrencies in the same call. Please note the API
    response will be wrapped in an additional object in this case.

    **Interval Options**

    There are 2 types of time interval formats that may be used for \"time_period\" and \"interval\"
    parameters. For \"time_period\" these return aggregate OHLCV data from the beginning to end of each
    interval period. Apply these time intervals to \"interval\" to adjust how frequently \"time_period\"
    is sampled.

    The first are calendar year and time constants in UTC time:
    **\"hourly\"** - Hour intervals in UTC.
    **\"daily\"** - Calendar day intervals for each UTC day.
    **\"weekly\"** - Calendar week intervals for each calendar week.
    **\"monthly\"** - Calendar month intervals for each calendar month.
    **\"yearly\"** - Calendar year intervals for each calendar year.

    The second are relative time intervals.
    **\"h\"**: Get the first quote available every \"h\" hours (3600 second intervals). Supported hour
    intervals are: \"1h\", \"2h\", \"3h\", \"4h\", \"6h\", \"12h\".
    **\"d\"**: Time periods that repeat every \"d\" days (86400 second intervals). Supported day
    intervals are: \"1d\", \"2d\", \"3d\", \"7d\", \"14d\", \"15d\", \"30d\", \"60d\", \"90d\",
    \"365d\".

    Please note that \"time_period\" currently supports the \"daily\" and \"hourly\" options.
    \"interval\" supports all interval options.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - ~~Basic~~
    - ~~Builder~~
    - Startup (1 month)
    - Growth (3 months)
    - Professional (12 months)
    - Enterprise (Up to 6 years)

    **Cache / Update frequency:** Latest Daily OHLCV record is available ~5 to ~10 minutes after each
    midnight UTC. The latest hourly OHLCV record is available 5 minutes after each UTC hour.
    **Plan credit use:** 1 call credit per 100 OHLCV data points returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our historical cryptocurrency data pages like
    [coinmarketcap.com/currencies/bitcoin/historical-
    data/](https://coinmarketcap.com/currencies/bitcoin/historical-data/).

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        time_period (GetV1CryptocurrencyOhlcvHistoricalTimePeriod | Unset):  Default: 'daily'.
        time_start (str | Unset):
        time_end (str | Unset):
        count (float | Unset):  Default: 10.0.
        interval (GetV1CryptocurrencyOhlcvHistoricalInterval | Unset):  Default: 'daily'.
        convert (str | Unset):
        convert_id (str | Unset):
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyOHLCVHistoricalResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            slug=slug,
            symbol=symbol,
            time_period=time_period,
            time_start=time_start,
            time_end=time_end,
            count=count,
            interval=interval,
            convert=convert,
            convert_id=convert_id,
            skip_invalid=skip_invalid,
        )
    ).parsed
