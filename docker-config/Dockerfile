FROM python:3.13-slim

WORKDIR /app

ENV POETRY_VERSION=1.8.5
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

ENV PATH="${PATH}:${POETRY_VENV}/bin"

COPY pyproject.toml ./
RUN poetry lock && \
    poetry install --only main

COPY . .

RUN ls -la /app && echo "manage.py exists: " && ls -la /app/manage.py

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]