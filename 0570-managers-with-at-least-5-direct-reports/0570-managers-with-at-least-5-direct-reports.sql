# Write your MySQL query statement below
select b.name as name
from Employee as a
inner join Employee as b on a.managerId = b.id
group by b.id
having count(a.id)>=5
