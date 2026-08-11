"""Tests for CoinMarketCap client."""

import inspect

import pytest

from coinmarketcap import ENVIRONMENTS, CoinMarketCap


def test_pro_requires_api_key():
    with pytest.raises(ValueError, match="api_key is required"):
        CoinMarketCap(environment="pro")


def test_public_no_key_needed():
    cmc = CoinMarketCap(environment="public")
    assert cmc.base_url == ENVIRONMENTS["public"]


def test_pro_base_url():
    cmc = CoinMarketCap(api_key="test-key")
    assert cmc.base_url == ENVIRONMENTS["pro"]


def test_custom_base_url():
    cmc = CoinMarketCap(api_key="test-key", base_url="https://custom.example.com")
    assert cmc.base_url == "https://custom.example.com"


def test_namespaces_bound():
    cmc = CoinMarketCap(api_key="test-key")
    assert hasattr(cmc, "cryptocurrency")
    assert hasattr(cmc, "exchange")
    assert hasattr(cmc, "global_metrics")


def test_namespace_has_methods():
    cmc = CoinMarketCap(api_key="test-key")
    assert callable(getattr(cmc.cryptocurrency, "quotes_latest", None))
    assert callable(getattr(cmc.cryptocurrency, "async_quotes_latest", None))
    assert callable(getattr(cmc.cryptocurrency, "listings_latest", None))


def test_post_body_param_required():
    """POST endpoints must expose body parameter, not silently drop it."""
    cmc = CoinMarketCap(api_key="test-key")
    sig = inspect.signature(cmc.token.batch_get_token_price)
    assert "body" in sig.parameters
    body_param = sig.parameters["body"]
    assert body_param.default is inspect.Parameter.empty
    assert "DqueryBatchPriceRequestDTO" in str(body_param.annotation)


def test_post_holders_body_param():
    cmc = CoinMarketCap(api_key="test-key")
    sig = inspect.signature(cmc.holder.holders)
    assert "body" in sig.parameters
    assert "DqueryHoldersRequestDTO" in str(sig.parameters["body"].annotation)


def test_response_type_not_any():
    """Namespace methods should preserve generated return types without error unions."""
    cmc = CoinMarketCap(api_key="test-key")
    sig = inspect.signature(cmc.cryptocurrency.quotes_latest)
    assert sig.return_annotation is not inspect.Signature.empty
    ret = str(sig.return_annotation)
    assert "CryptoQuoteV3DTO" in ret
    assert "HTTPStatus" not in ret


def test_index_return_type_strips_errors():
    cmc = CoinMarketCap(api_key="test-key")
    sig = inspect.signature(cmc.cmc_index.index_cmc100_latest)
    ret = str(sig.return_annotation)
    assert "ApiResponseOfIndexLatestResponseDTO" in ret
    assert "HTTPStatus400ErrorObject" not in ret
    assert "None" not in ret


def test_acronym_method_names():
    cmc = CoinMarketCap(api_key="test-key")
    assert hasattr(cmc.cmc_index, "index_cmc100_historical")
    assert hasattr(cmc.cryptocurrency, "ohlcv_historical")
    assert not hasattr(cmc.cmc_index, "index_c_m_c100_historical")


def test_context_manager():
    with CoinMarketCap(api_key="test-key") as cmc:
        assert cmc.base_url == ENVIRONMENTS["pro"]


def test_version_exposed():
    import coinmarketcap

    assert isinstance(coinmarketcap.__version__, str)
    assert coinmarketcap.__version__
