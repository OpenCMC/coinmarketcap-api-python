from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.category_response_model import CategoryResponseModel
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: str,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["start"] = start

    params["limit"] = limit

    params["convert"] = convert

    params["convert_id"] = convert_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/cryptocurrency/category",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CategoryResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = CategoryResponseModel.from_dict(response.json())

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
    CategoryResponseModel
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
    id: str,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> Response[
    CategoryResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Category

     Returns information about a single coin category available on CoinMarketCap. Includes a paginated
    list of the cryptocurrency quotes and metadata for the category.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Free
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/cryptocurrency/category`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Data is updated only as needed, every 30 seconds.
    **Plan credit use:** 1 API call credit per request + 1 call credit per 200 cryptocurrencies returned
    (rounded up) and 1 call credit per `convert` option beyond the first.
    **CMC equivalent pages:** Our Cryptocurrency Category page [coinmarketcap.com/cryptocurrency-
    category/](https://coinmarketcap.com/cryptocurrency-category/).

    Args:
        id (str):
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CategoryResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
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
    id: str,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> (
    CategoryResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Category

     Returns information about a single coin category available on CoinMarketCap. Includes a paginated
    list of the cryptocurrency quotes and metadata for the category.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Free
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/cryptocurrency/category`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Data is updated only as needed, every 30 seconds.
    **Plan credit use:** 1 API call credit per request + 1 call credit per 200 cryptocurrencies returned
    (rounded up) and 1 call credit per `convert` option beyond the first.
    **CMC equivalent pages:** Our Cryptocurrency Category page [coinmarketcap.com/cryptocurrency-
    category/](https://coinmarketcap.com/cryptocurrency-category/).

    Args:
        id (str):
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CategoryResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        id=id,
        start=start,
        limit=limit,
        convert=convert,
        convert_id=convert_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: str,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> Response[
    CategoryResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Category

     Returns information about a single coin category available on CoinMarketCap. Includes a paginated
    list of the cryptocurrency quotes and metadata for the category.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Free
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/cryptocurrency/category`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Data is updated only as needed, every 30 seconds.
    **Plan credit use:** 1 API call credit per request + 1 call credit per 200 cryptocurrencies returned
    (rounded up) and 1 call credit per `convert` option beyond the first.
    **CMC equivalent pages:** Our Cryptocurrency Category page [coinmarketcap.com/cryptocurrency-
    category/](https://coinmarketcap.com/cryptocurrency-category/).

    Args:
        id (str):
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CategoryResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
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
    id: str,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> (
    CategoryResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Category

     Returns information about a single coin category available on CoinMarketCap. Includes a paginated
    list of the cryptocurrency quotes and metadata for the category.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Free
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/cryptocurrency/category`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Data is updated only as needed, every 30 seconds.
    **Plan credit use:** 1 API call credit per request + 1 call credit per 200 cryptocurrencies returned
    (rounded up) and 1 call credit per `convert` option beyond the first.
    **CMC equivalent pages:** Our Cryptocurrency Category page [coinmarketcap.com/cryptocurrency-
    category/](https://coinmarketcap.com/cryptocurrency-category/).

    Args:
        id (str):
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CategoryResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            start=start,
            limit=limit,
            convert=convert,
            convert_id=convert_id,
        )
    ).parsed
