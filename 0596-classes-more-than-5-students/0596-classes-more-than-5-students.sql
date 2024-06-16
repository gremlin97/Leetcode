# Write your MySQL query statement below
with cte as (
    select class, count(class) as cnt from Courses
    group by class
)

select class from 
cte
where cnt >= 5