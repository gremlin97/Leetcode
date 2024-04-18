# Write your MySQL query statement below
select T1.customer_id, Count(T1.customer_id) as count_no_trans from Visits as T1 
left join Transactions as T2 
on T1.visit_id =  T2.visit_id
where T2.visit_id is Null
group by T1.customer_id