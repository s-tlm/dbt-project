with

    customers as (select * from {{ ref("stg_slamco__customers") }}),

    successful_orders as (
        select order_id, customer_id, created_date
        from {{ ref("stg_slamco__orders") }}
        where order_status = 'Completed'
    ),

    order_dates as (
        select
            customer_id,
            min(created_date) as first_order_date,
            max(created_date) as last_order_date
        from successful_orders
        group by customer_id
    ),

    joined as (
        select
            customers.*,
            order_dates.first_order_date as date_of_first_purchase,
            order_dates.last_order_date as date_of_last_purchase
        from customers
        left join order_dates on customers.customer_id = order_dates.customer_id
    )

select *
from joined
