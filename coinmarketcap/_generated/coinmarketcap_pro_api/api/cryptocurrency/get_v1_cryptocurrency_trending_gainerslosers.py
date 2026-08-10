from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cryptocurrency_trending_gainers_losers_response_model import (
    CryptocurrencyTrendingGainersLosersResponseModel,
)
from ...models.get_v1_cryptocurrency_trending_gainerslosers_sort import (
    GetV1CryptocurrencyTrendingGainerslosersSort,
)
from ...models.get_v1_cryptocurrency_trending_gainerslosers_sort_dir import (
    GetV1CryptocurrencyTrendingGainerslosersSortDir,
)
from ...models.get_v1_cryptocurrency_trending_gainerslosers_time_period import (
    GetV1CryptocurrencyTrendingGainerslosersTimePeriod,
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
    time_period: GetV1CryptocurrencyTrendingGainerslosersTimePeriod | Unset = "24h",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: GetV1CryptocurrencyTrendingGainerslosersSort | Unset = "percent_change_24h",
    sort_dir: GetV1CryptocurrencyTrendingGainerslosersSortDir | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["start"] = start

    params["limit"] = limit

    json_time_period: str | Unset = UNSET
    if not isinstance(time_period, Unset):
        json_time_period = time_period

    params["time_period"] = json_time_period

    params["convert"] = convert

    params["convert_id"] = convert_id

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_sort_dir: str | Unset = UNSET
    if not isinstance(sort_dir, Unset):
        json_sort_dir = sort_dir

    params["sort_dir"] = json_sort_dir

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/cryptocurrency/trending/gainers-losers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CryptocurrencyTrendingGainersLosersResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = CryptocurrencyTrendingGainersLosersResponseModel.from_dict(response.json())

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
    CryptocurrencyTrendingGainersLosersResponseModel
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
    time_period: GetV1CryptocurrencyTrendingGainerslosersTimePeriod | Unset = "24h",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: GetV1CryptocurrencyTrendingGainerslosersSort | Unset = "percent_change_24h",
    sort_dir: GetV1CryptocurrencyTrendingGainerslosersSortDir | Unset = UNSET,
) -> Response[
    CryptocurrencyTrendingGainersLosersResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """Trending Gainers & Losers

     Returns a paginated list of all trending cryptocurrencies, determined and sorted by the largest
    price gains or losses.


    You may sort against any of the following:
    **percent_change_24h**: 24 hour trading price percentage change for each currency.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 10 minutes.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our cryptocurrency Gainers & Losers page [coinmarketcap.com/gainers-
    losers/](https://coinmarketcap.com/gainers-losers/).

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        time_period (GetV1CryptocurrencyTrendingGainerslosersTimePeriod | Unset):  Default: '24h'.
        convert (str | Unset):
        convert_id (str | Unset):
        sort (GetV1CryptocurrencyTrendingGainerslosersSort | Unset):  Default:
            'percent_change_24h'.
        sort_dir (GetV1CryptocurrencyTrendingGainerslosersSortDir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyTrendingGainersLosersResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
        time_period=time_period,
        convert=convert,
        convert_id=convert_id,
        sort=sort,
        sort_dir=sort_dir,
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
    time_period: GetV1CryptocurrencyTrendingGainerslosersTimePeriod | Unset = "24h",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: GetV1CryptocurrencyTrendingGainerslosersSort | Unset = "percent_change_24h",
    sort_dir: GetV1CryptocurrencyTrendingGainerslosersSortDir | Unset = UNSET,
) -> (
    CryptocurrencyTrendingGainersLosersResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """Trending Gainers & Losers

     Returns a paginated list of all trending cryptocurrencies, determined and sorted by the largest
    price gains or losses.


    You may sort against any of the following:
    **percent_change_24h**: 24 hour trading price percentage change for each currency.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 10 minutes.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our cryptocurrency Gainers & Losers page [coinmarketcap.com/gainers-
    losers/](https://coinmarketcap.com/gainers-losers/).

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        time_period (GetV1CryptocurrencyTrendingGainerslosersTimePeriod | Unset):  Default: '24h'.
        convert (str | Unset):
        convert_id (str | Unset):
        sort (GetV1CryptocurrencyTrendingGainerslosersSort | Unset):  Default:
            'percent_change_24h'.
        sort_dir (GetV1CryptocurrencyTrendingGainerslosersSortDir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyTrendingGainersLosersResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        start=start,
        limit=limit,
        time_period=time_period,
        convert=convert,
        convert_id=convert_id,
        sort=sort,
        sort_dir=sort_dir,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    time_period: GetV1CryptocurrencyTrendingGainerslosersTimePeriod | Unset = "24h",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: GetV1CryptocurrencyTrendingGainerslosersSort | Unset = "percent_change_24h",
    sort_dir: GetV1CryptocurrencyTrendingGainerslosersSortDir | Unset = UNSET,
) -> Response[
    CryptocurrencyTrendingGainersLosersResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """Trending Gainers & Losers

     Returns a paginated list of all trending cryptocurrencies, determined and sorted by the largest
    price gains or losses.


    You may sort against any of the following:
    **percent_change_24h**: 24 hour trading price percentage change for each currency.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 10 minutes.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our cryptocurrency Gainers & Losers page [coinmarketcap.com/gainers-
    losers/](https://coinmarketcap.com/gainers-losers/).

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        time_period (GetV1CryptocurrencyTrendingGainerslosersTimePeriod | Unset):  Default: '24h'.
        convert (str | Unset):
        convert_id (str | Unset):
        sort (GetV1CryptocurrencyTrendingGainerslosersSort | Unset):  Default:
            'percent_change_24h'.
        sort_dir (GetV1CryptocurrencyTrendingGainerslosersSortDir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyTrendingGainersLosersResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
        time_period=time_period,
        convert=convert,
        convert_id=convert_id,
        sort=sort,
        sort_dir=sort_dir,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    time_period: GetV1CryptocurrencyTrendingGainerslosersTimePeriod | Unset = "24h",
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: GetV1CryptocurrencyTrendingGainerslosersSort | Unset = "percent_change_24h",
    sort_dir: GetV1CryptocurrencyTrendingGainerslosersSortDir | Unset = UNSET,
) -> (
    CryptocurrencyTrendingGainersLosersResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """Trending Gainers & Losers

     Returns a paginated list of all trending cryptocurrencies, determined and sorted by the largest
    price gains or losses.


    You may sort against any of the following:
    **percent_change_24h**: 24 hour trading price percentage change for each currency.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 10 minutes.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our cryptocurrency Gainers & Losers page [coinmarketcap.com/gainers-
    losers/](https://coinmarketcap.com/gainers-losers/).

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        time_period (GetV1CryptocurrencyTrendingGainerslosersTimePeriod | Unset):  Default: '24h'.
        convert (str | Unset):
        convert_id (str | Unset):
        sort (GetV1CryptocurrencyTrendingGainerslosersSort | Unset):  Default:
            'percent_change_24h'.
        sort_dir (GetV1CryptocurrencyTrendingGainerslosersSortDir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyTrendingGainersLosersResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            limit=limit,
            time_period=time_period,
            convert=convert,
            convert_id=convert_id,
            sort=sort,
            sort_dir=sort_dir,
        )
    ).parsed
