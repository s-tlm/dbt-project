#!/usr/bin/env bash

# Creates fake sales data.

PARENT_DIR=$(git rev-parse --show-toplevel)
SCRIPTS_DIR="$PARENT_DIR/scripts/python/"

# 1. Create users
echo "Creating user data..."
python3 "$SCRIPTS_DIR/create_users.py"
# 2. Create user billing
echo "Creating billing data..."
python3 "$SCRIPTS_DIR/create_user_billing.py"
# 3. create transactions and product list
echo "Creating transaction data..."
python3 "$SCRIPTS_DIR/create_transactions.py"
