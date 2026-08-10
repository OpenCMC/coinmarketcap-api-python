from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exchange_map_response_model import ExchangeMapResponseModel
from ...models.get_v1_exchange_map_sort import GetV1ExchangeMapSort
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    listing_status: str | Unset = "active",
    slug: str | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = UNSET,
    sort: GetV1ExchangeMapSort | Unset = "id",
    aux: str | Unset = "first_historical_data,last_historical_data,is_active",
    crypto_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["listing_status"] = listing_status

    params["slug"] = slug

    params["start"] = start

    params["limit"] = limit

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["aux"] = aux

    params["crypto_id"] = crypto_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/exchange/map",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ExchangeMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = ExchangeMapResponseModel.from_dict(response.json())

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
    ExchangeMapResponseModel
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
    listing_status: str | Unset = "active",
    slug: str | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = UNSET,
    sort: GetV1ExchangeMapSort | Unset = "id",
    aux: str | Unset = "first_historical_data,last_historical_data,is_active",
    crypto_id: str | Unset = UNSET,
) -> Response[
    ExchangeMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Exchange ID Map

     Returns a paginated list of all active cryptocurrency exchanges by ID. We recommend using this
    convenience endpoint to lookup and utilize our unique exchange `id` across all endpoints as typical
    exchange identifiers may change over time. As a convenience you may pass a comma-separated list of
    exchanges by `slug` to filter this list to only those you require or the `aux` parameter to slim
    down the payload.

    By default this endpoint returns exchanges that have at least 1 actively tracked market. You may
    receive a map of all inactive cryptocurrencies by passing `listing_status=inactive`. You may also
    receive a map of registered exchanges that are listed but do not yet meet methodology requirements
    to have tracked markets available via `listing_status=untracked`. Please review **(3) Listing
    Tiers** in our <a target=\"_blank\" href=\"https://coinmarketcap.com/methodology/\">methodology
    documentation</a> for additional details on listing states.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/exchange/map`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Mapping data is updated only as needed, every 30 seconds.
    **Plan credit use:** 1 call credit per call.
    **CMC equivalent pages:** No equivalent, this data is only available via API.

    Args:
        listing_status (str | Unset):  Default: 'active'.
        slug (str | Unset):
        start (int | Unset):  Default: 1.
        limit (int | Unset):
        sort (GetV1ExchangeMapSort | Unset):  Default: 'id'.
        aux (str | Unset):  Default: 'first_historical_data,last_historical_data,is_active'.
        crypto_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeMapResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        listing_status=listing_status,
        slug=slug,
        start=start,
        limit=limit,
        sort=sort,
        aux=aux,
        crypto_id=crypto_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    listing_status: str | Unset = "active",
    slug: str | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = UNSET,
    sort: GetV1ExchangeMapSort | Unset = "id",
    aux: str | Unset = "first_historical_data,last_historical_data,is_active",
    crypto_id: str | Unset = UNSET,
) -> (
    ExchangeMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Exchange ID Map

     Returns a paginated list of all active cryptocurrency exchanges by ID. We recommend using this
    convenience endpoint to lookup and utilize our unique exchange `id` across all endpoints as typical
    exchange identifiers may change over time. As a convenience you may pass a comma-separated list of
    exchanges by `slug` to filter this list to only those you require or the `aux` parameter to slim
    down the payload.

    By default this endpoint returns exchanges that have at least 1 actively tracked market. You may
    receive a map of all inactive cryptocurrencies by passing `listing_status=inactive`. You may also
    receive a map of registered exchanges that are listed but do not yet meet methodology requirements
    to have tracked markets available via `listing_status=untracked`. Please review **(3) Listing
    Tiers** in our <a target=\"_blank\" href=\"https://coinmarketcap.com/methodology/\">methodology
    documentation</a> for additional details on listing states.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/exchange/map`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Mapping data is updated only as needed, every 30 seconds.
    **Plan credit use:** 1 call credit per call.
    **CMC equivalent pages:** No equivalent, this data is only available via API.

    Args:
        listing_status (str | Unset):  Default: 'active'.
        slug (str | Unset):
        start (int | Unset):  Default: 1.
        limit (int | Unset):
        sort (GetV1ExchangeMapSort | Unset):  Default: 'id'.
        aux (str | Unset):  Default: 'first_historical_data,last_historical_data,is_active'.
        crypto_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeMapResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        listing_status=listing_status,
        slug=slug,
        start=start,
        limit=limit,
        sort=sort,
        aux=aux,
        crypto_id=crypto_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    listing_status: str | Unset = "active",
    slug: str | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = UNSET,
    sort: GetV1ExchangeMapSort | Unset = "id",
    aux: str | Unset = "first_historical_data,last_historical_data,is_active",
    crypto_id: str | Unset = UNSET,
) -> Response[
    ExchangeMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Exchange ID Map

     Returns a paginated list of all active cryptocurrency exchanges by ID. We recommend using this
    convenience endpoint to lookup and utilize our unique exchange `id` across all endpoints as typical
    exchange identifiers may change over time. As a convenience you may pass a comma-separated list of
    exchanges by `slug` to filter this list to only those you require or the `aux` parameter to slim
    down the payload.

    By default this endpoint returns exchanges that have at least 1 actively tracked market. You may
    receive a map of all inactive cryptocurrencies by passing `listing_status=inactive`. You may also
    receive a map of registered exchanges that are listed but do not yet meet methodology requirements
    to have tracked markets available via `listing_status=untracked`. Please review **(3) Listing
    Tiers** in our <a target=\"_blank\" href=\"https://coinmarketcap.com/methodology/\">methodology
    documentation</a> for additional details on listing states.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/exchange/map`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Mapping data is updated only as needed, every 30 seconds.
    **Plan credit use:** 1 call credit per call.
    **CMC equivalent pages:** No equivalent, this data is only available via API.

    Args:
        listing_status (str | Unset):  Default: 'active'.
        slug (str | Unset):
        start (int | Unset):  Default: 1.
        limit (int | Unset):
        sort (GetV1ExchangeMapSort | Unset):  Default: 'id'.
        aux (str | Unset):  Default: 'first_historical_data,last_historical_data,is_active'.
        crypto_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeMapResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        listing_status=listing_status,
        slug=slug,
        start=start,
        limit=limit,
        sort=sort,
        aux=aux,
        crypto_id=crypto_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    listing_status: str | Unset = "active",
    slug: str | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = UNSET,
    sort: GetV1ExchangeMapSort | Unset = "id",
    aux: str | Unset = "first_historical_data,last_historical_data,is_active",
    crypto_id: str | Unset = UNSET,
) -> (
    ExchangeMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Exchange ID Map

     Returns a paginated list of all active cryptocurrency exchanges by ID. We recommend using this
    convenience endpoint to lookup and utilize our unique exchange `id` across all endpoints as typical
    exchange identifiers may change over time. As a convenience you may pass a comma-separated list of
    exchanges by `slug` to filter this list to only those you require or the `aux` parameter to slim
    down the payload.

    By default this endpoint returns exchanges that have at least 1 actively tracked market. You may
    receive a map of all inactive cryptocurrencies by passing `listing_status=inactive`. You may also
    receive a map of registered exchanges that are listed but do not yet meet methodology requirements
    to have tracked markets available via `listing_status=untracked`. Please review **(3) Listing
    Tiers** in our <a target=\"_blank\" href=\"https://coinmarketcap.com/methodology/\">methodology
    documentation</a> for additional details on listing states.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/exchange/map`. See the [Keyless Public API](https://coinmarketcap.com/api/documentation/pro-
    api-reference/keyless-public-api) for the full list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Mapping data is updated only as needed, every 30 seconds.
    **Plan credit use:** 1 call credit per call.
    **CMC equivalent pages:** No equivalent, this data is only available via API.

    Args:
        listing_status (str | Unset):  Default: 'active'.
        slug (str | Unset):
        start (int | Unset):  Default: 1.
        limit (int | Unset):
        sort (GetV1ExchangeMapSort | Unset):  Default: 'id'.
        aux (str | Unset):  Default: 'first_historical_data,last_historical_data,is_active'.
        crypto_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeMapResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            listing_status=listing_status,
            slug=slug,
            start=start,
            limit=limit,
            sort=sort,
            aux=aux,
            crypto_id=crypto_id,
        )
    ).parsed
