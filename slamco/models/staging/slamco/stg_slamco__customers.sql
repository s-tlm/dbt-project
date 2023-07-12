with

source as (
    select * from {{ source('slamco', 'customers') }}
),

renamed as (
    select
        customer_id,
        created_date,
        gender,
        prefix as salutation,
        email as personal_email,
        company_email,
        building_number as street_number,
        street_name,
        street_suffix as street_type,
        city,
        postcode,
        country,
        phone_number,
        initcap(first_name) as first_name,
        initcap(last_name) as last_name,
        concat(first_name, ' ', last_name) as formal_greeting_name
    from source
)

select * from renamed
