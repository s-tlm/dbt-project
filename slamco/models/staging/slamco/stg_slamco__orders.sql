with

    source as (select * from {{ source("slamco", "orders") }}),

    renamed as (
        select
            order_id,
            customer_id,
            created_date,
            paid_date,
            payment_method as payment_type,
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
            currency_code as currency_abbreviation,
            currency_name
        from source
    )

select *
from renamed
