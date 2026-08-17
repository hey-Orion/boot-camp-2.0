select customer_id, total_amount
from orders
where total_amount >= 100;

select customer_id, count(*) as total_orders
from orders 
order by total_orders desc;
