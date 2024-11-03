with

    billing as (select * from {{ ref("stg_slamco__billing") }}),

    customers as (select * from {{ ref("stg_slamco__customers") }}),

    joined as (
        select
            b.billing_id,
            b.created_date,
            c.first_name as holder_first_name,
            c.last_name as holder_last_name,
            b.card_type,
            b.cvc_code,
            b.card_number,
            b.expiry_date,
            b.expiry_month,
            b.expiry_year
        from billing as b
        left join customers as c on b.customer_id = c.customer_id
    )

select *
from joined
