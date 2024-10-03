import requests
from src.redis_cache import RedisCache
from src.model import ExchangeRateMessage, ExchangeRequest
from src.logging_config import logger


redis_cache = RedisCache()


async def check_cache(request: ExchangeRequest) -> ExchangeRateMessage:
    try:
        await logger.ainfo(f"Checking cache for {request=}")
        result = await redis_cache.get(request)

        return ExchangeRateMessage(
            chat_id=request.chat_id,
            user_name=request.user_name,
            value_name=request.value_name,
            exchange_rate=result,
        )
    except ValueError:
        await logger.ainfo(f"Could not find exchange rate for {request=}")
        return await get_exchange_rate(request)


async def get_exchange_rate(request: ExchangeRequest) -> ExchangeRateMessage:
    logger.info(f"Getting request for {request} in CBR service")
    result = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    if result.status_code != 200:
        logger.error("Failed to get exchange rate", status_code=result.status_code)
        raise Exception("Failed to get exchange rate")
    try:
        exchange_rate = result.json()["Valute"][request.value_name]["Value"]
    except KeyError as exc:
        logger.exception(f"Could not find exchange rate for {request.value_name}")
        raise KeyError from exc
    exchange_rate = ExchangeRateMessage(
        chat_id=request.chat_id,
        user_name=request.user_name,
        value_name=request.value_name,
        exchange_rate=float(exchange_rate),
    )
    await redis_cache.set(exchange_rate)
    return exchange_rate
