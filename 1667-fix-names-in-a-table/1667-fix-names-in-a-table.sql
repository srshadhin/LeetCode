# Write your MySQL query statement below
# select user_id, CONCAT(UPPER(
#     left(name,1)), lower(right(name, length(name)-1))
#  )
# as name from Users order by user_id;

select user_id, CONCAT(UPPER(SUBSTR(name,1,1)),LOWER(SUBSTR(name,2))) as name from users order by user_id;
