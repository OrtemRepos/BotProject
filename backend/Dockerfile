FROM ghcr.io/astral-sh/uv:0.4.17-python3.12-bookworm

ENV UV_PYTHON_PREFERENCE=only-system

ARG PYTHONPATH
ENV PYTHONPATH=$PYTHONPATH:/app/src

RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get install curl -y

WORKDIR /app

ADD ./backend/requirements.txt ./

RUN uv pip install --system -r requirements.txt

ADD ./backend/src /app/src

CMD ["uv", "run", "uvicorn", "src/main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000
