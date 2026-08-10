from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cryptocurrencies_info_response_model import CryptocurrenciesInfoResponseModel
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
    address: str | Unset = UNSET,
    skip_invalid: bool | Unset = False,
    aux: str | Unset = "urls,logo,description,tags,platform,date_added,notice",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["slug"] = slug

    params["symbol"] = symbol

    params["address"] = address

    params["skip_invalid"] = skip_invalid

    params["aux"] = aux

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/cryptocurrency/info",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CryptocurrenciesInfoResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = CryptocurrenciesInfoResponseModel.from_dict(response.json())

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
    CryptocurrenciesInfoResponseModel
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
    address: str | Unset = UNSET,
    skip_invalid: bool | Unset = False,
    aux: str | Unset = "urls,logo,description,tags,platform,date_added,notice",
) -> Response[
    CryptocurrenciesInfoResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Metadata

     Returns all static metadata available for one or more cryptocurrencies. This information includes
    details like logo, description, official website URL, social links, and links to a cryptocurrency's
    technical documentation.

    **Please note**: This documentation relates to our updated V2 endpoint, which may be incompatible
    with our V1 versions. Documentation for deprecated endpoints can be found [the deprecated
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
    api/v2/cryptocurrency/info`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Static data is updated only as needed, every 30 seconds.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up).
    **CMC equivalent pages:** Cryptocurrency detail page metadata like
    [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        address (str | Unset):
        skip_invalid (bool | Unset):  Default: False.
        aux (str | Unset):  Default: 'urls,logo,description,tags,platform,date_added,notice'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrenciesInfoResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        symbol=symbol,
        address=address,
        skip_invalid=skip_invalid,
        aux=aux,
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
    address: str | Unset = UNSET,
    skip_invalid: bool | Unset = False,
    aux: str | Unset = "urls,logo,description,tags,platform,date_added,notice",
) -> (
    CryptocurrenciesInfoResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Metadata

     Returns all static metadata available for one or more cryptocurrencies. This information includes
    details like logo, description, official website URL, social links, and links to a cryptocurrency's
    technical documentation.

    **Please note**: This documentation relates to our updated V2 endpoint, which may be incompatible
    with our V1 versions. Documentation for deprecated endpoints can be found [the deprecated
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
    api/v2/cryptocurrency/info`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Static data is updated only as needed, every 30 seconds.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up).
    **CMC equivalent pages:** Cryptocurrency detail page metadata like
    [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        address (str | Unset):
        skip_invalid (bool | Unset):  Default: False.
        aux (str | Unset):  Default: 'urls,logo,description,tags,platform,date_added,notice'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrenciesInfoResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        id=id,
        slug=slug,
        symbol=symbol,
        address=address,
        skip_invalid=skip_invalid,
        aux=aux,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    address: str | Unset = UNSET,
    skip_invalid: bool | Unset = False,
    aux: str | Unset = "urls,logo,description,tags,platform,date_added,notice",
) -> Response[
    CryptocurrenciesInfoResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Metadata

     Returns all static metadata available for one or more cryptocurrencies. This information includes
    details like logo, description, official website URL, social links, and links to a cryptocurrency's
    technical documentation.

    **Please note**: This documentation relates to our updated V2 endpoint, which may be incompatible
    with our V1 versions. Documentation for deprecated endpoints can be found [the deprecated
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
    api/v2/cryptocurrency/info`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Static data is updated only as needed, every 30 seconds.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up).
    **CMC equivalent pages:** Cryptocurrency detail page metadata like
    [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        address (str | Unset):
        skip_invalid (bool | Unset):  Default: False.
        aux (str | Unset):  Default: 'urls,logo,description,tags,platform,date_added,notice'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrenciesInfoResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        symbol=symbol,
        address=address,
        skip_invalid=skip_invalid,
        aux=aux,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    address: str | Unset = UNSET,
    skip_invalid: bool | Unset = False,
    aux: str | Unset = "urls,logo,description,tags,platform,date_added,notice",
) -> (
    CryptocurrenciesInfoResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Metadata

     Returns all static metadata available for one or more cryptocurrencies. This information includes
    details like logo, description, official website URL, social links, and links to a cryptocurrency's
    technical documentation.

    **Please note**: This documentation relates to our updated V2 endpoint, which may be incompatible
    with our V1 versions. Documentation for deprecated endpoints can be found [the deprecated
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
    api/v2/cryptocurrency/info`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    **Cache / Update frequency:** Static data is updated only as needed, every 30 seconds.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up).
    **CMC equivalent pages:** Cryptocurrency detail page metadata like
    [coinmarketcap.com/currencies/bitcoin/](https://coinmarketcap.com/currencies/bitcoin/).

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        address (str | Unset):
        skip_invalid (bool | Unset):  Default: False.
        aux (str | Unset):  Default: 'urls,logo,description,tags,platform,date_added,notice'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrenciesInfoResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            slug=slug,
            symbol=symbol,
            address=address,
            skip_invalid=skip_invalid,
            aux=aux,
        )
    ).parsed
