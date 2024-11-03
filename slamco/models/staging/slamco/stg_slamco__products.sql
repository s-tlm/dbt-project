with

    source as (select * from {{ source("slamco", "products") }}),

    renamed as (
        select
            product_id,
            created_date,
            product_sku as sku_number,
            product_type,
            product_name,
            product_price as retail_price
        from source
    )

select *
from renamed
