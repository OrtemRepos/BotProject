# BotProject
Бот на aiogram для телеграма, backend сервис по запросу bot сервиса дергает CBR api и кэширует результат на 1 час (можно изменить в конфиге), после чего возвращает результат сервису bot, а тот отправляет сообщение пользователю, который сделал запрос. Взаимодействие между сервисами через Apache Kafka.
Технологии](#технологии)
- [Начало работы](#начало-работы)

## Технологии
- [Python 3.12](https://www.python.org/)
- [Apache Kafka](https://kafka.apache.org/)
- [Redis](https://redis.io/)
- [FastStream](https://faststream.airt.ai/latest/)
- [Aiogram](https://aiogram.dev/)

## Использование
Запустите скрипт start.sh, который соберет контейнеры из исходников и запустит docker-compose.

Запуск start.sh:
```bash
$ bash start.sh
```

## Разработка

### Требования
Для установки и запуска проекта, необходим [docker](https://www.docker.com/) и [docker-compose](https://docs.docker.com/compose/install/)

## Источники
- [bot](https://github.com/OrtemRepos/BotWIthKafka)
- [backend](https://github.com/OrtemRepos/BotApiBackendFaststream)
