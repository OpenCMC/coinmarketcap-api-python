from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cryptocurrency_quotes_latest_response_model import CryptocurrencyQuotesLatestResponseModel
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
    symbol: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    aux: str
    | Unset = "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply,is_active,is_fiat",
    skip_invalid: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["slug"] = slug

    params["symbol"] = symbol

    params["convert"] = convert

    params["convert_id"] = convert_id

    params["aux"] = aux

    params["skip_invalid"] = skip_invalid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/cryptocurrency/quotes/latest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CryptocurrencyQuotesLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = CryptocurrencyQuotesLatestResponseModel.from_dict(response.json())

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
    CryptocurrencyQuotesLatestResponseModel
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
    symbol: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    aux: str
    | Unset = "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply,is_active,is_fiat",
    skip_invalid: bool | Unset = True,
) -> Response[
    CryptocurrencyQuotesLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Quotes Latest v1 (deprecated)

     Returns the latest market quote for 1 or more cryptocurrencies. Use the \"convert\" option to return
    market values in multiple fiat and cryptocurrency conversions in the same call.


    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - Basic
    - Startup
    - Builder
    - Growth
    - Professional
    - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Latest market data pages for specific cryptocurrencies like
    [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).

    ***NOTE:** Use this endpoint to request the latest quote for specific cryptocurrencies. If you need
    to request all cryptocurrencies use `/v1/cryptocurrency/listings/latest` which is optimized for that
    purpose. The response data between these endpoints is otherwise the same.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        aux (str | Unset):  Default: 'num_market_pairs,cmc_rank,date_added,tags,platform,max_suppl
            y,circulating_supply,total_supply,is_active,is_fiat'.
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyQuotesLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        symbol=symbol,
        convert=convert,
        convert_id=convert_id,
        aux=aux,
        skip_invalid=skip_invalid,
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
    symbol: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    aux: str
    | Unset = "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply,is_active,is_fiat",
    skip_invalid: bool | Unset = True,
) -> (
    CryptocurrencyQuotesLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Quotes Latest v1 (deprecated)

     Returns the latest market quote for 1 or more cryptocurrencies. Use the \"convert\" option to return
    market values in multiple fiat and cryptocurrency conversions in the same call.


    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - Basic
    - Startup
    - Builder
    - Growth
    - Professional
    - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Latest market data pages for specific cryptocurrencies like
    [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).

    ***NOTE:** Use this endpoint to request the latest quote for specific cryptocurrencies. If you need
    to request all cryptocurrencies use `/v1/cryptocurrency/listings/latest` which is optimized for that
    purpose. The response data between these endpoints is otherwise the same.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        aux (str | Unset):  Default: 'num_market_pairs,cmc_rank,date_added,tags,platform,max_suppl
            y,circulating_supply,total_supply,is_active,is_fiat'.
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyQuotesLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        id=id,
        slug=slug,
        symbol=symbol,
        convert=convert,
        convert_id=convert_id,
        aux=aux,
        skip_invalid=skip_invalid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    aux: str
    | Unset = "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply,is_active,is_fiat",
    skip_invalid: bool | Unset = True,
) -> Response[
    CryptocurrencyQuotesLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Quotes Latest v1 (deprecated)

     Returns the latest market quote for 1 or more cryptocurrencies. Use the \"convert\" option to return
    market values in multiple fiat and cryptocurrency conversions in the same call.


    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - Basic
    - Startup
    - Builder
    - Growth
    - Professional
    - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Latest market data pages for specific cryptocurrencies like
    [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).

    ***NOTE:** Use this endpoint to request the latest quote for specific cryptocurrencies. If you need
    to request all cryptocurrencies use `/v1/cryptocurrency/listings/latest` which is optimized for that
    purpose. The response data between these endpoints is otherwise the same.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        aux (str | Unset):  Default: 'num_market_pairs,cmc_rank,date_added,tags,platform,max_suppl
            y,circulating_supply,total_supply,is_active,is_fiat'.
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyQuotesLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        symbol=symbol,
        convert=convert,
        convert_id=convert_id,
        aux=aux,
        skip_invalid=skip_invalid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    aux: str
    | Unset = "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply,is_active,is_fiat",
    skip_invalid: bool | Unset = True,
) -> (
    CryptocurrencyQuotesLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Quotes Latest v1 (deprecated)

     Returns the latest market quote for 1 or more cryptocurrencies. Use the \"convert\" option to return
    market values in multiple fiat and cryptocurrency conversions in the same call.


    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - Basic
    - Startup
    - Builder
    - Growth
    - Professional
    - Enterprise

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Latest market data pages for specific cryptocurrencies like
    [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).

    ***NOTE:** Use this endpoint to request the latest quote for specific cryptocurrencies. If you need
    to request all cryptocurrencies use `/v1/cryptocurrency/listings/latest` which is optimized for that
    purpose. The response data between these endpoints is otherwise the same.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        aux (str | Unset):  Default: 'num_market_pairs,cmc_rank,date_added,tags,platform,max_suppl
            y,circulating_supply,total_supply,is_active,is_fiat'.
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyQuotesLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            slug=slug,
            symbol=symbol,
            convert=convert,
            convert_id=convert_id,
            aux=aux,
            skip_invalid=skip_invalid,
        )
    ).parsed
