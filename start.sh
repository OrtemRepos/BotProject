#!/bin/bash

command -v docker >/dev/null 2>&1 || { echo >&2 "Ошибка: docker не установлен."; exit 1; }
command -v docker-compose >/dev/null 2>&1 || { echo >&2 "Ошибка: docker-compose не установлен."; exit 1; }

docker build -t backend_bot:0.1.0 . -f ./backend/Dockerfile
docker build -t bot_exchanger_api:0.1.0 . -f ./bot/Dockerfile

docker-compose up -d
