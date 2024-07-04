# Write your MySQL query statement below

with cte as (select category, count(category) as accounts_count from(
    select *, 
    case
        when income<20000 then 'Low Salary'
        when income>=20000 and income<=50000 then 'Average Salary'
        else 'High Salary'
    end as category
from Accounts) as T1
group by category),

cte2 as (select * from cte
union all
select 'Low Salary' as category,0 as accounts_count
union all 
select 'Average Salary' as category, 0 as accounts_count
union all 
select 'High Salary' as category, 0 as accounts_count)

select 
    category, 
    sum(accounts_count) as accounts_count 
from cte2 
group by category



