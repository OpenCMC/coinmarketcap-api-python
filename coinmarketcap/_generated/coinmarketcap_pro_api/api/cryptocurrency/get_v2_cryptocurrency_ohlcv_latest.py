from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cryptocurrency_ohlcv_latest_response_model import CryptocurrencyOHLCVLatestResponseModel
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
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params["symbol"] = symbol

    params["convert"] = convert

    params["convert_id"] = convert_id

    params["skip_invalid"] = skip_invalid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/cryptocurrency/ohlcv/latest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CryptocurrencyOHLCVLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = CryptocurrencyOHLCVLatestResponseModel.from_dict(response.json())

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
    CryptocurrencyOHLCVLatestResponseModel
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
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> Response[
    CryptocurrencyOHLCVLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """OHLCV Latest

     Returns the latest OHLCV (Open, High, Low, Close, Volume) market values for one or more
    cryptocurrencies for the current UTC day. Since the current UTC day is still active these values are
    updated frequently. You can find the final calculated OHLCV values for the last completed UTC day
    along with all historic days using /cryptocurrency/ohlcv/historical.

    **Please note**: This documentation relates to our updated V2 endpoint, which may be incompatible
    with our V1 versions. Documentation for deprecated endpoints can be found [the deprecated
    section](/pro-api-reference/deprecated).


      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - Startup
      - Growth
      - Professional
      - Enterprise

      **Cache / Update frequency:** Every 10 minutes. Additional OHLCV intervals and 1 minute updates
    will be available in the future.
      **Plan credit use:** 1 call credit per 100 OHLCV values returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
      **CMC equivalent pages:** No equivalent, this data is only available via API.

    Args:
        id (str | Unset):
        symbol (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyOHLCVLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        symbol=symbol,
        convert=convert,
        convert_id=convert_id,
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
    symbol: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> (
    CryptocurrencyOHLCVLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """OHLCV Latest

     Returns the latest OHLCV (Open, High, Low, Close, Volume) market values for one or more
    cryptocurrencies for the current UTC day. Since the current UTC day is still active these values are
    updated frequently. You can find the final calculated OHLCV values for the last completed UTC day
    along with all historic days using /cryptocurrency/ohlcv/historical.

    **Please note**: This documentation relates to our updated V2 endpoint, which may be incompatible
    with our V1 versions. Documentation for deprecated endpoints can be found [the deprecated
    section](/pro-api-reference/deprecated).


      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - Startup
      - Growth
      - Professional
      - Enterprise

      **Cache / Update frequency:** Every 10 minutes. Additional OHLCV intervals and 1 minute updates
    will be available in the future.
      **Plan credit use:** 1 call credit per 100 OHLCV values returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
      **CMC equivalent pages:** No equivalent, this data is only available via API.

    Args:
        id (str | Unset):
        symbol (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyOHLCVLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        id=id,
        symbol=symbol,
        convert=convert,
        convert_id=convert_id,
        skip_invalid=skip_invalid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> Response[
    CryptocurrencyOHLCVLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """OHLCV Latest

     Returns the latest OHLCV (Open, High, Low, Close, Volume) market values for one or more
    cryptocurrencies for the current UTC day. Since the current UTC day is still active these values are
    updated frequently. You can find the final calculated OHLCV values for the last completed UTC day
    along with all historic days using /cryptocurrency/ohlcv/historical.

    **Please note**: This documentation relates to our updated V2 endpoint, which may be incompatible
    with our V1 versions. Documentation for deprecated endpoints can be found [the deprecated
    section](/pro-api-reference/deprecated).


      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - Startup
      - Growth
      - Professional
      - Enterprise

      **Cache / Update frequency:** Every 10 minutes. Additional OHLCV intervals and 1 minute updates
    will be available in the future.
      **Plan credit use:** 1 call credit per 100 OHLCV values returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
      **CMC equivalent pages:** No equivalent, this data is only available via API.

    Args:
        id (str | Unset):
        symbol (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyOHLCVLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
        symbol=symbol,
        convert=convert,
        convert_id=convert_id,
        skip_invalid=skip_invalid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: bool | Unset = True,
) -> (
    CryptocurrencyOHLCVLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """OHLCV Latest

     Returns the latest OHLCV (Open, High, Low, Close, Volume) market values for one or more
    cryptocurrencies for the current UTC day. Since the current UTC day is still active these values are
    updated frequently. You can find the final calculated OHLCV values for the last completed UTC day
    along with all historic days using /cryptocurrency/ohlcv/historical.

    **Please note**: This documentation relates to our updated V2 endpoint, which may be incompatible
    with our V1 versions. Documentation for deprecated endpoints can be found [the deprecated
    section](/pro-api-reference/deprecated).


      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - ~~Basic~~
      - ~~Builder~~
      - Startup
      - Growth
      - Professional
      - Enterprise

      **Cache / Update frequency:** Every 10 minutes. Additional OHLCV intervals and 1 minute updates
    will be available in the future.
      **Plan credit use:** 1 call credit per 100 OHLCV values returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
      **CMC equivalent pages:** No equivalent, this data is only available via API.

    Args:
        id (str | Unset):
        symbol (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):
        skip_invalid (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyOHLCVLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            symbol=symbol,
            convert=convert,
            convert_id=convert_id,
            skip_invalid=skip_invalid,
        )
    ).parsed
