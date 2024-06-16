# Write your MySQL query statement below
with cte as (
    select num, count(num) as cnt from MyNumbers
    group by num
)

select (
select num from cte
where cnt = 1
order by num desc
limit 1 ) as num

