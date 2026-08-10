from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_info_response_model import AccountInfoResponseModel
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/key/info",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AccountInfoResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = AccountInfoResponseModel.from_dict(response.json())

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
    AccountInfoResponseModel
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
) -> Response[
    AccountInfoResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """Key Info

     Returns API key details and usage stats. This endpoint can be used to programmatically monitor your
    key usage compared to the rate limit and daily/monthly credit limits available to your API plan. You
    may use the Developer Portal's account dashboard as an alternative to this endpoint.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

      **Cache / Update frequency:** No cache, this endpoint updates as requests are made with your key.
      **Plan credit use:** No API credit cost. Requests to this endpoint do contribute to your minute
    based rate limit however.
      **CMC equivalent pages:** Our Developer Portal dashboard for your API Key at
    [pro.coinmarketcap.com/account](https://pro.coinmarketcap.com/account).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountInfoResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    AccountInfoResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """Key Info

     Returns API key details and usage stats. This endpoint can be used to programmatically monitor your
    key usage compared to the rate limit and daily/monthly credit limits available to your API plan. You
    may use the Developer Portal's account dashboard as an alternative to this endpoint.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

      **Cache / Update frequency:** No cache, this endpoint updates as requests are made with your key.
      **Plan credit use:** No API credit cost. Requests to this endpoint do contribute to your minute
    based rate limit however.
      **CMC equivalent pages:** Our Developer Portal dashboard for your API Key at
    [pro.coinmarketcap.com/account](https://pro.coinmarketcap.com/account).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountInfoResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AccountInfoResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """Key Info

     Returns API key details and usage stats. This endpoint can be used to programmatically monitor your
    key usage compared to the rate limit and daily/monthly credit limits available to your API plan. You
    may use the Developer Portal's account dashboard as an alternative to this endpoint.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

      **Cache / Update frequency:** No cache, this endpoint updates as requests are made with your key.
      **Plan credit use:** No API credit cost. Requests to this endpoint do contribute to your minute
    based rate limit however.
      **CMC equivalent pages:** Our Developer Portal dashboard for your API Key at
    [pro.coinmarketcap.com/account](https://pro.coinmarketcap.com/account).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountInfoResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    AccountInfoResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """Key Info

     Returns API key details and usage stats. This endpoint can be used to programmatically monitor your
    key usage compared to the rate limit and daily/monthly credit limits available to your API plan. You
    may use the Developer Portal's account dashboard as an alternative to this endpoint.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Basic
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

      **Cache / Update frequency:** No cache, this endpoint updates as requests are made with your key.
      **Plan credit use:** No API credit cost. Requests to this endpoint do contribute to your minute
    based rate limit however.
      **CMC equivalent pages:** Our Developer Portal dashboard for your API Key at
    [pro.coinmarketcap.com/account](https://pro.coinmarketcap.com/account).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountInfoResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
