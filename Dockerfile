# build from minimal postgres image
FROM postgres:14-alpine

# set environment variables
ENV POSTGRES_PASSWORD mydbtproject
ENV POSTGRES_USER dbtuser

COPY ./data/ /data/
# copy db init scripts. These are executed by the container when setting up the db
COPY ./scripts/setup_database.sh /docker-entrypoint-initdb.d/
