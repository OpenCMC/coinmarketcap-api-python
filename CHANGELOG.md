# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
