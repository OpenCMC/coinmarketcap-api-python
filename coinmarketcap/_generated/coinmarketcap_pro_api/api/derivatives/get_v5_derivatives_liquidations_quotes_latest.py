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
from ...models.liquidations_total_response_model import LiquidationsTotalResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    convert: str | Unset = "USD",
    convert_id: str | Unset = "2781",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["convert"] = convert

    params["convert_id"] = convert_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v5/derivatives/liquidations/quotes/latest",
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
    | LiquidationsTotalResponseModel
    | None
):
    if response.status_code == 200:
        response_200 = LiquidationsTotalResponseModel.from_dict(response.json())

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
    | LiquidationsTotalResponseModel
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
    convert: str | Unset = "USD",
    convert_id: str | Unset = "2781",
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | LiquidationsTotalResponseModel
]:
    """Latest Total Liquidations

     Returns aggregate perpetual and futures liquidation values across every exchange that CoinMarketCap
    tracks, summed over rolling 1-hour, 4-hour, and 24-hour windows. These are the global headline
    figures shown on the [CoinMarketCap liquidations
    chart](https://coinmarketcap.com/charts/liquidations/).

    Each window is reported three ways, and every value is denominated in the convert currency:

    - `long_liquidations_*` is the total value of long positions that were force-closed, meaning traders
    who were betting on a price increase had their positions liquidated through forced market sells.
    - `short_liquidations_*` is the total value of short positions that were force-closed, meaning
    traders who were betting on a price decrease had their positions liquidated through forced market
    buys.
    - `total_liquidations_*` is the combined value of the long and short liquidations in that same
    window.

    All three windows are rolling and end at the moment your request is made, rather than aligning to
    fixed calendar boundaries. This endpoint returns the global totals only. If you need the same
    figures broken down per exchange or per cryptocurrency, use
    [/v5/derivatives/liquidations/exchange/list/latest](/pro-api-reference/derivatives#latest-
    liquidations-by-exchange) or [/v5/derivatives/liquidations/cryptocurrency/list/latest](/pro-api-
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
    **Plan credit use:** 1 call credit per request, plus 1 credit per `convert` / `convert_id` option
    beyond the first.
    **CMC equivalent page:**
    [coinmarketcap.com/charts/liquidations/](https://coinmarketcap.com/charts/liquidations/)

    Args:
        convert (str | Unset):  Default: 'USD'. Example: USD.
        convert_id (str | Unset):  Default: '2781'. Example: 2781.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | LiquidationsTotalResponseModel]
    """

    kwargs = _get_kwargs(
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
    convert: str | Unset = "USD",
    convert_id: str | Unset = "2781",
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | LiquidationsTotalResponseModel
    | None
):
    """Latest Total Liquidations

     Returns aggregate perpetual and futures liquidation values across every exchange that CoinMarketCap
    tracks, summed over rolling 1-hour, 4-hour, and 24-hour windows. These are the global headline
    figures shown on the [CoinMarketCap liquidations
    chart](https://coinmarketcap.com/charts/liquidations/).

    Each window is reported three ways, and every value is denominated in the convert currency:

    - `long_liquidations_*` is the total value of long positions that were force-closed, meaning traders
    who were betting on a price increase had their positions liquidated through forced market sells.
    - `short_liquidations_*` is the total value of short positions that were force-closed, meaning
    traders who were betting on a price decrease had their positions liquidated through forced market
    buys.
    - `total_liquidations_*` is the combined value of the long and short liquidations in that same
    window.

    All three windows are rolling and end at the moment your request is made, rather than aligning to
    fixed calendar boundaries. This endpoint returns the global totals only. If you need the same
    figures broken down per exchange or per cryptocurrency, use
    [/v5/derivatives/liquidations/exchange/list/latest](/pro-api-reference/derivatives#latest-
    liquidations-by-exchange) or [/v5/derivatives/liquidations/cryptocurrency/list/latest](/pro-api-
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
    **Plan credit use:** 1 call credit per request, plus 1 credit per `convert` / `convert_id` option
    beyond the first.
    **CMC equivalent page:**
    [coinmarketcap.com/charts/liquidations/](https://coinmarketcap.com/charts/liquidations/)

    Args:
        convert (str | Unset):  Default: 'USD'. Example: USD.
        convert_id (str | Unset):  Default: '2781'. Example: 2781.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | LiquidationsTotalResponseModel
    """

    return sync_detailed(
        client=client,
        convert=convert,
        convert_id=convert_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    convert: str | Unset = "USD",
    convert_id: str | Unset = "2781",
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | LiquidationsTotalResponseModel
]:
    """Latest Total Liquidations

     Returns aggregate perpetual and futures liquidation values across every exchange that CoinMarketCap
    tracks, summed over rolling 1-hour, 4-hour, and 24-hour windows. These are the global headline
    figures shown on the [CoinMarketCap liquidations
    chart](https://coinmarketcap.com/charts/liquidations/).

    Each window is reported three ways, and every value is denominated in the convert currency:

    - `long_liquidations_*` is the total value of long positions that were force-closed, meaning traders
    who were betting on a price increase had their positions liquidated through forced market sells.
    - `short_liquidations_*` is the total value of short positions that were force-closed, meaning
    traders who were betting on a price decrease had their positions liquidated through forced market
    buys.
    - `total_liquidations_*` is the combined value of the long and short liquidations in that same
    window.

    All three windows are rolling and end at the moment your request is made, rather than aligning to
    fixed calendar boundaries. This endpoint returns the global totals only. If you need the same
    figures broken down per exchange or per cryptocurrency, use
    [/v5/derivatives/liquidations/exchange/list/latest](/pro-api-reference/derivatives#latest-
    liquidations-by-exchange) or [/v5/derivatives/liquidations/cryptocurrency/list/latest](/pro-api-
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
    **Plan credit use:** 1 call credit per request, plus 1 credit per `convert` / `convert_id` option
    beyond the first.
    **CMC equivalent page:**
    [coinmarketcap.com/charts/liquidations/](https://coinmarketcap.com/charts/liquidations/)

    Args:
        convert (str | Unset):  Default: 'USD'. Example: USD.
        convert_id (str | Unset):  Default: '2781'. Example: 2781.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | LiquidationsTotalResponseModel]
    """

    kwargs = _get_kwargs(
        convert=convert,
        convert_id=convert_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    convert: str | Unset = "USD",
    convert_id: str | Unset = "2781",
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | LiquidationsTotalResponseModel
    | None
):
    """Latest Total Liquidations

     Returns aggregate perpetual and futures liquidation values across every exchange that CoinMarketCap
    tracks, summed over rolling 1-hour, 4-hour, and 24-hour windows. These are the global headline
    figures shown on the [CoinMarketCap liquidations
    chart](https://coinmarketcap.com/charts/liquidations/).

    Each window is reported three ways, and every value is denominated in the convert currency:

    - `long_liquidations_*` is the total value of long positions that were force-closed, meaning traders
    who were betting on a price increase had their positions liquidated through forced market sells.
    - `short_liquidations_*` is the total value of short positions that were force-closed, meaning
    traders who were betting on a price decrease had their positions liquidated through forced market
    buys.
    - `total_liquidations_*` is the combined value of the long and short liquidations in that same
    window.

    All three windows are rolling and end at the moment your request is made, rather than aligning to
    fixed calendar boundaries. This endpoint returns the global totals only. If you need the same
    figures broken down per exchange or per cryptocurrency, use
    [/v5/derivatives/liquidations/exchange/list/latest](/pro-api-reference/derivatives#latest-
    liquidations-by-exchange) or [/v5/derivatives/liquidations/cryptocurrency/list/latest](/pro-api-
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
    **Plan credit use:** 1 call credit per request, plus 1 credit per `convert` / `convert_id` option
    beyond the first.
    **CMC equivalent page:**
    [coinmarketcap.com/charts/liquidations/](https://coinmarketcap.com/charts/liquidations/)

    Args:
        convert (str | Unset):  Default: 'USD'. Example: USD.
        convert_id (str | Unset):  Default: '2781'. Example: 2781.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | LiquidationsTotalResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            convert=convert,
            convert_id=convert_id,
        )
    ).parsed
