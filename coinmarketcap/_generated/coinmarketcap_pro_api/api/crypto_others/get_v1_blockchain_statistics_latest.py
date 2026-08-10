from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.blockchain_statistics_latest_response_model import BlockchainStatisticsLatestResponseModel
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    slug: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["symbol"] = symbol

    params["slug"] = slug

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/blockchain/statistics/latest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    BlockchainStatisticsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = BlockchainStatisticsLatestResponseModel.from_dict(response.json())

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
    BlockchainStatisticsLatestResponseModel
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
    symbol: str | Unset = UNSET,
    slug: str | Unset = UNSET,
) -> Response[
    BlockchainStatisticsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """Statistics Latest

     Returns the latest blockchain statistics data for 1 or more blockchains. Bitcoin, Litecoin, and
    Ethereum are currently supported. Additional blockchains will be made available on a regular basis.



      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - ~~Startup~~
      - ~~Growth~~
      - ~~Professional~~
      - Enterprise

    **Cache / Update frequency:** Every 15 seconds.
    **Plan credit use:** 1 call credit per request.
    **CMC equivalent pages:** Our blockchain explorer pages like
    [blockchain.coinmarketcap.com/](https://blockchain.coinmarketcap.com/).

    Args:
        id (str | Unset):
        symbol (str | Unset):
        slug (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockchainStatisticsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        symbol=symbol,
        slug=slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    slug: str | Unset = UNSET,
) -> (
    BlockchainStatisticsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """Statistics Latest

     Returns the latest blockchain statistics data for 1 or more blockchains. Bitcoin, Litecoin, and
    Ethereum are currently supported. Additional blockchains will be made available on a regular basis.



      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - ~~Startup~~
      - ~~Growth~~
      - ~~Professional~~
      - Enterprise

    **Cache / Update frequency:** Every 15 seconds.
    **Plan credit use:** 1 call credit per request.
    **CMC equivalent pages:** Our blockchain explorer pages like
    [blockchain.coinmarketcap.com/](https://blockchain.coinmarketcap.com/).

    Args:
        id (str | Unset):
        symbol (str | Unset):
        slug (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlockchainStatisticsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        id=id,
        symbol=symbol,
        slug=slug,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    slug: str | Unset = UNSET,
) -> Response[
    BlockchainStatisticsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """Statistics Latest

     Returns the latest blockchain statistics data for 1 or more blockchains. Bitcoin, Litecoin, and
    Ethereum are currently supported. Additional blockchains will be made available on a regular basis.



      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - ~~Startup~~
      - ~~Growth~~
      - ~~Professional~~
      - Enterprise

    **Cache / Update frequency:** Every 15 seconds.
    **Plan credit use:** 1 call credit per request.
    **CMC equivalent pages:** Our blockchain explorer pages like
    [blockchain.coinmarketcap.com/](https://blockchain.coinmarketcap.com/).

    Args:
        id (str | Unset):
        symbol (str | Unset):
        slug (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockchainStatisticsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        symbol=symbol,
        slug=slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    slug: str | Unset = UNSET,
) -> (
    BlockchainStatisticsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """Statistics Latest

     Returns the latest blockchain statistics data for 1 or more blockchains. Bitcoin, Litecoin, and
    Ethereum are currently supported. Additional blockchains will be made available on a regular basis.



      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - ~~Startup~~
      - ~~Growth~~
      - ~~Professional~~
      - Enterprise

    **Cache / Update frequency:** Every 15 seconds.
    **Plan credit use:** 1 call credit per request.
    **CMC equivalent pages:** Our blockchain explorer pages like
    [blockchain.coinmarketcap.com/](https://blockchain.coinmarketcap.com/).

    Args:
        id (str | Unset):
        symbol (str | Unset):
        slug (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlockchainStatisticsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            symbol=symbol,
            slug=slug,
        )
    ).parsed
