from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exchange_assets_response_model import ExchangeAssetsResponseModel
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/exchange/assets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ExchangeAssetsResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = ExchangeAssetsResponseModel.from_dict(response.json())

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
    ExchangeAssetsResponseModel
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
) -> Response[
    ExchangeAssetsResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Exchange Assets

     Returns the exchange assets in the form of token holdings. This information includes details like
    wallet address, cryptocurrency, blockchain platform, balance, and etc.


      * Only wallets containing at least 100,000 USD in balance are shown
      * Balances from wallets might be delayed

      ** Disclaimer:
      All information and data relating to the holdings in the third-party wallet addresses are provided
    by the third parties to CoinMarketCap, and CoinMarketCap does not confirm or verify the accuracy or
    timeliness of such information and data.
      The information and data are provided \"as is\" without warranty of any kind. CoinMarketCap shall
    have no responsibility or liability for these third parties’ information and data or have the duty
    to review, confirm, verify or otherwise perform any inquiry or investigation as to the completeness,
    accuracy, sufficiency, integrity, reliability or timeliness of any such information or data
    provided.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Free
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

      **Cache / Update frequency:** Balance data is updated statically based on the source. Price data
    is updated every 5 minutes.
      **Plan credit use:** 1 credit.
      **CMC equivalent pages:** Exchange detail page like
    [coinmarketcap.com/exchanges/binance/](https://coinmarketcap.com/exchanges/binance/)

    Args:
        id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeAssetsResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
) -> (
    ExchangeAssetsResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Exchange Assets

     Returns the exchange assets in the form of token holdings. This information includes details like
    wallet address, cryptocurrency, blockchain platform, balance, and etc.


      * Only wallets containing at least 100,000 USD in balance are shown
      * Balances from wallets might be delayed

      ** Disclaimer:
      All information and data relating to the holdings in the third-party wallet addresses are provided
    by the third parties to CoinMarketCap, and CoinMarketCap does not confirm or verify the accuracy or
    timeliness of such information and data.
      The information and data are provided \"as is\" without warranty of any kind. CoinMarketCap shall
    have no responsibility or liability for these third parties’ information and data or have the duty
    to review, confirm, verify or otherwise perform any inquiry or investigation as to the completeness,
    accuracy, sufficiency, integrity, reliability or timeliness of any such information or data
    provided.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Free
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

      **Cache / Update frequency:** Balance data is updated statically based on the source. Price data
    is updated every 5 minutes.
      **Plan credit use:** 1 credit.
      **CMC equivalent pages:** Exchange detail page like
    [coinmarketcap.com/exchanges/binance/](https://coinmarketcap.com/exchanges/binance/)

    Args:
        id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeAssetsResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
) -> Response[
    ExchangeAssetsResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    r"""Exchange Assets

     Returns the exchange assets in the form of token holdings. This information includes details like
    wallet address, cryptocurrency, blockchain platform, balance, and etc.


      * Only wallets containing at least 100,000 USD in balance are shown
      * Balances from wallets might be delayed

      ** Disclaimer:
      All information and data relating to the holdings in the third-party wallet addresses are provided
    by the third parties to CoinMarketCap, and CoinMarketCap does not confirm or verify the accuracy or
    timeliness of such information and data.
      The information and data are provided \"as is\" without warranty of any kind. CoinMarketCap shall
    have no responsibility or liability for these third parties’ information and data or have the duty
    to review, confirm, verify or otherwise perform any inquiry or investigation as to the completeness,
    accuracy, sufficiency, integrity, reliability or timeliness of any such information or data
    provided.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Free
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

      **Cache / Update frequency:** Balance data is updated statically based on the source. Price data
    is updated every 5 minutes.
      **Plan credit use:** 1 credit.
      **CMC equivalent pages:** Exchange detail page like
    [coinmarketcap.com/exchanges/binance/](https://coinmarketcap.com/exchanges/binance/)

    Args:
        id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeAssetsResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: str | Unset = UNSET,
) -> (
    ExchangeAssetsResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    r"""Exchange Assets

     Returns the exchange assets in the form of token holdings. This information includes details like
    wallet address, cryptocurrency, blockchain platform, balance, and etc.


      * Only wallets containing at least 100,000 USD in balance are shown
      * Balances from wallets might be delayed

      ** Disclaimer:
      All information and data relating to the holdings in the third-party wallet addresses are provided
    by the third parties to CoinMarketCap, and CoinMarketCap does not confirm or verify the accuracy or
    timeliness of such information and data.
      The information and data are provided \"as is\" without warranty of any kind. CoinMarketCap shall
    have no responsibility or liability for these third parties’ information and data or have the duty
    to review, confirm, verify or otherwise perform any inquiry or investigation as to the completeness,
    accuracy, sufficiency, integrity, reliability or timeliness of any such information or data
    provided.

      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Free
      - Builder
      - Startup
      - Growth
      - Professional
      - Enterprise

      **Cache / Update frequency:** Balance data is updated statically based on the source. Price data
    is updated every 5 minutes.
      **Plan credit use:** 1 credit.
      **CMC equivalent pages:** Exchange detail page like
    [coinmarketcap.com/exchanges/binance/](https://coinmarketcap.com/exchanges/binance/)

    Args:
        id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeAssetsResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
