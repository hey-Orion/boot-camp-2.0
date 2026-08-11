with monthly_customer_spending as (
select
    customer_id,
    customer_name,
    date_trunc('month', order_date) as order_month,
    sum(total_amount) as total_spent

