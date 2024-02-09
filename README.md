# README

## Overview

A simple data project using Docker, Postgres and dbt Core.

## What's Installed

1. Postgres Database
2. dbt Core

## Requirements

1. Docker Desktop
2. Python3

## Usage

### Creating Sample Data

Create a new Python virtual environment and install the Faker package.

```bash
# MacOS
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the provided script to generate sample sales data.

```bash
# MacOS
cd scripts
./create_sample_data.sh
```

This will generate the following CSVs in the `data` directory.

| File Name        | Description                                    |
| ---------------- | ---------------------------------------------- |
| billing.csv      | Contains sample user billing data.             |
| products.csv     | Contains sample product list and their prices. |
| orders.csv       | Contains sample orders.                        |
| customers.csv    | Contains sample customers.                     |

Product prices, user names, contact details, credit cards and orders are randomly generated using the `Faker` python package.

Existing CSVs will be overwritten each time the script is executed.

### Creating the Docker Container

Build the Dockerfile.

``` shell
docker build -t dbt-slamco .
```

Create and run the container in detached mode. The datasets we generated earlier will be loaded into the database when we start the container for the first time.

```shell
docker run --name dbt-slamco -d -p 5432:5432 dbt-slamco
```

The Postgres database will now run in the background and accessible via `localhost` on port `5432`.

You can run commands directly in the image using `psql` or `bash`.

```shell
# using psql
docker exec -it dbt-slamco psql -U dbtuser

# or bash
docker exec -it dbt-slamco bash
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

Configure DBT to connect to the database via `localhost` and port `5432` by adding the following configuration to `~/.dbt/profiles.yml`.

```yaml
---
slamco:
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
