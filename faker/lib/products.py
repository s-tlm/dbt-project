#!/usr/bin/env python3

"""
Class for creating fake product data using the Faker package.
"""

from datetime import datetime

from faker import Faker

fake = Faker("en_AU")


class ProductData:
    """A class to generate a product list with fake prices."""

    def __init__(self):
        # Instantiate product lists
        self.grocery_items = [
            "Ice-cream",
            "Chocolate",
            "Coffee",
            "Tea",
            "Milk",
            "Bread",
            "Butter",
            "Cheese",
            "Eggs",
            "Yoghurt",
            "Chicken",
            "Beef",
            "Pork",
            "Lamb",
            "Fish",
        ]
        self.clothing_items = [
            "T-Shirt",
            "Jeans",
            "Jumper",
            "Jacket",
            "Socks",
            "Shoes",
            "Hat",
            "Gloves",
            "Scarf",
            "Dress",
            "Underwear",
            "Pyjamas",
            "Belt",
            "Tie",
            "Suit",
            "Skirt",
        ]
        self.electronics_items = [
            "TV",
            "Laptop",
            "Tablet",
            "Phone",
            "Headphones",
            "Keyboard",
            "Mouse",
            "Monitor",
            "Printer",
            "Scanner",
            "Speakers",
            "Camera",
            "Drone",
            "Smartwatch",
            "Toaster",
            "Kettle",
            "Microwave",
            "Fridge",
            "Washing Machine",
        ]

    def generate_product_prices(self, product_list, min_price, max_price):
        """Generates random product prices for products."""
        prices = {}

        for item in product_list:
            prices[item] = fake.pydecimal(
                positive=True, right_digits=2, min_value=min_price, max_value=max_price
            )

        return prices

    def generate_data(self, product_type, min_price, max_price):
        """Generates the product list with random prices."""
        products = []
        if product_type == "Groceries":
            product_names = self.grocery_items
        elif product_type == "Clothing":
            product_names = self.clothing_items
        else:
            product_names = self.electronics_items

        start_date = datetime.strptime("1/1/2022", "%m/%d/%Y")
        end_date = datetime.strptime("1/1/2024", "%m/%d/%Y")

        prices = self.generate_product_prices(
            product_list=product_names, min_price=min_price, max_price=max_price
        )

        for product in product_names:
            product_price = prices[product]
            product_sku = fake.pystr_format(string_format="####-###-###")
            created_date = fake.date_between(start_date, end_date)
            products.append(
                [created_date, product_sku, product_type, product, product_price]
            )

        return products
