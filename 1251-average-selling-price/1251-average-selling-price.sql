# Write your MySQL query statement below

select P.product_id, ifnull(round(sum(P.price*U.units)/sum(U.units),2),0) as average_price from Prices as P
left join UnitsSold as U
on P.product_id = U.product_id and U.purchase_date between P.start_date and P.end_date
group by product_id


# select P.product_id, P.price from Prices as P
# inner join UnitsSold as U
# on P.product_id = U.product_id and U.purchase_date between P.start_date and P.end_date
