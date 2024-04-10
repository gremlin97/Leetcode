# Write your MySQL query statement below
select T2.product_name, T1.year, T1.price from Sales as T1
left join Product as T2 on T1.product_id = T2.product_id
