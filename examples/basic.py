"""Basic usage example for the CoinMarketCap Python SDK.

Run:
    export CMC_PRO_API_KEY="your-key"
    python examples/basic.py
"""

import os

from coinmarketcap import CoinMarketCap
from coinmarketcap.models import DqueryBatchPriceRequestDTO

def main():
    api_key = os.environ.get("CMC_PRO_API_KEY")

    if api_key:
        cmc = CoinMarketCap(api_key=api_key)
    else:
        print("No CMC_PRO_API_KEY set, using public mode\n")
        cmc = CoinMarketCap(environment="public")

    # GET endpoint
    print("=== Cryptocurrency Quotes ===")
    quotes = cmc.cryptocurrency.quotes_latest(id="1,1027")
    print(quotes)

    # POST endpoint (requires body)
    if api_key:
        print("\n=== Batch Token Prices (POST) ===")
        body = DqueryBatchPriceRequestDTO.from_dict({
            "tokens": [{"platform": "ethereum", "address": "0x..."}],
        })
        prices = cmc.token.batch_get_token_price(body=body)
        print(prices)


if __name__ == "__main__":
    main()
