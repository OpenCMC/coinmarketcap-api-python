from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fiat_map_response_model import FiatMapResponseModel
from ...models.get_v1_fiat_map_sort import GetV1FiatMapSort
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: int | Unset = 1,
    limit: int | Unset = UNSET,
    sort: GetV1FiatMapSort | Unset = "id",
    include_metals: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["start"] = start

    params["limit"] = limit

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["include_metals"] = include_metals

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/fiat/map",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FiatMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = FiatMapResponseModel.from_dict(response.json())

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
    FiatMapResponseModel
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
    start: int | Unset = 1,
    limit: int | Unset = UNSET,
    sort: GetV1FiatMapSort | Unset = "id",
    include_metals: bool | Unset = False,
) -> Response[
    FiatMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """Fiat ID Map

     Returns a mapping of all supported fiat currencies to unique CoinMarketCap ids. Per our Best
    Practices we recommend utilizing CMC ID instead of currency symbols to securely identify assets with
    our other endpoints and in your own application logic.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Mapping data is updated only as needed, every 30 seconds.
    **Plan credit use:** 1 API call credit per request no matter query size.
    **CMC equivalent pages:** No equivalent, this data is only available via API.

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):
        sort (GetV1FiatMapSort | Unset):  Default: 'id'.
        include_metals (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FiatMapResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
        sort=sort,
        include_metals=include_metals,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = UNSET,
    sort: GetV1FiatMapSort | Unset = "id",
    include_metals: bool | Unset = False,
) -> (
    FiatMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """Fiat ID Map

     Returns a mapping of all supported fiat currencies to unique CoinMarketCap ids. Per our Best
    Practices we recommend utilizing CMC ID instead of currency symbols to securely identify assets with
    our other endpoints and in your own application logic.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Mapping data is updated only as needed, every 30 seconds.
    **Plan credit use:** 1 API call credit per request no matter query size.
    **CMC equivalent pages:** No equivalent, this data is only available via API.

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):
        sort (GetV1FiatMapSort | Unset):  Default: 'id'.
        include_metals (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FiatMapResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        start=start,
        limit=limit,
        sort=sort,
        include_metals=include_metals,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = UNSET,
    sort: GetV1FiatMapSort | Unset = "id",
    include_metals: bool | Unset = False,
) -> Response[
    FiatMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """Fiat ID Map

     Returns a mapping of all supported fiat currencies to unique CoinMarketCap ids. Per our Best
    Practices we recommend utilizing CMC ID instead of currency symbols to securely identify assets with
    our other endpoints and in your own application logic.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Mapping data is updated only as needed, every 30 seconds.
    **Plan credit use:** 1 API call credit per request no matter query size.
    **CMC equivalent pages:** No equivalent, this data is only available via API.

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):
        sort (GetV1FiatMapSort | Unset):  Default: 'id'.
        include_metals (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FiatMapResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
        sort=sort,
        include_metals=include_metals,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = UNSET,
    sort: GetV1FiatMapSort | Unset = "id",
    include_metals: bool | Unset = False,
) -> (
    FiatMapResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """Fiat ID Map

     Returns a mapping of all supported fiat currencies to unique CoinMarketCap ids. Per our Best
    Practices we recommend utilizing CMC ID instead of currency symbols to securely identify assets with
    our other endpoints and in your own application logic.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Mapping data is updated only as needed, every 30 seconds.
    **Plan credit use:** 1 API call credit per request no matter query size.
    **CMC equivalent pages:** No equivalent, this data is only available via API.

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):
        sort (GetV1FiatMapSort | Unset):  Default: 'id'.
        include_metals (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FiatMapResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            limit=limit,
            sort=sort,
            include_metals=include_metals,
        )
    ).parsed
