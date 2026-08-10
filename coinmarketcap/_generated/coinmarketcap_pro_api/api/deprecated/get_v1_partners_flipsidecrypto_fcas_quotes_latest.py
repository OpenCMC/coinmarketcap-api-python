from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fcas_quote_latest_response_model import FCASQuoteLatestResponseModel
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
    aux: str | Unset = "point_change_24h,percent_change_24h",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["slug"] = slug

    params["symbol"] = symbol

    params["aux"] = aux

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/partners/flipside-crypto/fcas/quotes/latest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FCASQuoteLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = FCASQuoteLatestResponseModel.from_dict(response.json())

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
    FCASQuoteLatestResponseModel
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
    aux: str | Unset = "point_change_24h,percent_change_24h",
) -> Response[
    FCASQuoteLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""FCAS Quotes Latest (deprecated)

     Returns the latest FCAS score for 1 or more cryptocurrencies. FCAS ratings are on a 0-1000 point
    scale with a corresponding letter grade and is updated once a day at UTC midnight.



    FCAS stands for Fundamental Crypto Asset Score, a single, consistently comparable value for
    measuring cryptocurrency project health. FCAS measures User Activity, Developer Behavior and Market
    Maturity and is provided by <a rel=\"noopener noreferrer\" href=\"https://www.flipsidecrypto.com/\"
    target=\"_blank\">FlipSide Crypto</a>. Find out more about <a rel=\"noopener noreferrer\"
    href=\"https://www.flipsidecrypto.com/fcas-explained\" target=\"_blank\">FCAS methodology</a>. Users
    interested in FCAS historical data including sub-component scoring may inquire through our <a
    rel=\"noopener noreferrer\" href=\"https://pro.coinmarketcap.com/contact-data/\"
    target=\"_blank\">CSV Data Delivery</a> request form.

    *Disclaimer: Ratings that are calculated by third party organizations and are not influenced or
    endorsed by CoinMarketCap in any way.*

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Once a day at UTC midnight.
    **Plan credit use:** 1 call credit per 100 FCAS scores returned (rounded up).
    **CMC equivalent pages:** The FCAS ratings available under our cryptocurrency ratings tab like [coin
    marketcap.com/currencies/bitcoin/#ratings](https://coinmarketcap.com/currencies/bitcoin/#ratings).

    ***NOTE:** Use this endpoint to request the latest FCAS score for specific cryptocurrencies. If you
    require FCAS for all supported cryptocurrencies use `/v1/partners/flipside-
    crypto/fcas/listings/latest` which is optimized for that purpose. The response data between these
    endpoints is otherwise the same.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        aux (str | Unset):  Default: 'point_change_24h,percent_change_24h'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FCASQuoteLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
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
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    aux: str | Unset = "point_change_24h,percent_change_24h",
) -> (
    FCASQuoteLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""FCAS Quotes Latest (deprecated)

     Returns the latest FCAS score for 1 or more cryptocurrencies. FCAS ratings are on a 0-1000 point
    scale with a corresponding letter grade and is updated once a day at UTC midnight.



    FCAS stands for Fundamental Crypto Asset Score, a single, consistently comparable value for
    measuring cryptocurrency project health. FCAS measures User Activity, Developer Behavior and Market
    Maturity and is provided by <a rel=\"noopener noreferrer\" href=\"https://www.flipsidecrypto.com/\"
    target=\"_blank\">FlipSide Crypto</a>. Find out more about <a rel=\"noopener noreferrer\"
    href=\"https://www.flipsidecrypto.com/fcas-explained\" target=\"_blank\">FCAS methodology</a>. Users
    interested in FCAS historical data including sub-component scoring may inquire through our <a
    rel=\"noopener noreferrer\" href=\"https://pro.coinmarketcap.com/contact-data/\"
    target=\"_blank\">CSV Data Delivery</a> request form.

    *Disclaimer: Ratings that are calculated by third party organizations and are not influenced or
    endorsed by CoinMarketCap in any way.*

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Once a day at UTC midnight.
    **Plan credit use:** 1 call credit per 100 FCAS scores returned (rounded up).
    **CMC equivalent pages:** The FCAS ratings available under our cryptocurrency ratings tab like [coin
    marketcap.com/currencies/bitcoin/#ratings](https://coinmarketcap.com/currencies/bitcoin/#ratings).

    ***NOTE:** Use this endpoint to request the latest FCAS score for specific cryptocurrencies. If you
    require FCAS for all supported cryptocurrencies use `/v1/partners/flipside-
    crypto/fcas/listings/latest` which is optimized for that purpose. The response data between these
    endpoints is otherwise the same.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        aux (str | Unset):  Default: 'point_change_24h,percent_change_24h'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FCASQuoteLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        id=id,
        slug=slug,
        symbol=symbol,
        aux=aux,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    aux: str | Unset = "point_change_24h,percent_change_24h",
) -> Response[
    FCASQuoteLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""FCAS Quotes Latest (deprecated)

     Returns the latest FCAS score for 1 or more cryptocurrencies. FCAS ratings are on a 0-1000 point
    scale with a corresponding letter grade and is updated once a day at UTC midnight.



    FCAS stands for Fundamental Crypto Asset Score, a single, consistently comparable value for
    measuring cryptocurrency project health. FCAS measures User Activity, Developer Behavior and Market
    Maturity and is provided by <a rel=\"noopener noreferrer\" href=\"https://www.flipsidecrypto.com/\"
    target=\"_blank\">FlipSide Crypto</a>. Find out more about <a rel=\"noopener noreferrer\"
    href=\"https://www.flipsidecrypto.com/fcas-explained\" target=\"_blank\">FCAS methodology</a>. Users
    interested in FCAS historical data including sub-component scoring may inquire through our <a
    rel=\"noopener noreferrer\" href=\"https://pro.coinmarketcap.com/contact-data/\"
    target=\"_blank\">CSV Data Delivery</a> request form.

    *Disclaimer: Ratings that are calculated by third party organizations and are not influenced or
    endorsed by CoinMarketCap in any way.*

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Once a day at UTC midnight.
    **Plan credit use:** 1 call credit per 100 FCAS scores returned (rounded up).
    **CMC equivalent pages:** The FCAS ratings available under our cryptocurrency ratings tab like [coin
    marketcap.com/currencies/bitcoin/#ratings](https://coinmarketcap.com/currencies/bitcoin/#ratings).

    ***NOTE:** Use this endpoint to request the latest FCAS score for specific cryptocurrencies. If you
    require FCAS for all supported cryptocurrencies use `/v1/partners/flipside-
    crypto/fcas/listings/latest` which is optimized for that purpose. The response data between these
    endpoints is otherwise the same.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        aux (str | Unset):  Default: 'point_change_24h,percent_change_24h'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FCASQuoteLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        slug=slug,
        symbol=symbol,
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
    aux: str | Unset = "point_change_24h,percent_change_24h",
) -> (
    FCASQuoteLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""FCAS Quotes Latest (deprecated)

     Returns the latest FCAS score for 1 or more cryptocurrencies. FCAS ratings are on a 0-1000 point
    scale with a corresponding letter grade and is updated once a day at UTC midnight.



    FCAS stands for Fundamental Crypto Asset Score, a single, consistently comparable value for
    measuring cryptocurrency project health. FCAS measures User Activity, Developer Behavior and Market
    Maturity and is provided by <a rel=\"noopener noreferrer\" href=\"https://www.flipsidecrypto.com/\"
    target=\"_blank\">FlipSide Crypto</a>. Find out more about <a rel=\"noopener noreferrer\"
    href=\"https://www.flipsidecrypto.com/fcas-explained\" target=\"_blank\">FCAS methodology</a>. Users
    interested in FCAS historical data including sub-component scoring may inquire through our <a
    rel=\"noopener noreferrer\" href=\"https://pro.coinmarketcap.com/contact-data/\"
    target=\"_blank\">CSV Data Delivery</a> request form.

    *Disclaimer: Ratings that are calculated by third party organizations and are not influenced or
    endorsed by CoinMarketCap in any way.*

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Once a day at UTC midnight.
    **Plan credit use:** 1 call credit per 100 FCAS scores returned (rounded up).
    **CMC equivalent pages:** The FCAS ratings available under our cryptocurrency ratings tab like [coin
    marketcap.com/currencies/bitcoin/#ratings](https://coinmarketcap.com/currencies/bitcoin/#ratings).

    ***NOTE:** Use this endpoint to request the latest FCAS score for specific cryptocurrencies. If you
    require FCAS for all supported cryptocurrencies use `/v1/partners/flipside-
    crypto/fcas/listings/latest` which is optimized for that purpose. The response data between these
    endpoints is otherwise the same.*

    Args:
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        aux (str | Unset):  Default: 'point_change_24h,percent_change_24h'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FCASQuoteLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            slug=slug,
            symbol=symbol,
            aux=aux,
        )
    ).parsed
