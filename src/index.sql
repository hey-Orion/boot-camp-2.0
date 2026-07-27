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

