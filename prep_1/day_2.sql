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

