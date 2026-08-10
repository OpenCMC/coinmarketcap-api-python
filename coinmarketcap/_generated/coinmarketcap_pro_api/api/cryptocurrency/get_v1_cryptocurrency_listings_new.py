from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cryptocurrency_listings_new_response_model import CryptocurrencyListingsNewResponseModel
from ...models.get_v1_cryptocurrency_listings_new_sort_dir import (
    GetV1CryptocurrencyListingsNewSortDir,
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
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort_dir: GetV1CryptocurrencyListingsNewSortDir | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["start"] = start

    params["limit"] = limit

    params["convert"] = convert

    params["convert_id"] = convert_id

    json_sort_dir: str | Unset = UNSET
    if not isinstance(sort_dir, Unset):
        json_sort_dir = sort_dir

    params["sort_dir"] = json_sort_dir

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/cryptocurrency/listings/new",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CryptocurrencyListingsNewResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = CryptocurrencyListingsNewResponseModel.from_dict(response.json())

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
    CryptocurrencyListingsNewResponseModel
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
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort_dir: GetV1CryptocurrencyListingsNewSortDir | Unset = UNSET,
) -> Response[
    CryptocurrencyListingsNewResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Listings New

     Returns a paginated list of most recently added cryptocurrencies.


      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our \"new\" cryptocurrency page
    [coinmarketcap.com/new/](https://coinmarketcap.com/new)

    ***NOTE:** Use this endpoint if you need a sorted and paginated list of all recently added
    cryptocurrencies.*

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):
        convert_id (str | Unset):
        sort_dir (GetV1CryptocurrencyListingsNewSortDir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyListingsNewResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
        convert=convert,
        convert_id=convert_id,
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
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort_dir: GetV1CryptocurrencyListingsNewSortDir | Unset = UNSET,
) -> (
    CryptocurrencyListingsNewResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Listings New

     Returns a paginated list of most recently added cryptocurrencies.


      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our \"new\" cryptocurrency page
    [coinmarketcap.com/new/](https://coinmarketcap.com/new)

    ***NOTE:** Use this endpoint if you need a sorted and paginated list of all recently added
    cryptocurrencies.*

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):
        convert_id (str | Unset):
        sort_dir (GetV1CryptocurrencyListingsNewSortDir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyListingsNewResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        start=start,
        limit=limit,
        convert=convert,
        convert_id=convert_id,
        sort_dir=sort_dir,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort_dir: GetV1CryptocurrencyListingsNewSortDir | Unset = UNSET,
) -> Response[
    CryptocurrencyListingsNewResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Listings New

     Returns a paginated list of most recently added cryptocurrencies.


      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our \"new\" cryptocurrency page
    [coinmarketcap.com/new/](https://coinmarketcap.com/new)

    ***NOTE:** Use this endpoint if you need a sorted and paginated list of all recently added
    cryptocurrencies.*

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):
        convert_id (str | Unset):
        sort_dir (GetV1CryptocurrencyListingsNewSortDir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyListingsNewResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
        convert=convert,
        convert_id=convert_id,
        sort_dir=sort_dir,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort_dir: GetV1CryptocurrencyListingsNewSortDir | Unset = UNSET,
) -> (
    CryptocurrencyListingsNewResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Listings New

     Returns a paginated list of most recently added cryptocurrencies.


      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 200 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our \"new\" cryptocurrency page
    [coinmarketcap.com/new/](https://coinmarketcap.com/new)

    ***NOTE:** Use this endpoint if you need a sorted and paginated list of all recently added
    cryptocurrencies.*

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):
        convert_id (str | Unset):
        sort_dir (GetV1CryptocurrencyListingsNewSortDir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyListingsNewResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            limit=limit,
            convert=convert,
            convert_id=convert_id,
            sort_dir=sort_dir,
        )
    ).parsed
