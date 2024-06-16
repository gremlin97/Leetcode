# Write your MySQL query statement below


with cte as (
    select product_id, min(year) as year
    from Sales
    group by product_id)
    
select s.product_id, s.year as first_year, s.quantity, s.price from Sales as S
inner join cte as c
on c.product_id = s.product_id and c.year = s.year
    