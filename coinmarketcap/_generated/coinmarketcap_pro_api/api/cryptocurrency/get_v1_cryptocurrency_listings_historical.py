from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cryptocurrency_listings_latest_response_model import CryptocurrencyListingsLatestResponseModel
from ...models.get_v1_cryptocurrency_listings_historical_cryptocurrency_type import (
    GetV1CryptocurrencyListingsHistoricalCryptocurrencyType,
)
from ...models.get_v1_cryptocurrency_listings_historical_sort import (
    GetV1CryptocurrencyListingsHistoricalSort,
)
from ...models.get_v1_cryptocurrency_listings_historical_sort_dir import (
    GetV1CryptocurrencyListingsHistoricalSortDir,
)
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: str,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: GetV1CryptocurrencyListingsHistoricalSort | Unset = "cmc_rank",
    sort_dir: GetV1CryptocurrencyListingsHistoricalSortDir | Unset = UNSET,
    cryptocurrency_type: GetV1CryptocurrencyListingsHistoricalCryptocurrencyType | Unset = "all",
    aux: str | Unset = "platform,tags,date_added,circulating_supply,total_supply,max_supply,cmc_rank,num_market_pairs",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["date"] = date

    params["start"] = start

    params["limit"] = limit

    params["convert"] = convert

    params["convert_id"] = convert_id

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_sort_dir: str | Unset = UNSET
    if not isinstance(sort_dir, Unset):
        json_sort_dir = sort_dir

    params["sort_dir"] = json_sort_dir

    json_cryptocurrency_type: str | Unset = UNSET
    if not isinstance(cryptocurrency_type, Unset):
        json_cryptocurrency_type = cryptocurrency_type

    params["cryptocurrency_type"] = json_cryptocurrency_type

    params["aux"] = aux

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/cryptocurrency/listings/historical",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CryptocurrencyListingsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = CryptocurrencyListingsLatestResponseModel.from_dict(response.json())

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
    CryptocurrencyListingsLatestResponseModel
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
    date: str,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: GetV1CryptocurrencyListingsHistoricalSort | Unset = "cmc_rank",
    sort_dir: GetV1CryptocurrencyListingsHistoricalSortDir | Unset = UNSET,
    cryptocurrency_type: GetV1CryptocurrencyListingsHistoricalCryptocurrencyType | Unset = "all",
    aux: str | Unset = "platform,tags,date_added,circulating_supply,total_supply,max_supply,cmc_rank,num_market_pairs",
) -> Response[
    CryptocurrencyListingsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Listings Historical

     Returns a ranked and sorted list of all cryptocurrencies for a historical UTC date.


    **Technical Notes**
    - This endpoint is identical in format to our `/cryptocurrency/listings/latest` endpoint but is used
    to retrieve historical daily ranking snapshots from the end of each UTC day.
    - Daily snapshots reflect market data at the end of each UTC day and may be requested as far back as
    2013-04-28 (as supported by your plan's historical limits).
    - The required \"date\" parameter can be passed as a Unix timestamp or ISO 8601 date but only the
    date portion of the timestamp will be referenced. It is recommended to send an ISO date format like
    \"2019-10-10\" without time.
    - This endpoint is for retrieving paginated and sorted lists of all currencies. If you require
    historical market data on specific cryptocurrencies you should use
    `/cryptocurrency/quotes/historical`.



    Cryptocurrencies are listed by cmc_rank by default. You may optionally sort against any of the
    following:
    **cmc_rank**: CoinMarketCap's market cap rank as outlined in [our
    methodology](https://coinmarketcap.com/methodology/).
    **name**: The cryptocurrency name.
    **symbol**: The cryptocurrency symbol.
    **market_cap**: market cap (latest trade price x circulating supply).
    **price**: latest average trade price across markets.
    **circulating_supply**: approximate number of coins currently in circulation.
    **total_supply**: approximate total amount of coins in existence right now (minus any coins that
    have been verifiably burned).
    **max_supply**: our best approximation of the maximum amount of coins that will ever exist in the
    lifetime of the currency.
    **num_market_pairs**: number of market pairs across all exchanges trading each currency.
    **volume_24h**: 24 hour trading volume for each currency.
    **percent_change_1h**: 1 hour trading price percentage change for each currency.
    **percent_change_24h**: 24 hour trading price percentage change for each currency.
    **percent_change_7d**: 7 day trading price percentage change for each currency.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
    - Basic (1 year)
    - Builder (3 years)
    - Startup (from 2013)
    - Growth (from 2013)
    - Professional (from 2013)
    - Enterprise (from 2013)

    **Cache / Update frequency:** The last completed UTC day is available 30 minutes after midnight on
    the next UTC day.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our historical daily crypto ranking snapshot pages like this one on
    [February 02, 2014](https://coinmarketcap.com/historical/20140202/).

    Args:
        date (str):
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):
        convert_id (str | Unset):
        sort (GetV1CryptocurrencyListingsHistoricalSort | Unset):  Default: 'cmc_rank'.
        sort_dir (GetV1CryptocurrencyListingsHistoricalSortDir | Unset):
        cryptocurrency_type (GetV1CryptocurrencyListingsHistoricalCryptocurrencyType | Unset):
            Default: 'all'.
        aux (str | Unset):  Default: 'platform,tags,date_added,circulating_supply,total_supply,max
            _supply,cmc_rank,num_market_pairs'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyListingsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        date=date,
        start=start,
        limit=limit,
        convert=convert,
        convert_id=convert_id,
        sort=sort,
        sort_dir=sort_dir,
        cryptocurrency_type=cryptocurrency_type,
        aux=aux,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    date: str,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: GetV1CryptocurrencyListingsHistoricalSort | Unset = "cmc_rank",
    sort_dir: GetV1CryptocurrencyListingsHistoricalSortDir | Unset = UNSET,
    cryptocurrency_type: GetV1CryptocurrencyListingsHistoricalCryptocurrencyType | Unset = "all",
    aux: str | Unset = "platform,tags,date_added,circulating_supply,total_supply,max_supply,cmc_rank,num_market_pairs",
) -> (
    CryptocurrencyListingsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Listings Historical

     Returns a ranked and sorted list of all cryptocurrencies for a historical UTC date.


    **Technical Notes**
    - This endpoint is identical in format to our `/cryptocurrency/listings/latest` endpoint but is used
    to retrieve historical daily ranking snapshots from the end of each UTC day.
    - Daily snapshots reflect market data at the end of each UTC day and may be requested as far back as
    2013-04-28 (as supported by your plan's historical limits).
    - The required \"date\" parameter can be passed as a Unix timestamp or ISO 8601 date but only the
    date portion of the timestamp will be referenced. It is recommended to send an ISO date format like
    \"2019-10-10\" without time.
    - This endpoint is for retrieving paginated and sorted lists of all currencies. If you require
    historical market data on specific cryptocurrencies you should use
    `/cryptocurrency/quotes/historical`.



    Cryptocurrencies are listed by cmc_rank by default. You may optionally sort against any of the
    following:
    **cmc_rank**: CoinMarketCap's market cap rank as outlined in [our
    methodology](https://coinmarketcap.com/methodology/).
    **name**: The cryptocurrency name.
    **symbol**: The cryptocurrency symbol.
    **market_cap**: market cap (latest trade price x circulating supply).
    **price**: latest average trade price across markets.
    **circulating_supply**: approximate number of coins currently in circulation.
    **total_supply**: approximate total amount of coins in existence right now (minus any coins that
    have been verifiably burned).
    **max_supply**: our best approximation of the maximum amount of coins that will ever exist in the
    lifetime of the currency.
    **num_market_pairs**: number of market pairs across all exchanges trading each currency.
    **volume_24h**: 24 hour trading volume for each currency.
    **percent_change_1h**: 1 hour trading price percentage change for each currency.
    **percent_change_24h**: 24 hour trading price percentage change for each currency.
    **percent_change_7d**: 7 day trading price percentage change for each currency.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
    - Basic (1 year)
    - Builder (3 years)
    - Startup (from 2013)
    - Growth (from 2013)
    - Professional (from 2013)
    - Enterprise (from 2013)

    **Cache / Update frequency:** The last completed UTC day is available 30 minutes after midnight on
    the next UTC day.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our historical daily crypto ranking snapshot pages like this one on
    [February 02, 2014](https://coinmarketcap.com/historical/20140202/).

    Args:
        date (str):
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):
        convert_id (str | Unset):
        sort (GetV1CryptocurrencyListingsHistoricalSort | Unset):  Default: 'cmc_rank'.
        sort_dir (GetV1CryptocurrencyListingsHistoricalSortDir | Unset):
        cryptocurrency_type (GetV1CryptocurrencyListingsHistoricalCryptocurrencyType | Unset):
            Default: 'all'.
        aux (str | Unset):  Default: 'platform,tags,date_added,circulating_supply,total_supply,max
            _supply,cmc_rank,num_market_pairs'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyListingsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        date=date,
        start=start,
        limit=limit,
        convert=convert,
        convert_id=convert_id,
        sort=sort,
        sort_dir=sort_dir,
        cryptocurrency_type=cryptocurrency_type,
        aux=aux,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    date: str,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: GetV1CryptocurrencyListingsHistoricalSort | Unset = "cmc_rank",
    sort_dir: GetV1CryptocurrencyListingsHistoricalSortDir | Unset = UNSET,
    cryptocurrency_type: GetV1CryptocurrencyListingsHistoricalCryptocurrencyType | Unset = "all",
    aux: str | Unset = "platform,tags,date_added,circulating_supply,total_supply,max_supply,cmc_rank,num_market_pairs",
) -> Response[
    CryptocurrencyListingsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Listings Historical

     Returns a ranked and sorted list of all cryptocurrencies for a historical UTC date.


    **Technical Notes**
    - This endpoint is identical in format to our `/cryptocurrency/listings/latest` endpoint but is used
    to retrieve historical daily ranking snapshots from the end of each UTC day.
    - Daily snapshots reflect market data at the end of each UTC day and may be requested as far back as
    2013-04-28 (as supported by your plan's historical limits).
    - The required \"date\" parameter can be passed as a Unix timestamp or ISO 8601 date but only the
    date portion of the timestamp will be referenced. It is recommended to send an ISO date format like
    \"2019-10-10\" without time.
    - This endpoint is for retrieving paginated and sorted lists of all currencies. If you require
    historical market data on specific cryptocurrencies you should use
    `/cryptocurrency/quotes/historical`.



    Cryptocurrencies are listed by cmc_rank by default. You may optionally sort against any of the
    following:
    **cmc_rank**: CoinMarketCap's market cap rank as outlined in [our
    methodology](https://coinmarketcap.com/methodology/).
    **name**: The cryptocurrency name.
    **symbol**: The cryptocurrency symbol.
    **market_cap**: market cap (latest trade price x circulating supply).
    **price**: latest average trade price across markets.
    **circulating_supply**: approximate number of coins currently in circulation.
    **total_supply**: approximate total amount of coins in existence right now (minus any coins that
    have been verifiably burned).
    **max_supply**: our best approximation of the maximum amount of coins that will ever exist in the
    lifetime of the currency.
    **num_market_pairs**: number of market pairs across all exchanges trading each currency.
    **volume_24h**: 24 hour trading volume for each currency.
    **percent_change_1h**: 1 hour trading price percentage change for each currency.
    **percent_change_24h**: 24 hour trading price percentage change for each currency.
    **percent_change_7d**: 7 day trading price percentage change for each currency.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
    - Basic (1 year)
    - Builder (3 years)
    - Startup (from 2013)
    - Growth (from 2013)
    - Professional (from 2013)
    - Enterprise (from 2013)

    **Cache / Update frequency:** The last completed UTC day is available 30 minutes after midnight on
    the next UTC day.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our historical daily crypto ranking snapshot pages like this one on
    [February 02, 2014](https://coinmarketcap.com/historical/20140202/).

    Args:
        date (str):
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):
        convert_id (str | Unset):
        sort (GetV1CryptocurrencyListingsHistoricalSort | Unset):  Default: 'cmc_rank'.
        sort_dir (GetV1CryptocurrencyListingsHistoricalSortDir | Unset):
        cryptocurrency_type (GetV1CryptocurrencyListingsHistoricalCryptocurrencyType | Unset):
            Default: 'all'.
        aux (str | Unset):  Default: 'platform,tags,date_added,circulating_supply,total_supply,max
            _supply,cmc_rank,num_market_pairs'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptocurrencyListingsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        date=date,
        start=start,
        limit=limit,
        convert=convert,
        convert_id=convert_id,
        sort=sort,
        sort_dir=sort_dir,
        cryptocurrency_type=cryptocurrency_type,
        aux=aux,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    date: str,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    sort: GetV1CryptocurrencyListingsHistoricalSort | Unset = "cmc_rank",
    sort_dir: GetV1CryptocurrencyListingsHistoricalSortDir | Unset = UNSET,
    cryptocurrency_type: GetV1CryptocurrencyListingsHistoricalCryptocurrencyType | Unset = "all",
    aux: str | Unset = "platform,tags,date_added,circulating_supply,total_supply,max_supply,cmc_rank,num_market_pairs",
) -> (
    CryptocurrencyListingsLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Listings Historical

     Returns a ranked and sorted list of all cryptocurrencies for a historical UTC date.


    **Technical Notes**
    - This endpoint is identical in format to our `/cryptocurrency/listings/latest` endpoint but is used
    to retrieve historical daily ranking snapshots from the end of each UTC day.
    - Daily snapshots reflect market data at the end of each UTC day and may be requested as far back as
    2013-04-28 (as supported by your plan's historical limits).
    - The required \"date\" parameter can be passed as a Unix timestamp or ISO 8601 date but only the
    date portion of the timestamp will be referenced. It is recommended to send an ISO date format like
    \"2019-10-10\" without time.
    - This endpoint is for retrieving paginated and sorted lists of all currencies. If you require
    historical market data on specific cryptocurrencies you should use
    `/cryptocurrency/quotes/historical`.



    Cryptocurrencies are listed by cmc_rank by default. You may optionally sort against any of the
    following:
    **cmc_rank**: CoinMarketCap's market cap rank as outlined in [our
    methodology](https://coinmarketcap.com/methodology/).
    **name**: The cryptocurrency name.
    **symbol**: The cryptocurrency symbol.
    **market_cap**: market cap (latest trade price x circulating supply).
    **price**: latest average trade price across markets.
    **circulating_supply**: approximate number of coins currently in circulation.
    **total_supply**: approximate total amount of coins in existence right now (minus any coins that
    have been verifiably burned).
    **max_supply**: our best approximation of the maximum amount of coins that will ever exist in the
    lifetime of the currency.
    **num_market_pairs**: number of market pairs across all exchanges trading each currency.
    **volume_24h**: 24 hour trading volume for each currency.
    **percent_change_1h**: 1 hour trading price percentage change for each currency.
    **percent_change_24h**: 24 hour trading price percentage change for each currency.
    **percent_change_7d**: 7 day trading price percentage change for each currency.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
    - Basic (1 year)
    - Builder (3 years)
    - Startup (from 2013)
    - Growth (from 2013)
    - Professional (from 2013)
    - Enterprise (from 2013)

    **Cache / Update frequency:** The last completed UTC day is available 30 minutes after midnight on
    the next UTC day.
    **Plan credit use:** 1 call credit per 100 cryptocurrencies returned (rounded up) and 1 call credit
    per `convert` option beyond the first.
    **CMC equivalent pages:** Our historical daily crypto ranking snapshot pages like this one on
    [February 02, 2014](https://coinmarketcap.com/historical/20140202/).

    Args:
        date (str):
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):
        convert_id (str | Unset):
        sort (GetV1CryptocurrencyListingsHistoricalSort | Unset):  Default: 'cmc_rank'.
        sort_dir (GetV1CryptocurrencyListingsHistoricalSortDir | Unset):
        cryptocurrency_type (GetV1CryptocurrencyListingsHistoricalCryptocurrencyType | Unset):
            Default: 'all'.
        aux (str | Unset):  Default: 'platform,tags,date_added,circulating_supply,total_supply,max
            _supply,cmc_rank,num_market_pairs'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptocurrencyListingsLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            start=start,
            limit=limit,
            convert=convert,
            convert_id=convert_id,
            sort=sort,
            sort_dir=sort_dir,
            cryptocurrency_type=cryptocurrency_type,
            aux=aux,
        )
    ).parsed
