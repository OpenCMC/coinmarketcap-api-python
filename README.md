# coinmarketcap

[![PyPI version](https://img.shields.io/pypi/v/coinmarketcap.svg)](https://pypi.org/project/coinmarketcap/)
[![Python versions](https://img.shields.io/pypi/pyversions/coinmarketcap.svg)](https://pypi.org/project/coinmarketcap/)
[![License](https://img.shields.io/pypi/l/coinmarketcap.svg)](https://github.com/OpenCMC/coinmarketcap-api-python/blob/main/LICENSE)

The official Python SDK for the [CoinMarketCap Pro API](https://coinmarketcap.com/api/documentation/).

## Architecture

This SDK wraps `openapi-python-client` generated code (in `coinmarketcap/_generated/`) with:

- **`CoinMarketCap` client** — authentication, retry, pro/public environments
- **Namespace API** — `cmc.cryptocurrency.quotes_latest(...)` with full type safety
- **Typed errors** — `CMCError`, `RateLimitError`, etc.

Generated code is copied into `_generated/` during build/release (like TypeScript's `src/generated/`).
The namespace generator (`scripts/gen-py-namespaces.py`) reads generated function signatures
and produces typed wrapper methods — new OpenAPI endpoints are picked up automatically.

## Installation

```bash
pip install coinmarketcap
```

## Quick Start

```python
from coinmarketcap import CoinMarketCap

# Pro mode (requires API key)
cmc = CoinMarketCap(api_key="your-api-key")

# Get latest quotes for Bitcoin and Ethereum
quotes = cmc.cryptocurrency.quotes_latest(id="1,1027")
print(quotes)

# Get top 10 listings
listings = cmc.cryptocurrency.listings_latest(limit=10)
print(listings)
```

## Public Mode (Keyless)

```python
from coinmarketcap import CoinMarketCap

# No API key needed
cmc = CoinMarketCap(environment="public")

quotes = cmc.cryptocurrency.quotes_latest(id="1")
print(quotes)
```

## POST Endpoints (Request Models)

POST endpoints require typed request body models. Import them from `coinmarketcap.models`:

```python
from coinmarketcap import CoinMarketCap
from coinmarketcap.models import DqueryBatchPriceRequestDTO

cmc = CoinMarketCap(api_key="your-api-key")

body = DqueryBatchPriceRequestDTO.from_dict({
    "tokens": [{"platform": "ethereum", "address": "0x..."}],
})
prices = cmc.token.batch_get_token_price(body=body)
```

All 400+ request/response models are available via `coinmarketcap.models`.

## Async Support

```python
import asyncio
from coinmarketcap import CoinMarketCap

async def main():
    async with CoinMarketCap(api_key="your-key") as cmc:
        quotes = await cmc.cryptocurrency.async_quotes_latest(id="1,1027")
        print(quotes)

asyncio.run(main())
```

## Configuration

```python
cmc = CoinMarketCap(
    api_key="your-key",
    environment="pro",        # "pro" (default) or "public"
    base_url=None,            # Override base URL
    timeout=30.0,             # Request timeout in seconds
    max_retries=2,            # Retry on 429/5xx errors
)
```

## Available Namespaces

| Namespace | Description |
|-----------|-------------|
| `cmc.cryptocurrency` | Quotes, listings, market pairs, OHLCV, trending |
| `cmc.exchange` | Exchange info, listings, market pairs |
| `cmc.global_metrics` | Global market data |
| `cmc.tools` | Price conversion |
| `cmc.community` | Trending tokens and topics |
| `cmc.content` | News and posts |
| `cmc.cmc_index` | CMC 100/20 index data |
| `cmc.derivatives` | Derivatives markets |
| `cmc.real_world_assets` | RWA data |
| `cmc.token` | DEX token data |
| `cmc.holder` | Token holder analytics |
| `cmc.ohlcv` | DEX OHLCV data |
| `cmc.platform` | Blockchain platform info |

## Error Handling

```python
from coinmarketcap import CoinMarketCap, CMCError, RateLimitError, AuthenticationError

cmc = CoinMarketCap(api_key="your-key")

try:
    result = cmc.cryptocurrency.quotes_latest(id="1")
except RateLimitError as e:
    print(f"Rate limited: {e}, status: {e.status_code}")
except AuthenticationError as e:
    print(f"Auth failed: {e}")
except CMCError as e:
    print(f"API error {e.status_code}: {e}")
```

## Error Types

| Error | Status Code | Description |
|-------|-------------|-------------|
| `BadRequestError` | 400 | Invalid parameters |
| `AuthenticationError` | 401 | Missing or invalid API key |
| `PaymentRequiredError` | 402 | Plan doesn't cover endpoint |
| `ForbiddenError` | 403 | Access denied |
| `NotFoundError` | 404 | Resource not found |
| `RateLimitError` | 429 | Too many requests |
| `InternalServerError` | 5xx | Server error |
| `APITimeoutError` | — | Request timed out |
| `APIConnectionError` | — | Network failure |

## Retries

The client automatically retries on:
- 408, 409, 429, 500, 502, 503, 504

With exponential backoff (0.5s → 1s → 2s..., capped at 8s). For 429, the `Retry-After` header is respected.

## Requirements

- Python >= 3.10
- httpx >= 0.24.0

## License

MIT
