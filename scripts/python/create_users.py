#!/usr/bin/env python3
"""
Creates fake user data using the Faker package.
"""

from random import choice
from datetime import datetime, date
import os
import pandas as pd
from faker import Faker

NUM_CUSTOMERS = 10000
export_path = f'{os.path.dirname(__file__)}/../../data'

fake = Faker('en_AU')
users = []
start_date = datetime.strptime('1/1/2020', '%m/%d/%Y')

for user_id in range(NUM_CUSTOMERS):
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
    address = fake.street_address()
    city = fake.city()
    postcode = fake.postcode()
    country = fake.country()

    # Phone number
    phone_number = fake.phone_number()

    users.append([
        user_id,
        created_date,
        gender,
        prefix,
        first_name,
        last_name,
        email,
        company_email,
        address,
        city,
        postcode,
        country,
        phone_number
    ])

users_df = pd.DataFrame(
        users,
        columns=[
            'user_id',
            'created_date',
            'gender',
            'prefix',
            'first_name',
            'last_name',
            'email',
            'company_email',
            'address',
            'city',
            'postcode',
            'country',
            'phone_number'
        ])

if not os.path.exists(export_path):
    os.makedirs(export_path)
users_df.to_csv(f"{export_path}/users.csv", index=False)
