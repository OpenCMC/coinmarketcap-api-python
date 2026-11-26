from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cryptocurrency_ohlcv_historical_v5_response_model import CryptocurrencyOHLCVHistoricalV5ResponseModel
from ...models.get_v5_cryptocurrency_ohlcv_historical_interval import (
    GetV5CryptocurrencyOhlcvHistoricalInterval,
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
    interval: GetV5CryptocurrencyOhlcvHistoricalInterval,
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: int | Unset = UNSET,
    convert_id: str | Unset = "2781",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["slug"] = slug

    json_interval: str = interval
    params["interval"] = json_interval

    params["time_start"] = time_start

    params["time_end"] = time_end

    params["count"] = count

    params["convert_id"] = convert_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v5/cryptocurrency/ohlcv/historical",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CryptocurrencyOHLCVHistoricalV5ResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = CryptocurrencyOHLCVHistoricalV5ResponseModel.from_dict(response.json())

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
    CryptocurrencyOHLCVHistoricalV5ResponseModel
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
    interval: GetV5CryptocurrencyOhlcvHistoricalInterval,
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: int | Unset = UNSET,
    convert_id: str | Unset = "2781",
) -> Response[
    CryptocurrencyOHLCVHistoricalV5ResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """OHLCV Historical

     Returns historical OHLCV (open, high, low, close, volume) candles for one cryptocurrency, together
    with the market cap and the times of the high and the low in each candle. Each candle is a compact
    row of 10 values instead of a nested object, so long histories stay small and load straight into
    charting and analysis tools.

    Compared with the deprecated [/v2/cryptocurrency/ohlcv/historical](/pro-api-
    reference/deprecated#ohlcv-historical-v2-deprecated), this endpoint:

    - returns one cryptocurrency per request, by `id` or `slug`, in one currency set with `convert_id`.
    - uses the interval names `15m`, `1h`, `4h`, `1d`, `1w` and `1M`. `1w` is a calendar week starting
    on Monday and `1M` is a calendar month.
    - uses `time_start` and `count` when you send `time_start`, `time_end` and `count` together, instead
    of working out `count` from the time range.
    - rejects parameters it does not support, such as `symbol`, `convert`, `time_period` and
    `skip_invalid`, with a `400` error instead of ignoring them.

    **Candle rows**

    `data` is an array of candles, oldest first. Each candle is an array of 10 values in this fixed
    order, so read the values by position:

    | Index | Field | Type | Description |
    | --- | --- | --- | --- |
    | 0 | `openPrice` | number | Open price: the first price in the period. |
    | 1 | `highPrice` | number | High price: the highest price in the period. |
    | 2 | `lowPrice` | number | Low price: the lowest price in the period. |
    | 3 | `closePrice` | number | Close price: the last price in the period. |
    | 4 | `volume` | number | Trading volume in the period. |
    | 5 | `marketcap` | number | Market cap at the close of the period. |
    | 6 | `openTime` | string | Start of the period (ISO 8601, UTC). |
    | 7 | `highTime` | string | Time of the high price (ISO 8601, UTC). |
    | 8 | `lowTime` | string | Time of the low price (ISO 8601, UTC). |
    | 9 | `closeTime` | string | End of the period (ISO 8601, UTC), for example
    `2025-01-02T23:59:59.999Z`. |

    Prices, volume and market cap are in the currency set by `convert_id`. A value that is not available
    is returned as `null` in its position. Periods with no data, future periods and the period that is
    still open are left out, so a request with no data returns an empty `data` array.

    **Time window**

    `time_start` and `time_end` are inclusive, and both are rounded down to the start of their interval
    period in UTC. The window depends on which parameters you send:

    - `time_start` and `time_end`: every period in the range, up to 10000 periods.
    - `time_start` and `count`: `count` periods starting at `time_start`.
    - `time_end` and `count`: `count` periods ending with the period that contains `time_end`.
    - `time_start`, `time_end` and `count`: `count` periods starting at `time_start`. `time_end` must
    still be a valid timestamp, but it does not change the window.
    - Neither `time_start` nor `time_end`: the `count` most recent completed periods.

    `count` defaults to 10 when you do not send both `time_start` and `time_end`.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - Startup (intraday: 1 month, daily: from 2010)
      - Growth (intraday: 3 months, daily: from 2010)
      - Professional (intraday: 12 months, daily: from 2010)
      - Enterprise (intraday: from 2010, daily: from 2010)

    **Note:** Intraday = `15m`, `1h` and `4h` intervals, Daily = `1d`, `1w` and `1M` intervals

    **Cache / Update frequency:** Each candle is returned once its period has closed.
    **Plan credit use:** 1 call credit per 100 candles returned (rounded up). A request that returns no
    candles costs 0 credits.
    **CMC equivalent pages:** Our historical cryptocurrency data pages like
    [coinmarketcap.com/currencies/bitcoin/historical-
    data/](https://coinmarketcap.com/currencies/bitcoin/historical-data/).

    Args:
        id (str | Unset):  Example: 1.
        slug (str | Unset):
        interval (GetV5CryptocurrencyOhlcvHistoricalInterval):  Example: 1d.
        time_start (str | Unset):
        time_end (str | Unset):
        count (int | Unset):
        convert_id (str | Unset):  Default: '2781'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyOHLCVHistoricalV5ResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        interval=interval,
        time_start=time_start,
        time_end=time_end,
        count=count,
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
    interval: GetV5CryptocurrencyOhlcvHistoricalInterval,
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: int | Unset = UNSET,
    convert_id: str | Unset = "2781",
) -> (
    CryptocurrencyOHLCVHistoricalV5ResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """OHLCV Historical

     Returns historical OHLCV (open, high, low, close, volume) candles for one cryptocurrency, together
    with the market cap and the times of the high and the low in each candle. Each candle is a compact
    row of 10 values instead of a nested object, so long histories stay small and load straight into
    charting and analysis tools.

    Compared with the deprecated [/v2/cryptocurrency/ohlcv/historical](/pro-api-
    reference/deprecated#ohlcv-historical-v2-deprecated), this endpoint:

    - returns one cryptocurrency per request, by `id` or `slug`, in one currency set with `convert_id`.
    - uses the interval names `15m`, `1h`, `4h`, `1d`, `1w` and `1M`. `1w` is a calendar week starting
    on Monday and `1M` is a calendar month.
    - uses `time_start` and `count` when you send `time_start`, `time_end` and `count` together, instead
    of working out `count` from the time range.
    - rejects parameters it does not support, such as `symbol`, `convert`, `time_period` and
    `skip_invalid`, with a `400` error instead of ignoring them.

    **Candle rows**

    `data` is an array of candles, oldest first. Each candle is an array of 10 values in this fixed
    order, so read the values by position:

    | Index | Field | Type | Description |
    | --- | --- | --- | --- |
    | 0 | `openPrice` | number | Open price: the first price in the period. |
    | 1 | `highPrice` | number | High price: the highest price in the period. |
    | 2 | `lowPrice` | number | Low price: the lowest price in the period. |
    | 3 | `closePrice` | number | Close price: the last price in the period. |
    | 4 | `volume` | number | Trading volume in the period. |
    | 5 | `marketcap` | number | Market cap at the close of the period. |
    | 6 | `openTime` | string | Start of the period (ISO 8601, UTC). |
    | 7 | `highTime` | string | Time of the high price (ISO 8601, UTC). |
    | 8 | `lowTime` | string | Time of the low price (ISO 8601, UTC). |
    | 9 | `closeTime` | string | End of the period (ISO 8601, UTC), for example
    `2025-01-02T23:59:59.999Z`. |

    Prices, volume and market cap are in the currency set by `convert_id`. A value that is not available
    is returned as `null` in its position. Periods with no data, future periods and the period that is
    still open are left out, so a request with no data returns an empty `data` array.

    **Time window**

    `time_start` and `time_end` are inclusive, and both are rounded down to the start of their interval
    period in UTC. The window depends on which parameters you send:

    - `time_start` and `time_end`: every period in the range, up to 10000 periods.
    - `time_start` and `count`: `count` periods starting at `time_start`.
    - `time_end` and `count`: `count` periods ending with the period that contains `time_end`.
    - `time_start`, `time_end` and `count`: `count` periods starting at `time_start`. `time_end` must
    still be a valid timestamp, but it does not change the window.
    - Neither `time_start` nor `time_end`: the `count` most recent completed periods.

    `count` defaults to 10 when you do not send both `time_start` and `time_end`.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - Startup (intraday: 1 month, daily: from 2010)
      - Growth (intraday: 3 months, daily: from 2010)
      - Professional (intraday: 12 months, daily: from 2010)
      - Enterprise (intraday: from 2010, daily: from 2010)

    **Note:** Intraday = `15m`, `1h` and `4h` intervals, Daily = `1d`, `1w` and `1M` intervals

    **Cache / Update frequency:** Each candle is returned once its period has closed.
    **Plan credit use:** 1 call credit per 100 candles returned (rounded up). A request that returns no
    candles costs 0 credits.
    **CMC equivalent pages:** Our historical cryptocurrency data pages like
    [coinmarketcap.com/currencies/bitcoin/historical-
    data/](https://coinmarketcap.com/currencies/bitcoin/historical-data/).

    Args:
        id (str | Unset):  Example: 1.
        slug (str | Unset):
        interval (GetV5CryptocurrencyOhlcvHistoricalInterval):  Example: 1d.
        time_start (str | Unset):
        time_end (str | Unset):
        count (int | Unset):
        convert_id (str | Unset):  Default: '2781'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyOHLCVHistoricalV5ResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        id=id,
        slug=slug,
        interval=interval,
        time_start=time_start,
        time_end=time_end,
        count=count,
        convert_id=convert_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    interval: GetV5CryptocurrencyOhlcvHistoricalInterval,
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: int | Unset = UNSET,
    convert_id: str | Unset = "2781",
) -> Response[
    CryptocurrencyOHLCVHistoricalV5ResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """OHLCV Historical

     Returns historical OHLCV (open, high, low, close, volume) candles for one cryptocurrency, together
    with the market cap and the times of the high and the low in each candle. Each candle is a compact
    row of 10 values instead of a nested object, so long histories stay small and load straight into
    charting and analysis tools.

    Compared with the deprecated [/v2/cryptocurrency/ohlcv/historical](/pro-api-
    reference/deprecated#ohlcv-historical-v2-deprecated), this endpoint:

    - returns one cryptocurrency per request, by `id` or `slug`, in one currency set with `convert_id`.
    - uses the interval names `15m`, `1h`, `4h`, `1d`, `1w` and `1M`. `1w` is a calendar week starting
    on Monday and `1M` is a calendar month.
    - uses `time_start` and `count` when you send `time_start`, `time_end` and `count` together, instead
    of working out `count` from the time range.
    - rejects parameters it does not support, such as `symbol`, `convert`, `time_period` and
    `skip_invalid`, with a `400` error instead of ignoring them.

    **Candle rows**

    `data` is an array of candles, oldest first. Each candle is an array of 10 values in this fixed
    order, so read the values by position:

    | Index | Field | Type | Description |
    | --- | --- | --- | --- |
    | 0 | `openPrice` | number | Open price: the first price in the period. |
    | 1 | `highPrice` | number | High price: the highest price in the period. |
    | 2 | `lowPrice` | number | Low price: the lowest price in the period. |
    | 3 | `closePrice` | number | Close price: the last price in the period. |
    | 4 | `volume` | number | Trading volume in the period. |
    | 5 | `marketcap` | number | Market cap at the close of the period. |
    | 6 | `openTime` | string | Start of the period (ISO 8601, UTC). |
    | 7 | `highTime` | string | Time of the high price (ISO 8601, UTC). |
    | 8 | `lowTime` | string | Time of the low price (ISO 8601, UTC). |
    | 9 | `closeTime` | string | End of the period (ISO 8601, UTC), for example
    `2025-01-02T23:59:59.999Z`. |

    Prices, volume and market cap are in the currency set by `convert_id`. A value that is not available
    is returned as `null` in its position. Periods with no data, future periods and the period that is
    still open are left out, so a request with no data returns an empty `data` array.

    **Time window**

    `time_start` and `time_end` are inclusive, and both are rounded down to the start of their interval
    period in UTC. The window depends on which parameters you send:

    - `time_start` and `time_end`: every period in the range, up to 10000 periods.
    - `time_start` and `count`: `count` periods starting at `time_start`.
    - `time_end` and `count`: `count` periods ending with the period that contains `time_end`.
    - `time_start`, `time_end` and `count`: `count` periods starting at `time_start`. `time_end` must
    still be a valid timestamp, but it does not change the window.
    - Neither `time_start` nor `time_end`: the `count` most recent completed periods.

    `count` defaults to 10 when you do not send both `time_start` and `time_end`.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - Startup (intraday: 1 month, daily: from 2010)
      - Growth (intraday: 3 months, daily: from 2010)
      - Professional (intraday: 12 months, daily: from 2010)
      - Enterprise (intraday: from 2010, daily: from 2010)

    **Note:** Intraday = `15m`, `1h` and `4h` intervals, Daily = `1d`, `1w` and `1M` intervals

    **Cache / Update frequency:** Each candle is returned once its period has closed.
    **Plan credit use:** 1 call credit per 100 candles returned (rounded up). A request that returns no
    candles costs 0 credits.
    **CMC equivalent pages:** Our historical cryptocurrency data pages like
    [coinmarketcap.com/currencies/bitcoin/historical-
    data/](https://coinmarketcap.com/currencies/bitcoin/historical-data/).

    Args:
        id (str | Unset):  Example: 1.
        slug (str | Unset):
        interval (GetV5CryptocurrencyOhlcvHistoricalInterval):  Example: 1d.
        time_start (str | Unset):
        time_end (str | Unset):
        count (int | Unset):
        convert_id (str | Unset):  Default: '2781'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyOHLCVHistoricalV5ResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        interval=interval,
        time_start=time_start,
        time_end=time_end,
        count=count,
        convert_id=convert_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    interval: GetV5CryptocurrencyOhlcvHistoricalInterval,
    time_start: str | Unset = UNSET,
    time_end: str | Unset = UNSET,
    count: int | Unset = UNSET,
    convert_id: str | Unset = "2781",
) -> (
    CryptocurrencyOHLCVHistoricalV5ResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """OHLCV Historical

     Returns historical OHLCV (open, high, low, close, volume) candles for one cryptocurrency, together
    with the market cap and the times of the high and the low in each candle. Each candle is a compact
    row of 10 values instead of a nested object, so long histories stay small and load straight into
    charting and analysis tools.

    Compared with the deprecated [/v2/cryptocurrency/ohlcv/historical](/pro-api-
    reference/deprecated#ohlcv-historical-v2-deprecated), this endpoint:

    - returns one cryptocurrency per request, by `id` or `slug`, in one currency set with `convert_id`.
    - uses the interval names `15m`, `1h`, `4h`, `1d`, `1w` and `1M`. `1w` is a calendar week starting
    on Monday and `1M` is a calendar month.
    - uses `time_start` and `count` when you send `time_start`, `time_end` and `count` together, instead
    of working out `count` from the time range.
    - rejects parameters it does not support, such as `symbol`, `convert`, `time_period` and
    `skip_invalid`, with a `400` error instead of ignoring them.

    **Candle rows**

    `data` is an array of candles, oldest first. Each candle is an array of 10 values in this fixed
    order, so read the values by position:

    | Index | Field | Type | Description |
    | --- | --- | --- | --- |
    | 0 | `openPrice` | number | Open price: the first price in the period. |
    | 1 | `highPrice` | number | High price: the highest price in the period. |
    | 2 | `lowPrice` | number | Low price: the lowest price in the period. |
    | 3 | `closePrice` | number | Close price: the last price in the period. |
    | 4 | `volume` | number | Trading volume in the period. |
    | 5 | `marketcap` | number | Market cap at the close of the period. |
    | 6 | `openTime` | string | Start of the period (ISO 8601, UTC). |
    | 7 | `highTime` | string | Time of the high price (ISO 8601, UTC). |
    | 8 | `lowTime` | string | Time of the low price (ISO 8601, UTC). |
    | 9 | `closeTime` | string | End of the period (ISO 8601, UTC), for example
    `2025-01-02T23:59:59.999Z`. |

    Prices, volume and market cap are in the currency set by `convert_id`. A value that is not available
    is returned as `null` in its position. Periods with no data, future periods and the period that is
    still open are left out, so a request with no data returns an empty `data` array.

    **Time window**

    `time_start` and `time_end` are inclusive, and both are rounded down to the start of their interval
    period in UTC. The window depends on which parameters you send:

    - `time_start` and `time_end`: every period in the range, up to 10000 periods.
    - `time_start` and `count`: `count` periods starting at `time_start`.
    - `time_end` and `count`: `count` periods ending with the period that contains `time_end`.
    - `time_start`, `time_end` and `count`: `count` periods starting at `time_start`. `time_end` must
    still be a valid timestamp, but it does not change the window.
    - Neither `time_start` nor `time_end`: the `count` most recent completed periods.

    `count` defaults to 10 when you do not send both `time_start` and `time_end`.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - Startup (intraday: 1 month, daily: from 2010)
      - Growth (intraday: 3 months, daily: from 2010)
      - Professional (intraday: 12 months, daily: from 2010)
      - Enterprise (intraday: from 2010, daily: from 2010)

    **Note:** Intraday = `15m`, `1h` and `4h` intervals, Daily = `1d`, `1w` and `1M` intervals

    **Cache / Update frequency:** Each candle is returned once its period has closed.
    **Plan credit use:** 1 call credit per 100 candles returned (rounded up). A request that returns no
    candles costs 0 credits.
    **CMC equivalent pages:** Our historical cryptocurrency data pages like
    [coinmarketcap.com/currencies/bitcoin/historical-
    data/](https://coinmarketcap.com/currencies/bitcoin/historical-data/).

    Args:
        id (str | Unset):  Example: 1.
        slug (str | Unset):
        interval (GetV5CryptocurrencyOhlcvHistoricalInterval):  Example: 1d.
        time_start (str | Unset):
        time_end (str | Unset):
        count (int | Unset):
        convert_id (str | Unset):  Default: '2781'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyOHLCVHistoricalV5ResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            slug=slug,
            interval=interval,
            time_start=time_start,
            time_end=time_end,
            count=count,
            convert_id=convert_id,
        )
    ).parsed
