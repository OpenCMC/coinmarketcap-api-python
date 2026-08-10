# coinmarketcap-sdk

[![PyPI version](https://img.shields.io/pypi/v/coinmarketcap-sdk.svg)](https://pypi.org/project/coinmarketcap-sdk/)

The official Python SDK for the [CoinMarketCap Pro API](https://coinmarketcap.com/api/documentation/).

## Installation

```bash
pip install coinmarketcap-sdk
# or
uv add coinmarketcap-sdk
# or
poetry add coinmarketcap-sdk
```

> **Note:** The PyPI package is `coinmarketcap-sdk`, but you import it as `coinmarketcap`:
>
> ```python
> from coinmarketcap import CoinMarketCap
> ```

## Quick Start

```python
import os
from coinmarketcap import CoinMarketCap

cmc = CoinMarketCap(api_key=os.environ["CMC_PRO_API_KEY"])

# Use the namespace API — discover endpoints by category with autocomplete
quotes = cmc.cryptocurrency.quotes_latest(id="1,1027")  # 1 = BTC, 1027 = ETH
print(quotes)
```

## Usage

### Namespace API (Recommended)

All endpoints are grouped by category on the client instance:

```python
from coinmarketcap import CoinMarketCap

cmc = CoinMarketCap(api_key="your-key")

cmc.cryptocurrency.quotes_latest(id="1")
cmc.cryptocurrency.listings_latest(limit=10)
cmc.global_metrics.quotes_latest()
cmc.exchange.info(id="270")
```

Async variants are available with the `async_` prefix:

```python
quotes = await cmc.cryptocurrency.async_quotes_latest(id="1,1027")
```

### POST Endpoints (Request Models)

POST endpoints require typed request body models:

```python
from coinmarketcap import CoinMarketCap
from coinmarketcap.models import DqueryBatchPriceRequestDTO

cmc = CoinMarketCap(api_key="your-key")

body = DqueryBatchPriceRequestDTO.from_dict({
    "tokens": [{"platform": "ethereum", "address": "0x..."}],
})
prices = cmc.token.batch_get_token_price(body=body)
```

All 400+ request/response models are available via `coinmarketcap.models`.

### Configuration Options

```python
cmc = CoinMarketCap(
    # Required for 'pro' mode
    api_key="your-api-key",

    # Optional
    environment="pro",      # 'pro' (default) or 'public'
    base_url=None,          # Override base URL entirely
    timeout=30.0,           # Request timeout in seconds (default: 30s)
    max_retries=2,          # Auto-retry count (default: 2)
)
```

### Public (Keyless) Mode

Use the public API without an API key for publicly available endpoints:

```python
from coinmarketcap import CoinMarketCap

cmc = CoinMarketCap(environment="public")

cmc.cryptocurrency.listings_latest(limit=10)
```

## Error Handling

The SDK raises typed exception classes for common HTTP failures:

```python
from coinmarketcap import CoinMarketCap, CMCError, RateLimitError, AuthenticationError

cmc = CoinMarketCap(api_key="your-key")

try:
    quotes = cmc.cryptocurrency.quotes_latest(id="1")
except RateLimitError as e:
    print("Rate limited:", e)
except AuthenticationError as e:
    print("Invalid API key:", e)
except CMCError as e:
    print(f"API error {e.status_code}:", e)
```

### Error Types

| Status Code | Error Class            |
| ----------- | ---------------------- |
| 400         | `BadRequestError`      |
| 401         | `AuthenticationError`  |
| 402         | `PaymentRequiredError` |
| 403         | `ForbiddenError`       |
| 404         | `NotFoundError`        |
| 429         | `RateLimitError`       |
| 5xx         | `InternalServerError`  |
| Network     | `APIConnectionError`   |
| Timeout     | `APITimeoutError`      |

## Automatic Retries

Requests that fail with retryable status codes are automatically retried with exponential backoff:

- **Retryable**: 408, 409, 429, 500, 502, 503, 504, and network errors
- **Default**: 2 retries with 500ms initial delay, up to 8s max
- **429 responses**: Respects the `Retry-After` header when present

Disable retries:

```python
cmc = CoinMarketCap(api_key="your-key", max_retries=0)
```

## Timeout

Requests time out after 30 seconds by default:

```python
cmc = CoinMarketCap(api_key="your-key", timeout=10.0)  # 10 seconds
```

## Available Endpoints

All endpoints are available via `cmc.<category>.<method>()`. Categories include:

- `cmc.cryptocurrency` — Quotes, listings, market pairs, OHLCV, categories
- `cmc.exchange` — Exchange info, listings, market pairs
- `cmc.global_metrics` — Global stats, fear & greed index
- `cmc.content` — News, posts
- `cmc.community` — Trending tokens, topics
- `cmc.token` — DEX token data, pools, trades
- `cmc.derivatives` — Derivatives market data
- `cmc.cmc_index` — CMC 20/100 index

## Requirements

- Python >= 3.10

## License

MIT
