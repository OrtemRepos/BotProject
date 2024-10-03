import pytest
from src.config import settings
from redis.asyncio.client import Redis
from src.model import ExchangeRate


@pytest.fixture(scope="module")
def redis_cache():
    redis_cache = Redis(
        host=settings.redis_host,
        port=settings.redis_port,
    )
    return redis_cache


@pytest.fixture(scope="function")
def exchange_rate():
    exchange = ExchangeRate(value_name="USD", usd_exchange_rate=95.6)
    return exchange


@pytest.mark.asyncio(loop_scope="session")
async def test_set(redis_cache, exchange_rate):
    await redis_cache.set(exchange_rate.value_name, exchange_rate.usd_exchange_rate)
    result = await redis_cache.get(exchange_rate.value_name)
    assert float(result) == exchange_rate.usd_exchange_rate


@pytest.mark.asyncio(loop_scope="session")
async def test_set_new_value(redis_cache, exchange_rate):
    exchange_rate.usd_exchange_rate = 75.3
    await redis_cache.set(exchange_rate.value_name, exchange_rate.usd_exchange_rate)
    result = await redis_cache.get(exchange_rate.value_name)
    assert float(result) == exchange_rate.usd_exchange_rate
