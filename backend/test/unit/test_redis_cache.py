import pytest
from src.model import ExchangeRate
from src.redis_cache import RedisCache


@pytest.fixture(scope="module")
def redis_cache():
    return RedisCache()


@pytest.fixture(scope="function")
def exchange_rate():
    exchange = ExchangeRate(value_name="USD", usd_exchange_rate=95.6)
    return exchange


@pytest.mark.asyncio(loop_scope="session")
async def test_set(redis_cache, exchange_rate):
    result_bool = await redis_cache.set(exchange_rate)
    result = await redis_cache.get(exchange_rate.value_name)
    assert result_bool
    assert result == exchange_rate


@pytest.mark.asyncio(loop_scope="session")
async def test_override(redis_cache, exchange_rate):
    exchange_rate.usd_exchange_rate = 75.3
    result_bool = await redis_cache.set(exchange_rate)
    result = await redis_cache.get(exchange_rate.value_name)
    assert result_bool
    assert result == exchange_rate
