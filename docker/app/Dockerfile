FROM python:3.12 AS builder
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim AS base
WORKDIR /app
RUN apt update \
    && apt upgrade -y

FROM base AS develop
ENV PYTHONUNBUFFERED 1
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

FROM base AS production