# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
The TypeScript and Python SDKs share one version number (see Versioning in the README).

## [6.0.0] - 2026-11-20

Rebuilt from the OpenAPI spec published at
https://coinmarketcap.com/api/documentation/openapi.json (spec version `3.0.3`,
sha256 `177fcc41…32ae`).

### Added

- `cryptocurrency.ohlcv_historical` now calls `GET /v5/cryptocurrency/ohlcv/historical`
  (see Changed). Each candle is a list of 10 values: open, high, low, close, volume,
  market cap, then the open, high, low and close times.
- `real_world_assets.quotes_historical`: `GET /v5/real-world-assets/quotes/historical`,
  historical quotes for tokenized real-world assets.
- `Status` has `category` and `error_detail`, which some v5 endpoints return with an error.

### Changed (breaking)

- `cryptocurrency.ohlcv_historical` calls v5 instead of the deprecated v2 endpoint. It takes
  `id` or `slug`, a required `interval` (`15m`, `1h`, `4h`, `1d`, `1w`, `1M`), `time_start`,
  `time_end`, `count` and `convert_id`, and returns `CryptocurrencyOHLCVHistoricalV5ResponseModel`.
  `count` is sent only when you pass it, so `time_start` with `time_end` returns the whole range.
  To keep calling v2, use `deprecated.get_v2_cryptocurrency_ohlcv_historical`.
- RWA market pairs: `market_pair_quotes` is `market_pair_quote`, the name the API returns.
  The model is `RWAMarketPairsResultsObjectMarketPairsItemMarketPairQuote`.
- Each value in the `data` map is one object, or a list of them when you request by `symbol`
  and several assets match: `CryptocurrencyQuotesHistoricalResultObject | list[...]` for
  `cryptocurrency.quotes_historical` (v3), `deprecated.cryptocurrency_quotes_historical` (v1) and
  `deprecated.get_v2_cryptocurrency_quotes_historical`, and
  `CryptocurrencyOHLCVHistoricalResultsObject | list[...]` for
  `deprecated.cryptocurrency_ohlcv_historical` (v1) and `deprecated.get_v2_cryptocurrency_ohlcv_historical`.
- Renamed models: `CryptocurrencyOHLCVHistoricalResponseModelDataType0` is
  `CryptocurrencyOHLCVHistoricalResponseModelObjectMap`, and
  `CryptocurrencyQuotesLatestCryptocurrencyObjectTagsItemType1` is
  `CryptocurrencyQuotesLatestCryptocurrencyObjectTagObjectV2`.
- `Quote.price`, `Quote.market_cap` and `CryptoQuoteV3DTO.cmc_rank` can be `None`.
- `Status.error_code` is `int | str`: v5 endpoints send it as a string.

### Fixed

- The 5.0.1 fixes are in the package now: the 5.0.1 build on PyPI was made from older
  generated code. The `derivatives.liquidations_*` methods no longer send `convert_id=2781`
  by default (the API answered `4001 Invalid parameter`), and `cmc_index.index_cmc100_latest`
  and `cmc_index.index_cmc20_latest` return `last_update` as a `datetime.datetime`.

## [5.0.1] - 2026-10-30

Rebuilt from the OpenAPI spec published at
https://coinmarketcap.com/api/documentation/openapi.json (spec version `3.0.3`,
sha256 `3e72a1c4…17c9`).

### Fixed

- `derivatives.liquidations_quotes_latest`, `derivatives.liquidations_exchange_list_latest`
  and `derivatives.liquidations_cryptocurrency_list_latest` no longer send `convert_id=2781`
  by default. They sent it along with the default `convert=USD`, and the API rejected every
  call with `4001 Invalid parameter`. Pass `convert_id` yourself to convert by ID.
- `cmc_index.index_cmc100_latest` and `cmc_index.index_cmc20_latest` return
  `data.last_update` as a `datetime.datetime`, as the API sends it. It was a
  `datetime.date`, which dropped the time of day.

### Changed

- Docstrings follow the updated endpoint descriptions, for example which API plans
  include each endpoint.

## [5.0.0] - 2026-10-23

Rebuilt from the corrected OpenAPI spec published at
https://coinmarketcap.com/api/documentation/openapi.json (spec version `3.0.3`,
sha256 `855b21bb…3e0b`).

### Changed (breaking)

- 32 methods now return a response model with `.status` and `.data` (for example
  `V3CryptocurrencyQuotesLatestResponseModel`) instead of the bare item or list. Read
  results from `.data`. Several of these methods raised a parse error before, because the
  API always returned `{status, data}`.
  Affected: `cryptocurrency.quotes_latest`, `platform.list` and `platform.detail`, the DEX
  `token.*` methods (token, price, pools, search, trending, gainers/losers, meme, new,
  liquidity, security, swaps and batch queries), the `holder.*` methods,
  `ohlcv.kline_candles` and `ohlcv.kline_points`, and the deprecated v4 DEX methods.
- Field names now match the API: historical quotes `volume_24hr` is `volume_24h`;
  derivatives market pairs `market_pair` is `market_pair_symbol` and `crypto_id`/`symbol`
  are `convert_id`/`convert_symbol`; RWA market pairs `market_pair_quote` is
  `market_pair_quotes`.

### Fixed

- `cryptocurrency.listings_latest` no longer fails on Bitcoin, whose `platform` is `null`.
  Other fields the API can return as `null` are typed as optional too.
- DEX integer values that the API returns as strings (timestamps, counts) are typed as
  strings. `status.error_code` accepts an int or a string.
- Every endpoint uses the same `status` model.

### Added

- 146 response fields that were missing from the models, including the DeFi, stablecoin,
  derivatives and dominance fields on `global_metrics.globalmetrics_quotes_latest`.

## [4.0.3] - 2026-09-18

### Added

- `cmc_ai` namespace for the CMC AI endpoints: `cmc_ai.coins_map`
  (`GET /v5/cmc-ai/coins/map`), `cmc_ai.latest` (`GET /v5/cmc-ai/latest`) and
  `cmc_ai.coins_latest` (`GET /v5/cmc-ai/coins/latest`), each with an `async_` variant,
  and their response models.

## [4.0.2] - 2026-08-11

### Changed

- `APITimeoutError` takes a message instead of the timeout value and no longer has a
  `timeout` attribute. `APITimeoutError` and `APIConnectionError` accept the underlying
  `httpx` exception as the keyword argument `cause`.

### Fixed

- `async_*` methods returned an un-awaited coroutine instead of the response. They now
  return the data and raise the same errors as the sync methods.
- HTTP errors carry the response headers in `e.headers`, so a `RateLimitError` exposes
  `Retry-After`.
- Network failures and timeouts raise `APIConnectionError` and `APITimeoutError` once
  the retries run out, instead of the raw `httpx` exception.
- Read, write, protocol and proxy errors are retried, not only connect errors and
  timeouts.

### Added

- `coinmarketcap.__version__`.
- A `dev` extra with `pytest`, `ruff` and `mypy`.

## [4.0.1] - 2026-08-07

### Added

- Initial release of the Python SDK wrapper
- `CoinMarketCap` client class with authentication, retry, and timeout
- Pro and Public (keyless) environment support
- Namespace-based API access (`cmc.cryptocurrency.quotes_latest(...)`)
- Full async support (`await cmc.cryptocurrency.async_quotes_latest(...)`)
- Typed error hierarchy (CMCError, RateLimitError, etc.)
- Exponential backoff retry with Retry-After support
- Context manager support (`with`/`async with`)
