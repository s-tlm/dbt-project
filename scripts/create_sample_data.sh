#!/usr/bin/env bash

# Creates fake sales data.

PARENT_DIR=$(git rev-parse --show-toplevel)
SCRIPTS_DIR="$PARENT_DIR/scripts/python/"

# 1. Create users
echo "Creating customer data..."
python3 "$SCRIPTS_DIR/create_customers.py"
# 2. Create user billing
echo "Creating billing data..."
python3 "$SCRIPTS_DIR/create_customer_billing.py"
# 3. create orders and product list
echo "Creating order data..."
python3 "$SCRIPTS_DIR/create_orders.py"
