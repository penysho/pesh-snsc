FROM python:3.12 AS builder
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim AS base
WORKDIR /app
RUN apt update \
    && apt upgrade -y
RUN groupadd --system --gid 1000 app_web \
    && useradd --no-log-init --system -u 1000 --gid app_web --create-home app_web
USER app_web

FROM base AS develop
ENV PYTHONUNBUFFERED 1
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

FROM base AS production