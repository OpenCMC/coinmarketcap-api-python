from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.crypto_quote_v3dto import CryptoQuoteV3DTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    aux: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
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
        "url": "/v3/cryptocurrency/quotes/latest",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[CryptoQuoteV3DTO] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CryptoQuoteV3DTO.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[CryptoQuoteV3DTO]]:
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
    aux: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> Response[list[CryptoQuoteV3DTO]]:
    r"""Quotes Latest

     Returns the latest market quote for 1 or more cryptocurrencies. Use the \"convert\" option to return
    market values in multiple fiat and cryptocurrency conversions in the same call.

    **Please note**: This documentation relates to our updated V3 endpoint, which may be incompatible
    with our V2 versions. Documentation for deprecated endpoints can be found [the deprecated
    section](/pro-api-reference/deprecated).


    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - Basic
    - Startup
    - Builder
    - Growth
    - Professional
    - Enterprise

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v3/cryptocurrency/quotes/latest`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit
    per \`convert\` option beyond the first.
    **CMC equivalent pages:** Latest market data pages for specific cryptocurrencies like
    [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).

    ***NOTE:** Use this endpoint to request the latest quote for specific cryptocurrencies. If you need
    to request all cryptocurrencies use `/v3/cryptocurrency/listings/latest` which is optimized for that
    purpose. The response data between these endpoints is otherwise the same.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        aux (str | Unset):
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[CryptoQuoteV3DTO]]
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
    aux: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> list[CryptoQuoteV3DTO] | None:
    r"""Quotes Latest

     Returns the latest market quote for 1 or more cryptocurrencies. Use the \"convert\" option to return
    market values in multiple fiat and cryptocurrency conversions in the same call.

    **Please note**: This documentation relates to our updated V3 endpoint, which may be incompatible
    with our V2 versions. Documentation for deprecated endpoints can be found [the deprecated
    section](/pro-api-reference/deprecated).


    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - Basic
    - Startup
    - Builder
    - Growth
    - Professional
    - Enterprise

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v3/cryptocurrency/quotes/latest`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit
    per \`convert\` option beyond the first.
    **CMC equivalent pages:** Latest market data pages for specific cryptocurrencies like
    [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).

    ***NOTE:** Use this endpoint to request the latest quote for specific cryptocurrencies. If you need
    to request all cryptocurrencies use `/v3/cryptocurrency/listings/latest` which is optimized for that
    purpose. The response data between these endpoints is otherwise the same.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        aux (str | Unset):
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[CryptoQuoteV3DTO]
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
    aux: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> Response[list[CryptoQuoteV3DTO]]:
    r"""Quotes Latest

     Returns the latest market quote for 1 or more cryptocurrencies. Use the \"convert\" option to return
    market values in multiple fiat and cryptocurrency conversions in the same call.

    **Please note**: This documentation relates to our updated V3 endpoint, which may be incompatible
    with our V2 versions. Documentation for deprecated endpoints can be found [the deprecated
    section](/pro-api-reference/deprecated).


    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - Basic
    - Startup
    - Builder
    - Growth
    - Professional
    - Enterprise

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v3/cryptocurrency/quotes/latest`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit
    per \`convert\` option beyond the first.
    **CMC equivalent pages:** Latest market data pages for specific cryptocurrencies like
    [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).

    ***NOTE:** Use this endpoint to request the latest quote for specific cryptocurrencies. If you need
    to request all cryptocurrencies use `/v3/cryptocurrency/listings/latest` which is optimized for that
    purpose. The response data between these endpoints is otherwise the same.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        aux (str | Unset):
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[CryptoQuoteV3DTO]]
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
    aux: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> list[CryptoQuoteV3DTO] | None:
    r"""Quotes Latest

     Returns the latest market quote for 1 or more cryptocurrencies. Use the \"convert\" option to return
    market values in multiple fiat and cryptocurrency conversions in the same call.

    **Please note**: This documentation relates to our updated V3 endpoint, which may be incompatible
    with our V2 versions. Documentation for deprecated endpoints can be found [the deprecated
    section](/pro-api-reference/deprecated).


    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - Basic
    - Startup
    - Builder
    - Growth
    - Professional
    - Enterprise

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v3/cryptocurrency/quotes/latest`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Every 60 seconds.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit
    per \`convert\` option beyond the first.
    **CMC equivalent pages:** Latest market data pages for specific cryptocurrencies like
    [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).

    ***NOTE:** Use this endpoint to request the latest quote for specific cryptocurrencies. If you need
    to request all cryptocurrencies use `/v3/cryptocurrency/listings/latest` which is optimized for that
    purpose. The response data between these endpoints is otherwise the same.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        aux (str | Unset):
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[CryptoQuoteV3DTO]
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
