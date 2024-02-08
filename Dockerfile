# build from minimal postgres image
FROM postgres:14-alpine

ENV POSTGRES_PASSWORD mydbtproject
ENV POSTGRES_USER dbtuser

RUN apk update && apk add \
  git \
  python3 \
  py3-pip \
  build-base \
  libffi-dev \
  gcc \
  libc-dev \
  openssl-dev \
  python3-dev \
  --no-cache

RUN pip install dbt-postgres --break-system-packages

COPY ./data/ /data/
COPY ./scripts/setup_database.sh /docker-entrypoint-initdb.d/

WORKDIR /home
COPY ./slamco/ ./slamco
