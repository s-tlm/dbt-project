with

    source as (select * from {{ source("slamco", "billing") }}),

    renamed as (
        select
            created_date,
            billing_id,
            customer_id,
            credit_card_provider as card_type,
            credit_card_security_code as cvc_code,
            credit_card_number as card_number,
            credit_card_expiry_date as expiry_date,
            split_part(credit_card_expiry_date, '/', 1) as expiry_month,
            split_part(credit_card_expiry_date, '/', 2) as expiry_year
        from source
    )

select *
from renamed
