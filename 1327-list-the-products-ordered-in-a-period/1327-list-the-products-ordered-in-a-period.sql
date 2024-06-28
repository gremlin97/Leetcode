# Write your MySQL query statement below


select 
    product_name,
    unit
from (select 
    a.product_name,
    sum(b.unit) as unit,
    b.order_date
from Products a
inner join Orders b
on a.product_id = b.product_id
where month(order_date) = '02' and year(order_date) ='2020'
group by a.product_id) as T
where unit>=100