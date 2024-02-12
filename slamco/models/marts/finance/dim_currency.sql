with

currency_types as (
    select distinct
        {{ dbt_utils.generate_surrogate_key(['currency_abbreviation']) }} as currency_key,
        currency_abbreviation,
        currency_name
    from {{ ref('stg_slamco__orders') }}
)

select * from currency_types
