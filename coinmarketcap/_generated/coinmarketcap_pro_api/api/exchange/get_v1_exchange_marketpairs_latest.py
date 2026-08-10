from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exchange_market_pairs_latest_response_model import ExchangeMarketPairsLatestResponseModel
from ...models.get_v1_exchange_marketpairs_latest_category import (
    GetV1ExchangeMarketpairsLatestCategory,
)
from ...models.get_v1_exchange_marketpairs_latest_fee_type import (
    GetV1ExchangeMarketpairsLatestFeeType,
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
    start: int | Unset = 1,
    limit: int | Unset = 100,
    aux: str | Unset = "num_market_pairs,category,fee_type",
    matched_id: str | Unset = UNSET,
    matched_symbol: str | Unset = UNSET,
    category: GetV1ExchangeMarketpairsLatestCategory | Unset = "all",
    fee_type: GetV1ExchangeMarketpairsLatestFeeType | Unset = "all",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["slug"] = slug

    params["start"] = start

    params["limit"] = limit

    params["aux"] = aux

    params["matched_id"] = matched_id

    params["matched_symbol"] = matched_symbol

    json_category: str | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = category

    params["category"] = json_category

    json_fee_type: str | Unset = UNSET
    if not isinstance(fee_type, Unset):
        json_fee_type = fee_type

    params["fee_type"] = json_fee_type

    params["convert"] = convert

    params["convert_id"] = convert_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/exchange/market-pairs/latest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ExchangeMarketPairsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = ExchangeMarketPairsLatestResponseModel.from_dict(response.json())

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
    ExchangeMarketPairsLatestResponseModel
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
    start: int | Unset = 1,
    limit: int | Unset = 100,
    aux: str | Unset = "num_market_pairs,category,fee_type",
    matched_id: str | Unset = UNSET,
    matched_symbol: str | Unset = UNSET,
    category: GetV1ExchangeMarketpairsLatestCategory | Unset = "all",
    fee_type: GetV1ExchangeMarketpairsLatestFeeType | Unset = "all",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> Response[
    ExchangeMarketPairsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Market Pairs Latest

     Returns all active market pairs that CoinMarketCap tracks for a given exchange. The latest price and
    volume information is returned for each market. Use the \"convert\" option to return market values
    in multiple fiat and cryptocurrency conversions in the same call.'

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - ~~Startup~~
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 market pairs returned (rounded up) and 1 call credit per
    `convert` option beyond the first.
    **CMC equivalent pages:** Our exchange level active markets pages like
    [coinmarketcap.com/exchanges/binance/](https://coinmarketcap.com/exchanges/binance/).

    Args:
        id (str | Unset):
        slug (str | Unset):
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        aux (str | Unset):  Default: 'num_market_pairs,category,fee_type'.
        matched_id (str | Unset):
        matched_symbol (str | Unset):
        category (GetV1ExchangeMarketpairsLatestCategory | Unset):  Default: 'all'.
        fee_type (GetV1ExchangeMarketpairsLatestFeeType | Unset):  Default: 'all'.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeMarketPairsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        start=start,
        limit=limit,
        aux=aux,
        matched_id=matched_id,
        matched_symbol=matched_symbol,
        category=category,
        fee_type=fee_type,
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
    start: int | Unset = 1,
    limit: int | Unset = 100,
    aux: str | Unset = "num_market_pairs,category,fee_type",
    matched_id: str | Unset = UNSET,
    matched_symbol: str | Unset = UNSET,
    category: GetV1ExchangeMarketpairsLatestCategory | Unset = "all",
    fee_type: GetV1ExchangeMarketpairsLatestFeeType | Unset = "all",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> (
    ExchangeMarketPairsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Market Pairs Latest

     Returns all active market pairs that CoinMarketCap tracks for a given exchange. The latest price and
    volume information is returned for each market. Use the \"convert\" option to return market values
    in multiple fiat and cryptocurrency conversions in the same call.'

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - ~~Startup~~
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 market pairs returned (rounded up) and 1 call credit per
    `convert` option beyond the first.
    **CMC equivalent pages:** Our exchange level active markets pages like
    [coinmarketcap.com/exchanges/binance/](https://coinmarketcap.com/exchanges/binance/).

    Args:
        id (str | Unset):
        slug (str | Unset):
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        aux (str | Unset):  Default: 'num_market_pairs,category,fee_type'.
        matched_id (str | Unset):
        matched_symbol (str | Unset):
        category (GetV1ExchangeMarketpairsLatestCategory | Unset):  Default: 'all'.
        fee_type (GetV1ExchangeMarketpairsLatestFeeType | Unset):  Default: 'all'.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeMarketPairsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        id=id,
        slug=slug,
        start=start,
        limit=limit,
        aux=aux,
        matched_id=matched_id,
        matched_symbol=matched_symbol,
        category=category,
        fee_type=fee_type,
        convert=convert,
        convert_id=convert_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    aux: str | Unset = "num_market_pairs,category,fee_type",
    matched_id: str | Unset = UNSET,
    matched_symbol: str | Unset = UNSET,
    category: GetV1ExchangeMarketpairsLatestCategory | Unset = "all",
    fee_type: GetV1ExchangeMarketpairsLatestFeeType | Unset = "all",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> Response[
    ExchangeMarketPairsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Market Pairs Latest

     Returns all active market pairs that CoinMarketCap tracks for a given exchange. The latest price and
    volume information is returned for each market. Use the \"convert\" option to return market values
    in multiple fiat and cryptocurrency conversions in the same call.'

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - ~~Startup~~
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 market pairs returned (rounded up) and 1 call credit per
    `convert` option beyond the first.
    **CMC equivalent pages:** Our exchange level active markets pages like
    [coinmarketcap.com/exchanges/binance/](https://coinmarketcap.com/exchanges/binance/).

    Args:
        id (str | Unset):
        slug (str | Unset):
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        aux (str | Unset):  Default: 'num_market_pairs,category,fee_type'.
        matched_id (str | Unset):
        matched_symbol (str | Unset):
        category (GetV1ExchangeMarketpairsLatestCategory | Unset):  Default: 'all'.
        fee_type (GetV1ExchangeMarketpairsLatestFeeType | Unset):  Default: 'all'.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeMarketPairsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        start=start,
        limit=limit,
        aux=aux,
        matched_id=matched_id,
        matched_symbol=matched_symbol,
        category=category,
        fee_type=fee_type,
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
    start: int | Unset = 1,
    limit: int | Unset = 100,
    aux: str | Unset = "num_market_pairs,category,fee_type",
    matched_id: str | Unset = UNSET,
    matched_symbol: str | Unset = UNSET,
    category: GetV1ExchangeMarketpairsLatestCategory | Unset = "all",
    fee_type: GetV1ExchangeMarketpairsLatestFeeType | Unset = "all",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> (
    ExchangeMarketPairsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Market Pairs Latest

     Returns all active market pairs that CoinMarketCap tracks for a given exchange. The latest price and
    volume information is returned for each market. Use the \"convert\" option to return market values
    in multiple fiat and cryptocurrency conversions in the same call.'

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - ~~Startup~~
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 market pairs returned (rounded up) and 1 call credit per
    `convert` option beyond the first.
    **CMC equivalent pages:** Our exchange level active markets pages like
    [coinmarketcap.com/exchanges/binance/](https://coinmarketcap.com/exchanges/binance/).

    Args:
        id (str | Unset):
        slug (str | Unset):
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        aux (str | Unset):  Default: 'num_market_pairs,category,fee_type'.
        matched_id (str | Unset):
        matched_symbol (str | Unset):
        category (GetV1ExchangeMarketpairsLatestCategory | Unset):  Default: 'all'.
        fee_type (GetV1ExchangeMarketpairsLatestFeeType | Unset):  Default: 'all'.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeMarketPairsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            slug=slug,
            start=start,
            limit=limit,
            aux=aux,
            matched_id=matched_id,
            matched_symbol=matched_symbol,
            category=category,
            fee_type=fee_type,
            convert=convert,
            convert_id=convert_id,
        )
    ).parsed
