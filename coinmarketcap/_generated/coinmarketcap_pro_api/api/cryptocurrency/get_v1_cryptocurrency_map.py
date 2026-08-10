from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cryptocurrency_map_response_model import CryptocurrencyMapResponseModel
from ...models.get_v1_cryptocurrency_map_sort import GetV1CryptocurrencyMapSort
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    listing_status: str | Unset = "active",
    start: int | Unset = 1,
    limit: int | Unset = UNSET,
    sort: GetV1CryptocurrencyMapSort | Unset = "id",
    symbol: str | Unset = UNSET,
    aux: str | Unset = "platform,first_historical_data,last_historical_data,is_active",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["listing_status"] = listing_status

    params["start"] = start

    params["limit"] = limit

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["symbol"] = symbol

    params["aux"] = aux

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/cryptocurrency/map",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CryptocurrencyMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = CryptocurrencyMapResponseModel.from_dict(response.json())

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
    CryptocurrencyMapResponseModel
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
    start: int | Unset = 1,
    limit: int | Unset = UNSET,
    sort: GetV1CryptocurrencyMapSort | Unset = "id",
    symbol: str | Unset = UNSET,
    aux: str | Unset = "platform,first_historical_data,last_historical_data,is_active",
) -> Response[
    CryptocurrencyMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Cryptocurrency ID Map

     Returns a mapping of all cryptocurrencies to unique CoinMarketCap `id`s. Per our [Best
    practices](/guides/best-practices) we recommend utilizing CMC ID instead of cryptocurrency symbols
    to securely identify cryptocurrencies with our other endpoints and in your own application logic.
    Each cryptocurrency returned includes typical identifiers such as `name`, `symbol`, and
    `token_address` for flexible mapping to `id`.

      By default this endpoint returns cryptocurrencies that have actively tracked markets on supported
    exchanges. You may receive a map of all inactive cryptocurrencies by passing
    `listing_status=inactive`. You may also receive a map of registered cryptocurrency projects that are
    listed but do not yet meet methodology requirements to have tracked markets via
    `listing_status=untracked`. Please review our <a target=\"_blank\"
    href=\"https://coinmarketcap.com/methodology/\">methodology documentation</a> for additional details
    on listing states.

      Cryptocurrencies returned include `first_historical_data` and `last_historical_data` timestamps to
    conveniently reference historical date ranges available to query with historical time-series data
    endpoints. You may also use the `aux` parameter to only include properties you require to slim down
    the payload if calling this endpoint frequently.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

      **No credit is needed when querying this endpoint.**

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/cryptocurrency/map`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Mapping data is updated only as needed, every 30 seconds.
    **CMC equivalent pages:** No equivalent, this data is only available via API.

    Args:
        listing_status (str | Unset):  Default: 'active'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):
        sort (GetV1CryptocurrencyMapSort | Unset):  Default: 'id'.
        symbol (str | Unset):
        aux (str | Unset):  Default:
            'platform,first_historical_data,last_historical_data,is_active'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyMapResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        listing_status=listing_status,
        start=start,
        limit=limit,
        sort=sort,
        symbol=symbol,
        aux=aux,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    listing_status: str | Unset = "active",
    start: int | Unset = 1,
    limit: int | Unset = UNSET,
    sort: GetV1CryptocurrencyMapSort | Unset = "id",
    symbol: str | Unset = UNSET,
    aux: str | Unset = "platform,first_historical_data,last_historical_data,is_active",
) -> (
    CryptocurrencyMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Cryptocurrency ID Map

     Returns a mapping of all cryptocurrencies to unique CoinMarketCap `id`s. Per our [Best
    practices](/guides/best-practices) we recommend utilizing CMC ID instead of cryptocurrency symbols
    to securely identify cryptocurrencies with our other endpoints and in your own application logic.
    Each cryptocurrency returned includes typical identifiers such as `name`, `symbol`, and
    `token_address` for flexible mapping to `id`.

      By default this endpoint returns cryptocurrencies that have actively tracked markets on supported
    exchanges. You may receive a map of all inactive cryptocurrencies by passing
    `listing_status=inactive`. You may also receive a map of registered cryptocurrency projects that are
    listed but do not yet meet methodology requirements to have tracked markets via
    `listing_status=untracked`. Please review our <a target=\"_blank\"
    href=\"https://coinmarketcap.com/methodology/\">methodology documentation</a> for additional details
    on listing states.

      Cryptocurrencies returned include `first_historical_data` and `last_historical_data` timestamps to
    conveniently reference historical date ranges available to query with historical time-series data
    endpoints. You may also use the `aux` parameter to only include properties you require to slim down
    the payload if calling this endpoint frequently.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

      **No credit is needed when querying this endpoint.**

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/cryptocurrency/map`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Mapping data is updated only as needed, every 30 seconds.
    **CMC equivalent pages:** No equivalent, this data is only available via API.

    Args:
        listing_status (str | Unset):  Default: 'active'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):
        sort (GetV1CryptocurrencyMapSort | Unset):  Default: 'id'.
        symbol (str | Unset):
        aux (str | Unset):  Default:
            'platform,first_historical_data,last_historical_data,is_active'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyMapResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        listing_status=listing_status,
        start=start,
        limit=limit,
        sort=sort,
        symbol=symbol,
        aux=aux,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    listing_status: str | Unset = "active",
    start: int | Unset = 1,
    limit: int | Unset = UNSET,
    sort: GetV1CryptocurrencyMapSort | Unset = "id",
    symbol: str | Unset = UNSET,
    aux: str | Unset = "platform,first_historical_data,last_historical_data,is_active",
) -> Response[
    CryptocurrencyMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Cryptocurrency ID Map

     Returns a mapping of all cryptocurrencies to unique CoinMarketCap `id`s. Per our [Best
    practices](/guides/best-practices) we recommend utilizing CMC ID instead of cryptocurrency symbols
    to securely identify cryptocurrencies with our other endpoints and in your own application logic.
    Each cryptocurrency returned includes typical identifiers such as `name`, `symbol`, and
    `token_address` for flexible mapping to `id`.

      By default this endpoint returns cryptocurrencies that have actively tracked markets on supported
    exchanges. You may receive a map of all inactive cryptocurrencies by passing
    `listing_status=inactive`. You may also receive a map of registered cryptocurrency projects that are
    listed but do not yet meet methodology requirements to have tracked markets via
    `listing_status=untracked`. Please review our <a target=\"_blank\"
    href=\"https://coinmarketcap.com/methodology/\">methodology documentation</a> for additional details
    on listing states.

      Cryptocurrencies returned include `first_historical_data` and `last_historical_data` timestamps to
    conveniently reference historical date ranges available to query with historical time-series data
    endpoints. You may also use the `aux` parameter to only include properties you require to slim down
    the payload if calling this endpoint frequently.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

      **No credit is needed when querying this endpoint.**

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/cryptocurrency/map`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Mapping data is updated only as needed, every 30 seconds.
    **CMC equivalent pages:** No equivalent, this data is only available via API.

    Args:
        listing_status (str | Unset):  Default: 'active'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):
        sort (GetV1CryptocurrencyMapSort | Unset):  Default: 'id'.
        symbol (str | Unset):
        aux (str | Unset):  Default:
            'platform,first_historical_data,last_historical_data,is_active'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyMapResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        listing_status=listing_status,
        start=start,
        limit=limit,
        sort=sort,
        symbol=symbol,
        aux=aux,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    listing_status: str | Unset = "active",
    start: int | Unset = 1,
    limit: int | Unset = UNSET,
    sort: GetV1CryptocurrencyMapSort | Unset = "id",
    symbol: str | Unset = UNSET,
    aux: str | Unset = "platform,first_historical_data,last_historical_data,is_active",
) -> (
    CryptocurrencyMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Cryptocurrency ID Map

     Returns a mapping of all cryptocurrencies to unique CoinMarketCap `id`s. Per our [Best
    practices](/guides/best-practices) we recommend utilizing CMC ID instead of cryptocurrency symbols
    to securely identify cryptocurrencies with our other endpoints and in your own application logic.
    Each cryptocurrency returned includes typical identifiers such as `name`, `symbol`, and
    `token_address` for flexible mapping to `id`.

      By default this endpoint returns cryptocurrencies that have actively tracked markets on supported
    exchanges. You may receive a map of all inactive cryptocurrencies by passing
    `listing_status=inactive`. You may also receive a map of registered cryptocurrency projects that are
    listed but do not yet meet methodology requirements to have tracked markets via
    `listing_status=untracked`. Please review our <a target=\"_blank\"
    href=\"https://coinmarketcap.com/methodology/\">methodology documentation</a> for additional details
    on listing states.

      Cryptocurrencies returned include `first_historical_data` and `last_historical_data` timestamps to
    conveniently reference historical date ranges available to query with historical time-series data
    endpoints. You may also use the `aux` parameter to only include properties you require to slim down
    the payload if calling this endpoint frequently.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

      **No credit is needed when querying this endpoint.**

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v1/cryptocurrency/map`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Mapping data is updated only as needed, every 30 seconds.
    **CMC equivalent pages:** No equivalent, this data is only available via API.

    Args:
        listing_status (str | Unset):  Default: 'active'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):
        sort (GetV1CryptocurrencyMapSort | Unset):  Default: 'id'.
        symbol (str | Unset):
        aux (str | Unset):  Default:
            'platform,first_historical_data,last_historical_data,is_active'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyMapResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            listing_status=listing_status,
            start=start,
            limit=limit,
            sort=sort,
            symbol=symbol,
            aux=aux,
        )
    ).parsed
