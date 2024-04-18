# Write your MySQL query statement below
select W1.id from Weather as W1 
left join Weather as W2 on datediff(W1.recordDate, W2.recordDate) = 1
where W1.temperature > W2.temperature