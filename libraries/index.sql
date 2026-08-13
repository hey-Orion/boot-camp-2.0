select 
    date_trunc('month', u.signup_date) as cohort_month,
    count(distinct u.user_id) as cohort_size,
    count(
        distinct case
            when u.is_active
            then u.user_id
        end
    ) as still_active 
from users u 
group by date_trunc('month', u.signup_date)
order by cohort_month;


with signups as (
    select user_id, created_at from users
),
activated as (
    select distinct user_id
    from events
    where status = 'active'
)

paid as (
    select distinct user_id
    from sub
    where status = 'active'
)
select 
    count(distinct s.user_id) as total_signups,
    count(distinct a.user_id) as total_activated,
    count(distinct p.user_id) as total_paid
from signups s 
left join activated a 
on s.user_id = a.user_id
left join paid p 
on s.user_id = p.user_id;



select 
    order_id,
    order_date,
    amount,
    sum(amount) over (order by order_date) as running_total,
    round(
        100.0 * amount / sum(amount) over (), 2 
    ) as pct_of_total
from orders 
order by order_date;

select u.user_id, u.name
from users u 
left join orders o on u.user_id = o.user_id
where o.order_id is NULL;


with monthly_customer_spending as (
    select
        c.customer_id,
        c.customer_name,
        date_trunc('month', o.order_date) as order_month,
        sum(o.total_amount) as total_spent
    from customers c 
    join orders o on c.customer_id = o.customer_id
    where o.status = 'completed'
    group by c.customer_id, c.customer_name, date_trunc('month', o.order_date)
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

