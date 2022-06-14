# Write your MySQL query statement below
select actor_id, director_id From ActorDirector Group BY actor_id, director_id Having Count(*) >= 3
