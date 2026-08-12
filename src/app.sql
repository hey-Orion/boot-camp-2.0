with monthly_customer_spending as (
    select
        customer_id,
        customer_name,
        date_trunc('month', order_date) as order_month,
        sum(total_amount) as total_spent
    from customers c 
    join orders o on c.customer_id = o.customer_id
    where o.status = 'completed'
),
ranked_spending as (
    select *, 
        dense_rank() over (
            partition by order_month 
            order by total_spent desc
        ) as rnk 
    from monthly_customer_spending
)
select customer_id, customer_name, order_month, total_spent
from ranked_spending
where rnk <= 2
order by order_month desc, rnk asc;
