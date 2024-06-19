# Write your MySQL query statement below

# select salary as SecondHighestSalary
# from Employee
# order by salary
# limit 1
# offset 1


select (select salary from
    (select salary,
     dense_rank() over(order by salary desc) as rk
     from Employee) as T
where rk = 2 limit 1) as SecondHighestSalary