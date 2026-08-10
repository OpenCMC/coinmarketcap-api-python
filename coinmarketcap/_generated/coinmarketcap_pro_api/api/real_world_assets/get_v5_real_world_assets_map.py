from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v5_real_world_assets_map_asset_type import (
    GetV5RealWorldAssetsMapAssetType,
)
from ...models.get_v5_real_world_assets_map_sort import (
    GetV5RealWorldAssetsMapSort,
)
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...models.rwaid_map_response_model import RWAIDMapResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    asset_type: GetV5RealWorldAssetsMapAssetType | Unset = UNSET,
    symbol: str | Unset = UNSET,
    sort: GetV5RealWorldAssetsMapSort | Unset = "rwa_id",
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_asset_type: str | Unset = UNSET
    if not isinstance(asset_type, Unset):
        json_asset_type = asset_type

    params["asset_type"] = json_asset_type

    params["symbol"] = symbol

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v5/real-world-assets/map",
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
    | RWAIDMapResponseModel
    | None
):
    if response.status_code == 200:
        response_200 = RWAIDMapResponseModel.from_dict(response.json())

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
    | RWAIDMapResponseModel
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
    asset_type: GetV5RealWorldAssetsMapAssetType | Unset = UNSET,
    symbol: str | Unset = UNSET,
    sort: GetV5RealWorldAssetsMapSort | Unset = "rwa_id",
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAIDMapResponseModel
]:
    """RWA ID Map

     Returns a mapping of all Real-World Asset (RWA) assets to their unique `rwa_id`. Use this
    lightweight lookup to resolve the correct `rwa_id` (the stable identifier we recommend over
    symbols/tickers) before calling the heavier info, asset-list, market-pairs, or historical endpoints.
    No market data is returned here.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 30 seconds.
    **Plan credit use:** No credit is needed when querying this endpoint.

    Args:
        asset_type (GetV5RealWorldAssetsMapAssetType | Unset):
        symbol (str | Unset):  Example: NVDA,GOLD.
        sort (GetV5RealWorldAssetsMapSort | Unset):  Default: 'rwa_id'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAIDMapResponseModel]
    """

    kwargs = _get_kwargs(
        asset_type=asset_type,
        symbol=symbol,
        sort=sort,
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
    asset_type: GetV5RealWorldAssetsMapAssetType | Unset = UNSET,
    symbol: str | Unset = UNSET,
    sort: GetV5RealWorldAssetsMapSort | Unset = "rwa_id",
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAIDMapResponseModel
    | None
):
    """RWA ID Map

     Returns a mapping of all Real-World Asset (RWA) assets to their unique `rwa_id`. Use this
    lightweight lookup to resolve the correct `rwa_id` (the stable identifier we recommend over
    symbols/tickers) before calling the heavier info, asset-list, market-pairs, or historical endpoints.
    No market data is returned here.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 30 seconds.
    **Plan credit use:** No credit is needed when querying this endpoint.

    Args:
        asset_type (GetV5RealWorldAssetsMapAssetType | Unset):
        symbol (str | Unset):  Example: NVDA,GOLD.
        sort (GetV5RealWorldAssetsMapSort | Unset):  Default: 'rwa_id'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAIDMapResponseModel
    """

    return sync_detailed(
        client=client,
        asset_type=asset_type,
        symbol=symbol,
        sort=sort,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    asset_type: GetV5RealWorldAssetsMapAssetType | Unset = UNSET,
    symbol: str | Unset = UNSET,
    sort: GetV5RealWorldAssetsMapSort | Unset = "rwa_id",
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAIDMapResponseModel
]:
    """RWA ID Map

     Returns a mapping of all Real-World Asset (RWA) assets to their unique `rwa_id`. Use this
    lightweight lookup to resolve the correct `rwa_id` (the stable identifier we recommend over
    symbols/tickers) before calling the heavier info, asset-list, market-pairs, or historical endpoints.
    No market data is returned here.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 30 seconds.
    **Plan credit use:** No credit is needed when querying this endpoint.

    Args:
        asset_type (GetV5RealWorldAssetsMapAssetType | Unset):
        symbol (str | Unset):  Example: NVDA,GOLD.
        sort (GetV5RealWorldAssetsMapSort | Unset):  Default: 'rwa_id'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAIDMapResponseModel]
    """

    kwargs = _get_kwargs(
        asset_type=asset_type,
        symbol=symbol,
        sort=sort,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    asset_type: GetV5RealWorldAssetsMapAssetType | Unset = UNSET,
    symbol: str | Unset = UNSET,
    sort: GetV5RealWorldAssetsMapSort | Unset = "rwa_id",
    start: int | Unset = 1,
    limit: int | Unset = 100,
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAIDMapResponseModel
    | None
):
    """RWA ID Map

     Returns a mapping of all Real-World Asset (RWA) assets to their unique `rwa_id`. Use this
    lightweight lookup to resolve the correct `rwa_id` (the stable identifier we recommend over
    symbols/tickers) before calling the heavier info, asset-list, market-pairs, or historical endpoints.
    No market data is returned here.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 30 seconds.
    **Plan credit use:** No credit is needed when querying this endpoint.

    Args:
        asset_type (GetV5RealWorldAssetsMapAssetType | Unset):
        symbol (str | Unset):  Example: NVDA,GOLD.
        sort (GetV5RealWorldAssetsMapSort | Unset):  Default: 'rwa_id'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAIDMapResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            asset_type=asset_type,
            symbol=symbol,
            sort=sort,
            start=start,
            limit=limit,
        )
    ).parsed
