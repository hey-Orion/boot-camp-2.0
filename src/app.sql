select customer_id, total_amount
from orders 
where total_amount >= 100;

select customer_id, count(*) as total_orders
from orders
group by customer_id
order by total_orders desc;

select c.region, avg(o.total_amount) as avg_order_amount
from orders o 
join customers c on o.customer_id = c.customer_id
group by c.region;

select * 
from orders
where order_date >= current_date - interval '30 days';

select c.customer_id, c.name
from customers c 
left join orders o on c.customer_id = o.customer_id
where o.customer_id is NULL;