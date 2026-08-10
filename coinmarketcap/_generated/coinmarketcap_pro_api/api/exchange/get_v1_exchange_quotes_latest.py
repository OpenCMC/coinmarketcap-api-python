from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exchange_quotes_latest_response_model import ExchangeQuotesLatestResponseModel
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
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    aux: str | Unset = "num_market_pairs,traffic_score,rank,exchange_score,liquidity_score,effective_liquidity_24h",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["slug"] = slug

    params["convert"] = convert

    params["convert_id"] = convert_id

    params["aux"] = aux

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/exchange/quotes/latest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ExchangeQuotesLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = ExchangeQuotesLatestResponseModel.from_dict(response.json())

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
    ExchangeQuotesLatestResponseModel
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
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    aux: str | Unset = "num_market_pairs,traffic_score,rank,exchange_score,liquidity_score,effective_liquidity_24h",
) -> Response[
    ExchangeQuotesLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Quotes Latest

     Returns the latest aggregate market data for 1 or more exchanges. Use the \"convert\" option to
    return market values in multiple fiat and cryptocurrency conversions in the same call.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - ~~Basic~~
    - ~~Builder~~
    - ~~Startup~~
    - Growth
    - Professional
    - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 exchanges returned (rounded up) and 1 call credit per
    `convert` option beyond the first.
    **CMC equivalent pages:** Latest market data summary for specific exchanges like
    [coinmarketcap.com/rankings/exchanges/](https://coinmarketcap.com/rankings/exchanges/).

    ***NOTE:** “exchange_score\" will be deprecated on 4 November 2024.*

    *After this date, the \"exchange_score\" field return null from these endpoints. We encourage users
    to review and update their implementations accordingly to avoid any disruptions.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        aux (str | Unset):  Default: 'num_market_pairs,traffic_score,rank,exchange_score,liquidity
            _score,effective_liquidity_24h'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeQuotesLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        convert=convert,
        convert_id=convert_id,
        aux=aux,
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
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    aux: str | Unset = "num_market_pairs,traffic_score,rank,exchange_score,liquidity_score,effective_liquidity_24h",
) -> (
    ExchangeQuotesLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Quotes Latest

     Returns the latest aggregate market data for 1 or more exchanges. Use the \"convert\" option to
    return market values in multiple fiat and cryptocurrency conversions in the same call.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - ~~Basic~~
    - ~~Builder~~
    - ~~Startup~~
    - Growth
    - Professional
    - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 exchanges returned (rounded up) and 1 call credit per
    `convert` option beyond the first.
    **CMC equivalent pages:** Latest market data summary for specific exchanges like
    [coinmarketcap.com/rankings/exchanges/](https://coinmarketcap.com/rankings/exchanges/).

    ***NOTE:** “exchange_score\" will be deprecated on 4 November 2024.*

    *After this date, the \"exchange_score\" field return null from these endpoints. We encourage users
    to review and update their implementations accordingly to avoid any disruptions.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        aux (str | Unset):  Default: 'num_market_pairs,traffic_score,rank,exchange_score,liquidity
            _score,effective_liquidity_24h'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeQuotesLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        id=id,
        slug=slug,
        convert=convert,
        convert_id=convert_id,
        aux=aux,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    aux: str | Unset = "num_market_pairs,traffic_score,rank,exchange_score,liquidity_score,effective_liquidity_24h",
) -> Response[
    ExchangeQuotesLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Quotes Latest

     Returns the latest aggregate market data for 1 or more exchanges. Use the \"convert\" option to
    return market values in multiple fiat and cryptocurrency conversions in the same call.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - ~~Basic~~
    - ~~Builder~~
    - ~~Startup~~
    - Growth
    - Professional
    - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 exchanges returned (rounded up) and 1 call credit per
    `convert` option beyond the first.
    **CMC equivalent pages:** Latest market data summary for specific exchanges like
    [coinmarketcap.com/rankings/exchanges/](https://coinmarketcap.com/rankings/exchanges/).

    ***NOTE:** “exchange_score\" will be deprecated on 4 November 2024.*

    *After this date, the \"exchange_score\" field return null from these endpoints. We encourage users
    to review and update their implementations accordingly to avoid any disruptions.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        aux (str | Unset):  Default: 'num_market_pairs,traffic_score,rank,exchange_score,liquidity
            _score,effective_liquidity_24h'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeQuotesLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        convert=convert,
        convert_id=convert_id,
        aux=aux,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    aux: str | Unset = "num_market_pairs,traffic_score,rank,exchange_score,liquidity_score,effective_liquidity_24h",
) -> (
    ExchangeQuotesLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Quotes Latest

     Returns the latest aggregate market data for 1 or more exchanges. Use the \"convert\" option to
    return market values in multiple fiat and cryptocurrency conversions in the same call.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - ~~Basic~~
    - ~~Builder~~
    - ~~Startup~~
    - Growth
    - Professional
    - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 exchanges returned (rounded up) and 1 call credit per
    `convert` option beyond the first.
    **CMC equivalent pages:** Latest market data summary for specific exchanges like
    [coinmarketcap.com/rankings/exchanges/](https://coinmarketcap.com/rankings/exchanges/).

    ***NOTE:** “exchange_score\" will be deprecated on 4 November 2024.*

    *After this date, the \"exchange_score\" field return null from these endpoints. We encourage users
    to review and update their implementations accordingly to avoid any disruptions.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        aux (str | Unset):  Default: 'num_market_pairs,traffic_score,rank,exchange_score,liquidity
            _score,effective_liquidity_24h'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeQuotesLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            slug=slug,
            convert=convert,
            convert_id=convert_id,
            aux=aux,
        )
    ).parsed
