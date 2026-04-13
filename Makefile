COMPOSE := docker compose --env-file .env -f build/docker-compose.yml
UV := uv run

.PHONY: up build down logs migrate lint lint-auto test

up:
	$(COMPOSE) up -d

build:
	$(COMPOSE) build

down:
	$(COMPOSE) down

logs:
	$(COMPOSE) logs

migrate:
	$(UV) alembic upgrade head

lint:
	$(UV) ruff check .

lint-auto:
	$(UV) ruff check . --fix

test:
	$(UV) pytest
