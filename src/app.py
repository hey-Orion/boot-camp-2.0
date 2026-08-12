before we move forward with pandas here are the codes of python and SQL
i try to write these form memory with a little help of course  
Gemini updated the codes a little 
here are the codes it took me few looks but i got it 

def process_user_events(events: list[dict]) -> dict[str, int]:
    counts = {}

    for event in events:
        if not event.get("event_type") or not event.get("is_valid"):
            continue

        event_type = event["event_type"].lower().strip()
        counts[event_type] = counts.get(event_type, 0) + 1

    return counts

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
