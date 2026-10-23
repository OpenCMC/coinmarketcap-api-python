# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
The TypeScript and Python SDKs share one version number (see Versioning in the README).

## [5.0.0] - Unreleased

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
