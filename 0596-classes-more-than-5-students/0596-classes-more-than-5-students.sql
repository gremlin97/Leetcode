# Write your MySQL query statement below
select class from 
    (
        select class, count(class) as cnt from Courses
        group by class
    ) as T
where cnt >= 5