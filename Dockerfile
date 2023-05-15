FROM python:3.10.10-slim-buster

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.4.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends \
    build-essential default-libmysqlclient-dev curl vim

WORKDIR /api

COPY pyproject.toml ./
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false && poetry install

COPY . .

ENV FLASK_APP=app.py FLASK_ENV=development DEBUG=True RELOAD=True
