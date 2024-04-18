# Write your MySQL query statement below
select T1.name, T2.bonus from Employee as T1 
left join Bonus as T2
on T1.empId = T2.empId
where bonus < 1000 or bonus is Null
