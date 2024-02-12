with

orders as (
    select * from {{ ref('stg_slamco__orders') }}
),

unique_indicators as (
    select distinct
        {{ dbt_utils.generate_surrogate_key(['payment_type', 'financial_status', 'order_status']) }} as order_indicator_key,
        payment_type,
        financial_status,
        order_status
    from orders
)

select * from unique_indicators
