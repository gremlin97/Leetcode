# Write your MySQL query statement below

select Department, Employee, Salary from
(select 
    b.name as Department,
    a.name as Employee,
    a.salary as Salary,
    dense_rank() over(partition by a.departmentId order by a.salary desc) as rnk
from Employee a
inner join Department b
    on a.departmentId = b.id) as T
where rnk in (1,2,3)
    