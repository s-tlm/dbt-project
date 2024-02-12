#!/usr/bin/env python3
"""
Creates fake billing information.
"""

from datetime import datetime, date
from random import shuffle
import os
import pandas as pd
from faker import Faker

NUM_CUSTOMERS = 10000
export_path = f'{os.path.dirname(__file__)}/../data'

fake = Faker('en_AU')
billing = []
start_date = datetime.strptime('1/1/2020', '%m/%d/%Y')
end_date = datetime.strptime('1/1/2024', '%m/%d/%Y')

# Randomise customer ids
customer_ids = list(range(NUM_CUSTOMERS))
shuffle(customer_ids)

for billing_id in range(NUM_CUSTOMERS):
    # Record created date
    created_date = fake.date_between(start_date, end_date)

    # Customer ID record belongs to
    customer_id = customer_ids[billing_id]

    # Credit card information
    credit_card_provider = fake.credit_card_provider()
    credit_card_security_code = fake.credit_card_security_code()
    credit_card_number = fake.credit_card_number()
    credit_card_expiry_date = fake.credit_card_expire()

    billing.append([
        billing_id,
        customer_id,
        created_date,
        credit_card_provider,
        credit_card_security_code,
        credit_card_number,
        credit_card_expiry_date
    ])

billing_df = pd.DataFrame(
        billing,
        columns=[
            'billing_id',
            'customer_id',
            'created_date',
            'credit_card_provider',
            'credit_card_security_code',
            'credit_card_number',
            'credit_card_expiry_date'
        ])

if not os.path.exists(export_path):
    os.makedirs(export_path)
billing_df.to_csv(f"{export_path}/billing.csv", index=False)
