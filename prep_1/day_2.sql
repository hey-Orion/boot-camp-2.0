ok so the thing is that for these sql questions I needed hints I got the hints from Gemini
now review the codes and then I will rewrite it without hints 

orders(order_id, customer_id, order_date, amount, status)
customers(customer_id, name, country, signup_date)

SELECT 
    order_id, 
    customer_id,
    order_date, 
    amount,
    LAG(amount) OVER (
        PARTITION BY customer_id 
        ORDER BY order_date
    ) AS previous_order_amount
FROM orders;

SELECT 
    c.name, 
    sum(o.amount) as total_amount,
    dense_rank() over (order by sum(o.amount) desc) as customer_rank
from customers c 
join orders o on c.customer_id = o.customer_id
group by c.name;

SELECT
    order_id,
    customer_id,
    amount,
    amount - avg(amount) over (PARTITION by customer_id) as diff_avg
from orders;

with customer_table as (
    SELECT
        customer_id,
        sum(amount) as total_amount
    from orders
    group by customer_id
)
SELECT customer_id, total_amount
from customer_table
where total_amount > (SELECT avg(total_amount) from customer_table);

WITH ranked_orders AS (
    SELECT
        customer_id,
        order_id,
        amount,
        DENSE_RANK() OVER (
            PARTITION BY customer_id 
            ORDER BY amount DESC
        ) AS rnk 
    FROM orders 
)
SELECT customer_id, order_id, amount
FROM ranked_orders
WHERE rnk = 2;