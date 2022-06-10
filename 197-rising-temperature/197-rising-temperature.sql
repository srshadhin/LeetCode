# Write your MySQL query statement below
SELECT t1.id From Weather t1, Weather t2
WHERE t1.temperature > t2.temperature
AND subdate(t1.recordDate, 1) = t2.recordDate;