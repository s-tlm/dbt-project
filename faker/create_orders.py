#!/usr/bin/env python3

"""
Creates fake customer orders.
"""

from datetime import datetime, date, timedelta
import os
from faker import Faker
from faker.providers import BaseProvider
from products import ProductData
import pandas as pd

class OrderProvider(BaseProvider):
    """Create fake order information."""
    financial_statuses = ['Paid', 'Refunded', 'Bounced']
    payment_methods = ['Credit Card', 'Cash']

    def financial_status(self):
        """Return a random financial status."""
        return self.random_element(self.financial_statuses)

    def order_status(self, status):
        """Create fake order statuses based on the financial status."""
        if status == 'Bounced':
            return 'Failed'
        return 'Completed'

    def payment_method(self):
        """Return a random payment method."""
        return self.random_element(self.payment_methods)

NUM_ORDERS = 100000
NUM_CUSTOMERS = 10000
CURRENCY_CODE = 'AUD'
CURRENCY_NAME = 'Australian Dollar'
export_path = f'{os.path.dirname(__file__)}/../data'
orders = []
start_date = datetime.strptime('1/1/2020', '%m/%d/%Y')

fake = Faker('en_AU')
fake.add_provider(OrderProvider)
products = ProductData()

# Generate product data
grocery_product_data = products.generate_data(
        product_type='Groceries',
        min_price=5,
        max_price=20
)
clothing_product_data = products.generate_data(
        product_type='Clothing',
        min_price=10,
        max_price=100
)
electronics_product_data = products.generate_data(
        product_type='Electronics',
        min_price=100,
        max_price=1000
)

grocery_product_data.extend(clothing_product_data)
grocery_product_data.extend(electronics_product_data)

products_df = pd.DataFrame(
        grocery_product_data,
        columns=[
            'created_date',
            'product_sku',
            'product_type',
            'product_name',
            'product_price'
        ])

for order_id in range(NUM_ORDERS):
    # Customer ID
    customer_id = fake.random_int(max=NUM_CUSTOMERS-1)
    product = products_df.sample()

    # Statuses
    financial_status = fake.financial_status()
    order_status = fake.order_status(status=financial_status)

    # Order dates
    created_date = fake.date_between(start_date, date.today())
    paid_date = fake.date_between(created_date, created_date + timedelta(days=5))
    payment_method = fake.payment_method()

    # Line items
    line_item_quantity = fake.random_int(min=1, max=5)
    line_item_name = product.iloc[0]['product_name']
    line_item_price = product.iloc[0]['product_price']
    line_item_sku = product.iloc[0]['product_sku']

    # shipping
    shipping = 6 if fake.pybool() else 0
    subtotal = float(line_item_quantity * line_item_price)
    taxes = round(0.1 * subtotal, 2)
    total = round(shipping + subtotal + taxes, 2)

    # Payment Methods
    # payment method id

    orders.append([
        order_id,
        customer_id,
        created_date,
        paid_date,
        payment_method,
        order_status,
        line_item_sku,
        line_item_name,
        line_item_quantity,
        line_item_price,
        financial_status,
        subtotal,
        taxes,
        shipping,
        total,
        CURRENCY_CODE,
        CURRENCY_NAME
    ])

orders_df = pd.DataFrame(
        orders,
        columns=[
            'order_id',
            'customer_id',
            'created_date',
            'paid_date',
            'payment_method',
            'order_status',
            'line_item_sku',
            'line_item_name',
            'line_item_quantity',
            'line_item_price',
            'financial_status',
            'subtotal',
            'taxes',
            'shipping',
            'total',
            'currency_code',
            'currency_name'
        ])

if not os.path.exists(export_path):
    os.makedirs(export_path)
orders_df.to_csv(f"{export_path}/orders.csv", index=False)
products_df.to_csv(f"{export_path}/products.csv", index=True, index_label='product_id')
