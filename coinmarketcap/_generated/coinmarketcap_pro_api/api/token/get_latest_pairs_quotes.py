from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dex_paris_quotes_dto import DexParisQuotesDTO
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
        "url": "/v4/dex/pairs/quotes/latest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[DexParisQuotesDTO] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DexParisQuotesDTO.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[DexParisQuotesDTO]]:
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
) -> Response[list[DexParisQuotesDTO]]:
    r"""Quotes Latest

     Returns the latest market quote for 1 or more spot pairs. Use the \"convert\" option to return
    market values in multiple fiat and cryptocurrency conversions in the same call.

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v4/dex/pairs/quotes/latest`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

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
        Response[list[DexParisQuotesDTO]]
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
) -> list[DexParisQuotesDTO] | None:
    r"""Quotes Latest

     Returns the latest market quote for 1 or more spot pairs. Use the \"convert\" option to return
    market values in multiple fiat and cryptocurrency conversions in the same call.

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v4/dex/pairs/quotes/latest`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

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
        list[DexParisQuotesDTO]
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
) -> Response[list[DexParisQuotesDTO]]:
    r"""Quotes Latest

     Returns the latest market quote for 1 or more spot pairs. Use the \"convert\" option to return
    market values in multiple fiat and cryptocurrency conversions in the same call.

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v4/dex/pairs/quotes/latest`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

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
        Response[list[DexParisQuotesDTO]]
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
) -> list[DexParisQuotesDTO] | None:
    r"""Quotes Latest

     Returns the latest market quote for 1 or more spot pairs. Use the \"convert\" option to return
    market values in multiple fiat and cryptocurrency conversions in the same call.

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v4/dex/pairs/quotes/latest`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

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
        list[DexParisQuotesDTO]
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
