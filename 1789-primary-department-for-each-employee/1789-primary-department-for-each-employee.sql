# Write your MySQL query statement below

with cte as (
    select employee_id, department_id
    from Employee
    group by employee_id, primary_flag
    having primary_flag = 'Y'),

cte1 as (
    select employee_id, department_id, primary_flag
    from Employee
    group by employee_id
    having count(employee_id) = 1
)

select * from cte 
union 
select employee_id, department_id from cte1 where primary_flag = 'N'
