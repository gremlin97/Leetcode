# Write your MySQL query statement below

select visited_on, amount, average_amount from (
    select visited_on,
    sum(sum(amount)) over(rows between 6 preceding and current row) as amount,
    round(avg(sum(amount)) over(rows between 6 preceding and current row),2) as average_amount,
    lag(visited_on, 6) over() as start_lag
    from Customer
    group by visited_on
    order by visited_on) as T
where start_lag is not null