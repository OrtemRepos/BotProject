from redis.asyncio.client import Redis
from src.config import settings
from src.model import ExchangeRateMessage, ExchangeRequest
from src.logging_config import logger


class RedisCache:
    reids_cache = Redis(
        host=settings.redis_host,
        port=settings.redis_port,
    )

    async def get(self, request: ExchangeRequest) -> float:
        result = await self.reids_cache.get(request.value_name)
        if result is None:
            raise ValueError(f"Could not find exchange rate for request {request}")
        return float(result)

    async def set(self, exchange_rate: ExchangeRateMessage) -> bool:
        result = await self.reids_cache.set(
            exchange_rate.value_name, exchange_rate.exchange_rate
        )
        if not result:
            logger.error(f"Could not set exchange rate for {exchange_rate=}")
            raise ValueError(f"Could not set exchange rate for {exchange_rate=}")
        return result
