# Write your MySQL query statement below

select a.user_id, round(sum(case when action='confirmed' then 1 else 0 end)/count(a.user_id),2) as confirmation_rate from Signups as a
left join Confirmations as b 
on a.user_id = b.user_id
group by a.user_id
order by a.user_id