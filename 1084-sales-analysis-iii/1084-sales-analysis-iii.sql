# Write your MySQL query statement below
SELECT p.product_id, p.product_name
FROM Product AS p
JOIN Sales AS s ON p.product_id = s.product_id
GROUP BY p.product_id
HAVING MAX(QUARTER(sale_date)) = 1;
