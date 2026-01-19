FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app


COPY pyproject.toml ./
COPY uv.lock ./

COPY src/ ./src
ENV PYTHONPATH=/app/src
RUN uv sync --no-dev

RUN uv run python src/manage.py collectstatic --noinput

# Команда запуска через uv run
CMD ["sh", "-c", "\
    until nc -z $DB_HOST $DB_PORT; do \
      echo 'Waiting for DB...'; sleep 1; \
    done; \
    echo 'DB is up, applying migrations...'; \
    uv run python src/manage.py migrate && \
    uv run python src/manage.py collectstatic --noinput && \
    uv run gunicorn src.hotelservice.wsgi:application --bind 0.0.0.0:8000 \
"]
