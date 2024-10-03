# BotProject
Бот на aiogram для телеграма, backend сервис по запросу bot сервиса дергает CBR api и кэширует результат на 1 час (можно изменить в конфиге), после чего возвращает результат сервису bot, а тот отправляет сообщение пользователю, который сделал запрос. Взаимодействие между сервисами через Apache Kafka.
- [Технологии](#технологии)
- [Использование](#использование)
- [Требования](#требования)
- [Источники](#источники)

## Технологии
- [Python](https://www.python.org/)
- [Apache Kafka](https://kafka.apache.org/)
- [Redis](https://redis.io/)
- [FastStream](https://faststream.airt.ai/latest/)
- [Aiogram](https://aiogram.dev/)

## Использование
Запустите скрипт start.sh, который соберет контейнеры из исходников и запустит docker-compose.  
**Внимание**:  
Приложение занимает следующие порты
- Redis: 8001, 6379
- Докумнентация AsyncAPI backend: 8000 (доступна на http://127.0.0.1:8000/docs)
- Документация AsyncAPI bot: 8002 (доступна на http://127.0.0.1:8002/docs)
  
Убедитесь, что эти порты не заняты другими приложениями или уберите их из ports в docker-compose.yaml.  
Так же вам нужнен [.env файл](https://github.com/OrtemRepos/BotProject/blob/main/.env.example) или же введите переменные среды в docker-compose.yaml, например:
```Compose
backend:
    image: backend_bot:0.1.0
    container_name: backend
    networks:
      - net
    environment:
      BOOTSTRAP_SERVER: "broker:9092"
      REDIS_HOST: "redis"
      REDIS_POER: "6379"
      EXPIRE_TIME: 3600 
    ports:
      - "8000:8000"
    depends_on:
      redis:
        condition: service_healthy
      broker:
        condition: service_healthy
    entrypoint: ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

  bot:
    image: bot_exchanger_api:0.1.0
    container_name: bot
    networks:
      - net
    environment:
      BOOTSTRAP_SERVER: "broker:9092"
      TOKEN=: "<BOT_TOKEN>"
    ports:
      - "8002:8002"
    depends_on:
      redis:
        condition: service_healthy
      broker:
        condition: service_healthy
      backend:
        condition: service_started
    entrypoint: ["uv", "run", "src/main.py"]
```

   
Запуск start.sh:
```bash
$ bash start.sh
```

### Требования
Для установки и запуска проекта, необходим [docker](https://www.docker.com/) и [docker-compose](https://docs.docker.com/compose/install/)

## Источники
- [bot](https://github.com/OrtemRepos/BotWIthKafka)
- [backend](https://github.com/OrtemRepos/BotApiBackendFaststream)
