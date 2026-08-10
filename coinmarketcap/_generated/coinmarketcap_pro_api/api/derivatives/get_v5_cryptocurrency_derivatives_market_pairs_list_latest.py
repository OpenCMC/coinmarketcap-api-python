from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.derivatives_crypto_market_pairs_list_latest_response_model import (
    DerivativesCryptoMarketPairsListLatestResponseModel,
)
from ...models.get_v5_cryptocurrency_derivatives_market_pairs_list_latest_category import (
    GetV5CryptocurrencyDerivativesMarketPairsListLatestCategory,
)
from ...models.get_v5_cryptocurrency_derivatives_market_pairs_list_latest_center_type import (
    GetV5CryptocurrencyDerivativesMarketPairsListLatestCenterType,
)
from ...models.get_v5_cryptocurrency_derivatives_market_pairs_list_latest_fee_type import (
    GetV5CryptocurrencyDerivativesMarketPairsListLatestFeeType,
)
from ...models.get_v5_cryptocurrency_derivatives_market_pairs_list_latest_sort import (
    GetV5CryptocurrencyDerivativesMarketPairsListLatestSort,
)
from ...models.get_v5_cryptocurrency_derivatives_market_pairs_list_latest_sort_dir import (
    GetV5CryptocurrencyDerivativesMarketPairsListLatestSortDir,
)
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    crypto_id: int | Unset = UNSET,
    crypto_slug: str | Unset = UNSET,
    crypto_symbol: str | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    sort_dir: GetV5CryptocurrencyDerivativesMarketPairsListLatestSortDir | Unset = "desc",
    sort: GetV5CryptocurrencyDerivativesMarketPairsListLatestSort | Unset = "volume_24h_strict",
    category: GetV5CryptocurrencyDerivativesMarketPairsListLatestCategory | Unset = "all",
    fee_type: GetV5CryptocurrencyDerivativesMarketPairsListLatestFeeType | Unset = "all",
    matched_id: str | Unset = UNSET,
    matched_symbol: str | Unset = UNSET,
    center_type: GetV5CryptocurrencyDerivativesMarketPairsListLatestCenterType | Unset = "all",
    convert: str | Unset = "USD",
    convert_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["crypto_id"] = crypto_id

    params["crypto_slug"] = crypto_slug

    params["crypto_symbol"] = crypto_symbol

    params["start"] = start

    params["limit"] = limit

    json_sort_dir: str | Unset = UNSET
    if not isinstance(sort_dir, Unset):
        json_sort_dir = sort_dir

    params["sort_dir"] = json_sort_dir

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_category: str | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = category

    params["category"] = json_category

    json_fee_type: str | Unset = UNSET
    if not isinstance(fee_type, Unset):
        json_fee_type = fee_type

    params["fee_type"] = json_fee_type

    params["matched_id"] = matched_id

    params["matched_symbol"] = matched_symbol

    json_center_type: str | Unset = UNSET
    if not isinstance(center_type, Unset):
        json_center_type = center_type

    params["center_type"] = json_center_type

    params["convert"] = convert

    params["convert_id"] = convert_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v5/cryptocurrency/derivatives/market-pairs/list/latest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DerivativesCryptoMarketPairsListLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = DerivativesCryptoMarketPairsListLatestResponseModel.from_dict(response.json())

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
    DerivativesCryptoMarketPairsListLatestResponseModel
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
    crypto_id: int | Unset = UNSET,
    crypto_slug: str | Unset = UNSET,
    crypto_symbol: str | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    sort_dir: GetV5CryptocurrencyDerivativesMarketPairsListLatestSortDir | Unset = "desc",
    sort: GetV5CryptocurrencyDerivativesMarketPairsListLatestSort | Unset = "volume_24h_strict",
    category: GetV5CryptocurrencyDerivativesMarketPairsListLatestCategory | Unset = "all",
    fee_type: GetV5CryptocurrencyDerivativesMarketPairsListLatestFeeType | Unset = "all",
    matched_id: str | Unset = UNSET,
    matched_symbol: str | Unset = UNSET,
    center_type: GetV5CryptocurrencyDerivativesMarketPairsListLatestCenterType | Unset = "all",
    convert: str | Unset = "USD",
    convert_id: str | Unset = UNSET,
) -> Response[
    DerivativesCryptoMarketPairsListLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """Derivative market pairs by cryptocurrency

     Returns all active derivative market pairs that CoinMarketCap tracks for a given cryptocurrency,
    across exchanges.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Free
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.

    Args:
        crypto_id (int | Unset):  Example: 1.
        crypto_slug (str | Unset):  Example: bitcoin.
        crypto_symbol (str | Unset):  Example: BTC.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        sort_dir (GetV5CryptocurrencyDerivativesMarketPairsListLatestSortDir | Unset):  Default:
            'desc'.
        sort (GetV5CryptocurrencyDerivativesMarketPairsListLatestSort | Unset):  Default:
            'volume_24h_strict'.
        category (GetV5CryptocurrencyDerivativesMarketPairsListLatestCategory | Unset):  Default:
            'all'.
        fee_type (GetV5CryptocurrencyDerivativesMarketPairsListLatestFeeType | Unset):  Default:
            'all'.
        matched_id (str | Unset):  Example: 2781.
        matched_symbol (str | Unset):  Example: USD.
        center_type (GetV5CryptocurrencyDerivativesMarketPairsListLatestCenterType | Unset):
            Default: 'all'.
        convert (str | Unset):  Default: 'USD'.
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DerivativesCryptoMarketPairsListLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        crypto_id=crypto_id,
        crypto_slug=crypto_slug,
        crypto_symbol=crypto_symbol,
        start=start,
        limit=limit,
        sort_dir=sort_dir,
        sort=sort,
        category=category,
        fee_type=fee_type,
        matched_id=matched_id,
        matched_symbol=matched_symbol,
        center_type=center_type,
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
    crypto_id: int | Unset = UNSET,
    crypto_slug: str | Unset = UNSET,
    crypto_symbol: str | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    sort_dir: GetV5CryptocurrencyDerivativesMarketPairsListLatestSortDir | Unset = "desc",
    sort: GetV5CryptocurrencyDerivativesMarketPairsListLatestSort | Unset = "volume_24h_strict",
    category: GetV5CryptocurrencyDerivativesMarketPairsListLatestCategory | Unset = "all",
    fee_type: GetV5CryptocurrencyDerivativesMarketPairsListLatestFeeType | Unset = "all",
    matched_id: str | Unset = UNSET,
    matched_symbol: str | Unset = UNSET,
    center_type: GetV5CryptocurrencyDerivativesMarketPairsListLatestCenterType | Unset = "all",
    convert: str | Unset = "USD",
    convert_id: str | Unset = UNSET,
) -> (
    DerivativesCryptoMarketPairsListLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """Derivative market pairs by cryptocurrency

     Returns all active derivative market pairs that CoinMarketCap tracks for a given cryptocurrency,
    across exchanges.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Free
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.

    Args:
        crypto_id (int | Unset):  Example: 1.
        crypto_slug (str | Unset):  Example: bitcoin.
        crypto_symbol (str | Unset):  Example: BTC.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        sort_dir (GetV5CryptocurrencyDerivativesMarketPairsListLatestSortDir | Unset):  Default:
            'desc'.
        sort (GetV5CryptocurrencyDerivativesMarketPairsListLatestSort | Unset):  Default:
            'volume_24h_strict'.
        category (GetV5CryptocurrencyDerivativesMarketPairsListLatestCategory | Unset):  Default:
            'all'.
        fee_type (GetV5CryptocurrencyDerivativesMarketPairsListLatestFeeType | Unset):  Default:
            'all'.
        matched_id (str | Unset):  Example: 2781.
        matched_symbol (str | Unset):  Example: USD.
        center_type (GetV5CryptocurrencyDerivativesMarketPairsListLatestCenterType | Unset):
            Default: 'all'.
        convert (str | Unset):  Default: 'USD'.
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DerivativesCryptoMarketPairsListLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        crypto_id=crypto_id,
        crypto_slug=crypto_slug,
        crypto_symbol=crypto_symbol,
        start=start,
        limit=limit,
        sort_dir=sort_dir,
        sort=sort,
        category=category,
        fee_type=fee_type,
        matched_id=matched_id,
        matched_symbol=matched_symbol,
        center_type=center_type,
        convert=convert,
        convert_id=convert_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    crypto_id: int | Unset = UNSET,
    crypto_slug: str | Unset = UNSET,
    crypto_symbol: str | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    sort_dir: GetV5CryptocurrencyDerivativesMarketPairsListLatestSortDir | Unset = "desc",
    sort: GetV5CryptocurrencyDerivativesMarketPairsListLatestSort | Unset = "volume_24h_strict",
    category: GetV5CryptocurrencyDerivativesMarketPairsListLatestCategory | Unset = "all",
    fee_type: GetV5CryptocurrencyDerivativesMarketPairsListLatestFeeType | Unset = "all",
    matched_id: str | Unset = UNSET,
    matched_symbol: str | Unset = UNSET,
    center_type: GetV5CryptocurrencyDerivativesMarketPairsListLatestCenterType | Unset = "all",
    convert: str | Unset = "USD",
    convert_id: str | Unset = UNSET,
) -> Response[
    DerivativesCryptoMarketPairsListLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """Derivative market pairs by cryptocurrency

     Returns all active derivative market pairs that CoinMarketCap tracks for a given cryptocurrency,
    across exchanges.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Free
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.

    Args:
        crypto_id (int | Unset):  Example: 1.
        crypto_slug (str | Unset):  Example: bitcoin.
        crypto_symbol (str | Unset):  Example: BTC.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        sort_dir (GetV5CryptocurrencyDerivativesMarketPairsListLatestSortDir | Unset):  Default:
            'desc'.
        sort (GetV5CryptocurrencyDerivativesMarketPairsListLatestSort | Unset):  Default:
            'volume_24h_strict'.
        category (GetV5CryptocurrencyDerivativesMarketPairsListLatestCategory | Unset):  Default:
            'all'.
        fee_type (GetV5CryptocurrencyDerivativesMarketPairsListLatestFeeType | Unset):  Default:
            'all'.
        matched_id (str | Unset):  Example: 2781.
        matched_symbol (str | Unset):  Example: USD.
        center_type (GetV5CryptocurrencyDerivativesMarketPairsListLatestCenterType | Unset):
            Default: 'all'.
        convert (str | Unset):  Default: 'USD'.
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DerivativesCryptoMarketPairsListLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        crypto_id=crypto_id,
        crypto_slug=crypto_slug,
        crypto_symbol=crypto_symbol,
        start=start,
        limit=limit,
        sort_dir=sort_dir,
        sort=sort,
        category=category,
        fee_type=fee_type,
        matched_id=matched_id,
        matched_symbol=matched_symbol,
        center_type=center_type,
        convert=convert,
        convert_id=convert_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    crypto_id: int | Unset = UNSET,
    crypto_slug: str | Unset = UNSET,
    crypto_symbol: str | Unset = UNSET,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    sort_dir: GetV5CryptocurrencyDerivativesMarketPairsListLatestSortDir | Unset = "desc",
    sort: GetV5CryptocurrencyDerivativesMarketPairsListLatestSort | Unset = "volume_24h_strict",
    category: GetV5CryptocurrencyDerivativesMarketPairsListLatestCategory | Unset = "all",
    fee_type: GetV5CryptocurrencyDerivativesMarketPairsListLatestFeeType | Unset = "all",
    matched_id: str | Unset = UNSET,
    matched_symbol: str | Unset = UNSET,
    center_type: GetV5CryptocurrencyDerivativesMarketPairsListLatestCenterType | Unset = "all",
    convert: str | Unset = "USD",
    convert_id: str | Unset = UNSET,
) -> (
    DerivativesCryptoMarketPairsListLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """Derivative market pairs by cryptocurrency

     Returns all active derivative market pairs that CoinMarketCap tracks for a given cryptocurrency,
    across exchanges.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Free
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 60 seconds.

    Args:
        crypto_id (int | Unset):  Example: 1.
        crypto_slug (str | Unset):  Example: bitcoin.
        crypto_symbol (str | Unset):  Example: BTC.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        sort_dir (GetV5CryptocurrencyDerivativesMarketPairsListLatestSortDir | Unset):  Default:
            'desc'.
        sort (GetV5CryptocurrencyDerivativesMarketPairsListLatestSort | Unset):  Default:
            'volume_24h_strict'.
        category (GetV5CryptocurrencyDerivativesMarketPairsListLatestCategory | Unset):  Default:
            'all'.
        fee_type (GetV5CryptocurrencyDerivativesMarketPairsListLatestFeeType | Unset):  Default:
            'all'.
        matched_id (str | Unset):  Example: 2781.
        matched_symbol (str | Unset):  Example: USD.
        center_type (GetV5CryptocurrencyDerivativesMarketPairsListLatestCenterType | Unset):
            Default: 'all'.
        convert (str | Unset):  Default: 'USD'.
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DerivativesCryptoMarketPairsListLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            crypto_id=crypto_id,
            crypto_slug=crypto_slug,
            crypto_symbol=crypto_symbol,
            start=start,
            limit=limit,
            sort_dir=sort_dir,
            sort=sort,
            category=category,
            fee_type=fee_type,
            matched_id=matched_id,
            matched_symbol=matched_symbol,
            center_type=center_type,
            convert=convert,
            convert_id=convert_id,
        )
    ).parsed
