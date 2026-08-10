from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exchange_listings_latest_response_model import ExchangeListingsLatestResponseModel
from ...models.get_v1_exchange_listings_latest_category import (
    GetV1ExchangeListingsLatestCategory,
)
from ...models.get_v1_exchange_listings_latest_market_type import (
    GetV1ExchangeListingsLatestMarketType,
)
from ...models.get_v1_exchange_listings_latest_sort import (
    GetV1ExchangeListingsLatestSort,
)
from ...models.get_v1_exchange_listings_latest_sort_dir import (
    GetV1ExchangeListingsLatestSortDir,
)
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    sort: GetV1ExchangeListingsLatestSort | Unset = "volume_24h",
    sort_dir: GetV1ExchangeListingsLatestSortDir | Unset = UNSET,
    market_type: GetV1ExchangeListingsLatestMarketType | Unset = "all",
    category: GetV1ExchangeListingsLatestCategory | Unset = "all",
    aux: str | Unset = "num_market_pairs,traffic_score,rank,exchange_score,effective_liquidity_24h",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["start"] = start

    params["limit"] = limit

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_sort_dir: str | Unset = UNSET
    if not isinstance(sort_dir, Unset):
        json_sort_dir = sort_dir

    params["sort_dir"] = json_sort_dir

    json_market_type: str | Unset = UNSET
    if not isinstance(market_type, Unset):
        json_market_type = market_type

    params["market_type"] = json_market_type

    json_category: str | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = category

    params["category"] = json_category

    params["aux"] = aux

    params["convert"] = convert

    params["convert_id"] = convert_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/exchange/listings/latest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ExchangeListingsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = ExchangeListingsLatestResponseModel.from_dict(response.json())

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
    ExchangeListingsLatestResponseModel
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
    start: int | Unset = 1,
    limit: int | Unset = 100,
    sort: GetV1ExchangeListingsLatestSort | Unset = "volume_24h",
    sort_dir: GetV1ExchangeListingsLatestSortDir | Unset = UNSET,
    market_type: GetV1ExchangeListingsLatestMarketType | Unset = "all",
    category: GetV1ExchangeListingsLatestCategory | Unset = "all",
    aux: str | Unset = "num_market_pairs,traffic_score,rank,exchange_score,effective_liquidity_24h",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> Response[
    ExchangeListingsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Listings Latest

     Returns a paginated list of all cryptocurrency exchanges including the latest aggregate market data
    for each exchange. Use the \"convert\" option to return market values in multiple fiat and
    cryptocurrency conversions in the same call.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - ~~Startup~~
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 1 minute.
    **Plan credit use:** 1 call credit per 100 exchanges returned (rounded up) and 1 call credit per
    `convert` option beyond the first.
    **CMC equivalent pages:** Our latest exchange listing and ranking pages like
    [coinmarketcap.com/rankings/exchanges/](https://coinmarketcap.com/rankings/exchanges/).

    ***NOTE:** Use this endpoint if you need a sorted and paginated list of exchanges. If you want to
    query for market data on a few specific exchanges use /v1/exchange/quotes/latest which is optimized
    for that purpose. The response data between these endpoints is otherwise the same.*

    *“exchange_score\" will be deprecated on 4 November 2024.*

    *After this date, the \"exchange_score\" field return null from these endpoints. We encourage users
    to review and update their implementations accordingly to avoid any disruptions.*

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        sort (GetV1ExchangeListingsLatestSort | Unset):  Default: 'volume_24h'.
        sort_dir (GetV1ExchangeListingsLatestSortDir | Unset):
        market_type (GetV1ExchangeListingsLatestMarketType | Unset):  Default: 'all'.
        category (GetV1ExchangeListingsLatestCategory | Unset):  Default: 'all'.
        aux (str | Unset):  Default:
            'num_market_pairs,traffic_score,rank,exchange_score,effective_liquidity_24h'.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeListingsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
        sort=sort,
        sort_dir=sort_dir,
        market_type=market_type,
        category=category,
        aux=aux,
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
    start: int | Unset = 1,
    limit: int | Unset = 100,
    sort: GetV1ExchangeListingsLatestSort | Unset = "volume_24h",
    sort_dir: GetV1ExchangeListingsLatestSortDir | Unset = UNSET,
    market_type: GetV1ExchangeListingsLatestMarketType | Unset = "all",
    category: GetV1ExchangeListingsLatestCategory | Unset = "all",
    aux: str | Unset = "num_market_pairs,traffic_score,rank,exchange_score,effective_liquidity_24h",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> (
    ExchangeListingsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Listings Latest

     Returns a paginated list of all cryptocurrency exchanges including the latest aggregate market data
    for each exchange. Use the \"convert\" option to return market values in multiple fiat and
    cryptocurrency conversions in the same call.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - ~~Startup~~
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 1 minute.
    **Plan credit use:** 1 call credit per 100 exchanges returned (rounded up) and 1 call credit per
    `convert` option beyond the first.
    **CMC equivalent pages:** Our latest exchange listing and ranking pages like
    [coinmarketcap.com/rankings/exchanges/](https://coinmarketcap.com/rankings/exchanges/).

    ***NOTE:** Use this endpoint if you need a sorted and paginated list of exchanges. If you want to
    query for market data on a few specific exchanges use /v1/exchange/quotes/latest which is optimized
    for that purpose. The response data between these endpoints is otherwise the same.*

    *“exchange_score\" will be deprecated on 4 November 2024.*

    *After this date, the \"exchange_score\" field return null from these endpoints. We encourage users
    to review and update their implementations accordingly to avoid any disruptions.*

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        sort (GetV1ExchangeListingsLatestSort | Unset):  Default: 'volume_24h'.
        sort_dir (GetV1ExchangeListingsLatestSortDir | Unset):
        market_type (GetV1ExchangeListingsLatestMarketType | Unset):  Default: 'all'.
        category (GetV1ExchangeListingsLatestCategory | Unset):  Default: 'all'.
        aux (str | Unset):  Default:
            'num_market_pairs,traffic_score,rank,exchange_score,effective_liquidity_24h'.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeListingsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        start=start,
        limit=limit,
        sort=sort,
        sort_dir=sort_dir,
        market_type=market_type,
        category=category,
        aux=aux,
        convert=convert,
        convert_id=convert_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    sort: GetV1ExchangeListingsLatestSort | Unset = "volume_24h",
    sort_dir: GetV1ExchangeListingsLatestSortDir | Unset = UNSET,
    market_type: GetV1ExchangeListingsLatestMarketType | Unset = "all",
    category: GetV1ExchangeListingsLatestCategory | Unset = "all",
    aux: str | Unset = "num_market_pairs,traffic_score,rank,exchange_score,effective_liquidity_24h",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> Response[
    ExchangeListingsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Listings Latest

     Returns a paginated list of all cryptocurrency exchanges including the latest aggregate market data
    for each exchange. Use the \"convert\" option to return market values in multiple fiat and
    cryptocurrency conversions in the same call.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - ~~Startup~~
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 1 minute.
    **Plan credit use:** 1 call credit per 100 exchanges returned (rounded up) and 1 call credit per
    `convert` option beyond the first.
    **CMC equivalent pages:** Our latest exchange listing and ranking pages like
    [coinmarketcap.com/rankings/exchanges/](https://coinmarketcap.com/rankings/exchanges/).

    ***NOTE:** Use this endpoint if you need a sorted and paginated list of exchanges. If you want to
    query for market data on a few specific exchanges use /v1/exchange/quotes/latest which is optimized
    for that purpose. The response data between these endpoints is otherwise the same.*

    *“exchange_score\" will be deprecated on 4 November 2024.*

    *After this date, the \"exchange_score\" field return null from these endpoints. We encourage users
    to review and update their implementations accordingly to avoid any disruptions.*

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        sort (GetV1ExchangeListingsLatestSort | Unset):  Default: 'volume_24h'.
        sort_dir (GetV1ExchangeListingsLatestSortDir | Unset):
        market_type (GetV1ExchangeListingsLatestMarketType | Unset):  Default: 'all'.
        category (GetV1ExchangeListingsLatestCategory | Unset):  Default: 'all'.
        aux (str | Unset):  Default:
            'num_market_pairs,traffic_score,rank,exchange_score,effective_liquidity_24h'.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeListingsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
        sort=sort,
        sort_dir=sort_dir,
        market_type=market_type,
        category=category,
        aux=aux,
        convert=convert,
        convert_id=convert_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    sort: GetV1ExchangeListingsLatestSort | Unset = "volume_24h",
    sort_dir: GetV1ExchangeListingsLatestSortDir | Unset = UNSET,
    market_type: GetV1ExchangeListingsLatestMarketType | Unset = "all",
    category: GetV1ExchangeListingsLatestCategory | Unset = "all",
    aux: str | Unset = "num_market_pairs,traffic_score,rank,exchange_score,effective_liquidity_24h",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> (
    ExchangeListingsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Listings Latest

     Returns a paginated list of all cryptocurrency exchanges including the latest aggregate market data
    for each exchange. Use the \"convert\" option to return market values in multiple fiat and
    cryptocurrency conversions in the same call.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - ~~Startup~~
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 1 minute.
    **Plan credit use:** 1 call credit per 100 exchanges returned (rounded up) and 1 call credit per
    `convert` option beyond the first.
    **CMC equivalent pages:** Our latest exchange listing and ranking pages like
    [coinmarketcap.com/rankings/exchanges/](https://coinmarketcap.com/rankings/exchanges/).

    ***NOTE:** Use this endpoint if you need a sorted and paginated list of exchanges. If you want to
    query for market data on a few specific exchanges use /v1/exchange/quotes/latest which is optimized
    for that purpose. The response data between these endpoints is otherwise the same.*

    *“exchange_score\" will be deprecated on 4 November 2024.*

    *After this date, the \"exchange_score\" field return null from these endpoints. We encourage users
    to review and update their implementations accordingly to avoid any disruptions.*

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        sort (GetV1ExchangeListingsLatestSort | Unset):  Default: 'volume_24h'.
        sort_dir (GetV1ExchangeListingsLatestSortDir | Unset):
        market_type (GetV1ExchangeListingsLatestMarketType | Unset):  Default: 'all'.
        category (GetV1ExchangeListingsLatestCategory | Unset):  Default: 'all'.
        aux (str | Unset):  Default:
            'num_market_pairs,traffic_score,rank,exchange_score,effective_liquidity_24h'.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeListingsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            limit=limit,
            sort=sort,
            sort_dir=sort_dir,
            market_type=market_type,
            category=category,
            aux=aux,
            convert=convert,
            convert_id=convert_id,
        )
    ).parsed
