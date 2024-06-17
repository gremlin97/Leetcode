with cte1 as (
    select employee_id, manager_id
    from Employees
    where salary < 30000
    order by employee_id
),
cte2 as (
    select employee_id from Employees
)

select employee_id from cte1
where manager_id not in (select * from cte2)


