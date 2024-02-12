with

orders as (
    select * from {{ ref('stg_slamco__orders') }}
),

customer_billing as(
    select * from {{ ref('stg_slamco__billing') }}
),

final as (
    select
        o.order_id,
        {{ dbt_utils.generate_surrogate_key(['o.payment_type', 'o.financial_status', 'o.order_status']) }} as order_indicator_key,
        o.created_date,
        o.paid_date,
        {{ dbt_utils.generate_surrogate_key(['o.customer_id']) }} as customer_key,
        {{ dbt_utils.generate_surrogate_key(['c.billing_id']) }} as credit_card_key,
        {{ dbt_utils.generate_surrogate_key(['o.currency_abbreviation']) }} as currency_key,
        {{ dbt_utils.generate_surrogate_key(['o.line_item_sku']) }} as product_key,
        o.line_item_quantity,
        o.subtotal,
        o.taxes,
        o.shipping,
        o.total
    from orders as o
    left join customer_billing as c
        on o.customer_id = c.customer_id
)

select * from final
