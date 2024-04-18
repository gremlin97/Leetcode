# Write your MySQL query statement below
select T1.customer_id, Count(T1.customer_id) as count_no_trans from Visits as T1 
where T1.visit_id not in 
(
  select T2.visit_id from Transactions as T2
)
group by T1.customer_id