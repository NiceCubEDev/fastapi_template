# FastAPI Template

Готовый каркас FastAPI-приложения с настройками через `.env`, версионированным API,
асинхронным SQLAlchemy, Alembic и Docker Compose для PostgreSQL.

## Быстрый старт

```bash
cp .env.example .env
uv sync
uv run uvicorn src.main:app --reload
```

Приложение будет доступно на http://127.0.0.1:8000.

## Проверки

```bash
uv run ruff check .
uv run pytest
```

## Make

```bash
make up
make build
make down
make migrate
make lint
make lint-auto
```

## Docker

```bash
docker compose --env-file .env -f build/docker-compose.yml up --build
```

## Alembic

```bash
uv run alembic revision --autogenerate -m "init"
uv run alembic upgrade head
```

## Эндпоинты

- `GET /health`
- `GET /api/v1/template`
