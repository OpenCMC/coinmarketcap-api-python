from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...models.tools_price_conversion_response_model import ToolsPriceConversionResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    amount: float,
    id: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    time: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["amount"] = amount

    params["id"] = id

    params["symbol"] = symbol

    params["time"] = time

    params["convert"] = convert

    params["convert_id"] = convert_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tools/price-conversion",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | ToolsPriceConversionResponseModel
    | None
):
    if response.status_code == 200:
        response_200 = ToolsPriceConversionResponseModel.from_dict(response.json())

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
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | ToolsPriceConversionResponseModel
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
    amount: float,
    id: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    time: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | ToolsPriceConversionResponseModel
]:
    """Price Conversion v1 (deprecated)

     Convert an amount of one cryptocurrency or fiat currency into one or more different currencies
    utilizing the latest market rate for each currency. You may optionally pass a historical timestamp
    as `time` to convert values based on historical rates (as your API plan supports).


    **Technical Notes**
    - Latest market rate conversions are accurate to 1 minute of specificity. Historical conversions are
    accurate to 1 minute of specificity outside of non-USD fiat conversions which have 5 minute
    specificity.
    - You may reference a current list of all supported cryptocurrencies via the
    [cryptocurrency/map](/pro-api-reference/cryptocurrency#cryptocurrency-id-map) endpoint. This
    endpoint also returns the supported date ranges for historical conversions via the
    `first_historical_data` and `last_historical_data` properties.
    - Conversions are supported in 93 different fiat currencies and 4 precious metals [as outlined
    here](/guides/standards-and-conventions). Historical fiat conversions are supported as far back as
    2013-04-28.
    - A `last_updated` timestamp is included for both your source currency and each conversion currency.
    This is the timestamp of the closest market rate record referenced for each currency during the
    conversion.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - Basic (Latest market price conversions)
    - Builder (Latest market price conversions + 1 month historical)
    - Startup (Latest market price conversions + 1 month historical)
    - Growth (Latest market price conversions + 3 months historical)
    - Professional (Latest market price conversions + 12 months historical)
    - Enterprise (Latest market price conversions + up to 6 years historical)

    **Cache / Update frequency:** Every 60 seconds for the lastest cryptocurrency and fiat currency
    rates.
    **Plan credit use:** 1 call credit per call and 1 call credit per `convert` option beyond the first.
    **CMC equivalent pages:** Our cryptocurrency conversion page at
    [coinmarketcap.com/converter/](https://coinmarketcap.com/converter/).

    Args:
        amount (float):
        id (str | Unset):
        symbol (str | Unset):
        time (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | ToolsPriceConversionResponseModel]
    """

    kwargs = _get_kwargs(
        amount=amount,
        id=id,
        symbol=symbol,
        time=time,
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
    amount: float,
    id: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    time: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | ToolsPriceConversionResponseModel
    | None
):
    """Price Conversion v1 (deprecated)

     Convert an amount of one cryptocurrency or fiat currency into one or more different currencies
    utilizing the latest market rate for each currency. You may optionally pass a historical timestamp
    as `time` to convert values based on historical rates (as your API plan supports).


    **Technical Notes**
    - Latest market rate conversions are accurate to 1 minute of specificity. Historical conversions are
    accurate to 1 minute of specificity outside of non-USD fiat conversions which have 5 minute
    specificity.
    - You may reference a current list of all supported cryptocurrencies via the
    [cryptocurrency/map](/pro-api-reference/cryptocurrency#cryptocurrency-id-map) endpoint. This
    endpoint also returns the supported date ranges for historical conversions via the
    `first_historical_data` and `last_historical_data` properties.
    - Conversions are supported in 93 different fiat currencies and 4 precious metals [as outlined
    here](/guides/standards-and-conventions). Historical fiat conversions are supported as far back as
    2013-04-28.
    - A `last_updated` timestamp is included for both your source currency and each conversion currency.
    This is the timestamp of the closest market rate record referenced for each currency during the
    conversion.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - Basic (Latest market price conversions)
    - Builder (Latest market price conversions + 1 month historical)
    - Startup (Latest market price conversions + 1 month historical)
    - Growth (Latest market price conversions + 3 months historical)
    - Professional (Latest market price conversions + 12 months historical)
    - Enterprise (Latest market price conversions + up to 6 years historical)

    **Cache / Update frequency:** Every 60 seconds for the lastest cryptocurrency and fiat currency
    rates.
    **Plan credit use:** 1 call credit per call and 1 call credit per `convert` option beyond the first.
    **CMC equivalent pages:** Our cryptocurrency conversion page at
    [coinmarketcap.com/converter/](https://coinmarketcap.com/converter/).

    Args:
        amount (float):
        id (str | Unset):
        symbol (str | Unset):
        time (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | ToolsPriceConversionResponseModel
    """

    return sync_detailed(
        client=client,
        amount=amount,
        id=id,
        symbol=symbol,
        time=time,
        convert=convert,
        convert_id=convert_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    amount: float,
    id: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    time: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | ToolsPriceConversionResponseModel
]:
    """Price Conversion v1 (deprecated)

     Convert an amount of one cryptocurrency or fiat currency into one or more different currencies
    utilizing the latest market rate for each currency. You may optionally pass a historical timestamp
    as `time` to convert values based on historical rates (as your API plan supports).


    **Technical Notes**
    - Latest market rate conversions are accurate to 1 minute of specificity. Historical conversions are
    accurate to 1 minute of specificity outside of non-USD fiat conversions which have 5 minute
    specificity.
    - You may reference a current list of all supported cryptocurrencies via the
    [cryptocurrency/map](/pro-api-reference/cryptocurrency#cryptocurrency-id-map) endpoint. This
    endpoint also returns the supported date ranges for historical conversions via the
    `first_historical_data` and `last_historical_data` properties.
    - Conversions are supported in 93 different fiat currencies and 4 precious metals [as outlined
    here](/guides/standards-and-conventions). Historical fiat conversions are supported as far back as
    2013-04-28.
    - A `last_updated` timestamp is included for both your source currency and each conversion currency.
    This is the timestamp of the closest market rate record referenced for each currency during the
    conversion.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - Basic (Latest market price conversions)
    - Builder (Latest market price conversions + 1 month historical)
    - Startup (Latest market price conversions + 1 month historical)
    - Growth (Latest market price conversions + 3 months historical)
    - Professional (Latest market price conversions + 12 months historical)
    - Enterprise (Latest market price conversions + up to 6 years historical)

    **Cache / Update frequency:** Every 60 seconds for the lastest cryptocurrency and fiat currency
    rates.
    **Plan credit use:** 1 call credit per call and 1 call credit per `convert` option beyond the first.
    **CMC equivalent pages:** Our cryptocurrency conversion page at
    [coinmarketcap.com/converter/](https://coinmarketcap.com/converter/).

    Args:
        amount (float):
        id (str | Unset):
        symbol (str | Unset):
        time (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | ToolsPriceConversionResponseModel]
    """

    kwargs = _get_kwargs(
        amount=amount,
        id=id,
        symbol=symbol,
        time=time,
        convert=convert,
        convert_id=convert_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    amount: float,
    id: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    time: str | Unset = UNSET,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | ToolsPriceConversionResponseModel
    | None
):
    """Price Conversion v1 (deprecated)

     Convert an amount of one cryptocurrency or fiat currency into one or more different currencies
    utilizing the latest market rate for each currency. You may optionally pass a historical timestamp
    as `time` to convert values based on historical rates (as your API plan supports).


    **Technical Notes**
    - Latest market rate conversions are accurate to 1 minute of specificity. Historical conversions are
    accurate to 1 minute of specificity outside of non-USD fiat conversions which have 5 minute
    specificity.
    - You may reference a current list of all supported cryptocurrencies via the
    [cryptocurrency/map](/pro-api-reference/cryptocurrency#cryptocurrency-id-map) endpoint. This
    endpoint also returns the supported date ranges for historical conversions via the
    `first_historical_data` and `last_historical_data` properties.
    - Conversions are supported in 93 different fiat currencies and 4 precious metals [as outlined
    here](/guides/standards-and-conventions). Historical fiat conversions are supported as far back as
    2013-04-28.
    - A `last_updated` timestamp is included for both your source currency and each conversion currency.
    This is the timestamp of the closest market rate record referenced for each currency during the
    conversion.

    **This endpoint is available on the following [API plans](https://coinmarketcap.com/api/pricing/):**
    - Basic (Latest market price conversions)
    - Builder (Latest market price conversions + 1 month historical)
    - Startup (Latest market price conversions + 1 month historical)
    - Growth (Latest market price conversions + 3 months historical)
    - Professional (Latest market price conversions + 12 months historical)
    - Enterprise (Latest market price conversions + up to 6 years historical)

    **Cache / Update frequency:** Every 60 seconds for the lastest cryptocurrency and fiat currency
    rates.
    **Plan credit use:** 1 call credit per call and 1 call credit per `convert` option beyond the first.
    **CMC equivalent pages:** Our cryptocurrency conversion page at
    [coinmarketcap.com/converter/](https://coinmarketcap.com/converter/).

    Args:
        amount (float):
        id (str | Unset):
        symbol (str | Unset):
        time (str | Unset):
        convert (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | ToolsPriceConversionResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            amount=amount,
            id=id,
            symbol=symbol,
            time=time,
            convert=convert,
            convert_id=convert_id,
        )
    ).parsed
