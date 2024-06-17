with cte1 as (
    select employee_id, manager_id
    from Employees
    where salary < 30000
    order by employee_id
)

select employee_id from cte1
where manager_id not in (select employee_id from Employees)


