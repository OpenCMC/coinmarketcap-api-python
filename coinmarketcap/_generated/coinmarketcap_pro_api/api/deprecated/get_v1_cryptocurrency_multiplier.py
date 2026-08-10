from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cryptocurrency_multiplier_response_model import CryptocurrencyMultiplierResponseModel
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    crypto_id: str | Unset = UNSET,
    crypto_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    token_address: str | Unset = UNSET,
    skip_invalid: bool | Unset = False,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["crypto_id"] = crypto_id

    params["crypto_slug"] = crypto_slug

    params["symbol"] = symbol

    params["token_address"] = token_address

    params["skip_invalid"] = skip_invalid

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/cryptocurrency/multiplier",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CryptocurrencyMultiplierResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = CryptocurrencyMultiplierResponseModel.from_dict(response.json())

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
    CryptocurrencyMultiplierResponseModel
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
    crypto_id: str | Unset = UNSET,
    crypto_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    token_address: str | Unset = UNSET,
    skip_invalid: bool | Unset = False,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> Response[
    CryptocurrencyMultiplierResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """Cryptocurrency Multiplier

     Returns a paginated list of cryptocurrencies that has a **ERC-8056 UI multiplier**.

    **Filtering and pagination**
    - Use `crypto_id`, `crypto_slug`, `symbol`, or `token_address` to look up specific cryptocurrencies.
    These four filters are **mutually exclusive**, pass only one per request. Omit all four to page
    through every cryptocurrency that currently has a UI multiplier, sorted by ascending CoinMarketCap
    ID.
    - `total_size` is the total number of results before pagination.
    - `start` and `limit` paginate the list (1-based `start`, default `start=1`, `limit=100`).
    `has_more` is `true` when `start + limit` has not yet reached `total_size`.

    **No credit is needed when querying this endpoint.**

    **Cache / Update frequency:** Refreshed whenever multiplier changes are applied.
    **CMC equivalent pages:** Cryptocurrency detail pages that display adjusted supply or price using
    the UI multiplier.

    Args:
        crypto_id (str | Unset):
        crypto_slug (str | Unset):
        symbol (str | Unset):
        token_address (str | Unset):
        skip_invalid (bool | Unset):  Default: False.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyMultiplierResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        crypto_id=crypto_id,
        crypto_slug=crypto_slug,
        symbol=symbol,
        token_address=token_address,
        skip_invalid=skip_invalid,
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    crypto_id: str | Unset = UNSET,
    crypto_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    token_address: str | Unset = UNSET,
    skip_invalid: bool | Unset = False,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> (
    CryptocurrencyMultiplierResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """Cryptocurrency Multiplier

     Returns a paginated list of cryptocurrencies that has a **ERC-8056 UI multiplier**.

    **Filtering and pagination**
    - Use `crypto_id`, `crypto_slug`, `symbol`, or `token_address` to look up specific cryptocurrencies.
    These four filters are **mutually exclusive**, pass only one per request. Omit all four to page
    through every cryptocurrency that currently has a UI multiplier, sorted by ascending CoinMarketCap
    ID.
    - `total_size` is the total number of results before pagination.
    - `start` and `limit` paginate the list (1-based `start`, default `start=1`, `limit=100`).
    `has_more` is `true` when `start + limit` has not yet reached `total_size`.

    **No credit is needed when querying this endpoint.**

    **Cache / Update frequency:** Refreshed whenever multiplier changes are applied.
    **CMC equivalent pages:** Cryptocurrency detail pages that display adjusted supply or price using
    the UI multiplier.

    Args:
        crypto_id (str | Unset):
        crypto_slug (str | Unset):
        symbol (str | Unset):
        token_address (str | Unset):
        skip_invalid (bool | Unset):  Default: False.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyMultiplierResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        crypto_id=crypto_id,
        crypto_slug=crypto_slug,
        symbol=symbol,
        token_address=token_address,
        skip_invalid=skip_invalid,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    crypto_id: str | Unset = UNSET,
    crypto_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    token_address: str | Unset = UNSET,
    skip_invalid: bool | Unset = False,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> Response[
    CryptocurrencyMultiplierResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """Cryptocurrency Multiplier

     Returns a paginated list of cryptocurrencies that has a **ERC-8056 UI multiplier**.

    **Filtering and pagination**
    - Use `crypto_id`, `crypto_slug`, `symbol`, or `token_address` to look up specific cryptocurrencies.
    These four filters are **mutually exclusive**, pass only one per request. Omit all four to page
    through every cryptocurrency that currently has a UI multiplier, sorted by ascending CoinMarketCap
    ID.
    - `total_size` is the total number of results before pagination.
    - `start` and `limit` paginate the list (1-based `start`, default `start=1`, `limit=100`).
    `has_more` is `true` when `start + limit` has not yet reached `total_size`.

    **No credit is needed when querying this endpoint.**

    **Cache / Update frequency:** Refreshed whenever multiplier changes are applied.
    **CMC equivalent pages:** Cryptocurrency detail pages that display adjusted supply or price using
    the UI multiplier.

    Args:
        crypto_id (str | Unset):
        crypto_slug (str | Unset):
        symbol (str | Unset):
        token_address (str | Unset):
        skip_invalid (bool | Unset):  Default: False.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyMultiplierResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        crypto_id=crypto_id,
        crypto_slug=crypto_slug,
        symbol=symbol,
        token_address=token_address,
        skip_invalid=skip_invalid,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    crypto_id: str | Unset = UNSET,
    crypto_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    token_address: str | Unset = UNSET,
    skip_invalid: bool | Unset = False,
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> (
    CryptocurrencyMultiplierResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """Cryptocurrency Multiplier

     Returns a paginated list of cryptocurrencies that has a **ERC-8056 UI multiplier**.

    **Filtering and pagination**
    - Use `crypto_id`, `crypto_slug`, `symbol`, or `token_address` to look up specific cryptocurrencies.
    These four filters are **mutually exclusive**, pass only one per request. Omit all four to page
    through every cryptocurrency that currently has a UI multiplier, sorted by ascending CoinMarketCap
    ID.
    - `total_size` is the total number of results before pagination.
    - `start` and `limit` paginate the list (1-based `start`, default `start=1`, `limit=100`).
    `has_more` is `true` when `start + limit` has not yet reached `total_size`.

    **No credit is needed when querying this endpoint.**

    **Cache / Update frequency:** Refreshed whenever multiplier changes are applied.
    **CMC equivalent pages:** Cryptocurrency detail pages that display adjusted supply or price using
    the UI multiplier.

    Args:
        crypto_id (str | Unset):
        crypto_slug (str | Unset):
        symbol (str | Unset):
        token_address (str | Unset):
        skip_invalid (bool | Unset):  Default: False.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyMultiplierResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            crypto_id=crypto_id,
            crypto_slug=crypto_slug,
            symbol=symbol,
            token_address=token_address,
            skip_invalid=skip_invalid,
            start=start,
            limit=limit,
        )
    ).parsed
