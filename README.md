# README

## Overview

A simple data project using Docker, Postgres and DBT.

## What's Installed

1. Postgres Database
2. DBT Core

## Requirements

1. Docker
2. Python3

## Usage

### Creating Sample Data

By default, sample data is located in the `data` directory.

| File Name        | Description                                   |
| ---------------- | --------------------------------------------- |
| billing.csv      | Contains sample user billing data             |
| products.csv     | Contains sample product list and their prices |
| transactions.csv | Contains sample transactions                  |
| users.csv        | Contains sample userbase                      |

Product prices, user names, contact details, credit cards and transactions are
randomly generated using the `Faker` python package.

To recreate a new set of sample data:

```bash
cd scripts
./create_sample_data.sh
```

Datasets are exported in CSV format to the `data` directory. Existing CSVs will
be overwritten.

### Creating Postgres Database with Docker

Build the Dockerfile.

``` shell
docker build -t db-image .
```

Create and run the container in detached mode. When the image runs for the first
time, it will automatically load the database with the sample datasets in the
`data` folder.

```shell
docker run --name dbt-project -d -p 5432:5432 db-image

```

The Postgres database will now run in the background.
It is bound to `localhost` on port 5432.

You can run commands directly in the image using `psql` or `bash`.

```shell
# using psql
docker exec -it dbt-project psql -U dbtuser

# or bash
docker exec -it dbt-project bash -U dbtuser
```

## Connecting to the Database

### Using an IDE

Connect to the database with your favourite IDE using the following
details.

```yaml
hostname: localhost
port: 5432
database: dbtuser
username: dbtuser
password: mydbtproject
```

### Using DBT

Configure DBT to connect to the database via `localhost` and port `5432` by
adding the following configuration to `~/.dbt/profiles.yml`.

```yaml
---
dbt_slamco:
  outputs:
    dev:
      type: postgres
      threads: 1
      host: localhost
      port: 5432
      user: dbtuser
      pass: mydbtproject
      dbname: development
      schema: dbt_user
  target: dev
```

Verify your configuration by running `dbt debug`.

> :warning: Docker image needs to be running.

```bash
# Check you are inside the DBT project directory
$ pwd
dbt-project/dbt
$ dbt debug
07:44:06  Running with dbt=1.5.0
07:44:06  dbt version: 1.5.0
07:44:06  python version: 3.11.3
07:44:06  python path: /Users/slam/Repositories/dbt-project/dbt-venv/bin/python3.11
07:44:06  os info: macOS-13.3.1-arm64-arm-64bit
07:44:06  Using profiles.yml file at /Users/slam/.dbt/profiles.yml
07:44:06  Using dbt_project.yml file at /Users/slam/Repositories/dbt-project/dbt/dbt_project.yml
07:44:06  Configuration:
07:44:06    profiles.yml file [OK found and valid]
07:44:06    dbt_project.yml file [OK found and valid]
07:44:06  Required dependencies:
07:44:06   - git [OK found]

07:44:06  Connection:
07:44:06    host: localhost
07:44:06    port: 5432
07:44:06    user: dbtuser
07:44:06    database: development
07:44:06    schema: dbt_user
07:44:06    search_path: None
07:44:06    keepalives_idle: 0
07:44:06    sslmode: None
07:44:06    Connection test: [OK connection ok]

07:44:06  All checks passed!
```
