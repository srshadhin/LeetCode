# Write your MySQL query statement below
# select name from Customers INNER JOIN Customers ON Order.customerId = Customers.id;
SELECT name as Customers
FROM Customers
LEFT JOIN Orders ON Orders.customerId=Customers.id
where Orders.customerId IS NULL;
