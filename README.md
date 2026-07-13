# Ascend

Соц-RPG платформа саморазвития: реальные привычки прокачивают «характеристики
жизни» (XP, уровни, классы), а стрики, ачивки, лидерборды и чат обновляются в
реальном времени. Подробная концепция и фазы — в каталоге `Plan Ascend/`.

## Стек

- **Backend:** Python 3.14, FastAPI, Uvicorn, Pydantic v2
- **DB:** SQLAlchemy 2.0 (async) + asyncpg, Alembic
- **Инфра (dev):** PostgreSQL, Redis, Redpanda — через Docker Compose
- **Тулинг:** uv, ruff, mypy (strict), pytest

## Структура

```
backend/
  app/
    main.py            # сборка FastAPI-приложения (create_app)
    core/              # config, db, security
    api/router.py      # агрегатор роутеров
    modules/           # домены (system, users, ...)
      <domain>/
        router.py schemas.py service.py models.py
  migrations/          # Alembic
  tests/
deploy/                # docker-compose с инфраструктурой
frontend/              # (позже) React + Vite + TypeScript
```

## Быстрый старт

```bash
# 1. Зависимости
uv sync --dev

# 2. Конфиг
cp .env.example .env   # и подставить значения

# 3. Инфраструктура (Postgres/Redis/Redpanda)
docker compose -f deploy/docker-compose.yml up -d

# 4. Миграции
uv run alembic revision --autogenerate -m "init"
uv run alembic upgrade head

# 5. Запуск API
uv run uvicorn backend.app.main:app --reload
```

API-доки: `http://localhost:8000/docs`. Healthcheck: `/system/healthz`.

## Проверки качества

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy backend
uv run pytest
```
