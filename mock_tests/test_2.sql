SELECT 
    c.name, 
    o.amount
FROM customers c
JOIN orders o 
    ON c.customer_id = o.customer_id  -- 1. Combine tables on primary/foreign key
WHERE c.country = 'Germany'            -- 2. First condition
  AND o.amount > 100                   -- 3. Second condition (chained with AND)
ORDER BY c.customer_id;                -- 4. Sort results (uses c.customer_id even though it's not selected!)

