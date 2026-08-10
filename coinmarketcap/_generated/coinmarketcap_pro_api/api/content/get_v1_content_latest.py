from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.content_latest_response_model import ContentLatestResponseModel
from ...models.get_v1_content_latest_language import GetV1ContentLatestLanguage
from ...models.http_status_400_error_object import HTTPStatus400ErrorObject
from ...models.http_status_401_error_object import HTTPStatus401ErrorObject
from ...models.http_status_403_error_object import HTTPStatus403ErrorObject
from ...models.http_status_429_error_object import HTTPStatus429ErrorObject
from ...models.http_status_500_error_object import HTTPStatus500ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    news_type: str | Unset = "all",
    content_type: str | Unset = "all",
    category: str | Unset = UNSET,
    language: GetV1ContentLatestLanguage | Unset = "en",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["start"] = start

    params["limit"] = limit

    params["id"] = id

    params["slug"] = slug

    params["symbol"] = symbol

    params["news_type"] = news_type

    params["content_type"] = content_type

    params["category"] = category

    json_language: str | Unset = UNSET
    if not isinstance(language, Unset):
        json_language = language

    params["language"] = json_language

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/content/latest",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ContentLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    if response.status_code == 200:
        response_200 = ContentLatestResponseModel.from_dict(response.json())

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
    ContentLatestResponseModel
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
    limit: int | Unset = 100,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    news_type: str | Unset = "all",
    content_type: str | Unset = "all",
    category: str | Unset = UNSET,
    language: GetV1ContentLatestLanguage | Unset = "en",
) -> Response[
    ContentLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """Content Latest

     Returns a paginated list of content pulled from CMC News/Headlines and Alexandria articles.


      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Five Minutes
    **Plan credit use:** 0 credit

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        news_type (str | Unset):  Default: 'all'.
        content_type (str | Unset):  Default: 'all'.
        category (str | Unset):
        language (GetV1ContentLatestLanguage | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContentLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
        id=id,
        slug=slug,
        symbol=symbol,
        news_type=news_type,
        content_type=content_type,
        category=category,
        language=language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    news_type: str | Unset = "all",
    content_type: str | Unset = "all",
    category: str | Unset = UNSET,
    language: GetV1ContentLatestLanguage | Unset = "en",
) -> (
    ContentLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """Content Latest

     Returns a paginated list of content pulled from CMC News/Headlines and Alexandria articles.


      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Five Minutes
    **Plan credit use:** 0 credit

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        news_type (str | Unset):  Default: 'all'.
        content_type (str | Unset):  Default: 'all'.
        category (str | Unset):
        language (GetV1ContentLatestLanguage | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContentLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return sync_detailed(
        client=client,
        start=start,
        limit=limit,
        id=id,
        slug=slug,
        symbol=symbol,
        news_type=news_type,
        content_type=content_type,
        category=category,
        language=language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    news_type: str | Unset = "all",
    content_type: str | Unset = "all",
    category: str | Unset = UNSET,
    language: GetV1ContentLatestLanguage | Unset = "en",
) -> Response[
    ContentLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
]:
    """Content Latest

     Returns a paginated list of content pulled from CMC News/Headlines and Alexandria articles.


      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Five Minutes
    **Plan credit use:** 0 credit

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        news_type (str | Unset):  Default: 'all'.
        content_type (str | Unset):  Default: 'all'.
        category (str | Unset):
        language (GetV1ContentLatestLanguage | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContentLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject]
    """

    kwargs = _get_kwargs(
        start=start,
        limit=limit,
        id=id,
        slug=slug,
        symbol=symbol,
        news_type=news_type,
        content_type=content_type,
        category=category,
        language=language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start: int | Unset = 1,
    limit: int | Unset = 100,
    id: str | Unset = UNSET,
    slug: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    news_type: str | Unset = "all",
    content_type: str | Unset = "all",
    category: str | Unset = UNSET,
    language: GetV1ContentLatestLanguage | Unset = "en",
) -> (
    ContentLatestResponseModel
    | HTTPStatus400ErrorObject
    | HTTPStatus401ErrorObject
    | HTTPStatus403ErrorObject
    | HTTPStatus429ErrorObject
    | HTTPStatus500ErrorObject
    | None
):
    """Content Latest

     Returns a paginated list of content pulled from CMC News/Headlines and Alexandria articles.


      **This endpoint is available on the following [API
    plans](https://coinmarketcap.com/api/pricing/):**
      - Growth
      - Professional
      - Enterprise

    **Cache / Update frequency:** Five Minutes
    **Plan credit use:** 0 credit

    Args:
        start (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 100.
        id (str | Unset):
        slug (str | Unset):
        symbol (str | Unset):
        news_type (str | Unset):  Default: 'all'.
        content_type (str | Unset):  Default: 'all'.
        category (str | Unset):
        language (GetV1ContentLatestLanguage | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContentLatestResponseModel | HTTPStatus400ErrorObject | HTTPStatus401ErrorObject | HTTPStatus403ErrorObject | HTTPStatus429ErrorObject | HTTPStatus500ErrorObject
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            limit=limit,
            id=id,
            slug=slug,
            symbol=symbol,
            news_type=news_type,
            content_type=content_type,
            category=category,
            language=language,
        )
    ).parsed
