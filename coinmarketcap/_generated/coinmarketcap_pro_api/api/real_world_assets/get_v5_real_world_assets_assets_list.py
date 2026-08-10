from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v5_real_world_assets_assets_list_asset_type import (
    GetV5RealWorldAssetsAssetsListAssetType,
)
from ...models.get_v5_real_world_assets_assets_list_sort import (
    GetV5RealWorldAssetsAssetsListSort,
)
from ...models.get_v5_real_world_assets_assets_list_sort_dir import (
    GetV5RealWorldAssetsAssetsListSortDir,
)
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...models.rwa_asset_list_response_model import RWAAssetListResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    rwa_id: str | Unset = UNSET,
    rwa_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    asset_type: GetV5RealWorldAssetsAssetsListAssetType | Unset = UNSET,
    sort: GetV5RealWorldAssetsAssetsListSort | Unset = "rwa_rank",
    sort_dir: GetV5RealWorldAssetsAssetsListSortDir | Unset = "asc",
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["rwa_id"] = rwa_id

    params["rwa_slug"] = rwa_slug

    params["symbol"] = symbol

    json_asset_type: str | Unset = UNSET
    if not isinstance(asset_type, Unset):
        json_asset_type = asset_type

    params["asset_type"] = json_asset_type

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_sort_dir: str | Unset = UNSET
    if not isinstance(sort_dir, Unset):
        json_sort_dir = sort_dir

    params["sort_dir"] = json_sort_dir

    params["start"] = start

    params["limit"] = limit

    params["convert"] = convert

    params["convert_id"] = convert_id

    params["skip_invalid"] = skip_invalid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v5/real-world-assets/assets/list",
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
    | RWAAssetListResponseModel
    | None
):
    if response.status_code == 200:
        response_200 = RWAAssetListResponseModel.from_dict(response.json())

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
    | RWAAssetListResponseModel
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
    rwa_id: str | Unset = UNSET,
    rwa_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    asset_type: GetV5RealWorldAssetsAssetsListAssetType | Unset = UNSET,
    sort: GetV5RealWorldAssetsAssetsListSort | Unset = "rwa_rank",
    sort_dir: GetV5RealWorldAssetsAssetsListSortDir | Unset = "asc",
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAAssetListResponseModel
]:
    """RWA List

     Returns a paginated list of tracked Real-World Asset (RWA) assets with their tokenized aggregate
    quotes — average tokenized price, tokenized market cap, and 24h tokenized volume. Static metadata is
    **not** returned here — use `/v5/real-world-assets/info` for that. Mirrors the `/listings` market-
    data convention. Results default to `rwa_rank` ascending.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 1 minute.
    **Plan credit use:** 1 call credit per 250 RWA assets returned (rounded up), plus 1 credit per
    `convert`/`convert_id` beyond the first.

    Args:
        rwa_id (str | Unset):  Example: 1,2.
        rwa_slug (str | Unset):  Example: nvidia,gold.
        symbol (str | Unset):  Example: NVDA,GOLD.
        asset_type (GetV5RealWorldAssetsAssetsListAssetType | Unset):
        sort (GetV5RealWorldAssetsAssetsListSort | Unset):  Default: 'rwa_rank'.
        sort_dir (GetV5RealWorldAssetsAssetsListSortDir | Unset):  Default: 'asc'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):  Example: USD.
        convert_id (str | Unset):  Example: 2781.
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAAssetListResponseModel]
    """

    kwargs = _get_kwargs(
        rwa_id=rwa_id,
        rwa_slug=rwa_slug,
        symbol=symbol,
        asset_type=asset_type,
        sort=sort,
        sort_dir=sort_dir,
        start=start,
        limit=limit,
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
    rwa_id: str | Unset = UNSET,
    rwa_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    asset_type: GetV5RealWorldAssetsAssetsListAssetType | Unset = UNSET,
    sort: GetV5RealWorldAssetsAssetsListSort | Unset = "rwa_rank",
    sort_dir: GetV5RealWorldAssetsAssetsListSortDir | Unset = "asc",
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAAssetListResponseModel
    | None
):
    """RWA List

     Returns a paginated list of tracked Real-World Asset (RWA) assets with their tokenized aggregate
    quotes — average tokenized price, tokenized market cap, and 24h tokenized volume. Static metadata is
    **not** returned here — use `/v5/real-world-assets/info` for that. Mirrors the `/listings` market-
    data convention. Results default to `rwa_rank` ascending.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 1 minute.
    **Plan credit use:** 1 call credit per 250 RWA assets returned (rounded up), plus 1 credit per
    `convert`/`convert_id` beyond the first.

    Args:
        rwa_id (str | Unset):  Example: 1,2.
        rwa_slug (str | Unset):  Example: nvidia,gold.
        symbol (str | Unset):  Example: NVDA,GOLD.
        asset_type (GetV5RealWorldAssetsAssetsListAssetType | Unset):
        sort (GetV5RealWorldAssetsAssetsListSort | Unset):  Default: 'rwa_rank'.
        sort_dir (GetV5RealWorldAssetsAssetsListSortDir | Unset):  Default: 'asc'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):  Example: USD.
        convert_id (str | Unset):  Example: 2781.
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAAssetListResponseModel
    """

    return sync_detailed(
        client=client,
        rwa_id=rwa_id,
        rwa_slug=rwa_slug,
        symbol=symbol,
        asset_type=asset_type,
        sort=sort,
        sort_dir=sort_dir,
        start=start,
        limit=limit,
        convert=convert,
        convert_id=convert_id,
        skip_invalid=skip_invalid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    rwa_id: str | Unset = UNSET,
    rwa_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    asset_type: GetV5RealWorldAssetsAssetsListAssetType | Unset = UNSET,
    sort: GetV5RealWorldAssetsAssetsListSort | Unset = "rwa_rank",
    sort_dir: GetV5RealWorldAssetsAssetsListSortDir | Unset = "asc",
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> Response[
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAAssetListResponseModel
]:
    """RWA List

     Returns a paginated list of tracked Real-World Asset (RWA) assets with their tokenized aggregate
    quotes — average tokenized price, tokenized market cap, and 24h tokenized volume. Static metadata is
    **not** returned here — use `/v5/real-world-assets/info` for that. Mirrors the `/listings` market-
    data convention. Results default to `rwa_rank` ascending.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 1 minute.
    **Plan credit use:** 1 call credit per 250 RWA assets returned (rounded up), plus 1 credit per
    `convert`/`convert_id` beyond the first.

    Args:
        rwa_id (str | Unset):  Example: 1,2.
        rwa_slug (str | Unset):  Example: nvidia,gold.
        symbol (str | Unset):  Example: NVDA,GOLD.
        asset_type (GetV5RealWorldAssetsAssetsListAssetType | Unset):
        sort (GetV5RealWorldAssetsAssetsListSort | Unset):  Default: 'rwa_rank'.
        sort_dir (GetV5RealWorldAssetsAssetsListSortDir | Unset):  Default: 'asc'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):  Example: USD.
        convert_id (str | Unset):  Example: 2781.
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAAssetListResponseModel]
    """

    kwargs = _get_kwargs(
        rwa_id=rwa_id,
        rwa_slug=rwa_slug,
        symbol=symbol,
        asset_type=asset_type,
        sort=sort,
        sort_dir=sort_dir,
        start=start,
        limit=limit,
        convert=convert,
        convert_id=convert_id,
        skip_invalid=skip_invalid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    rwa_id: str | Unset = UNSET,
    rwa_slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    asset_type: GetV5RealWorldAssetsAssetsListAssetType | Unset = UNSET,
    sort: GetV5RealWorldAssetsAssetsListSort | Unset = "rwa_rank",
    sort_dir: GetV5RealWorldAssetsAssetsListSortDir | Unset = "asc",
    start: int | Unset = 1,
    limit: int | Unset = 100,
    convert: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
) -> (
    HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | RWAAssetListResponseModel
    | None
):
    """RWA List

     Returns a paginated list of tracked Real-World Asset (RWA) assets with their tokenized aggregate
    quotes — average tokenized price, tokenized market cap, and 24h tokenized volume. Static metadata is
    **not** returned here — use `/v5/real-world-assets/info` for that. Mirrors the `/listings` market-
    data convention. Results default to `rwa_rank` ascending.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Every 1 minute.
    **Plan credit use:** 1 call credit per 250 RWA assets returned (rounded up), plus 1 credit per
    `convert`/`convert_id` beyond the first.

    Args:
        rwa_id (str | Unset):  Example: 1,2.
        rwa_slug (str | Unset):  Example: nvidia,gold.
        symbol (str | Unset):  Example: NVDA,GOLD.
        asset_type (GetV5RealWorldAssetsAssetsListAssetType | Unset):
        sort (GetV5RealWorldAssetsAssetsListSort | Unset):  Default: 'rwa_rank'.
        sort_dir (GetV5RealWorldAssetsAssetsListSortDir | Unset):  Default: 'asc'.
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        convert (str | Unset):  Example: USD.
        convert_id (str | Unset):  Example: 2781.
        skip_invalid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject | RWAAssetListResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            rwa_id=rwa_id,
            rwa_slug=rwa_slug,
            symbol=symbol,
            asset_type=asset_type,
            sort=sort,
            sort_dir=sort_dir,
            start=start,
            limit=limit,
            convert=convert,
            convert_id=convert_id,
            skip_invalid=skip_invalid,
        )
    ).parsed
