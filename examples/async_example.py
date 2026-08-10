"""Async usage example for the CoinMarketCap Python SDK.

Run:
    export CMC_PRO_API_KEY="your-key"
    python examples/async_example.py
"""

import asyncio
import os

from coinmarketcap import CoinMarketCap


async def main():
    api_key = os.environ.get("CMC_PRO_API_KEY")

    if api_key:
        cmc = CoinMarketCap(api_key=api_key)
    else:
        print("No CMC_PRO_API_KEY set, using public mode\n")
        cmc = CoinMarketCap(environment="public")

    async with cmc:
        # Concurrent requests
        quotes, listings = await asyncio.gather(
            cmc.cryptocurrency.async_quotes_latest(id="1,1027"),
            cmc.cryptocurrency.async_listings_latest(limit=5),
        )

        print("=== Quotes ===")
        print(quotes)

        print("\n=== Listings ===")
        print(listings)


if __name__ == "__main__":
    asyncio.run(main())
