from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.v1k_line_candles_response_model import V1KLineCandlesResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    unit: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    pm: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["platform"] = platform

    params["address"] = address

    params["interval"] = interval

    params["from"] = from_

    params["to"] = to

    params["unit"] = unit

    params["limit"] = limit

    params["pm"] = pm

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/k-line/candles",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> V1KLineCandlesResponseModel | None:
    if response.status_code == 200:
        response_200 = V1KLineCandlesResponseModel.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V1KLineCandlesResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    unit: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    pm: str | Unset = UNSET,
) -> Response[V1KLineCandlesResponseModel]:
    r"""Get K-line candles

     Get K-line candle (OHLCV) data for a token.

    Response Format: Each candle is an array with 7 elements:
    - **[0]** open: Opening price
    - **[1]** high: Highest price
    - **[2]** low: Lowest price
    - **[3]** close: Closing price
    - **[4]** volume: Trading volume
    - **[5]** timestamp: UNIX timestamp (seconds)
    - **[6]** traders: Number of unique traders

    Example: ``[[1.23, 1.45, 1.20, 1.40, 50000, 1705363200, 128], ...]``

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/k-line/candles`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):
        interval (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        unit (str | Unset):
        limit (int | Unset):
        pm (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V1KLineCandlesResponseModel]
    """

    kwargs = _get_kwargs(
        platform=platform,
        address=address,
        interval=interval,
        from_=from_,
        to=to,
        unit=unit,
        limit=limit,
        pm=pm,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    unit: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    pm: str | Unset = UNSET,
) -> V1KLineCandlesResponseModel | None:
    r"""Get K-line candles

     Get K-line candle (OHLCV) data for a token.

    Response Format: Each candle is an array with 7 elements:
    - **[0]** open: Opening price
    - **[1]** high: Highest price
    - **[2]** low: Lowest price
    - **[3]** close: Closing price
    - **[4]** volume: Trading volume
    - **[5]** timestamp: UNIX timestamp (seconds)
    - **[6]** traders: Number of unique traders

    Example: ``[[1.23, 1.45, 1.20, 1.40, 50000, 1705363200, 128], ...]``

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/k-line/candles`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):
        interval (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        unit (str | Unset):
        limit (int | Unset):
        pm (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V1KLineCandlesResponseModel
    """

    return sync_detailed(
        client=client,
        platform=platform,
        address=address,
        interval=interval,
        from_=from_,
        to=to,
        unit=unit,
        limit=limit,
        pm=pm,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    unit: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    pm: str | Unset = UNSET,
) -> Response[V1KLineCandlesResponseModel]:
    r"""Get K-line candles

     Get K-line candle (OHLCV) data for a token.

    Response Format: Each candle is an array with 7 elements:
    - **[0]** open: Opening price
    - **[1]** high: Highest price
    - **[2]** low: Lowest price
    - **[3]** close: Closing price
    - **[4]** volume: Trading volume
    - **[5]** timestamp: UNIX timestamp (seconds)
    - **[6]** traders: Number of unique traders

    Example: ``[[1.23, 1.45, 1.20, 1.40, 50000, 1705363200, 128], ...]``

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/k-line/candles`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):
        interval (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        unit (str | Unset):
        limit (int | Unset):
        pm (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V1KLineCandlesResponseModel]
    """

    kwargs = _get_kwargs(
        platform=platform,
        address=address,
        interval=interval,
        from_=from_,
        to=to,
        unit=unit,
        limit=limit,
        pm=pm,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    platform: str | Unset = UNSET,
    address: str | Unset = UNSET,
    interval: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    unit: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    pm: str | Unset = UNSET,
) -> V1KLineCandlesResponseModel | None:
    r"""Get K-line candles

     Get K-line candle (OHLCV) data for a token.

    Response Format: Each candle is an array with 7 elements:
    - **[0]** open: Opening price
    - **[1]** high: Highest price
    - **[2]** low: Lowest price
    - **[3]** close: Closing price
    - **[4]** volume: Trading volume
    - **[5]** timestamp: UNIX timestamp (seconds)
    - **[6]** traders: Number of unique traders

    Example: ``[[1.23, 1.45, 1.20, 1.40, 50000, 1705363200, 128], ...]``

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/k-line/candles`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        platform (str | Unset):
        address (str | Unset):
        interval (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        unit (str | Unset):
        limit (int | Unset):
        pm (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V1KLineCandlesResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            platform=platform,
            address=address,
            interval=interval,
            from_=from_,
            to=to,
            unit=unit,
            limit=limit,
            pm=pm,
        )
    ).parsed
