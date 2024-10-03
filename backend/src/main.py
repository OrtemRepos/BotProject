from faststream.asgi import AsgiFastStream, make_ping_asgi, make_asyncapi_asgi
from faststream.kafka import KafkaBroker
from faststream.asyncapi.schema import Contact, License
from src.model import ExchangeRateMessage, ExchangeRequest
from src.config import settings
from src.logging_config import logger


from src.service import check_cache

broker = KafkaBroker(bootstrap_servers=settings.bootstrap_server)


app = AsgiFastStream(
    broker,
    logger=logger,
    asgi_routes=[
        ("/health", make_ping_asgi(broker, timeout=5.0)),
    ],
    title="Exchange rate service",
    version="0.0.1",
    description="Exchange rate service",
    license=License(name="MIT", url="https://opensource.org/license/mit/"),  #  type: ignore
    contact=Contact(name="Sadykov Artem", url="https://t.me/ortem917"),  #  type: ignore
)

publisher = broker.publisher(
    topic="exchange-rate-output",
    description="Exchange rate output from cbr",
    headers={"content-type": "application/json"},
    schema=ExchangeRateMessage,
)


@publisher
@broker.subscriber("exchange-rate-request", description="Exchange rate request")
async def on_exchange_rate(request: ExchangeRequest) -> ExchangeRateMessage:
    return await check_cache(request)


app.mount("/docs", make_asyncapi_asgi(app))
