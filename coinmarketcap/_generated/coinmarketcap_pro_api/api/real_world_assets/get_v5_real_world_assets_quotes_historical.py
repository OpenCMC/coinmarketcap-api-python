from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v5_real_world_assets_quotes_historical_interval import (
    GetV5RealWorldAssetsQuotesHistoricalInterval,
)
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...models.rwa_quotes_historical_response_model import RWAQuotesHistoricalResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    rwa_id: str | Unset = UNSET,
    rwa_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: int | Unset = UNSET,
    interval: GetV5RealWorldAssetsQuotesHistoricalInterval | Unset = "daily",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["rwa_id"] = rwa_id

    params["rwa_slug"] = rwa_slug

    params["symbol"] = symbol

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
        "url": "/v5/real-world-assets/quotes/historical",
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
    | RWAQuotesHistoricalResponseModel
    | None
):
    if response.status_code == 200:
        response_200 = RWAQuotesHistoricalResponseModel.from_dict(response.json())

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
    | RWAQuotesHistoricalResponseModel
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
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: int | Unset = UNSET,
    interval: GetV5RealWorldAssetsQuotesHistoricalInterval | Unset = "daily",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAQuotesHistoricalResponseModel
]:
    """Quotes Historical

     Returns a time series of tokenized aggregate values for one or more Real-World Asset (RWA) assets:
    the average tokenized price, tokenized market cap and 24h tokenized volume, with one data point per
    interval period. For the current values, use [/v5/real-world-assets/quotes/latest](/pro-api-
    reference/real-world-assets#quotes-latest-5). For the history of one underlying token, call
    [/v3/cryptocurrency/quotes/historical](/pro-api-reference/cryptocurrency#quotes-historical) with the
    token's `crypto_id`.

    At least one of `rwa_id`, `rwa_slug`, or `symbol` is required, and only one identifier type may be
    used per request. Assets are returned in the order requested. Each asset's `quotes` array is flat:
    one entry per data point per convert currency, tagged with `convert_id` and `convert_symbol`, oldest
    first and grouped by currency in the order requested. An asset with `has_tokens: false` returns an
    empty `quotes` array.

    **Time window**

    `time_start` and `time_end` are inclusive, and both are rounded down to the start of their interval
    period. The window depends on which parameters you send:

    - Neither `time_start` nor `time_end`: the `count` most recent periods.
    - `time_end` only: `count` periods ending with the period that contains `time_end`.
    - `time_start` only: `count` periods starting at `time_start`.
    - `time_start` and `time_end`: every period in the range. If you also send `count`, the first
    `count` periods from `time_start`.

    `count` defaults to 10 unless you send both `time_start` and `time_end`. It counts interval periods,
    not data points: a period with no data is skipped, so fewer data points can come back.

    **Data points**

    Each data point is the first value recorded in its period, stamped at the start of the period. Daily
    and longer periods start at 00:00 UTC for commodities, and at midnight New York time (04:00 or 05:00
    UTC) for stocks and ETFs. `weekly` periods start on Monday and `monthly` periods on the 1st.

    **Limits**

    - History starts no earlier than January 1, 2020. A range that starts earlier returns data from the
    first available data point, with no notice.
    - One request returns at most 10,000 data points, counted as the number of assets times the number
    of periods in the range. A larger request returns `400`.
    - `hourly` and `1h` to `12h` reach back at most 100 days, and `5m` to `45m` at most 10 days. Lower
    plans reach back less, as listed below. A request beyond your plan's window returns `403` with error
    code `1014`.
    - Up to 3 `convert` or `convert_id` values per request.

    How far back you can go depends on your plan and the interval.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic (hourly: 1 month, daily: 1 year)
      - Builder (hourly: 1 month, daily: 3 years)
      - Startup (hourly: 1 month, daily: from 2020)
      - Growth (hourly: 3 months, daily: from 2020)
      - Professional (hourly: 100 days, daily: from 2020)
      - Enterprise (hourly: 100 days, daily: from 2020, `5m` to `45m`: 10 days)

    **Note:** Hourly = `hourly` and `1h` to `12h` intervals, Daily = `daily`, `weekly`, `monthly`,
    `yearly` and `1d` to `365d` intervals. The `5m` to `45m` intervals are available on Enterprise only.

    **Cache / Update frequency:** Every 5 minutes.
    **Plan credit use:** 1 call credit per 100 data points returned (rounded up), counted across all
    requested assets, plus 1 credit per `convert`/`convert_id` beyond the first. A request that returns
    no data points costs 0 credits.
    **CMC equivalent pages:** The price chart on RWA asset pages like [coinmarketcap.com/real-world-
    assets/nvidia/](https://coinmarketcap.com/real-world-assets/nvidia/).

    Args:
        rwa_id (str | Unset):  Example: 1,2.
        rwa_slug (str | Unset):  Example: nvidia,gold.
        symbol (str | Unset):  Example: NVDA,GOLD.
        time_start (str | Unset):  Example: 2026-11-01T00:00:00Z.
        time_end (str | Unset):  Example: 2026-11-10T00:00:00Z.
        count (int | Unset):
        interval (GetV5RealWorldAssetsQuotesHistoricalInterval | Unset):  Default: 'daily'.
        convert (str | Unset):  Example: USD.
        convert_id (str | Unset):  Example: 2781.
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAQuotesHistoricalResponseModel]
    """

    kwargs = _get_kwargs(
        rwa_id=rwa_id,
        rwa_slug=rwa_slug,
        symbol=symbol,
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
    rwa_id: str | Unset = UNSET,
    rwa_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: int | Unset = UNSET,
    interval: GetV5RealWorldAssetsQuotesHistoricalInterval | Unset = "daily",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAQuotesHistoricalResponseModel
    | None
):
    """Quotes Historical

     Returns a time series of tokenized aggregate values for one or more Real-World Asset (RWA) assets:
    the average tokenized price, tokenized market cap and 24h tokenized volume, with one data point per
    interval period. For the current values, use [/v5/real-world-assets/quotes/latest](/pro-api-
    reference/real-world-assets#quotes-latest-5). For the history of one underlying token, call
    [/v3/cryptocurrency/quotes/historical](/pro-api-reference/cryptocurrency#quotes-historical) with the
    token's `crypto_id`.

    At least one of `rwa_id`, `rwa_slug`, or `symbol` is required, and only one identifier type may be
    used per request. Assets are returned in the order requested. Each asset's `quotes` array is flat:
    one entry per data point per convert currency, tagged with `convert_id` and `convert_symbol`, oldest
    first and grouped by currency in the order requested. An asset with `has_tokens: false` returns an
    empty `quotes` array.

    **Time window**

    `time_start` and `time_end` are inclusive, and both are rounded down to the start of their interval
    period. The window depends on which parameters you send:

    - Neither `time_start` nor `time_end`: the `count` most recent periods.
    - `time_end` only: `count` periods ending with the period that contains `time_end`.
    - `time_start` only: `count` periods starting at `time_start`.
    - `time_start` and `time_end`: every period in the range. If you also send `count`, the first
    `count` periods from `time_start`.

    `count` defaults to 10 unless you send both `time_start` and `time_end`. It counts interval periods,
    not data points: a period with no data is skipped, so fewer data points can come back.

    **Data points**

    Each data point is the first value recorded in its period, stamped at the start of the period. Daily
    and longer periods start at 00:00 UTC for commodities, and at midnight New York time (04:00 or 05:00
    UTC) for stocks and ETFs. `weekly` periods start on Monday and `monthly` periods on the 1st.

    **Limits**

    - History starts no earlier than January 1, 2020. A range that starts earlier returns data from the
    first available data point, with no notice.
    - One request returns at most 10,000 data points, counted as the number of assets times the number
    of periods in the range. A larger request returns `400`.
    - `hourly` and `1h` to `12h` reach back at most 100 days, and `5m` to `45m` at most 10 days. Lower
    plans reach back less, as listed below. A request beyond your plan's window returns `403` with error
    code `1014`.
    - Up to 3 `convert` or `convert_id` values per request.

    How far back you can go depends on your plan and the interval.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic (hourly: 1 month, daily: 1 year)
      - Builder (hourly: 1 month, daily: 3 years)
      - Startup (hourly: 1 month, daily: from 2020)
      - Growth (hourly: 3 months, daily: from 2020)
      - Professional (hourly: 100 days, daily: from 2020)
      - Enterprise (hourly: 100 days, daily: from 2020, `5m` to `45m`: 10 days)

    **Note:** Hourly = `hourly` and `1h` to `12h` intervals, Daily = `daily`, `weekly`, `monthly`,
    `yearly` and `1d` to `365d` intervals. The `5m` to `45m` intervals are available on Enterprise only.

    **Cache / Update frequency:** Every 5 minutes.
    **Plan credit use:** 1 call credit per 100 data points returned (rounded up), counted across all
    requested assets, plus 1 credit per `convert`/`convert_id` beyond the first. A request that returns
    no data points costs 0 credits.
    **CMC equivalent pages:** The price chart on RWA asset pages like [coinmarketcap.com/real-world-
    assets/nvidia/](https://coinmarketcap.com/real-world-assets/nvidia/).

    Args:
        rwa_id (str | Unset):  Example: 1,2.
        rwa_slug (str | Unset):  Example: nvidia,gold.
        symbol (str | Unset):  Example: NVDA,GOLD.
        time_start (str | Unset):  Example: 2026-11-01T00:00:00Z.
        time_end (str | Unset):  Example: 2026-11-10T00:00:00Z.
        count (int | Unset):
        interval (GetV5RealWorldAssetsQuotesHistoricalInterval | Unset):  Default: 'daily'.
        convert (str | Unset):  Example: USD.
        convert_id (str | Unset):  Example: 2781.
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAQuotesHistoricalResponseModel
    """

    return sync_detailed(
        client=client,
        rwa_id=rwa_id,
        rwa_slug=rwa_slug,
        symbol=symbol,
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
    rwa_id: str | Unset = UNSET,
    rwa_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: int | Unset = UNSET,
    interval: GetV5RealWorldAssetsQuotesHistoricalInterval | Unset = "daily",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAQuotesHistoricalResponseModel
]:
    """Quotes Historical

     Returns a time series of tokenized aggregate values for one or more Real-World Asset (RWA) assets:
    the average tokenized price, tokenized market cap and 24h tokenized volume, with one data point per
    interval period. For the current values, use [/v5/real-world-assets/quotes/latest](/pro-api-
    reference/real-world-assets#quotes-latest-5). For the history of one underlying token, call
    [/v3/cryptocurrency/quotes/historical](/pro-api-reference/cryptocurrency#quotes-historical) with the
    token's `crypto_id`.

    At least one of `rwa_id`, `rwa_slug`, or `symbol` is required, and only one identifier type may be
    used per request. Assets are returned in the order requested. Each asset's `quotes` array is flat:
    one entry per data point per convert currency, tagged with `convert_id` and `convert_symbol`, oldest
    first and grouped by currency in the order requested. An asset with `has_tokens: false` returns an
    empty `quotes` array.

    **Time window**

    `time_start` and `time_end` are inclusive, and both are rounded down to the start of their interval
    period. The window depends on which parameters you send:

    - Neither `time_start` nor `time_end`: the `count` most recent periods.
    - `time_end` only: `count` periods ending with the period that contains `time_end`.
    - `time_start` only: `count` periods starting at `time_start`.
    - `time_start` and `time_end`: every period in the range. If you also send `count`, the first
    `count` periods from `time_start`.

    `count` defaults to 10 unless you send both `time_start` and `time_end`. It counts interval periods,
    not data points: a period with no data is skipped, so fewer data points can come back.

    **Data points**

    Each data point is the first value recorded in its period, stamped at the start of the period. Daily
    and longer periods start at 00:00 UTC for commodities, and at midnight New York time (04:00 or 05:00
    UTC) for stocks and ETFs. `weekly` periods start on Monday and `monthly` periods on the 1st.

    **Limits**

    - History starts no earlier than January 1, 2020. A range that starts earlier returns data from the
    first available data point, with no notice.
    - One request returns at most 10,000 data points, counted as the number of assets times the number
    of periods in the range. A larger request returns `400`.
    - `hourly` and `1h` to `12h` reach back at most 100 days, and `5m` to `45m` at most 10 days. Lower
    plans reach back less, as listed below. A request beyond your plan's window returns `403` with error
    code `1014`.
    - Up to 3 `convert` or `convert_id` values per request.

    How far back you can go depends on your plan and the interval.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic (hourly: 1 month, daily: 1 year)
      - Builder (hourly: 1 month, daily: 3 years)
      - Startup (hourly: 1 month, daily: from 2020)
      - Growth (hourly: 3 months, daily: from 2020)
      - Professional (hourly: 100 days, daily: from 2020)
      - Enterprise (hourly: 100 days, daily: from 2020, `5m` to `45m`: 10 days)

    **Note:** Hourly = `hourly` and `1h` to `12h` intervals, Daily = `daily`, `weekly`, `monthly`,
    `yearly` and `1d` to `365d` intervals. The `5m` to `45m` intervals are available on Enterprise only.

    **Cache / Update frequency:** Every 5 minutes.
    **Plan credit use:** 1 call credit per 100 data points returned (rounded up), counted across all
    requested assets, plus 1 credit per `convert`/`convert_id` beyond the first. A request that returns
    no data points costs 0 credits.
    **CMC equivalent pages:** The price chart on RWA asset pages like [coinmarketcap.com/real-world-
    assets/nvidia/](https://coinmarketcap.com/real-world-assets/nvidia/).

    Args:
        rwa_id (str | Unset):  Example: 1,2.
        rwa_slug (str | Unset):  Example: nvidia,gold.
        symbol (str | Unset):  Example: NVDA,GOLD.
        time_start (str | Unset):  Example: 2026-11-01T00:00:00Z.
        time_end (str | Unset):  Example: 2026-11-10T00:00:00Z.
        count (int | Unset):
        interval (GetV5RealWorldAssetsQuotesHistoricalInterval | Unset):  Default: 'daily'.
        convert (str | Unset):  Example: USD.
        convert_id (str | Unset):  Example: 2781.
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAQuotesHistoricalResponseModel]
    """

    kwargs = _get_kwargs(
        rwa_id=rwa_id,
        rwa_slug=rwa_slug,
        symbol=symbol,
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
    rwa_id: str | Unset = UNSET,
    rwa_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: int | Unset = UNSET,
    interval: GetV5RealWorldAssetsQuotesHistoricalInterval | Unset = "daily",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAQuotesHistoricalResponseModel
    | None
):
    """Quotes Historical

     Returns a time series of tokenized aggregate values for one or more Real-World Asset (RWA) assets:
    the average tokenized price, tokenized market cap and 24h tokenized volume, with one data point per
    interval period. For the current values, use [/v5/real-world-assets/quotes/latest](/pro-api-
    reference/real-world-assets#quotes-latest-5). For the history of one underlying token, call
    [/v3/cryptocurrency/quotes/historical](/pro-api-reference/cryptocurrency#quotes-historical) with the
    token's `crypto_id`.

    At least one of `rwa_id`, `rwa_slug`, or `symbol` is required, and only one identifier type may be
    used per request. Assets are returned in the order requested. Each asset's `quotes` array is flat:
    one entry per data point per convert currency, tagged with `convert_id` and `convert_symbol`, oldest
    first and grouped by currency in the order requested. An asset with `has_tokens: false` returns an
    empty `quotes` array.

    **Time window**

    `time_start` and `time_end` are inclusive, and both are rounded down to the start of their interval
    period. The window depends on which parameters you send:

    - Neither `time_start` nor `time_end`: the `count` most recent periods.
    - `time_end` only: `count` periods ending with the period that contains `time_end`.
    - `time_start` only: `count` periods starting at `time_start`.
    - `time_start` and `time_end`: every period in the range. If you also send `count`, the first
    `count` periods from `time_start`.

    `count` defaults to 10 unless you send both `time_start` and `time_end`. It counts interval periods,
    not data points: a period with no data is skipped, so fewer data points can come back.

    **Data points**

    Each data point is the first value recorded in its period, stamped at the start of the period. Daily
    and longer periods start at 00:00 UTC for commodities, and at midnight New York time (04:00 or 05:00
    UTC) for stocks and ETFs. `weekly` periods start on Monday and `monthly` periods on the 1st.

    **Limits**

    - History starts no earlier than January 1, 2020. A range that starts earlier returns data from the
    first available data point, with no notice.
    - One request returns at most 10,000 data points, counted as the number of assets times the number
    of periods in the range. A larger request returns `400`.
    - `hourly` and `1h` to `12h` reach back at most 100 days, and `5m` to `45m` at most 10 days. Lower
    plans reach back less, as listed below. A request beyond your plan's window returns `403` with error
    code `1014`.
    - Up to 3 `convert` or `convert_id` values per request.

    How far back you can go depends on your plan and the interval.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic (hourly: 1 month, daily: 1 year)
      - Builder (hourly: 1 month, daily: 3 years)
      - Startup (hourly: 1 month, daily: from 2020)
      - Growth (hourly: 3 months, daily: from 2020)
      - Professional (hourly: 100 days, daily: from 2020)
      - Enterprise (hourly: 100 days, daily: from 2020, `5m` to `45m`: 10 days)

    **Note:** Hourly = `hourly` and `1h` to `12h` intervals, Daily = `daily`, `weekly`, `monthly`,
    `yearly` and `1d` to `365d` intervals. The `5m` to `45m` intervals are available on Enterprise only.

    **Cache / Update frequency:** Every 5 minutes.
    **Plan credit use:** 1 call credit per 100 data points returned (rounded up), counted across all
    requested assets, plus 1 credit per `convert`/`convert_id` beyond the first. A request that returns
    no data points costs 0 credits.
    **CMC equivalent pages:** The price chart on RWA asset pages like [coinmarketcap.com/real-world-
    assets/nvidia/](https://coinmarketcap.com/real-world-assets/nvidia/).

    Args:
        rwa_id (str | Unset):  Example: 1,2.
        rwa_slug (str | Unset):  Example: nvidia,gold.
        symbol (str | Unset):  Example: NVDA,GOLD.
        time_start (str | Unset):  Example: 2026-11-01T00:00:00Z.
        time_end (str | Unset):  Example: 2026-11-10T00:00:00Z.
        count (int | Unset):
        interval (GetV5RealWorldAssetsQuotesHistoricalInterval | Unset):  Default: 'daily'.
        convert (str | Unset):  Example: USD.
        convert_id (str | Unset):  Example: 2781.
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAQuotesHistoricalResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            rwa_id=rwa_id,
            rwa_slug=rwa_slug,
            symbol=symbol,
            time_start=time_start,
            time_end=time_end,
            count=count,
            interval=interval,
            convert=convert,
            convert_id=convert_id,
            skip_invalid=skip_invalid,
        )
    ).parsed
