FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN apt-get update && apt-get install netcat-traditional -y && apt-get autoremove -y && apt-get clean

WORKDIR /code
COPY ./docker/  /code/docker/
COPY ./pyproject.toml ./uv.lock* /code/
COPY ./src/  /code/src/
WORKDIR /code/src

RUN uv sync --frozen
