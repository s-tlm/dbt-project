with

    customers as (
        select
            {{ dbt_utils.generate_surrogate_key(["customer_id"]) }} as customer_key,
            customer_id,
            created_date,
            gender,
            salutation,
            first_name,
            last_name,
            formal_greeting_name,
            personal_email,
            company_email,
            street_number,
            street_name,
            street_type,
            city,
            postcode,
            country,
            phone_number,
            date_of_first_purchase,
            date_of_last_purchase
        from {{ ref("int_customers_expanded") }}
    )

select *
from customers
