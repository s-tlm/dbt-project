#!/usr/bin/env bash

# This script is automatically used to initialise the Docker database when starting up
# for the first time.

# functions
create_new_database() {
  # create a new database in psql only if it doesn't exist
  psql -tc "select 1 from pg_database where datname = '$1'" -U "$POSTGRES_USER" | grep -q 1 || psql -c "create database $1;" -U dbtuser
}

create_new_schema() {
  # create new schema in selected database if it doesn't exist
  psql -d "$1" -c "create schema if not exists $2;" -U "$POSTGRES_USER"
}

load_csv_to_database() {
  # load csv into the selected database and schema from path
  psql -d "$1" -c "\copy $2 from '$3' csv header;" -U "$POSTGRES_USER"
}

# setup databases
create_new_database 'raw'
create_new_database 'development'

# setup schemas
create_new_schema 'raw' 'slamco' # for raw data
create_new_schema 'development' 'dbt_user' # for dbt

# create empty tables in airbnb schema
psql -d 'raw' -c \
    'create table if not exists slamco.customers (
        customer_id integer,
        created_date date,
        gender varchar,
        prefix varchar,
        first_name varchar,
        last_name varchar,
        email varchar,
        company_email varchar,
        building_number varchar,
        street_name varchar,
        street_suffix varchar,
        city varchar,
        postcode varchar,
        country varchar,
        phone_number varchar
    );
    create table if not exists slamco.products (
        product_id integer,
        created_date date,
        product_sku varchar,
        product_type varchar,
        product_name varchar,
        product_price float
    );
    create table if not exists slamco.billing (
        billing_id integer,
        customer_id integer,
        created_date date,
        credit_card_provider varchar,
        credit_card_security_code varchar,
        credit_card_number varchar,
        credit_card_expiry_date varchar
    );
    create table if not exists slamco.orders (
        order_id integer,
        customer_id integer,
        created_date date,
        paid_date date,
        payment_method varchar,
        order_status varchar,
        line_item_sku varchar,
        line_item_name varchar,
        line_item_quantity integer,
        line_item_price float,
        financial_status varchar,
        subtotal float,
        taxes float,
        shipping float,
        total float,
        currency_code varchar,
        currency_name varchar
    );' -U "$POSTGRES_USER"

# load data from csv files
load_csv_to_database 'raw' 'slamco.customers' "/data/customers.csv"
load_csv_to_database 'raw' 'slamco.products' "/data/products.csv"
load_csv_to_database 'raw' 'slamco.billing' "/data/billing.csv"
load_csv_to_database 'raw' 'slamco.orders' "/data/orders.csv"
