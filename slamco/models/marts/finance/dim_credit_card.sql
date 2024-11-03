with

    billing as (
        select
            {{ dbt_utils.generate_surrogate_key(["billing_id"]) }} as credit_card_key,
            billing_id,
            created_date,
            holder_first_name,
            holder_last_name,
            card_type,
            cvc_code,
            card_number,
            expiry_date,
            expiry_month,
            expiry_year
        from {{ ref("int_billing_to_customer_joined") }}
    )

select *
from billing
