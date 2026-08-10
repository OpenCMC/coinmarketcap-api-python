from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dex_spot_pair_dto import DexSpotPairDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    network_id: str | Unset = UNSET,
    network_slug: str | Unset = UNSET,
    dex_id: str | Unset = UNSET,
    dex_slug: str | Unset = UNSET,
    base_asset_id: str | Unset = UNSET,
    base_asset_symbol: str | Unset = UNSET,
    base_asset_contract_address: str | Unset = UNSET,
    base_asset_ucid: str | Unset = UNSET,
    quote_asset_id: str | Unset = UNSET,
    quote_asset_symbol: str | Unset = UNSET,
    quote_asset_contract_address: str | Unset = UNSET,
    quote_asset_ucid: str | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    liquidity_min: str | Unset = UNSET,
    liquidity_max: str | Unset = UNSET,
    volume_24h_min: str | Unset = UNSET,
    volume_24h_max: str | Unset = UNSET,
    no_of_transactions_24h_min: str | Unset = UNSET,
    no_of_transactions_24h_max: str | Unset = UNSET,
    percent_change_24h_min: str | Unset = UNSET,
    percent_change_24h_max: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    aux: str | Unset = UNSET,
    reverse_order: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["network_id"] = network_id

    params["network_slug"] = network_slug

    params["dex_id"] = dex_id

    params["dex_slug"] = dex_slug

    params["base_asset_id"] = base_asset_id

    params["base_asset_symbol"] = base_asset_symbol

    params["base_asset_contract_address"] = base_asset_contract_address

    params["base_asset_ucid"] = base_asset_ucid

    params["quote_asset_id"] = quote_asset_id

    params["quote_asset_symbol"] = quote_asset_symbol

    params["quote_asset_contract_address"] = quote_asset_contract_address

    params["quote_asset_ucid"] = quote_asset_ucid

    params["scroll_id"] = scroll_id

    params["limit"] = limit

    params["liquidity_min"] = liquidity_min

    params["liquidity_max"] = liquidity_max

    params["volume_24h_min"] = volume_24h_min

    params["volume_24h_max"] = volume_24h_max

    params["no_of_transactions_24h_min"] = no_of_transactions_24h_min

    params["no_of_transactions_24h_max"] = no_of_transactions_24h_max

    params["percent_change_24h_min"] = percent_change_24h_min

    params["percent_change_24h_max"] = percent_change_24h_max

    params["sort"] = sort

    params["sort_dir"] = sort_dir

    params["aux"] = aux

    params["reverse_order"] = reverse_order

    params["convert_id"] = convert_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/dex/spot-pairs/latest",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[DexSpotPairDTO] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DexSpotPairDTO.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[DexSpotPairDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    network_id: str | Unset = UNSET,
    network_slug: str | Unset = UNSET,
    dex_id: str | Unset = UNSET,
    dex_slug: str | Unset = UNSET,
    base_asset_id: str | Unset = UNSET,
    base_asset_symbol: str | Unset = UNSET,
    base_asset_contract_address: str | Unset = UNSET,
    base_asset_ucid: str | Unset = UNSET,
    quote_asset_id: str | Unset = UNSET,
    quote_asset_symbol: str | Unset = UNSET,
    quote_asset_contract_address: str | Unset = UNSET,
    quote_asset_ucid: str | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    liquidity_min: str | Unset = UNSET,
    liquidity_max: str | Unset = UNSET,
    volume_24h_min: str | Unset = UNSET,
    volume_24h_max: str | Unset = UNSET,
    no_of_transactions_24h_min: str | Unset = UNSET,
    no_of_transactions_24h_max: str | Unset = UNSET,
    percent_change_24h_min: str | Unset = UNSET,
    percent_change_24h_max: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    aux: str | Unset = UNSET,
    reverse_order: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> Response[list[DexSpotPairDTO]]:
    r"""Pairs Listings Latest

     Returns a paginated list of all active dex spot pairs with latest market data. Use the \"convert\"
    option to return market values in multiple fiat and cryptocurrency conversions in the same call.

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v4/dex/spot-pairs/latest`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        network_id (str | Unset):
        network_slug (str | Unset):
        dex_id (str | Unset):
        dex_slug (str | Unset):
        base_asset_id (str | Unset):
        base_asset_symbol (str | Unset):
        base_asset_contract_address (str | Unset):
        base_asset_ucid (str | Unset):
        quote_asset_id (str | Unset):
        quote_asset_symbol (str | Unset):
        quote_asset_contract_address (str | Unset):
        quote_asset_ucid (str | Unset):
        scroll_id (str | Unset):
        limit (str | Unset):
        liquidity_min (str | Unset):
        liquidity_max (str | Unset):
        volume_24h_min (str | Unset):
        volume_24h_max (str | Unset):
        no_of_transactions_24h_min (str | Unset):
        no_of_transactions_24h_max (str | Unset):
        percent_change_24h_min (str | Unset):
        percent_change_24h_max (str | Unset):
        sort (str | Unset):
        sort_dir (str | Unset):
        aux (str | Unset):
        reverse_order (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[DexSpotPairDTO]]
    """

    kwargs = _get_kwargs(
        network_id=network_id,
        network_slug=network_slug,
        dex_id=dex_id,
        dex_slug=dex_slug,
        base_asset_id=base_asset_id,
        base_asset_symbol=base_asset_symbol,
        base_asset_contract_address=base_asset_contract_address,
        base_asset_ucid=base_asset_ucid,
        quote_asset_id=quote_asset_id,
        quote_asset_symbol=quote_asset_symbol,
        quote_asset_contract_address=quote_asset_contract_address,
        quote_asset_ucid=quote_asset_ucid,
        scroll_id=scroll_id,
        limit=limit,
        liquidity_min=liquidity_min,
        liquidity_max=liquidity_max,
        volume_24h_min=volume_24h_min,
        volume_24h_max=volume_24h_max,
        no_of_transactions_24h_min=no_of_transactions_24h_min,
        no_of_transactions_24h_max=no_of_transactions_24h_max,
        percent_change_24h_min=percent_change_24h_min,
        percent_change_24h_max=percent_change_24h_max,
        sort=sort,
        sort_dir=sort_dir,
        aux=aux,
        reverse_order=reverse_order,
        convert_id=convert_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    network_id: str | Unset = UNSET,
    network_slug: str | Unset = UNSET,
    dex_id: str | Unset = UNSET,
    dex_slug: str | Unset = UNSET,
    base_asset_id: str | Unset = UNSET,
    base_asset_symbol: str | Unset = UNSET,
    base_asset_contract_address: str | Unset = UNSET,
    base_asset_ucid: str | Unset = UNSET,
    quote_asset_id: str | Unset = UNSET,
    quote_asset_symbol: str | Unset = UNSET,
    quote_asset_contract_address: str | Unset = UNSET,
    quote_asset_ucid: str | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    liquidity_min: str | Unset = UNSET,
    liquidity_max: str | Unset = UNSET,
    volume_24h_min: str | Unset = UNSET,
    volume_24h_max: str | Unset = UNSET,
    no_of_transactions_24h_min: str | Unset = UNSET,
    no_of_transactions_24h_max: str | Unset = UNSET,
    percent_change_24h_min: str | Unset = UNSET,
    percent_change_24h_max: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    aux: str | Unset = UNSET,
    reverse_order: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> list[DexSpotPairDTO] | None:
    r"""Pairs Listings Latest

     Returns a paginated list of all active dex spot pairs with latest market data. Use the \"convert\"
    option to return market values in multiple fiat and cryptocurrency conversions in the same call.

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v4/dex/spot-pairs/latest`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        network_id (str | Unset):
        network_slug (str | Unset):
        dex_id (str | Unset):
        dex_slug (str | Unset):
        base_asset_id (str | Unset):
        base_asset_symbol (str | Unset):
        base_asset_contract_address (str | Unset):
        base_asset_ucid (str | Unset):
        quote_asset_id (str | Unset):
        quote_asset_symbol (str | Unset):
        quote_asset_contract_address (str | Unset):
        quote_asset_ucid (str | Unset):
        scroll_id (str | Unset):
        limit (str | Unset):
        liquidity_min (str | Unset):
        liquidity_max (str | Unset):
        volume_24h_min (str | Unset):
        volume_24h_max (str | Unset):
        no_of_transactions_24h_min (str | Unset):
        no_of_transactions_24h_max (str | Unset):
        percent_change_24h_min (str | Unset):
        percent_change_24h_max (str | Unset):
        sort (str | Unset):
        sort_dir (str | Unset):
        aux (str | Unset):
        reverse_order (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[DexSpotPairDTO]
    """

    return sync_detailed(
        client=client,
        network_id=network_id,
        network_slug=network_slug,
        dex_id=dex_id,
        dex_slug=dex_slug,
        base_asset_id=base_asset_id,
        base_asset_symbol=base_asset_symbol,
        base_asset_contract_address=base_asset_contract_address,
        base_asset_ucid=base_asset_ucid,
        quote_asset_id=quote_asset_id,
        quote_asset_symbol=quote_asset_symbol,
        quote_asset_contract_address=quote_asset_contract_address,
        quote_asset_ucid=quote_asset_ucid,
        scroll_id=scroll_id,
        limit=limit,
        liquidity_min=liquidity_min,
        liquidity_max=liquidity_max,
        volume_24h_min=volume_24h_min,
        volume_24h_max=volume_24h_max,
        no_of_transactions_24h_min=no_of_transactions_24h_min,
        no_of_transactions_24h_max=no_of_transactions_24h_max,
        percent_change_24h_min=percent_change_24h_min,
        percent_change_24h_max=percent_change_24h_max,
        sort=sort,
        sort_dir=sort_dir,
        aux=aux,
        reverse_order=reverse_order,
        convert_id=convert_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    network_id: str | Unset = UNSET,
    network_slug: str | Unset = UNSET,
    dex_id: str | Unset = UNSET,
    dex_slug: str | Unset = UNSET,
    base_asset_id: str | Unset = UNSET,
    base_asset_symbol: str | Unset = UNSET,
    base_asset_contract_address: str | Unset = UNSET,
    base_asset_ucid: str | Unset = UNSET,
    quote_asset_id: str | Unset = UNSET,
    quote_asset_symbol: str | Unset = UNSET,
    quote_asset_contract_address: str | Unset = UNSET,
    quote_asset_ucid: str | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    liquidity_min: str | Unset = UNSET,
    liquidity_max: str | Unset = UNSET,
    volume_24h_min: str | Unset = UNSET,
    volume_24h_max: str | Unset = UNSET,
    no_of_transactions_24h_min: str | Unset = UNSET,
    no_of_transactions_24h_max: str | Unset = UNSET,
    percent_change_24h_min: str | Unset = UNSET,
    percent_change_24h_max: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    aux: str | Unset = UNSET,
    reverse_order: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> Response[list[DexSpotPairDTO]]:
    r"""Pairs Listings Latest

     Returns a paginated list of all active dex spot pairs with latest market data. Use the \"convert\"
    option to return market values in multiple fiat and cryptocurrency conversions in the same call.

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v4/dex/spot-pairs/latest`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        network_id (str | Unset):
        network_slug (str | Unset):
        dex_id (str | Unset):
        dex_slug (str | Unset):
        base_asset_id (str | Unset):
        base_asset_symbol (str | Unset):
        base_asset_contract_address (str | Unset):
        base_asset_ucid (str | Unset):
        quote_asset_id (str | Unset):
        quote_asset_symbol (str | Unset):
        quote_asset_contract_address (str | Unset):
        quote_asset_ucid (str | Unset):
        scroll_id (str | Unset):
        limit (str | Unset):
        liquidity_min (str | Unset):
        liquidity_max (str | Unset):
        volume_24h_min (str | Unset):
        volume_24h_max (str | Unset):
        no_of_transactions_24h_min (str | Unset):
        no_of_transactions_24h_max (str | Unset):
        percent_change_24h_min (str | Unset):
        percent_change_24h_max (str | Unset):
        sort (str | Unset):
        sort_dir (str | Unset):
        aux (str | Unset):
        reverse_order (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[DexSpotPairDTO]]
    """

    kwargs = _get_kwargs(
        network_id=network_id,
        network_slug=network_slug,
        dex_id=dex_id,
        dex_slug=dex_slug,
        base_asset_id=base_asset_id,
        base_asset_symbol=base_asset_symbol,
        base_asset_contract_address=base_asset_contract_address,
        base_asset_ucid=base_asset_ucid,
        quote_asset_id=quote_asset_id,
        quote_asset_symbol=quote_asset_symbol,
        quote_asset_contract_address=quote_asset_contract_address,
        quote_asset_ucid=quote_asset_ucid,
        scroll_id=scroll_id,
        limit=limit,
        liquidity_min=liquidity_min,
        liquidity_max=liquidity_max,
        volume_24h_min=volume_24h_min,
        volume_24h_max=volume_24h_max,
        no_of_transactions_24h_min=no_of_transactions_24h_min,
        no_of_transactions_24h_max=no_of_transactions_24h_max,
        percent_change_24h_min=percent_change_24h_min,
        percent_change_24h_max=percent_change_24h_max,
        sort=sort,
        sort_dir=sort_dir,
        aux=aux,
        reverse_order=reverse_order,
        convert_id=convert_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    network_id: str | Unset = UNSET,
    network_slug: str | Unset = UNSET,
    dex_id: str | Unset = UNSET,
    dex_slug: str | Unset = UNSET,
    base_asset_id: str | Unset = UNSET,
    base_asset_symbol: str | Unset = UNSET,
    base_asset_contract_address: str | Unset = UNSET,
    base_asset_ucid: str | Unset = UNSET,
    quote_asset_id: str | Unset = UNSET,
    quote_asset_symbol: str | Unset = UNSET,
    quote_asset_contract_address: str | Unset = UNSET,
    quote_asset_ucid: str | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    liquidity_min: str | Unset = UNSET,
    liquidity_max: str | Unset = UNSET,
    volume_24h_min: str | Unset = UNSET,
    volume_24h_max: str | Unset = UNSET,
    no_of_transactions_24h_min: str | Unset = UNSET,
    no_of_transactions_24h_max: str | Unset = UNSET,
    percent_change_24h_min: str | Unset = UNSET,
    percent_change_24h_max: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,
    aux: str | Unset = UNSET,
    reverse_order: str | Unset = UNSET,
    convert_id: str | Unset = UNSET,
) -> list[DexSpotPairDTO] | None:
    r"""Pairs Listings Latest

     Returns a paginated list of all active dex spot pairs with latest market data. Use the \"convert\"
    option to return market values in multiple fiat and cryptocurrency conversions in the same call.

    <Callout type=\"tip\" title=\"Available with no API key\">Call this endpoint keyless - no API key,
    no signup. Prefix the path with `/public-api`: `https://pro-api.coinmarketcap.com/public-
    api/v4/dex/spot-pairs/latest`. See the [Keyless Public
    API](https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api) for the full
    list, rate limits, and examples.</Callout>

    Args:
        network_id (str | Unset):
        network_slug (str | Unset):
        dex_id (str | Unset):
        dex_slug (str | Unset):
        base_asset_id (str | Unset):
        base_asset_symbol (str | Unset):
        base_asset_contract_address (str | Unset):
        base_asset_ucid (str | Unset):
        quote_asset_id (str | Unset):
        quote_asset_symbol (str | Unset):
        quote_asset_contract_address (str | Unset):
        quote_asset_ucid (str | Unset):
        scroll_id (str | Unset):
        limit (str | Unset):
        liquidity_min (str | Unset):
        liquidity_max (str | Unset):
        volume_24h_min (str | Unset):
        volume_24h_max (str | Unset):
        no_of_transactions_24h_min (str | Unset):
        no_of_transactions_24h_max (str | Unset):
        percent_change_24h_min (str | Unset):
        percent_change_24h_max (str | Unset):
        sort (str | Unset):
        sort_dir (str | Unset):
        aux (str | Unset):
        reverse_order (str | Unset):
        convert_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[DexSpotPairDTO]
    """

    return (
        await asyncio_detailed(
            client=client,
            network_id=network_id,
            network_slug=network_slug,
            dex_id=dex_id,
            dex_slug=dex_slug,
            base_asset_id=base_asset_id,
            base_asset_symbol=base_asset_symbol,
            base_asset_contract_address=base_asset_contract_address,
            base_asset_ucid=base_asset_ucid,
            quote_asset_id=quote_asset_id,
            quote_asset_symbol=quote_asset_symbol,
            quote_asset_contract_address=quote_asset_contract_address,
            quote_asset_ucid=quote_asset_ucid,
            scroll_id=scroll_id,
            limit=limit,
            liquidity_min=liquidity_min,
            liquidity_max=liquidity_max,
            volume_24h_min=volume_24h_min,
            volume_24h_max=volume_24h_max,
            no_of_transactions_24h_min=no_of_transactions_24h_min,
            no_of_transactions_24h_max=no_of_transactions_24h_max,
            percent_change_24h_min=percent_change_24h_min,
            percent_change_24h_max=percent_change_24h_max,
            sort=sort,
            sort_dir=sort_dir,
            aux=aux,
            reverse_order=reverse_order,
            convert_id=convert_id,
        )
    ).parsed
