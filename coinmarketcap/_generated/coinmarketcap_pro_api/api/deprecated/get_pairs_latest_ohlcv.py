from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.v4dex_pairs_ohlcv_latest_response_model import V4DEXPairsOhlcvLatestResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    contract_address: str | Unset = UNSET,
    network_id: str | Unset = UNSET,
    network_slug: str | Unset = UNSET,
    aux: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
    reverse_order: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["contract_address"] = contract_address

    params["network_id"] = network_id

    params["network_slug"] = network_slug

    params["aux"] = aux

    params["convert_id"] = convert_id

    params["skip_invalid"] = skip_invalid

    params["reverse_order"] = reverse_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/dex/pairs/ohlcv/latest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> V4DEXPairsOhlcvLatestResponseModel | None:
    if response.status_code == 200:
        response_200 = V4DEXPairsOhlcvLatestResponseModel.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[V4DEXPairsOhlcvLatestResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    contract_address: str | Unset = UNSET,
    network_id: str | Unset = UNSET,
    network_slug: str | Unset = UNSET,
    aux: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
    reverse_order: str | Unset = UNSET,
) -> Response[V4DEXPairsOhlcvLatestResponseModel]:
    """OHLCV Latest

     Returns the latest OHLCV (Open, High, Low, Close, Volume) market values for one or more spot pairs
    for the current UTC day. Since the current UTC day is still active these values are updated
    frequently. You can find the final calculated OHLCV values for the last completed UTC day along with
    all historic days using /dex/pairs/ohlcv/historical.

    Args:
        contract_address (str | Unset):
        network_id (str | Unset):
        network_slug (str | Unset):
        aux (str | Unset):
        convert_id (str | Unset):
        skip_invalid (str | Unset):
        reverse_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V4DEXPairsOhlcvLatestResponseModel]
    """

    kwargs = _get_kwargs(
        contract_address=contract_address,
        network_id=network_id,
        network_slug=network_slug,
        aux=aux,
        convert_id=convert_id,
        skip_invalid=skip_invalid,
        reverse_order=reverse_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    contract_address: str | Unset = UNSET,
    network_id: str | Unset = UNSET,
    network_slug: str | Unset = UNSET,
    aux: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
    reverse_order: str | Unset = UNSET,
) -> V4DEXPairsOhlcvLatestResponseModel | None:
    """OHLCV Latest

     Returns the latest OHLCV (Open, High, Low, Close, Volume) market values for one or more spot pairs
    for the current UTC day. Since the current UTC day is still active these values are updated
    frequently. You can find the final calculated OHLCV values for the last completed UTC day along with
    all historic days using /dex/pairs/ohlcv/historical.

    Args:
        contract_address (str | Unset):
        network_id (str | Unset):
        network_slug (str | Unset):
        aux (str | Unset):
        convert_id (str | Unset):
        skip_invalid (str | Unset):
        reverse_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V4DEXPairsOhlcvLatestResponseModel
    """

    return sync_detailed(
        client=client,
        contract_address=contract_address,
        network_id=network_id,
        network_slug=network_slug,
        aux=aux,
        convert_id=convert_id,
        skip_invalid=skip_invalid,
        reverse_order=reverse_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    contract_address: str | Unset = UNSET,
    network_id: str | Unset = UNSET,
    network_slug: str | Unset = UNSET,
    aux: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
    reverse_order: str | Unset = UNSET,
) -> Response[V4DEXPairsOhlcvLatestResponseModel]:
    """OHLCV Latest

     Returns the latest OHLCV (Open, High, Low, Close, Volume) market values for one or more spot pairs
    for the current UTC day. Since the current UTC day is still active these values are updated
    frequently. You can find the final calculated OHLCV values for the last completed UTC day along with
    all historic days using /dex/pairs/ohlcv/historical.

    Args:
        contract_address (str | Unset):
        network_id (str | Unset):
        network_slug (str | Unset):
        aux (str | Unset):
        convert_id (str | Unset):
        skip_invalid (str | Unset):
        reverse_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V4DEXPairsOhlcvLatestResponseModel]
    """

    kwargs = _get_kwargs(
        contract_address=contract_address,
        network_id=network_id,
        network_slug=network_slug,
        aux=aux,
        convert_id=convert_id,
        skip_invalid=skip_invalid,
        reverse_order=reverse_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    contract_address: str | Unset = UNSET,
    network_id: str | Unset = UNSET,
    network_slug: str | Unset = UNSET,
    aux: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
    skip_invalid: str | Unset = UNSET,
    reverse_order: str | Unset = UNSET,
) -> V4DEXPairsOhlcvLatestResponseModel | None:
    """OHLCV Latest

     Returns the latest OHLCV (Open, High, Low, Close, Volume) market values for one or more spot pairs
    for the current UTC day. Since the current UTC day is still active these values are updated
    frequently. You can find the final calculated OHLCV values for the last completed UTC day along with
    all historic days using /dex/pairs/ohlcv/historical.

    Args:
        contract_address (str | Unset):
        network_id (str | Unset):
        network_slug (str | Unset):
        aux (str | Unset):
        convert_id (str | Unset):
        skip_invalid (str | Unset):
        reverse_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V4DEXPairsOhlcvLatestResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            contract_address=contract_address,
            network_id=network_id,
            network_slug=network_slug,
            aux=aux,
            convert_id=convert_id,
            skip_invalid=skip_invalid,
            reverse_order=reverse_order,
        )
    ).parsed
