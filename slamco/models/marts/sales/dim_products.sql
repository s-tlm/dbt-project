with

    products as (
        select
            {{ dbt_utils.generate_surrogate_key(["sku_number"]) }} as product_key,
            sku_number,
            created_date,
            product_type,
            product_name,
            retail_price
        from {{ ref("stg_slamco__products") }}
    )

select *
from products
