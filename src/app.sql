SELECT customer_id, total_amount
FROM orders
WHERE total_amount >= 100;

SELECT customer_id, count(ordar_id) as total_ordars
from table
group by customer_id
order by total_ordars desc

SELECT region, avg(ordar_amount) as avg_ordar_amount
from table
group by region

SELECT *
FROM orders
WHERE timestamp >= CURRENT_DATE - INTERVAL '30 days'; 

SELECT c.customer_id, c.name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.customer_id IS NULL;

