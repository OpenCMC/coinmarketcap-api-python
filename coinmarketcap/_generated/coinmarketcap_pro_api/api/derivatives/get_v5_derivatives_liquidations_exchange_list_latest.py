from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v5_derivatives_liquidations_exchange_list_latest_sort import (
    GetV5DerivativesLiquidationsExchangeListLatestSort,
)
from ...models.get_v5_derivatives_liquidations_exchange_list_latest_sort_dir import (
    GetV5DerivativesLiquidationsExchangeListLatestSortDir,
)
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...models.liquidations_by_exchange_response_model import LiquidationsByExchangeResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    exchange_id: str | Unset = UNSET,
    exchange_slug: str | Unset = UNSET,
    skip_invalid: bool | Unset = False,
    sort: GetV5DerivativesLiquidationsExchangeListLatestSort | Unset = "total_liquidations_24h",
    sort_dir: GetV5DerivativesLiquidationsExchangeListLatestSortDir | Unset = "desc",
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = "USD",
    convert_id: str | Unset = "2781",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["exchange_id"] = exchange_id

    params["exchange_slug"] = exchange_slug

    params["skip_invalid"] = skip_invalid

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_sort_dir: str | Unset = UNSET
    if not isinstance(sort_dir, Unset):
        json_sort_dir = sort_dir

    params["sort_dir"] = json_sort_dir

    params["start"] = start

    params["limit"] = limit

    params["convert"] = convert

    params["convert_id"] = convert_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v5/derivatives/liquidations/exchange/list/latest",
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
    | LiquidationsByExchangeResponseModel
    | None
):
    if response.status_code == 200:
        response_200 = LiquidationsByExchangeResponseModel.from_dict(response.json())

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
    | LiquidationsByExchangeResponseModel
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
    exchange_id: str | Unset = UNSET,
    exchange_slug: str | Unset = UNSET,
    skip_invalid: bool | Unset = False,
    sort: GetV5DerivativesLiquidationsExchangeListLatestSort | Unset = "total_liquidations_24h",
    sort_dir: GetV5DerivativesLiquidationsExchangeListLatestSortDir | Unset = "desc",
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = "USD",
    convert_id: str | Unset = "2781",
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | LiquidationsByExchangeResponseModel
]:
    """Latest Liquidations by Exchange

     Returns a paginated, sorted list of the derivatives exchanges that CoinMarketCap tracks, each with
    its perpetual and futures liquidation values over rolling 1-hour, 4-hour, and 24-hour windows. This
    is the per-exchange leaderboard shown on the [CoinMarketCap liquidations
    chart](https://coinmarketcap.com/charts/liquidations/). When you call it without any filters, it
    returns every tracked exchange sorted by `total_liquidations_24h` in descending order.

    Only exchanges that have an integrated liquidation feed are included in the results, and an exchange
    that is otherwise valid but has recorded no liquidations across any of the tracked windows is left
    out of the list entirely. Because of this, a request whose filter matches only such exchanges still
    succeeds: it returns an empty list with `total_size` set to `0` rather than failing with an error.

    This endpoint covers exchanges only. To see the same liquidation values aggregated per
    cryptocurrency, use [/v5/derivatives/liquidations/cryptocurrency/list/latest](/pro-api-
    reference/derivatives#latest-liquidations-by-cryptocurrency) instead.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 exchanges returned (rounded up), plus 1 credit per
    `convert` / `convert_id` option beyond the first.
    **CMC equivalent page:**
    [coinmarketcap.com/charts/liquidations/](https://coinmarketcap.com/charts/liquidations/)

    Args:
        exchange_id (str | Unset):  Example: 270,294.
        exchange_slug (str | Unset):  Example: binance,bybit.
        skip_invalid (bool | Unset):  Default: False.
        sort (GetV5DerivativesLiquidationsExchangeListLatestSort | Unset):  Default:
            'total_liquidations_24h'.
        sort_dir (GetV5DerivativesLiquidationsExchangeListLatestSortDir | Unset):  Default:
            'desc'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):  Default: 'USD'. Example: USD.
        convert_id (str | Unset):  Default: '2781'. Example: 2781.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | LiquidationsByExchangeResponseModel]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        exchange_slug=exchange_slug,
        skip_invalid=skip_invalid,
        sort=sort,
        sort_dir=sort_dir,
        start=start,
        limit=limit,
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
    exchange_id: str | Unset = UNSET,
    exchange_slug: str | Unset = UNSET,
    skip_invalid: bool | Unset = False,
    sort: GetV5DerivativesLiquidationsExchangeListLatestSort | Unset = "total_liquidations_24h",
    sort_dir: GetV5DerivativesLiquidationsExchangeListLatestSortDir | Unset = "desc",
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = "USD",
    convert_id: str | Unset = "2781",
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | LiquidationsByExchangeResponseModel
    | None
):
    """Latest Liquidations by Exchange

     Returns a paginated, sorted list of the derivatives exchanges that CoinMarketCap tracks, each with
    its perpetual and futures liquidation values over rolling 1-hour, 4-hour, and 24-hour windows. This
    is the per-exchange leaderboard shown on the [CoinMarketCap liquidations
    chart](https://coinmarketcap.com/charts/liquidations/). When you call it without any filters, it
    returns every tracked exchange sorted by `total_liquidations_24h` in descending order.

    Only exchanges that have an integrated liquidation feed are included in the results, and an exchange
    that is otherwise valid but has recorded no liquidations across any of the tracked windows is left
    out of the list entirely. Because of this, a request whose filter matches only such exchanges still
    succeeds: it returns an empty list with `total_size` set to `0` rather than failing with an error.

    This endpoint covers exchanges only. To see the same liquidation values aggregated per
    cryptocurrency, use [/v5/derivatives/liquidations/cryptocurrency/list/latest](/pro-api-
    reference/derivatives#latest-liquidations-by-cryptocurrency) instead.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 exchanges returned (rounded up), plus 1 credit per
    `convert` / `convert_id` option beyond the first.
    **CMC equivalent page:**
    [coinmarketcap.com/charts/liquidations/](https://coinmarketcap.com/charts/liquidations/)

    Args:
        exchange_id (str | Unset):  Example: 270,294.
        exchange_slug (str | Unset):  Example: binance,bybit.
        skip_invalid (bool | Unset):  Default: False.
        sort (GetV5DerivativesLiquidationsExchangeListLatestSort | Unset):  Default:
            'total_liquidations_24h'.
        sort_dir (GetV5DerivativesLiquidationsExchangeListLatestSortDir | Unset):  Default:
            'desc'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):  Default: 'USD'. Example: USD.
        convert_id (str | Unset):  Default: '2781'. Example: 2781.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | LiquidationsByExchangeResponseModel
    """

    return sync_detailed(
        client=client,
        exchange_id=exchange_id,
        exchange_slug=exchange_slug,
        skip_invalid=skip_invalid,
        sort=sort,
        sort_dir=sort_dir,
        start=start,
        limit=limit,
        convert=convert,
        convert_id=convert_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    exchange_id: str | Unset = UNSET,
    exchange_slug: str | Unset = UNSET,
    skip_invalid: bool | Unset = False,
    sort: GetV5DerivativesLiquidationsExchangeListLatestSort | Unset = "total_liquidations_24h",
    sort_dir: GetV5DerivativesLiquidationsExchangeListLatestSortDir | Unset = "desc",
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = "USD",
    convert_id: str | Unset = "2781",
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | LiquidationsByExchangeResponseModel
]:
    """Latest Liquidations by Exchange

     Returns a paginated, sorted list of the derivatives exchanges that CoinMarketCap tracks, each with
    its perpetual and futures liquidation values over rolling 1-hour, 4-hour, and 24-hour windows. This
    is the per-exchange leaderboard shown on the [CoinMarketCap liquidations
    chart](https://coinmarketcap.com/charts/liquidations/). When you call it without any filters, it
    returns every tracked exchange sorted by `total_liquidations_24h` in descending order.

    Only exchanges that have an integrated liquidation feed are included in the results, and an exchange
    that is otherwise valid but has recorded no liquidations across any of the tracked windows is left
    out of the list entirely. Because of this, a request whose filter matches only such exchanges still
    succeeds: it returns an empty list with `total_size` set to `0` rather than failing with an error.

    This endpoint covers exchanges only. To see the same liquidation values aggregated per
    cryptocurrency, use [/v5/derivatives/liquidations/cryptocurrency/list/latest](/pro-api-
    reference/derivatives#latest-liquidations-by-cryptocurrency) instead.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 exchanges returned (rounded up), plus 1 credit per
    `convert` / `convert_id` option beyond the first.
    **CMC equivalent page:**
    [coinmarketcap.com/charts/liquidations/](https://coinmarketcap.com/charts/liquidations/)

    Args:
        exchange_id (str | Unset):  Example: 270,294.
        exchange_slug (str | Unset):  Example: binance,bybit.
        skip_invalid (bool | Unset):  Default: False.
        sort (GetV5DerivativesLiquidationsExchangeListLatestSort | Unset):  Default:
            'total_liquidations_24h'.
        sort_dir (GetV5DerivativesLiquidationsExchangeListLatestSortDir | Unset):  Default:
            'desc'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):  Default: 'USD'. Example: USD.
        convert_id (str | Unset):  Default: '2781'. Example: 2781.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | LiquidationsByExchangeResponseModel]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        exchange_slug=exchange_slug,
        skip_invalid=skip_invalid,
        sort=sort,
        sort_dir=sort_dir,
        start=start,
        limit=limit,
        convert=convert,
        convert_id=convert_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    exchange_id: str | Unset = UNSET,
    exchange_slug: str | Unset = UNSET,
    skip_invalid: bool | Unset = False,
    sort: GetV5DerivativesLiquidationsExchangeListLatestSort | Unset = "total_liquidations_24h",
    sort_dir: GetV5DerivativesLiquidationsExchangeListLatestSortDir | Unset = "desc",
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = "USD",
    convert_id: str | Unset = "2781",
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | LiquidationsByExchangeResponseModel
    | None
):
    """Latest Liquidations by Exchange

     Returns a paginated, sorted list of the derivatives exchanges that CoinMarketCap tracks, each with
    its perpetual and futures liquidation values over rolling 1-hour, 4-hour, and 24-hour windows. This
    is the per-exchange leaderboard shown on the [CoinMarketCap liquidations
    chart](https://coinmarketcap.com/charts/liquidations/). When you call it without any filters, it
    returns every tracked exchange sorted by `total_liquidations_24h` in descending order.

    Only exchanges that have an integrated liquidation feed are included in the results, and an exchange
    that is otherwise valid but has recorded no liquidations across any of the tracked windows is left
    out of the list entirely. Because of this, a request whose filter matches only such exchanges still
    succeeds: it returns an empty list with `total_size` set to `0` rather than failing with an error.

    This endpoint covers exchanges only. To see the same liquidation values aggregated per
    cryptocurrency, use [/v5/derivatives/liquidations/cryptocurrency/list/latest](/pro-api-
    reference/derivatives#latest-liquidations-by-cryptocurrency) instead.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 exchanges returned (rounded up), plus 1 credit per
    `convert` / `convert_id` option beyond the first.
    **CMC equivalent page:**
    [coinmarketcap.com/charts/liquidations/](https://coinmarketcap.com/charts/liquidations/)

    Args:
        exchange_id (str | Unset):  Example: 270,294.
        exchange_slug (str | Unset):  Example: binance,bybit.
        skip_invalid (bool | Unset):  Default: False.
        sort (GetV5DerivativesLiquidationsExchangeListLatestSort | Unset):  Default:
            'total_liquidations_24h'.
        sort_dir (GetV5DerivativesLiquidationsExchangeListLatestSortDir | Unset):  Default:
            'desc'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):  Default: 'USD'. Example: USD.
        convert_id (str | Unset):  Default: '2781'. Example: 2781.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | LiquidationsByExchangeResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            exchange_id=exchange_id,
            exchange_slug=exchange_slug,
            skip_invalid=skip_invalid,
            sort=sort,
            sort_dir=sort_dir,
            start=start,
            limit=limit,
            convert=convert,
            convert_id=convert_id,
        )
    ).parsed
