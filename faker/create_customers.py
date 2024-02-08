#!/usr/bin/env python3
"""
Creates fake customer data using the Faker package.
"""

from random import choice
from datetime import datetime, date
import os
import pandas as pd
from faker import Faker

NUM_CUSTOMERS = 10000
export_path = f'{os.path.dirname(__file__)}/../data'

fake = Faker('en_AU')
customers = []
start_date = datetime.strptime('1/1/2020', '%m/%d/%Y')

for customer_id in range(NUM_CUSTOMERS):
    # Record created date
    created_date = fake.date_between(start_date, date.today())

    # Gender
    gender = choice(["Male", "Female"])

    # Customer names
    if gender == "Male":
        prefix = fake.prefix_male()
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
    else:
        prefix = fake.prefix_female()
        first_name = fake.first_name_female()
        last_name = fake.last_name_female()

    # Email
    email = fake.ascii_email()
    company_email = fake.company_email()

    # Address
    building_number = fake.building_number()
    street_name = fake.street_name()
    street_suffix = fake.street_suffix()
    city = fake.city()
    postcode = fake.postcode()

    # Phone number
    phone_number = fake.phone_number()

    customers.append([
        customer_id,
        created_date,
        gender,
        prefix,
        first_name,
        last_name,
        email,
        company_email,
        building_number,
        street_name,
        street_suffix,
        city,
        postcode,
        'Australia',
        phone_number
    ])

customers_df = pd.DataFrame(
        customers,
        columns=[
            'customer_id',
            'created_date',
            'gender',
            'prefix',
            'first_name',
            'last_name',
            'email',
            'company_email',
            'building_number',
            'street_name',
            'street_suffix',
            'city',
            'postcode',
            'country',
            'phone_number'
        ])

if not os.path.exists(export_path):
    os.makedirs(export_path)
customers_df.to_csv(f"{export_path}/customers.csv", index=False)
